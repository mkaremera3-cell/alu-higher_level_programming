#!/usr/bin/python3
"""Sends a request to a URL and displays the X-Request-Id header value."""
import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers.get('X-Request-Id'))
