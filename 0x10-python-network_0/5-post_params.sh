#!/bin/bash
# Sends a POST request to URL.
curl -s -X POST -d "email=test@gmail.com&subjet=I will always be here for PLD" "$1"
