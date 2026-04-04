#!/bin/bash
# Takes a URL, sends a GET request, and displays body of 200 response
curl -s -L -f "$1"
