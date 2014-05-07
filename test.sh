#!/bin/sh

set -e
trap 'echo ERROR' 0 

export PYTHONPATH=$(pwd)
for PY_G in python python3 ; do
$PY_G ./yapps2 examples/expr.g examples/expr.py

for PY_X in python python3 ; do
test "$(echo "1+2*3+4" | $PY_X examples/expr.py goal)" = 11
done

done

trap 'rm examples/expr.py; echo OK' 0 
