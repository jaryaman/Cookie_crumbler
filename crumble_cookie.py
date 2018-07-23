import subprocess
from os import system
from os.path import expanduser
import sqlite3 as sq
from sys import argv

if len(argv) == 2:
	cookie_target = argv[1]
else:
	raise Exception('Usage: bash cookie_crumbler.sh [TARGET]')

# find where cookies live
home = expanduser("~")
try:
    result = subprocess.check_output(["find", "{}/.mozilla/firefox".format(home), "-name", "cookies.sqlite"])
except subprocess.CalledProcessError:
    print("Couldn't find your cookies database.")
cookies_fn = result[:-1].decode("utf-8") # remove '\n' and cast as string
cookies_dir = cookies_fn.split('/cookies.sqlite')[0]

# backup cookies + temp files
bck_cook_command = 'cp ' + cookies_fn + ' ' + cookies_fn + '.backup'
out = system(bck_cook_command)

# SQL commands to be run
get_ids='''SELECT id,baseDomain FROM moz_cookies 
                WHERE 
                baseDomain LIKE "%{0}%"
                OR
                host LIKE "%{0}%"'''.format(cookie_target)

delete_records = '''DELETE FROM moz_cookies
					WHERE 
					id IN(
						SELECT id FROM moz_cookies 
		                WHERE 
		                baseDomain LIKE "%{0}%"
		                OR
		                host LIKE "%{0}%"
						) 

'''.format(cookie_target)

# Connect to database and delete cookies
conn = sq.connect(cookies_fn)
c = conn.cursor()

c.execute(get_ids)
records_before = c.fetchall()

c.execute(delete_records)

c.execute(get_ids)
records_after = c.fetchall()

conn.commit()
conn.close()

# Print output
print('Records before')
print(records_before)

print('Records after')
print(records_after)

print("And that's the way the cookie crumbles")

'''
Y U NO WORK???
'''

