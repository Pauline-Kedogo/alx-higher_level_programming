#!/usr/bin/python3
"""Fetchs https://alx-intranet.hbtn.io/status
sends a request to URL and displays the value
of the X-Request_id in the header
"""
import requests
import sys


def fetch_url():
    """funtion to displays the value
    of the X-Request_id in the header
    """
    res = requests.get(sys.argv[1])
    r = res.headers.get('X-Request-id')
    print(r)


if __name__ == "__main__":
    fetch_url()
