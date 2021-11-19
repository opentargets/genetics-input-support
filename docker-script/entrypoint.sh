#!/bin/sh

echo "Running Genetics input support with parameters $*"
conda run --no-capture-output -n pis-py3.8 python3 genetics-input-support.py "$@"

exit $!