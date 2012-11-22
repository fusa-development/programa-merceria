#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk
import pango
import sqlite3 as bdapi
import csv

from altas.agregar_producto import agregar_producto
from bajas.eliminar_producto import eliminar_producto
from modificaciones.modificar_producto import modificar_producto
from control.consulta_stk import consultas_stk
from actualizaciones.actualizar_producto import actualizar_producto
from registros.win_registro_stock import win_registro_stock

from bbdd.administrar_BD_stock import administrar_BD_stock
from bbdd.leer_ruta_BD import leer_ruta
from bbdd.fail_bd import BD_no_especificada

class dibujar_stock():
	def conectar_BD(self,self_ventana_principal):
		nombres_bd = ["lana","merceria","regaleria","santeria","bijouterie","jugueteria"]
		liststore = [self.liststore_lana,self.liststore_merceria,self.liststore_regaleria,self.liststore_santeria,self.liststore_bijouterie,self.liststore_jugueteria]
		self.bbdd=bdapi.connect( leer_ruta() )
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
				self.liststore_ropa.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),int(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),int(tupla[9]),"Si",True])
			else:
				self.liststore_ropa.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),int(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),int(tupla[9]),"No",False])
		self.bbdd.commit()
		self.cursor.close()
		self.bbdd.close()
		self.bbdd.close()

	def agregar_producto(self,widget,self_ventana_principal):
		agregar_producto(self_ventana_principal.window,self.total_liststore_productos)

	def eliminar_producto(self,widget,self_ventana_principal):
		eliminar_producto(self,self_ventana_principal)
		self.button_eliminar_producto.set_sensitive(False)
		self.button_modificar_producto.set_sensitive(False)
		self.button_actualizar_producto.set_sensitive(False)
		if self.id_anterior_lana != 0:
			self.borrar_en_lana()
		if self.id_anterior_merceria != 0:
			self.borrar_en_merceria()
		if self.id_anterior_regaleria != 0:
			self.borrar_en_regaleria()
		if self.id_anterior_jugueteria != 0:
			self.borrar_en_jugueteria()
		if self.id_anterior_bijouterie != 0:
			self.borrar_en_bijouterie()
		if self.id_anterior_ropa != 0:
			self.borrar_en_ropa()
		if self.id_anterior_santeria != 0:
			self.borrar_en_santeria()

	def borrar_en_lana(self):
		self.liststore_lana.set_value(self.fila_anterior_lana, 0, None)
		self.treeselection_lana.unselect_all()
		self.id_anterior_lana,self.fila_anterior_lana=0,0

	def borrar_en_santeria(self):
		self.liststore_santeria.set_value(self.fila_anterior_santeria, 0, None)
		self.treeselection_santeria.unselect_all()
		self.id_anterior_santeria,self.fila_anterior_santeria=0,0

	def borrar_en_regaleria(self):
		self.liststore_regaleria.set_value(self.fila_anterior_regaleria, 0, None)
		self.treeselection_regaleria.unselect_all()
		self.id_anterior_regaleria,self.fila_anterior_regaleria=0,0

	def borrar_en_lana(self):
		self.liststore_lana.set_value(self.fila_anterior_lana, 0, None)
		self.treeselection_lana.unselect_all()
		self.id_anterior_lana,self.fila_anterior_lana=0,0

	def borrar_en_merceria(self):
		self.liststore_merceria.set_value(self.fila_anterior_merceria, 0, None)
		self.treeselection_merceria.unselect_all()
		self.id_anterior_merceria,self.fila_anterior_merceria=0,0

	def borrar_en_jugueteria(self):
		self.liststore_jugueteria.set_value(self.fila_anterior_jugueteria, 0, None)
		self.treeselection_jugueteria.unselect_all()
		self.id_anterior_jugueteria,self.fila_anterior_jugueteria=0,0

	def borrar_en_bijouterie(self):
		self.liststore_bijouterie.set_value(self.fila_anterior_bijouterie, 0, None)
		self.treeselection_bijouterie.unselect_all()
		self.id_anterior_bijouterie,self.fila_anterior_bijouterie=0,0



	def modificar_producto(self,widget,self_ventana_principal):
		modificar_producto(self_ventana_principal,self)

	def actualizar_producto(self,widget,self_ventana_principal):
		actualizar_producto(self_ventana_principal,self)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
												#TARGETs
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	def borrar_en_merceria(self):
		self.liststore_merceria.set_value(self.fila_anterior_merceria, 0, None)
		self.treeselection_merceria.unselect_all()
		self.id_anterior_merceria,self.fila_anterior_merceria=0,0

	def borrar_en_lana(self):
		self.liststore_lana.set_value(self.fila_anterior_lana, 0, None)
		self.treeselection_lana.unselect_all()
		self.id_anterior_lana,self.fila_anterior_lana=0,0

	def borrar_en_ropa(self):
		self.liststore_ropa.set_value(self.fila_anterior_ropa, 0, None)
		self.treeselection_ropa.unselect_all()
		self.id_anterior_ropa,self.fila_anterior_ropa=0,0

	def borrar_en_bijouterie(self):
		self.liststore_bijouterie.set_value(self.fila_anterior_bijouterie, 0, None)
		self.treeselection_bijouterie.unselect_all()
		self.id_anterior_bijouterie,self.fila_anterior_bijouterie=0,0

	def borrar_en_jugueteria(self):
		self.liststore_jugueteria.set_value(self.fila_anterior_jugueteria, 0, None)
		self.treeselection_jugueteria.unselect_all()
		self.id_anterior_jugueteria,self.fila_anterior_jugueteria=0,0

	def borrar_en_santeria(self):
		self.liststore_santeria.set_value(self.fila_anterior_santeria, 0, None)
		self.treeselection_santeria.unselect_all()
		self.id_anterior_santeria,self.fila_anterior_santeria=0,0

	def borrar_en_regaleria(self):
		self.liststore_regaleria.set_value(self.fila_anterior_regaleria, 0, None)
		self.treeselection_regaleria.unselect_all()
		self.id_anterior_regaleria,self.fila_anterior_regaleria=0,0

							#TARGET merceria
#-----------------------------------------------------------------------------------------------------------------
	def target_merceria(self,widget,event,data=None):
		self.tipo_producto="merceria"
		self.desbloquear_botones()
		if self.datos_seleccionados_productos != []:
			self.datos_seleccionados_productos=[]
		(model, iter) = self.treeselection_merceria.get_selected()
		for x in range(11):
			self.datos_seleccionados_productos.append(self.liststore_merceria.get_value(iter,x))
		self.datos_seleccionados_productos.append(iter)
		self.liststore_merceria.set_value(iter, 0, gtk.STOCK_MEDIA_PLAY)
		if self.id_anterior_lana != 0:
			self.borrar_en_lana()
		elif self.id_anterior_ropa != 0:
			self.borrar_en_ropa()
		elif self.id_anterior_jugueteria != 0:
			self.borrar_en_jugueteria()
		elif self.id_anterior_santeria != 0:
			self.borrar_en_santeria()
		elif self.id_anterior_regaleria != 0:
			self.borrar_en_regaleria()
		elif self.id_anterior_bijouterie != 0:
			self.borrar_en_bijouterie()

		if self.id_anterior_merceria != 0 and self.id_anterior_merceria != self.datos_seleccionados_productos[1]:
			self.liststore_merceria.set_value(self.fila_anterior_merceria, 0, None)

		self.id_anterior_merceria=self.datos_seleccionados_productos[1]
		self.fila_anterior_merceria=iter

									#TARGET lana
#-----------------------------------------------------------------------------------------------------------------
	def target_lana(self,widget,event,data=None):
		self.tipo_producto="lana"
		self.desbloquear_botones()
		if self.datos_seleccionados_productos != []:
			self.datos_seleccionados_productos=[]
		(model, iter) = self.treeselection_lana.get_selected()
		for x in range(11):
			self.datos_seleccionados_productos.append(self.liststore_lana.get_value(iter,x))
		self.datos_seleccionados_productos.append(iter)
		self.liststore_lana.set_value(iter, 0, gtk.STOCK_MEDIA_PLAY)
		if self.id_anterior_merceria != 0:
			self.borrar_en_merceria()
		elif self.id_anterior_ropa != 0:
			self.borrar_en_ropa()
		elif self.id_anterior_santeria != 0:
			self.borrar_en_santeria()
		elif self.id_anterior_jugueteria != 0:
			self.borrar_en_jugueteria()
		elif self.id_anterior_regaleria != 0:
			self.borrar_en_regaleria()
		elif self.id_anterior_bijouterie != 0:
			self.borrar_en_bijouterie()

		if self.id_anterior_lana != 0 and self.id_anterior_lana != self.datos_seleccionados_productos[1]:
			self.liststore_lana.set_value(self.fila_anterior_lana, 0, None)

		self.id_anterior_lana=self.datos_seleccionados_productos[1]
		self.fila_anterior_lana=iter

								#TARGET ropa
#-----------------------------------------------------------------------------------------------------------------
	def target_ropa(self,widget,event,data=None):
		self.tipo_producto="ropa"
		self.desbloquear_botones()
		if self.datos_seleccionados_productos != []:
			self.datos_seleccionados_productos=[]
		(model, iter) = self.treeselection_ropa.get_selected()
		for x in range(12):
			self.datos_seleccionados_productos.append(self.liststore_ropa.get_value(iter,x))
		self.datos_seleccionados_productos.append(iter)
		self.liststore_ropa.set_value(iter, 0, gtk.STOCK_MEDIA_PLAY)
		if self.id_anterior_merceria != 0:
			self.borrar_en_merceria()
		elif self.id_anterior_lana != 0:
			self.borrar_en_lana()
		elif self.id_anterior_regaleria != 0:
			self.borrar_en_regaleria()
		elif self.id_anterior_jugueteria != 0:
			self.borrar_en_jugueteria()
		elif self.id_anterior_santeria != 0:
			self.borrar_en_santeria()
		elif self.id_anterior_bijouterie != 0:
			self.borrar_en_bijouterie()

		if self.id_anterior_ropa != 0 and self.id_anterior_ropa != self.datos_seleccionados_productos[1]:
			self.liststore_ropa.set_value(self.fila_anterior_ropa, 0, None)

		self.id_anterior_ropa=self.datos_seleccionados_productos[1]
		self.fila_anterior_ropa=iter

									#TARGET MOTORES
#-----------------------------------------------------------------------------------------------------------------
	def target_bijouterie(self,widget,event,data=None):
		self.tipo_producto="bijouterie"
		self.desbloquear_botones()
		if self.datos_seleccionados_productos != []:
			self.datos_seleccionados_productos=[]
		(model, iter) = self.treeselection_bijouterie.get_selected()
		for x in range(11):
			self.datos_seleccionados_productos.append(self.liststore_bijouterie.get_value(iter,x))
		self.datos_seleccionados_productos.append(iter)
		self.liststore_bijouterie.set_value(iter, 0, gtk.STOCK_MEDIA_PLAY)
		if self.id_anterior_merceria != 0:
			self.borrar_en_merceria()
		elif self.id_anterior_lana != 0:
			self.borrar_en_lana()
		elif self.id_anterior_ropa != 0:
			self.borrar_en_ropa()
		elif self.id_anterior_santeria != 0:
			self.borrar_en_santeria()
		elif self.id_anterior_jugueteria != 0:
			self.borrar_en_jugueteria()
		elif self.id_anterior_regaleria != 0:
			self.borrar_en_regaleria()

		if self.id_anterior_bijouterie != 0 and self.id_anterior_bijouterie != self.datos_seleccionados_productos[1]:
			self.liststore_bijouterie.set_value(self.fila_anterior_bijouterie, 0, None)

		self.id_anterior_bijouterie=self.datos_seleccionados_productos[1]
		self.fila_anterior_bijouterie=iter
									#TARGET jugueteria
#-----------------------------------------------------------------------------------------------------------------
	def target_jugueteria(self,widget,event,data=None):
		self.tipo_producto="jugueteria"
		self.desbloquear_botones()
		if self.datos_seleccionados_productos != []:
			self.datos_seleccionados_productos=[]
		(model, iter) = self.treeselection_jugueteria.get_selected()
		for x in range(11):
			self.datos_seleccionados_productos.append(self.liststore_jugueteria.get_value(iter,x))
		self.datos_seleccionados_productos.append(iter)
		self.liststore_jugueteria.set_value(iter, 0, gtk.STOCK_MEDIA_PLAY)
		if self.id_anterior_merceria != 0:
			self.borrar_en_merceria()
		elif self.id_anterior_lana != 0:
			self.borrar_en_lana()
		elif self.id_anterior_ropa != 0:
			self.borrar_en_ropa()
		elif self.id_anterior_santeria != 0:
			self.borrar_en_santeria()
		elif self.id_anterior_regaleria != 0:
			self.borrar_en_regaleria()
		elif self.id_anterior_bijouterie != 0:
			self.borrar_en_bijouterie()

		if self.id_anterior_jugueteria != 0 and self.id_anterior_jugueteria != self.datos_seleccionados_productos[1]:
			self.liststore_jugueteria.set_value(self.fila_anterior_jugueteria, 0, None)

		self.id_anterior_jugueteria=self.datos_seleccionados_productos[1]
		self.fila_anterior_jugueteria=iter
									#TARGET regaleria
#-----------------------------------------------------------------------------------------------------------------
	def target_regaleria(self,widget,event,data=None):
		self.tipo_producto="regaleria"
		self.desbloquear_botones()
		if self.datos_seleccionados_productos != []:
			self.datos_seleccionados_productos=[]
		(model, iter) = self.treeselection_regaleria.get_selected()
		for x in range(11):
			self.datos_seleccionados_productos.append(self.liststore_regaleria.get_value(iter,x))
		self.datos_seleccionados_productos.append(iter)
		self.liststore_regaleria.set_value(iter, 0, gtk.STOCK_MEDIA_PLAY)
		if self.id_anterior_merceria != 0:
			self.borrar_en_merceria()
		elif self.id_anterior_lana != 0:
			self.borrar_en_lana()
		elif self.id_anterior_ropa != 0:
			self.borrar_en_ropa()
		elif self.id_anterior_jugueteria != 0:
			self.borrar_en_jugueteria()
		elif self.id_anterior_santeria != 0:
			self.borrar_en_santeria()
		elif self.id_anterior_bijouterie != 0:
			self.borrar_en_bijouterie()

		if self.id_anterior_regaleria != 0 and self.id_anterior_regaleria != self.datos_seleccionados_productos[1]:
			self.liststore_regaleria.set_value(self.fila_anterior_regaleria, 0, None)

		self.id_anterior_regaleria=self.datos_seleccionados_productos[1]
		self.fila_anterior_regaleria=iter
		
	def target_santeria(self,widget,event,data=None):
		self.tipo_producto="santeria"
		self.desbloquear_botones()
		if self.datos_seleccionados_productos != []:
			self.datos_seleccionados_productos=[]
		(model, iter) = self.treeselection_santeria.get_selected()
		for x in range(11):
			self.datos_seleccionados_productos.append(self.liststore_santeria.get_value(iter,x))
		self.datos_seleccionados_productos.append(iter)
		self.liststore_santeria.set_value(iter, 0, gtk.STOCK_MEDIA_PLAY)
		if self.id_anterior_merceria != 0:
			self.borrar_en_merceria()
		elif self.id_anterior_lana != 0:
			self.borrar_en_lana()
		elif self.id_anterior_ropa != 0:
			self.borrar_en_ropa()
		elif self.id_anterior_jugueteria != 0:
			self.borrar_en_jugueteria()
		elif self.id_anterior_regaleria != 0:
			self.borrar_en_regaleria()
		elif self.id_anterior_bijouterie != 0:
			self.borrar_en_bijouterie()

		if self.id_anterior_santeria != 0 and self.id_anterior_santeria != self.datos_seleccionados_productos[1]:
			self.liststore_santeria.set_value(self.fila_anterior_santeria, 0, None)

		self.id_anterior_santeria=self.datos_seleccionados_productos[1]
		self.fila_anterior_santeria=iter

	def bloquear_botones(self):
		self.button_eliminar_producto.set_sensitive(False)
		self.button_modificar_producto.set_sensitive(False)
		self.button_actualizar_producto.set_sensitive(False)

	def desbloquear_botones(self):
		self.button_eliminar_producto.set_sensitive(True)
		self.button_modificar_producto.set_sensitive(True)
		self.button_actualizar_producto.set_sensitive(True)


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	def mostrar_adm_stock(self,widget,self_ventana_principal):
		administrar_BD_stock(self,self_ventana_principal)

	def __init__(self,self_ventana_principal):

		self_ventana_principal.item_administrar_BDproducto.connect("activate",self.mostrar_adm_stock,self_ventana_principal)
	
		self.tipo_producto=""
		self.datos_seleccionados_productos=[]
		self.total_liststore_productos=[]

		self.id_anterior_merceria,self.fila_anterior_merceria=0,0
		self.id_anterior_lana,self.fila_anterior_lana=0,0
		self.id_anterior_ropa,self.fila_anterior_ropa=0,0
		self.id_anterior_jugueteria,self.fila_anterior_jugueteria=0,0
		self.id_anterior_regaleria,self.fila_anterior_regaleria=0,0
		self.id_anterior_santeria,self.fila_anterior_santeria=0,0
		self.id_anterior_bijouterie,self.fila_anterior_bijouterie=0,0

		image_agregar=gtk.Image()
		image_eliminar=gtk.Image()
		image_modificar=gtk.Image()
		image_actualizar=gtk.Image()
		image_buscar=gtk.Image()
		image_detalle=gtk.Image()

		image_agregar.set_from_file("../Images/agregar1.png")
		image_eliminar.set_from_file("../Images/eliminar1.png")
		image_modificar.set_from_file("../Images/modificar1.png")
		image_actualizar.set_from_file("../Images/actualizar1.png")
		image_buscar.set_from_file("../Images/buscar1.png")
		image_detalle.set_from_file("../Images/detalle.png")

		self.button_agregar_producto=gtk.Button()
		self.button_eliminar_producto=gtk.Button()
		self.button_modificar_producto=gtk.Button()
		self.button_actualizar_producto=gtk.Button()
		self.button_resumen = gtk.Button()
		self.button_buscar=gtk.Button()

		self.button_agregar_producto.add(image_agregar)
		self.button_eliminar_producto.add(image_eliminar)
		self.button_modificar_producto.add(image_modificar)
		self.button_actualizar_producto.add(image_actualizar)
		self.button_buscar.add(image_buscar)
		self.button_resumen.add(image_detalle)

		self.button_agregar_producto.set_size_request(120,50)
		self.button_eliminar_producto.set_size_request(120,50)
		self.button_modificar_producto.set_size_request(120,50)
		self.button_actualizar_producto.set_size_request(120,50)
		self.button_resumen.set_size_request(120,50)
		self.button_buscar.set_size_request(120,50)

		self.button_agregar_producto.set_property("relief",2)
		self.button_eliminar_producto.set_property("relief",2)
		self.button_modificar_producto.set_property("relief",2)
		self.button_actualizar_producto.set_property("relief",2)
		self.button_resumen.set_property("relief",2)
		self.button_buscar.set_property("relief",2)

		self.button_agregar_producto.set_property("can-focus",0)
		self.button_eliminar_producto.set_property("can-focus",0)
		self.button_modificar_producto.set_property("can-focus",0)
		self.button_actualizar_producto.set_property("can-focus",0)
		self.button_resumen.set_property("can-focus",0)
		self.button_buscar.set_property("can-focus",0)

		self.button_eliminar_producto.set_sensitive(False)
		self.button_modificar_producto.set_sensitive(False)
		self.button_actualizar_producto.set_sensitive(False)

		botonera_superior=gtk.HButtonBox()
		botonera_superior.set_property("layout-style",1)
		botonera_superior.set_size_request(1366,50)

		botonera_superior.pack_start(self.button_agregar_producto,False,False,0)
		botonera_superior.pack_start(self.button_eliminar_producto,False,False,0)
		botonera_superior.pack_start(self.button_modificar_producto,False,False,0)
		botonera_superior.pack_start(self.button_actualizar_producto,False,False,0)
		botonera_superior.pack_start(self.button_resumen,False,False,0)
		botonera_superior.pack_start(self.button_buscar,False,False,0)

		self_ventana_principal.vbox.pack_start(botonera_superior,False, False,2)

		separador=gtk.HSeparator()
		self_ventana_principal.vbox.pack_start(separador, False, False,2)

		self.notebook = gtk.Notebook()
		self.notebook.set_tab_pos(gtk.POS_TOP)
		self.notebook.set_size_request(1260,500)
		self.notebook.set_property("tab-border",7)
		self.notebook.set_property("enable-popup",1)

		self.scroll_win_merceria = gtk.ScrolledWindow()
		self.scroll_win_merceria.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)

		self.scroll_win_lana = gtk.ScrolledWindow()
		self.scroll_win_lana.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		
		self.scroll_win_ropa = gtk.ScrolledWindow()
		self.scroll_win_ropa.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		
		self.scroll_win_regaleria = gtk.ScrolledWindow()
		self.scroll_win_regaleria.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		
		self.scroll_win_jugueteria = gtk.ScrolledWindow()
		self.scroll_win_jugueteria.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		
		self.scroll_win_santeria = gtk.ScrolledWindow()
		self.scroll_win_santeria.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		
		self.scroll_win_bijouterie = gtk.ScrolledWindow()
		self.scroll_win_bijouterie.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)

		atributos = pango.AttrList()
		atributos.insert(pango.AttrSize(11000,0,-1))
		atributos.insert(pango.AttrWeight(1200,0,-1))

		lbl_merceria=gtk.Label("Merceria")
		lbl_lana=gtk.Label("Lana")
		lbl_ropa=gtk.Label("Ropa")
		lbl_regaleria=gtk.Label("Regaleria")
		lbl_jugueteria=gtk.Label("Jugueteria")
		lbl_santeria=gtk.Label("Santeria")
		lbl_bijouterie=gtk.Label("Bijouterie")

		lbl_merceria.set_attributes(atributos)
		lbl_lana.set_attributes(atributos)
		lbl_regaleria.set_attributes(atributos)
		lbl_santeria.set_attributes(atributos)
		lbl_jugueteria.set_attributes(atributos)
		lbl_ropa.set_attributes(atributos)
		lbl_bijouterie.set_attributes(atributos)

	#       PAGINA DE merceria

		self.liststore_merceria=gtk.ListStore(str,int,str,str,float,float,float,float,float,float,str,'gboolean')
		self.treeview_merceria=gtk.TreeView(self.liststore_merceria)
		self.total_liststore_productos.append(self.liststore_merceria)
		self.treeselection_merceria = self.treeview_merceria.get_selection()
		self.treeview_merceria.set_rules_hint(True)
		self.cell_merceria = gtk.CellRendererText()
		self.cell_merceria.set_property('size', 14000)
		self.cell_merceria.set_property("xalign",0.5)
		self.cell_merceria.set_property('weight', 700)
		self.cell_merceria.set_property('cell-background', '#71ACE2')
		self.cellpb_merceria = gtk.CellRendererPixbuf()
		self.cellpb_merceria.set_property('cell-background', '#71ACE2')
		self.cellpb_merceria.set_property("stock-size",3)
		columna_merceria=[]
		titulo_columna_merceria=("    ","#","Codigo","Descripcion","Costo","Precio","Ganancia","Stock inicial","Stock Dispnible","Punto Reposicion","Reponer")
		ultima = len(titulo_columna_merceria)
		for x in range(ultima):
			if x ==0:
				columna_merceria.append( gtk.TreeViewColumn(titulo_columna_merceria[x]) )
				columna_merceria[x].pack_start(self.cellpb_merceria,True)
				columna_merceria[x].set_attributes(self.cellpb_merceria,stock_id=x,cell_background_set=ultima)
			else:
				columna_merceria.append( gtk.TreeViewColumn(titulo_columna_merceria[x]) )
				columna_merceria[x].set_sort_column_id(x)
				columna_merceria[x].pack_start(self.cell_merceria,True)
				columna_merceria[x].set_expand(True)
				columna_merceria[x].set_attributes(self.cell_merceria, text=x,cell_background_set=ultima)
				columna_merceria[x].set_property("alignment",0.50)
			if x!=1 and x != 6:
				self.treeview_merceria.append_column(columna_merceria[x])
				
			self.treeview_merceria.set_search_column(x)

	#       PAGINA DE lana

		self.liststore_lana=gtk.ListStore(str,int,str,str,float,float,float,float,float,float,str,'gboolean')
		self.treeview_lana=gtk.TreeView(self.liststore_lana)
		self.total_liststore_productos.append(self.liststore_lana)
		self.treeselection_lana = self.treeview_lana.get_selection()
		self.treeview_lana.set_rules_hint(True)
		self.cell_lana = gtk.CellRendererText()
		self.cell_lana.set_property('size', 14000)
		self.cell_lana.set_property("xalign",0.5)
		self.cell_lana.set_property('weight', 700)
		self.cell_lana.set_property('cell-background', '#71ACE2')
		self.cellpb_lana = gtk.CellRendererPixbuf()
		self.cellpb_lana.set_property('cell-background', '#71ACE2')
		self.cellpb_lana.set_property("stock-size",3)
		columna_lana=[]
		titulo_columna_lana=("     ","#","Codigo","Descripcion","Costo","Precio","Ganancia","Stock inicial","Stock Disponible","Punto Reposicion","Reponer")
		ultima = len(titulo_columna_lana)
		for x in range(ultima):
			if x == 0:
				columna_lana.append( gtk.TreeViewColumn(titulo_columna_lana[x]) )
				columna_lana[x].pack_start(self.cellpb_lana,True)
				columna_lana[x].set_attributes(self.cellpb_lana,stock_id=0,cell_background_set=ultima)
			else:
				columna_lana.append( gtk.TreeViewColumn(titulo_columna_lana[x]) )
				columna_lana[x].set_sort_column_id(x)
				columna_lana[x].pack_start(self.cell_lana,True)
				columna_lana[x].set_expand(True)
				columna_lana[x].set_attributes(self.cell_lana, text=x,cell_background_set=ultima)
				columna_lana[x].set_property("alignment",0.50)
			if x!=1 and x !=6:
				self.treeview_lana.append_column(columna_lana[x])
			self.treeview_lana.set_search_column(x)


	#       PAGINA DE ropa

		titulo_columna_ropa=("     ","#","Codigo","Descripcion","Talle","Costo","Precio","Ganancia","Stock inicial","Stock Disponible","Punto Reposicion","Reponer")
		self.liststore_ropa=gtk.ListStore(str,int,str,str,float,float,float,int,int,int,int,str,'gboolean')
		self.treeview_ropa=gtk.TreeView(self.liststore_ropa)
		self.total_liststore_productos.append(self.liststore_ropa)
		self.treeselection_ropa = self.treeview_ropa.get_selection()
		self.treeview_ropa.set_rules_hint(True)
		self.cell_ropa = gtk.CellRendererText()
		self.cell_ropa.set_property('size', 14000)
		self.cell_ropa.set_property("xalign",0.5)
		self.cell_ropa.set_property('weight', 700)
		self.cell_ropa.set_property('cell-background', '#71ACE2')
		self.cellpb_ropa = gtk.CellRendererPixbuf()
		self.cellpb_ropa.set_property('cell-background', '#71ACE2')
		self.cellpb_ropa.set_property("stock-size",3)
		columna_ropa=[]
		ultima = len(titulo_columna_ropa)
		for x in range(ultima):
			if x ==0:
				columna_ropa.append( gtk.TreeViewColumn(titulo_columna_ropa[x]) )
				columna_ropa[x].pack_start(self.cellpb_ropa,True)
				columna_ropa[x].set_attributes(self.cellpb_ropa,stock_id=0,cell_background_set=ultima)
			else:
				columna_ropa.append( gtk.TreeViewColumn(titulo_columna_ropa[x]) )
				columna_ropa[x].set_sort_column_id(x)
				columna_ropa[x].pack_start(self.cell_ropa,True)
				columna_ropa[x].set_expand(True)
				columna_ropa[x].set_attributes(self.cell_ropa, text=x,cell_background_set=ultima)
				columna_ropa[x].set_property("alignment",0.50)
			if x!=1 and x !=4 and x !=7:
				self.treeview_ropa.append_column(columna_ropa[x])
			self.treeview_ropa.set_search_column(x)

	#       PAGINA DE regaleria

		titulo_columna_regaleria=("     ","#","Codigo","Descripcion","Costo","Precio","Ganancia","Stock inicial","Stock Disponible","Punto Reposicion","Reponer")
		self.liststore_regaleria=gtk.ListStore(str,int,str,str,float,float,int,int,int,int,str,'gboolean')
		self.treeview_regaleria=gtk.TreeView(self.liststore_regaleria)
		self.total_liststore_productos.append(self.liststore_regaleria)
		self.treeselection_regaleria = self.treeview_regaleria.get_selection()
		self.treeview_regaleria.set_rules_hint(True)
		self.cell_regaleria = gtk.CellRendererText()
		self.cell_regaleria.set_property('size', 14000)
		self.cell_regaleria.set_property("xalign",0.5)
		self.cell_regaleria.set_property('weight', 700)
		self.cell_regaleria.set_property('cell-background', '#71ACE2')
		self.cellpb_regaleria = gtk.CellRendererPixbuf()
		self.cellpb_regaleria.set_property('cell-background', '#71ACE2')
		self.cellpb_regaleria.set_property("stock-size",3)
		columna_regaleria=[]
		ultima = len(titulo_columna_regaleria)
		for x in range(ultima):
			if x ==0:
				columna_regaleria.append( gtk.TreeViewColumn(titulo_columna_regaleria[x]) )
				columna_regaleria[x].pack_start(self.cellpb_regaleria,True)
				columna_regaleria[x].set_attributes(self.cellpb_regaleria,stock_id=0,cell_background_set=ultima)
			else:
				columna_regaleria.append( gtk.TreeViewColumn(titulo_columna_regaleria[x]) )
				columna_regaleria[x].set_sort_column_id(x)
				columna_regaleria[x].set_expand(True)
				columna_regaleria[x].pack_start(self.cell_regaleria,True)
				columna_regaleria[x].set_attributes(self.cell_regaleria, text=x,cell_background_set=ultima)
				columna_regaleria[x].set_property("alignment",0.50)
			if x!=1:
				self.treeview_regaleria.append_column(columna_regaleria[x])
			self.treeview_regaleria.set_search_column(x)

	#       PAGINA DE jugueteria

		titulo_columna_jugueteria=("     ","#","Codigo","Descripcion","Costo","Precio","Ganancia","Stock inicial","Stock Disponible","Punto Reposicion","Reponer")
		self.liststore_jugueteria=gtk.ListStore(str,int,str,str,float,float,int,int,int,int,str,'gboolean')
		self.treeview_jugueteria=gtk.TreeView(self.liststore_jugueteria)
		self.total_liststore_productos.append(self.liststore_jugueteria)
		self.treeselection_jugueteria = self.treeview_jugueteria.get_selection()
		self.treeview_jugueteria.set_rules_hint(True)
		self.cell_jugueteria = gtk.CellRendererText()
		self.cell_jugueteria.set_property('size', 14000)
		self.cell_jugueteria.set_property("xalign",0.5)
		self.cell_jugueteria.set_property('weight', 700)
		self.cell_jugueteria.set_property('cell-background', '#71ACE2')
		self.cellpb_jugueteria = gtk.CellRendererPixbuf()
		self.cellpb_jugueteria.set_property('cell-background', '#71ACE2')
		self.cellpb_jugueteria.set_property("stock-size",3)
		columna_jugueteria=[]
		ultima = len(titulo_columna_jugueteria)
		for x in range(ultima):
			if x ==0:
				columna_jugueteria.append( gtk.TreeViewColumn(titulo_columna_jugueteria[x]) )
				columna_jugueteria[x].pack_start(self.cellpb_jugueteria,True)
				columna_jugueteria[x].set_attributes(self.cellpb_jugueteria,stock_id=0,cell_background_set=ultima)
			else:
				columna_jugueteria.append( gtk.TreeViewColumn(titulo_columna_jugueteria[x]) )
				columna_jugueteria[x].set_sort_column_id(x)
				columna_jugueteria[x].pack_start(self.cell_jugueteria,True)
				columna_jugueteria[x].set_expand(True)
				columna_jugueteria[x].set_attributes(self.cell_jugueteria, text=x,cell_background_set=ultima)
				columna_jugueteria[x].set_property("alignment",0.50)
			if x!=1 and x !=6:
				self.treeview_jugueteria.append_column(columna_jugueteria[x])
			self.treeview_jugueteria.set_search_column(x)

	#       PAGINA DE santeria
		titulo_columna_santeria=("     ","#","Codigo","Descripcion","Costo","Precio","Ganancia","Stock inicial","Stock Disponible","Punto Reposicion","Reponer")
		self.liststore_santeria=gtk.ListStore(str,int,str,str,float,float,int,int,int,int,str,'gboolean')
		self.treeview_santeria=gtk.TreeView(self.liststore_santeria)
		self.total_liststore_productos.append(self.liststore_santeria)
		self.treeselection_santeria = self.treeview_santeria.get_selection()
		self.treeview_santeria.set_rules_hint(True)
		#self.treeview_santeria.set_property("can-focus",0)
		self.cell_santeria = gtk.CellRendererText()
		self.cell_santeria.set_property('size', 14000)
		self.cell_santeria.set_property("xalign",0.5)
		self.cell_santeria.set_property('weight', 700)
		self.cell_santeria.set_property('cell-background', '#71ACE2')
		self.cellpb_santeria = gtk.CellRendererPixbuf()
		self.cellpb_santeria.set_property('cell-background', '#71ACE2')
		self.cellpb_santeria.set_property("stock-size",3)
		columna_santeria=[]
		ultima = len(titulo_columna_santeria)
		for x in range(ultima):
			if x ==0:
				columna_santeria.append( gtk.TreeViewColumn(titulo_columna_santeria[x]) )
				columna_santeria[x].pack_start(self.cellpb_santeria,True)
				columna_santeria[x].set_attributes(self.cellpb_santeria,stock_id=0,cell_background_set=ultima)
			else:
				columna_santeria.append( gtk.TreeViewColumn(titulo_columna_santeria[x]) )
				columna_santeria[x].set_sort_column_id(x)
				columna_santeria[x].pack_start(self.cell_santeria,True)
				columna_santeria[x].set_expand(True)
				columna_santeria[x].set_attributes(self.cell_santeria, text=x,cell_background_set=ultima)
				columna_santeria[x].set_property("alignment",0.50)
			if x!=1 and x !=6:
				self.treeview_santeria.append_column(columna_santeria[x])
			self.treeview_santeria.set_search_column(x)

	#       PAGINA DE bijouterie
		titulo_columna_bijouterie=("     ","#","Codigo","Descripcion","Costo","Precio","Ganancia","Stock inicial","Stock Disponible","Punto Reposicion","Reponer")
		self.liststore_bijouterie=gtk.ListStore(str,int,str,str,float,float,int,int,int,int,str,'gboolean')
		self.treeview_bijouterie=gtk.TreeView(self.liststore_bijouterie)
		self.total_liststore_productos.append(self.liststore_bijouterie)
		self.treeselection_bijouterie = self.treeview_bijouterie.get_selection()
		self.treeview_bijouterie.set_rules_hint(True)
		#self.treeview_bijouterie.set_property("can-focus",0)
		self.cell_bijouterie = gtk.CellRendererText()
		self.cell_bijouterie.set_property('size', 14000)
		self.cell_bijouterie.set_property("xalign",0.5)
		self.cell_bijouterie.set_property('weight', 700)
		self.cell_bijouterie.set_property('cell-background', '#71ACE2')
		self.cellpb_bijouterie = gtk.CellRendererPixbuf()
		self.cellpb_bijouterie.set_property('cell-background', '#71ACE2')
		self.cellpb_bijouterie.set_property("stock-size",3)
		columna_bijouterie=[]
		ultima = len(titulo_columna_bijouterie)
		for x in range(ultima):
			if x ==0:
				columna_bijouterie.append( gtk.TreeViewColumn(titulo_columna_bijouterie[x]) )
				columna_bijouterie[x].pack_start(self.cellpb_bijouterie,True)
				columna_bijouterie[x].set_attributes(self.cellpb_bijouterie,stock_id=0,cell_background_set=ultima)
			else:
				columna_bijouterie.append( gtk.TreeViewColumn(titulo_columna_bijouterie[x]) )
				columna_bijouterie[x].set_sort_column_id(x)
				columna_bijouterie[x].pack_start(self.cell_bijouterie,True)
				columna_bijouterie[x].set_expand(True)
				columna_bijouterie[x].set_attributes(self.cell_bijouterie, text=x,cell_background_set=ultima)
				columna_bijouterie[x].set_property("alignment",0.50)
			if x!=1 and x !=6:
				self.treeview_bijouterie.append_column(columna_bijouterie[x])
			self.treeview_bijouterie.set_search_column(x)

	 #---------------------------------------------------------------------------------------
	 
							#AGREGANDO TREEVIEW A LOS SCROLL WIN
		self.scroll_win_merceria.add(self.treeview_merceria)
		self.scroll_win_lana.add(self.treeview_lana)
		self.scroll_win_bijouterie.add(self.treeview_bijouterie)
		self.scroll_win_ropa.add(self.treeview_ropa)
		self.scroll_win_regaleria.add(self.treeview_regaleria)
		self.scroll_win_jugueteria.add(self.treeview_jugueteria)
		self.scroll_win_santeria.add(self.treeview_santeria)

	 #---------------------------------------------------------------------------------------
	 
	##########################################################################################
								#AÑADIENDO PAGINAS A LOS LIBROS
		self.notebook.append_page(self.scroll_win_merceria,lbl_merceria)
		self.notebook.append_page(self.scroll_win_lana,lbl_lana)
		self.notebook.append_page(self.scroll_win_bijouterie,lbl_bijouterie)
		self.notebook.append_page(self.scroll_win_ropa,lbl_ropa)
		self.notebook.append_page(self.scroll_win_regaleria,lbl_regaleria)
		self.notebook.append_page(self.scroll_win_jugueteria,lbl_jugueteria)
		self.notebook.append_page(self.scroll_win_santeria,lbl_santeria)

	##########################################################################################

		self_ventana_principal.fixed_stock=gtk.Fixed()
		image_wtf=gtk.Image()
		image_wtf.set_from_file("../Images/imagen_fondo.png")

		self_ventana_principal.fixed_stock.add(image_wtf)
		self_ventana_principal.frame_stock=gtk.Frame()
		self_ventana_principal.frame_stock.set_property("shadow-type",4)
		self_ventana_principal.frame_stock.add(self_ventana_principal.fixed_stock)

		self_ventana_principal.vbox.pack_start(self_ventana_principal.frame_stock, False, False,2)

		self_ventana_principal.fixed_stock.put(self.notebook,7,20)

		try:
			self.conectar_BD(self_ventana_principal)
		except:
			BD_no_especificada(self_ventana_principal)

		self.button_agregar_producto.connect("clicked",self.agregar_producto,self_ventana_principal)
		self.button_eliminar_producto.connect("clicked",self.eliminar_producto,self_ventana_principal)
		self.button_modificar_producto.connect("clicked",self.modificar_producto,self_ventana_principal)
		self.button_actualizar_producto.connect("clicked",self.actualizar_producto,self_ventana_principal)
		self.button_resumen.connect("clicked",win_registro_stock,self_ventana_principal)
		self.button_buscar.connect("clicked",consultas_stk,self,self_ventana_principal)

#=======================================================================================
#====================treeviews,merceria,lana,ropa,motores,repuestos===============

		self.treeview_merceria.connect("row_activated",self.target_merceria)
		self.treeview_lana.connect("row_activated",self.target_lana)
		self.treeview_ropa.connect("row_activated",self.target_ropa)
		self.treeview_regaleria.connect("row_activated",self.target_regaleria)
		self.treeview_jugueteria.connect("row_activated",self.target_jugueteria)
		self.treeview_bijouterie.connect("row_activated",self.target_bijouterie)
		self.treeview_santeria.connect("row_activated",self.target_santeria)


