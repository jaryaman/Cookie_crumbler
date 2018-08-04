# Cookie crumbler

Removes all cookies from a website whose name is similar to the target. Has been written for Firefox in Ubuntu (tested on 14.04 LTS). 

## Installation

Requires `wmctrl` to safely close firefox before clearing cookies. To install:

```
sudo apt-get install wmctrl
```

Then, 

```
git clone https://github.com/jaryaman/Cookie_crumbler.git
```

## Usage

```
cd Cookie_crumbler
bash cookie_crumbler.sh [TARGET]
```

where `[TARGET]` is a substring of the name of the website for which you want to remove all the cookies, for example

```
bash cookie_crumbler.sh google
```

will remove all cookies which come from sites with the name 'google' in it.

## Disclaimer

This has only been tested on Ubuntu 14.04 LTS. I made this for fun, use at your own peril...
