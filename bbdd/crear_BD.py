#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3 as bdapi
import random
bbdd=bdapi.connect('stock_merceria.db')
cursor=bbdd.cursor()

cursor.execute("""create table lana (id INTEGER PRIMARY KEY,
				codigo text,
				descripcion text,
				costo float,
				precio float,
				ganancia int,
				stk_ini float,
				stk_disp float,
				pnt_rep float,
				aviso bool
				)""")
				
cursor.execute("""create table merceria (id INTEGER PRIMARY KEY,
				codigo text,
				descripcion text,
				costo float,
				precio float,
				ganancia int,
				stk_ini float,
				stk_disp float,
				pnt_rep float,
				aviso bool
				)""")
				
cursor.execute("""create table regaleria (id INTEGER PRIMARY KEY,
				codigo text,
				descripcion text,
				costo float,
				precio float,
				ganancia int,
				stk_ini int,
				stk_disp int,
				pnt_rep int,
				aviso bool
				)""")
				
cursor.execute("""create table santeria (id INTEGER PRIMARY KEY,
				codigo text,
				descripcion text,
				costo float,
				precio float,
				ganancia int,
				stk_ini int,
				stk_disp int,
				pnt_rep int,
				aviso bool
				)""")
				
cursor.execute("""create table ropa (id INTEGER PRIMARY KEY,
				codigo text,
				descripcion text,
				talle int,
				costo float,
				precio float,
				ganancia int,
				stk_ini int,
				stk_disp int,
				pnt_rep int,
				aviso bool
				)""")
				
cursor.execute("""create table bijouterie (id INTEGER PRIMARY KEY,
				codigo text,
				descripcion text,
				costo float,
				precio float,
				ganancia int,
				stk_ini int,
				stk_disp int,
				pnt_rep int,
				aviso bool
				)""")
				
cursor.execute("""create table jugueteria (id INTEGER PRIMARY KEY,
				codigo text,
				descripcion text,
				costo float,
				precio float,
				ganancia int,
				stk_ini int,
				stk_disp int,
				pnt_rep int,
				aviso bool
				)""")
				


aviso = False
listar = ["RC-","RI-","LE-"]
for x in range(10): 
	
	lista1 = []
	lista2 = []
	lista3 = []
	lista4 = []
	lista5 = []
	lista6 = []
	lista7 = []

	lista1.append("LA-"+str(x+40))
	lista2.append("M-"+str(x+20))
	lista3.append("RE-"+str(x+1))
	lista4.append("J-"+str(x+60))
	lista5.append("RC-"+str(x+30))
	lista6.append("SA-"+str(x+50))
	lista7.append("Bi-"+str(x+50))
	
	lista1.append("lana"+str(x))
	lista2.append("merceria"+str(x))
	lista3.append("ropa"+str(x))
	lista4.append("jugueteria"+str(x))
	lista5.append("regaleria"+str(x))
	lista6.append("Santeria"+str(x))
	lista7.append("Bijouterie"+str(x))
	lista3.append(random.randint(30,50))
	
	lista1.append(random.randint(30,70))
	lista2.append(random.randint(30,70))
	lista3.append(random.randint(30,70))
	lista4.append(random.randint(30,70))
	lista6.append(random.randint(30,70))
	lista5.append(random.randint(30,70))
	lista7.append(random.randint(30,70))
	
	lista1.append(random.randint(70,80))
	lista2.append(random.randint(70,80))
	lista3.append(random.randint(70,80))
	lista4.append(random.randint(70,80))
	lista5.append(random.randint(70,80))
	lista6.append(random.randint(70,80))
	lista7.append(random.randint(70,80))
	
	lista1.append(random.randint(30,50))
	lista2.append(random.randint(30,50))
	lista3.append(random.randint(30,50))
	lista4.append(random.randint(30,50))
	lista5.append(random.randint(30,50))
	lista6.append(random.randint(30,50))
	lista7.append(random.randint(30,50))
	
	lista1.append(random.randint(30,60))
	lista2.append(random.randint(30,60))
	lista3.append(random.randint(30,60))
	lista4.append(random.randint(30,60))
	lista5.append(random.randint(30,60))
	lista6.append(random.randint(30,60))
	lista7.append(random.randint(30,60))
	
	lista1.append(random.randint(30,60))
	lista2.append(random.randint(30,60))
	lista3.append(random.randint(30,60))
	lista4.append(random.randint(30,60))
	lista5.append(random.randint(30,60))
	lista6.append(random.randint(30,60))
	lista7.append(random.randint(30,60))
	
	lista1.append(random.randint(10,20))
	lista2.append(random.randint(10,20))
	lista3.append(random.randint(10,20))
	lista4.append(random.randint(10,20))
	lista5.append(random.randint(10,20))
	lista6.append(random.randint(10,20))
	lista7.append(random.randint(10,20))
	
	
	lista1.append(aviso)
	lista2.append(aviso)
	lista3.append(aviso)
	lista4.append(aviso)
	lista5.append(aviso)
	lista6.append(aviso)
	lista7.append(aviso)
	
	"""lista1.append(sw)
	lista2.append(sw)
	lista3.append(sw)
	lista4.append(sw)
	lista5.append(sw)
	lista6.append(sw)"""

	#cursor.execute(" INSERT INTO  lana (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",lista1)
	#cursor.execute(" INSERT INTO  merceria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",lista2)
	#cursor.execute(" INSERT INTO  ropa (codigo, descripcion, talle, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?,?)",lista3)
	#cursor.execute(" INSERT INTO  jugueteria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",lista4)
	#cursor.execute(" INSERT INTO  regaleria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",lista5)
	#cursor.execute(" INSERT INTO  santeria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",lista6)
	#cursor.execute(" INSERT INTO  bijouterie (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",lista7)
bbdd.commit()




cursor.close()
bbdd.close()
