#!/bin/bash

respuesta=1

function factor(){
        
        typeset -i factorial=1
	n=$1
	valor=$n


        if [ $n -eq 0 ] || [ $n -eq 1 ]; then
                rta[0]=$valor
		rta[1]=$factorial
		respuesta=$factorial

	else
		while [ $n -gt 1 ]
                do
			let factorial=$factorial*$n
                        let n=$n-1
                done
		rta[0]=$valor
                rta[1]=$factorial
                respuesta=$factorial
        fi
}

