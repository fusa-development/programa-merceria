#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk
from seccion_stock import *
import csv

class buscar_BD:

	def guardar_ruta(self): #si relogea el programa ya tiene la nueva ruta de la db
		ruta=[]
		ruta.append(self.ruta_archivo_db)
		manejador=open(".ruta_db.csv","w")
		manejador_csv=csv.writer(manejador)
		manejador_csv.writerow(ruta)
		manejador.close()

	def conectar_BD(self,self_seccion_stock):
		nombres_bd = ["lana","merceria","regaleria","santeria","bijouterie","jugueteria"]
		liststore = [self_seccion_stock.liststore_lana,self_seccion_stock.liststore_merceria,self_seccion_stock.liststore_regaleria,self_seccion_stock.liststore_santeria,self_seccion_stock.liststore_bijouterie,self_seccion_stock.liststore_jugueteria]
		self.bbdd=bdapi.connect( self.ruta_archivo_db )
		for i,nombre in enumerate(nombres_bd):
			if nombre == "lana" or nombre == "merceria":
				liststore[i].clear()
				self.cursor=self.bbdd.cursor()
				self.cursor.execute("SELECT * FROM "+nombre)
				for tupla in self.cursor.fetchall():
					if tupla[9]:
						liststore[i].append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),float(tupla[6]),float(tupla[7]) ,float(tupla[8]),"Si",True])
					else:
						liststore[i].append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),float(tupla[6]),float(tupla[7]) ,float(tupla[8]),"No",False])
			else:
				liststore[i].clear()
				self.cursor=self.bbdd.cursor()
				self.cursor.execute("SELECT * FROM "+nombre)
				for tupla in self.cursor.fetchall():
					if tupla[9]:
						liststore[i].append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),int(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),"Si",True])
					else:
						liststore[i].append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),int(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),"No",False])
				self.bbdd.commit()
		self.cursor.execute("SELECT * FROM ropa")
		for tupla in self.cursor.fetchall():
			if tupla[10]:
				self_seccion_stock.liststore_ropa.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),int(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),int(tupla[9]),"Si",True])
			else:
				self_seccion_stock.liststore_ropa.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),int(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),int(tupla[9]),"No",False])
		self.bbdd.commit()
		self.cursor.close()
		self.bbdd.close()
		self.guardar_ruta()


	def __init__(self,object,self_seccion_stock):
		self.ruta_archivo_db=""
		object.set_sensitive(False)
		self.dialog = gtk.FileChooserDialog("Abrir Base de Datos",
											None,
											gtk.FILE_CHOOSER_ACTION_OPEN,
											(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
											gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		self.dialog.set_default_response(gtk.RESPONSE_OK)
		self.filter2 = gtk.FileFilter()
		self.filter2.set_name("Base de Datos")
		self.filter2.add_mime_type("archi/db")
		self.filter2.add_pattern("*.db")
		self.dialog.add_filter(self.filter2)
		self.dialog.set_current_folder("")
		response = self.dialog.run()
		if response == gtk.RESPONSE_OK:
			self.ruta_archivo_db=self.dialog.get_filename()
			self.conectar_BD(self_seccion_stock)


		object.set_sensitive(True)
		self.dialog.destroy()
