#!/usr/bin/python
# coding=utf8

##############################################################
#  Script     : Sha512_Dict_Attack.py
#  Author     : Abraham Pasamar (@apasamar)
#  Date       : 12/11/2015
#  Last Edited: 14/11/2015, apasamar
#  Description: Dictionary attack for sha512 password with salt
#               CiberRetoES
#               https://twitter.com/CiberPoliES/status/664871406073679872
##############################################################

import passlib.hash
import sys

count=0

with open("passwords.txt","r") as f:   # abrimos fichero 
	for line in f:                     # recorremos el archivo línea por línea, el archivo de passwords podría ser muy grande
		mypass=line.rstrip('\n')       # leemos password del fichero, quitamos el salto de línea, asignamos a mypass
		hash=passlib.hash.sha512_crypt.encrypt(mypass,rounds=5000,salt='CiberPoliES')  # calculamos el digest/hash -> sha512 con password=mypass y salt='CiberPoliES'
		short=hash.split('$')          # split de las salida para quedarnos solo con el hash  ($x$salt$hash)
		if 'YK/llxn54BL9a5idCFcBUqMd5' in short[3]:    # verificamos si coincide con el hash cuyo password hay que localizar (solo compararo un trozo, no todo) 
			print mypass               # si se localiza se imprime el password
			print hash                 # y el hash
			break                      # salimos del bucle
		else:
			sys.stdout.write('.')      # si no coincide se pinta un '.' por la pantalla sin retorno de carro
			sys.stdout.flush()
		count+=1                       
		if count % 100 == 0:       # cada X contraseñas escibe el número de interaciones. X=100
			print '== '+str(count)+' ==',	       # sin salto de línea (, al final del print)


print 'EOF'                            # Alcanzado final del fichero
