#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

def leer_ruta():
	manejador=open(".ruta_db.csv","r")
	manejador_csv=csv.reader(manejador)
	for ruta in manejador_csv:
		pass
	manejador.close()
	return ruta[0]

