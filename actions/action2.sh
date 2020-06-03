#!/bin/bash
echo 'Program liczacy iloczyny kolejnych wpisanych cyfr'
echo 'Podaj licze zatrzymujaca'
read stoper
echo 'Podaj maksymalna liczbe liczb'
read n
iloczyn=1
l=0

while [ $l -lt $n ]
do
	echo 'Podaj liczbe'
	read a
	
	iloczyn=$[$iloczyn*a]
	
	if [ $a -eq $stoper ]	
	then
		break
	fi
	
	l=$[$l+1]
done
echo iloczyn=$iloczyn
