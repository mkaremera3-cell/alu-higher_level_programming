#!/bin/bash
# Displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1" -i | grep Allow | cut -d' ' -f2-
