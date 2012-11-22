#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import pygtk
import pango
import sqlite3 as bdapi

import csv

from bbdd.leer_ruta_BD import leer_ruta

class actualizar_producto():


	def delete_event(self,widget,event,self_ventana_principal):
		self_ventana_principal.window.set_sensitive(True)
		self.window.destroy()


	def destroy (self,widget,self_ventana_principal):
		self_ventana_principal.window.set_sensitive(True)
		self.window.destroy()

	def calcular_reponer(self,cantidad,cantidad_minima):

		if float(cantidad_minima) >=float(cantidad):
			reponer="Si"
		else:
			reponer="No"
		return reponer
#-----------------------------------------------------------------------------------------------------------------
	def calcular_pintar(self,cantidad,cantidad_minima):
		if float(cantidad_minima) >=float(cantidad):
			pintar=True
		else:
			pintar=False
		return pintar


	def actualizar(self,widget,self_seccion_stock,self_ventana_principal):
		bbdd=bdapi.connect(leer_ruta() )
		cursor=bbdd.cursor()
		nombre_bd=self_seccion_stock.tipo_producto.lower()
		if self_seccion_stock.tipo_producto!="ropa":
			self.liststore_elejido.set_value(self.fila_seleccionada,6,self.pin_generales[0].get_value())#ganancia
			self.liststore_elejido.set_value(self.fila_seleccionada,7,self.pin_generales[1].get_value()) #stk inical
			self.liststore_elejido.set_value(self.fila_seleccionada,8,self.pin_generales[2].get_value()) #stk disponible
			self.liststore_elejido.set_value(self.fila_seleccionada,9,self.pin_generales[3].get_value()) #pnt rep
			self.liststore_elejido.set_value(self.fila_seleccionada,10,self.calcular_reponer(self.pin_generales[2].get_value(),self.pin_generales[3].get_value()) ) #reponer
			self.liststore_elejido.set_value(self.fila_seleccionada,11,self.calcular_pintar(self.pin_generales[2].get_value(),self.pin_generales[3].get_value()) ) #pintar
			valores_update=[]
			for x in range(4):
				valores_update.append(self.pin_generales[x].get_value() )
			valores_update.append(self.calcular_pintar(self.pin_generales[2].get_value(),self.pin_generales[3].get_value() ) )
			valores_update.append(self_seccion_stock.datos_seleccionados_productos[2] )
		else:
			self.liststore_elejido.set_value(self.fila_seleccionada,7,self.pin_generales[0].get_value()) #ganancia
			self.liststore_elejido.set_value(self.fila_seleccionada,8,self.pin_generales[1].get_value()) #stock inicial
			self.liststore_elejido.set_value(self.fila_seleccionada,9,self.pin_generales[2].get_value()) #stock disponible
			self.liststore_elejido.set_value(self.fila_seleccionada,10,self.pin_generales[3].get_value())#punto reposicion
			self.liststore_elejido.set_value(self.fila_seleccionada,11,self.calcular_reponer(self.pin_generales[2].get_value(),self.pin_generales[3].get_value()) )#reponer
			self.liststore_elejido.set_value(self.fila_seleccionada,12,self.calcular_pintar(self.pin_generales[2].get_value(),self.pin_generales[3].get_value()) )#pintar
			valores_update=[]
			for x in range(4):
				valores_update.append(self.pin_generales[x].get_value() )
			valores_update.append(self.calcular_pintar(self.pin_generales[2].get_value(),self.pin_generales[3].get_value() ) )
			valores_update.append(self_seccion_stock.datos_seleccionados_productos[2] )
		cursor.execute("UPDATE "+str(nombre_bd)+" SET ganancia=? , stk_ini=?, stk_disp=?, pnt_rep=? ,aviso=? WHERE codigo = ?",valores_update)

		bbdd.commit()
		cursor.close()
		bbdd.close()
		self.window.destroy()
		self_ventana_principal.window.set_sensitive(True)


	def __init__(self,self_ventana_principal,self_seccion_stock):

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

		icono="../Imagenes/fusa_icon.png"
		self_ventana_principal.window.set_sensitive(False)
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("delete_event",self.delete_event,self_ventana_principal)
		self.window.set_title("Actualizar Producto")
		self.window.set_resizable(False)
		self.window.set_position(gtk.WIN_POS_CENTER)
		#self.window.set_icon(gtk.gdk.pixbuf_new_from_file(icono) )
		self.window.set_size_request(700,400)
		image_fondo=gtk.Image()
		#image_fondo.set_from_file("../Imagenes/background2.svg")

		self.fixed_generales=gtk.Fixed()
		self.fixed_generales.add(image_fondo)
		self.window.add(self.fixed_generales)

		atributos = pango.AttrList()
		atributos.insert(pango.AttrSize(14000,0,-1))
		atributos.insert(pango.AttrWeight(700,0,-1))

		fuente_entrys="Sans 13"
		font_entry = pango.FontDescription(fuente_entrys)

		self.tipo_producto=gtk.Label("Tipo de Producto : ")
		self.tipo_producto.set_attributes(atributos)
		self.fixed_generales.put(self.tipo_producto,20,30)

		self.entry_tipo_producto=gtk.Entry()
		self.entry_tipo_producto.modify_font(font_entry)
		self.fixed_generales.put(self.entry_tipo_producto,190,28)
		self.entry_tipo_producto.set_property("editable",0)

		self.entry_tipo_producto.set_text(self_seccion_stock.tipo_producto)

		self.codigo_producto=gtk.Label("Codigo : ")
		self.codigo_producto.set_attributes(atributos)
		self.fixed_generales.put(self.codigo_producto,385,30)

		self.entry_codigo_producto=gtk.Entry()
		self.entry_codigo_producto.modify_font(font_entry)
		self.entry_codigo_producto.set_size_request(210,30)
		self.entry_codigo_producto.set_property("editable",0)
		self.fixed_generales.put(self.entry_codigo_producto,470,28)

		self.entry_codigo_producto.set_text(self_seccion_stock.datos_seleccionados_productos[2])

		titulo_labels_generales=("Ganancia : ","Stock Inicial : ","Stock Disponible : ","Punto Reposicion : ")
		#labels_cordenadaY_generales=(102,172,242,312)
		labels_cordenadaY_generales=(102,152,202,252)
		self.labels_generales=[]
		for x in range(4):
			self.labels_generales.append(gtk.Label(titulo_labels_generales[x]) )
			self.labels_generales[x].set_attributes(atributos)
			self.fixed_generales.put(self.labels_generales[x],180,labels_cordenadaY_generales[x])

		self.pin_generales=[]
		adj_generales=[]
		#coordenadasY=(100,170,240,310)
		coordenadasY=(100,150,200,250)
		if self_seccion_stock.tipo_producto=="merceria" or self_seccion_stock.tipo_producto=="lana":
			for x in range(4):
				adj_generales.append( gtk.Adjustment(value=0, lower=0, upper=999,step_incr=0.1,page_incr=0.1,page_size=0) )
				self.pin_generales.append ( gtk.SpinButton(adjustment=adj_generales[x], climb_rate=1.0, digits=2) )
				self.pin_generales[x].set_numeric(True)
				self.pin_generales[x].set_size_request(120,28)
				#self.pin_generales[x].set_max_length(3)
				font_spin_generales = pango.FontDescription(fuente_entrys)
				self.pin_generales[x].modify_font(font_spin_generales)
				self.fixed_generales.put(self.pin_generales[x],390,coordenadasY[x])
		else:
			for x in range(4):
				adj_generales.append( gtk.Adjustment(value=0, lower=0, upper=999,step_incr=1,page_incr=1,page_size=0) )
				self.pin_generales.append ( gtk.SpinButton(adjustment=adj_generales[x], climb_rate=1.0, digits=0) )
				self.pin_generales[x].set_numeric(True)
				self.pin_generales[x].set_size_request(120,28)
				#self.pin_generales[x].set_max_length(3)
				font_spin_generales = pango.FontDescription(fuente_entrys)
				self.pin_generales[x].modify_font(font_spin_generales)
				self.fixed_generales.put(self.pin_generales[x],390,coordenadasY[x])

		b=len(self_seccion_stock.datos_seleccionados_productos)
		self.fila_seleccionada=self_seccion_stock.datos_seleccionados_productos[b-1]

		if self_seccion_stock.tipo_producto!="ropa":
			self.pin_generales[0].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,6) )#ganancia
			self.pin_generales[1].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,7) )#stk ini
			self.pin_generales[2].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,8) )#stk dis
			self.pin_generales[3].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,9) )#pnt rep
		else:
			self.pin_generales[0].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,7) )
			self.pin_generales[1].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,8) )
			self.pin_generales[2].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,9) )
			self.pin_generales[3].set_value(self.liststore_elejido.get_value(self.fila_seleccionada,10) )


						#botones
		self.botones_totales=[]
		imagenes=[]
		ruta_imagenes=("../Images/boton_aceptar.png","../Images/boton_cerrar.png")

		for x in range(2):
			imagenes.append(gtk.Image() )
			self.botones_totales.append( gtk.Button() )
			self.botones_totales[x].set_property("relief",2)
			#self.botones_totales[x].set_property("can-focus",0)
			self.botones_totales[x].set_size_request(120,40)
			imagenes[x].set_from_file(ruta_imagenes[x])
			self.botones_totales[x].add(imagenes[x] )

		self.botones_totales[0].connect("clicked",self.actualizar,self_seccion_stock,self_ventana_principal)
		self.botones_totales[1].connect("clicked",self.destroy,self_ventana_principal)
		self.vbox1 = gtk.VBox(False, 0)
		self.vbox1.set_size_request(700,40)

		botonera=gtk.HButtonBox()
		botonera.set_property("layout-style",1)
		self.vbox1.pack_start(botonera,False, False,2)
		botonera.pack_start(self.botones_totales[0],False,True,0)
		botonera.pack_start(self.botones_totales[1],False,True,0)

		self.fixed_generales.put(self.vbox1,0,350)

		self.window.show_all()

