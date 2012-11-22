#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
def dividir_hora():
	hora_actual=[]
	acc=""
	texto_hora=time.ctime()
	for x in texto_hora:
		if x != " ":
			acc+=x
		else:
			hora_actual.append(acc)
			acc=""
	hora_actual.append(acc)
	del hora_actual[0]#solo es el dia,encima en ingles,malditos putos del orto...
	hora_acomodada=str(hora_actual[1])+"-"+str(hora_actual[0])+"-"+str(hora_actual[3])+"-"+str(hora_actual[2])
	return hora_acomodada
