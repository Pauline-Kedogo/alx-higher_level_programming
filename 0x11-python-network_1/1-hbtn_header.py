#!/usr/bin/python3
"""Fetchs https://alx-intranet.hbtn.io/status
sends a request to URL and displays the value
of the X-Request_id in the header
"""
import urllib.request
import sys


def fetch_url():
    """funtion to displays the value
    of the X-Request_id in the header
    """
    with urllib.request.urlopen(sys.argv[1]) as response:
        res = response.headers.get('X-Request-Id')
        print(res)


if __name__ == "__main__":
    fetch_url()
