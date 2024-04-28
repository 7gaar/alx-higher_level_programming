#!/bin/bash
# takes a url and displays all HTTP methods.
curl -sI "$1" | grep "ALLOW" | cut -d " " -f 2-
