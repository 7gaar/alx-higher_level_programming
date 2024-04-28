#!/bin/bash
# get byte size of the http response.
curl -s "$1" | wc -c
