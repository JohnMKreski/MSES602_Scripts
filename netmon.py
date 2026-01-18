#!/usr/bin/env python

# monitor_wifi.py
import os
import urllib3

from time import sleep
from datetime import datetime

SLEEP_TIME = 1 * 60

def is_internet_on(method=2):
    """Check if the Internet connection is on."""

    if method == 2:
        # http://stackoverflow.com/questions/3764291/checking-network-connection
        try:
            http = urllib3.PoolManager()
            http.request('GET', 'http://www.google.com', timeout=1, retries=False)
            return True
        except urllib3.exceptions.NewConnectionError:
            return False
    else:
        print('# warning: unknown method in is_internet_on()')


def main():
    while True:
        if not is_internet_on():
            print('# network is down')
        else:
            print('# network is up')
            pass

        print ('# sleeping for ' +  str(SLEEP_TIME) + ' seconds...')
        sleep(SLEEP_TIME)


#############################################################################

if __name__ == "__main__":
    main()