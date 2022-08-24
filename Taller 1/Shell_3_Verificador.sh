
pass=0

function checkvalue(){
if [ $1 -eq 1 ];then
	pass=1
else
	echo "Intente de nuevo, asegurese de que el primer parámetro = 1"
fi
}
while [ $pass -eq 0 ]
do
	read -p "Inserte valor: "
	checkvalue ${REPLY}
done

