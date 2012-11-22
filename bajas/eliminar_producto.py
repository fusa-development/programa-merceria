#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk
import pango
import sqlite3 as bdapi

import csv

from bbdd.leer_ruta_BD import leer_ruta

class eliminar_producto:

	def eliminar(self,widget,self_seccion_stock,self_ventana_principal):
		bbdd=bdapi.connect(leer_ruta() )
		cursor=bbdd.cursor()
		if self_seccion_stock.tipo_producto == "merceria":
			self_seccion_stock.total_liststore_productos[0].remove(self.fila_seleccionada)
			cursor.execute("DELETE FROM merceria WHERE codigo = ?",self.codigo)
			bbdd.commit()
			cursor.close()
			bbdd.close()
		elif self_seccion_stock.tipo_producto == "lana":
			self_seccion_stock.total_liststore_productos[1].remove(self.fila_seleccionada)
			cursor.execute("DELETE FROM lana WHERE codigo = ?",self.codigo)
			bbdd.commit()
			cursor.close()
			bbdd.close()
		elif self_seccion_stock.tipo_producto == "ropa":
			self_seccion_stock.total_liststore_productos[2].remove(self.fila_seleccionada)
			cursor.execute("DELETE FROM ropa WHERE codigo = ?",self.codigo)
			bbdd.commit()
			cursor.close()
			bbdd.close()
		elif self_seccion_stock.tipo_producto == "regaleria":
			self_seccion_stock.total_liststore_productos[3].remove(self.fila_seleccionada)
			cursor.execute("DELETE FROM regaleria WHERE codigo = ?",self.codigo)
			bbdd.commit()
			cursor.close()
			bbdd.close()
		elif self_seccion_stock.tipo_producto == "santeria":
			self_seccion_stock.total_liststore_productos[5].remove(self.fila_seleccionada)
			cursor.execute("DELETE FROM santeria WHERE codigo = ?",self.codigo)
			bbdd.commit()
			cursor.close()
			bbdd.close()
		elif self_seccion_stock.tipo_producto == "jugueteria":
			self_seccion_stock.total_liststore_productos[4].remove(self.fila_seleccionada)
			cursor.execute("DELETE FROM jugueteria WHERE codigo = ?",self.codigo)
			bbdd.commit()
			cursor.close()
			bbdd.close()
		elif self_seccion_stock.tipo_producto == "bijouterie":
			self_seccion_stock.total_liststore_productos[6].remove(self.fila_seleccionada)
			cursor.execute("DELETE FROM bijouterie WHERE codigo = ?",self.codigo)
			bbdd.commit()
			cursor.close()
			bbdd.close()
		self.window.destroy()
		self_ventana_principal.window.set_sensitive(True)

	def cerrar(self,widget,event,self_ventana_principal):
		self.window.destroy()
		self_ventana_principal.window.set_sensitive(True)

	def cerrar_button(self,widget,self_ventana_principal):
		self.window.destroy()
		self_ventana_principal.window.set_sensitive(True)


	def __init__(self,self_seccion_stock,self_ventana_principal):

		if self_seccion_stock.tipo_producto=="merceria":
			self.liststore_elejido=self_seccion_stock.total_liststore_productos[0]
		elif self_seccion_stock.tipo_producto=="lana":
			self.liststore_elejido=self_seccion_stock.total_liststore_productos[1]
		elif self_seccion_stock.tipo_producto=="ropa":
			self.liststore_elejido=self_seccion_stock.total_liststore_productos[2]
		elif self_seccion_stock.tipo_producto=="regaleria":
			self.liststore_elejido=self_seccion_stock.total_liststore_productos[3]
		elif self_seccion_stock.tipo_producto=="jugueteria":
			self.liststore_elejido=self_seccion_stock.total_liststore_productos[4]
		elif self_seccion_stock.tipo_producto=="santeria":
			self.liststore_elejido=self_seccion_stock.total_liststore_productos[5]
		elif self_seccion_stock.tipo_producto=="bijouterie":
			self.liststore_elejido=self_seccion_stock.total_liststore_productos[6]

		self_ventana_principal.window.set_sensitive(False)
		self.codigo = [self_seccion_stock.datos_seleccionados_productos[2]]

		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		icono="../Images/fusa_icon.png"
		self.window.set_icon(gtk.gdk.pixbuf_new_from_file(icono) )
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_title("Eliminar Producto")
		self.window.set_size_request(500,430)
		self.window.set_resizable(False)
		self.window.connect("delete-event",self.cerrar,self_ventana_principal)

		fixed=gtk.Fixed()
		self.window.add(fixed)

		atributos = pango.AttrList()
		atributos.insert(pango.AttrSize(12400,0,-1))
		atributos.insert(pango.AttrWeight(1200,0,-1))

		fuente_entrys="Sans 13"
#############################################################################################################

			#labels
		titulo_labels_generales=("Tipo de Producto : ","Codigo : ","Descripcion : ","Stock Disponible : ")
		labels_cordenadaY_generales=(50,100,150,200)
		self.labels_generales=[]
		for x in range(4):
			self.labels_generales.append(gtk.Label(titulo_labels_generales[x]) )
			self.labels_generales[x].set_attributes(atributos)
			fixed.put(self.labels_generales[x],70,labels_cordenadaY_generales[x])

			#entrys
		self.entry_generales=[]
		coordenadas_entryYgenerales=(47,97,147,197)
		for x in range(4):
			self.entry_generales.append( gtk.Entry() )
			font_entry_generales = pango.FontDescription(fuente_entrys)
			self.entry_generales[x].modify_font(font_entry_generales)
			self.entry_generales[x].set_size_request(200,26)
			fixed.put(self.entry_generales[x],230,coordenadas_entryYgenerales[x])
			self.entry_generales[x].set_editable(False)


			#mensaje
		self.vbox = gtk.VBox(False, 0)
		self.vbox.set_size_request(500,25)
		label_pregunta=gtk.Label("¿Desea eliminar el Producto?")
		label_pregunta.set_attributes(atributos)
		self.vbox.pack_start(label_pregunta,False,True, 0)
		fixed.put(self.vbox,0,330)

									#BOTONES
###############################################################################################################
		self.botones=[]
		imagenes=[]
		ruta_imagenes=("../Images/boton_aceptar.png","../Images/boton_cancelar.png")
		for x in range(2):
			imagenes.append(gtk.Image() )
			self.botones.append( gtk.Button() )
			self.botones[x].set_property("relief",2)
			self.botones[x].set_property("can-focus",0)
			self.botones[x].set_size_request(130,40)
			imagenes[x].set_from_file(ruta_imagenes[x])
			self.botones[x].add(imagenes[x] )

		fixed.put(self.botones[0],110,370)
		fixed.put(self.botones[1],260,370)

		self.botones[0].connect("clicked",self.eliminar,self_seccion_stock,self_ventana_principal)
		self.botones[1].connect("clicked",self.cerrar_button,self_ventana_principal)

		b=len(self_seccion_stock.datos_seleccionados_productos)
		self.fila_seleccionada=self_seccion_stock.datos_seleccionados_productos[b-1]

		if self_seccion_stock.tipo_producto=="ropa":
			fila_stock_disponible=9
		else:
			fila_stock_disponible=8

		self.entry_generales[0].set_text(self_seccion_stock.tipo_producto)
		self.entry_generales[1].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,2)) )
		self.entry_generales[2].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,3)) )
		self.entry_generales[3].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,fila_stock_disponible)) )

		self.window.show_all()
