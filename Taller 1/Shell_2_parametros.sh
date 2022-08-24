function help(){

	echo "---Debe incluir tres parámetros: posición inicial, velocidad inicial y tiempo total"

}

if ! [ $# -eq 3 ]; then
	help
	exit 1
else
	echo "Corriendo Programa"
fi
