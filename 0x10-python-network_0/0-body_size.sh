#!/bin/bash
# Bash script that takes in a URL, sends a request and
curl -s "$1" | wc -c
