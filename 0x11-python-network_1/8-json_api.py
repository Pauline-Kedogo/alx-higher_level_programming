#!/usr/bin/python3
"""A script that takes in a letter
sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


def Search_API():
    """sends POST request to http://0.0.0.0:5000/search_user
    """
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ''
    payload = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    Search_API()
