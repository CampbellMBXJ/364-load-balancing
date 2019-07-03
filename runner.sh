#!/bin/bash

python3 ./main.py $1 $2 $3 > out.lp
"$4/cplex/cplex/bin/x86-64_linux/cplex" -c "read out.lp" "optimize" "display solution variables -"
