#!/bin/bash
source Shell_1_factorial.sh

n=20
r=3

factor $n

n_fact=$respuesta

den_val=1

let den_val=$((20-3))

factor $den_val

den=$respuesta

v_nr=1

let v_nr=$(($n_fact/$den))

echo "n_fact:$n_fact"
echo "den_val:$den_val"
echo "den:$den"
echo "V:$v_nr"
