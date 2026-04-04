#!/bin/bash
# Sends a GET request with X-School-User-Id header and displays the body
curl -s -H "X-School-User-Id: 98" "$1"
