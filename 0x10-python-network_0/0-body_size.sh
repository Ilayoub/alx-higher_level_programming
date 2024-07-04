#!/bin/bash
# Bash script that takes in a URL, sends a request and
# displays the size of the body of the response

curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
