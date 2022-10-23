#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import sys


def Error_Code():
    """sends a request to the URL
    displays the body of the response (decoded in utf-8).
    """

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    Error_Code()
