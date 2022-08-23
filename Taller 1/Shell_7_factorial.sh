#!/bin/bash
source Shell_1_factorial.sh

for (( i=1; i<=20; i++ ))
do
	factor $i
	echo $i $respuesta
done

