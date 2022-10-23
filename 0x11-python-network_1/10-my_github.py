#!/usr/bin/python3
"""Takes my Github credentials (username and password)
and uses the Github API to display my Github id.
"""
import requests
from sys import argv


def github_API():
    """Github Authentication
    """

    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(argv[1], argv[2])).json()

    print(req.get('id'))


if __name__ == "__main__":
    github_API()
