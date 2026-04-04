#!/bin/bash
curl -s -X OPTIONS "$1" -i | grep Allow | cut -d' ' -f2-
