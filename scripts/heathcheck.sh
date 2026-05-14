#!/bin/bash

rsync --version >/dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Healthcheck passed"
    exit 0
else
    echo "Healthcheck failed"
    exit 1
fi
