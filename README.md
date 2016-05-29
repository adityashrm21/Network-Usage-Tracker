# Network-Usage-Calculator
A python script to set a limit and know whether your network usage has exceeded it

### Requirements:

#####**This script needs Python 2+**

You may also need to install vnstat if you don't have it already installed
```bash
$ sudo apt-get install vnstat
```

### Usage:

```bash
$ python bandwidth.py xxx MiB/GiB &
```
The '&' has been added to run the process in background. If you want to stop the process at any time use :

```bash
$ ps -ef
```
to get the list of running processes and then get the pid of the process you want to kill and do :

```bash
$ kill pid
```
