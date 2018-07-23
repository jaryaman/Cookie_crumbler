TARGET=$1
DISPLAY=:0.0 wmctrl -c "Firefox"
sleep 0.5
python crumble_cookie.py $TARGET
sleep 0.5
nohup firefox &
