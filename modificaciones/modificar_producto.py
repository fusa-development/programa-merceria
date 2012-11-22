#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk
import pango
import sqlite3 as bdapi

import csv

from bbdd.leer_ruta_BD import leer_ruta

class modificar_producto:

	def aceptar_datos(self,widget,self_seccion_stock,self_ventana_principal):
		b=len(self_seccion_stock.datos_seleccionados_productos)
		iter=self_seccion_stock.datos_seleccionados_productos[b-1]
		bbdd=bdapi.connect(leer_ruta() )
		cursor=bbdd.cursor()

		if self_seccion_stock.tipo_producto !="ropa":
			valores_update=[]
			for x in range(4):
				valores_update.append( self.entry_generales[x+1].get_text() )
			#valores_update.append(self.pin_generales.get_text() )
			valores_update.append( self.codigo_anterior )
			self.liststore_elejido.set_value(iter,2,self.entry_generales[1].get_text())#codigo
			self.liststore_elejido.set_value(iter,3,self.entry_generales[2].get_text())#descripcion
			self.liststore_elejido.set_value(iter,4,float(self.entry_generales[3].get_text() ))#costo
			self.liststore_elejido.set_value(iter,5,float(self.entry_generales[4].get_text() ))#precio
			#self.liststore_elejido.set_value(iter,6,int(self.pin_generales.get_text() ))#ganancia
			nombre_bd=self_seccion_stock.tipo_producto.lower()#wtf!!
			cursor.execute("UPDATE "+str(nombre_bd)+" SET codigo=? , descripcion=?, costo=?, precio=? WHERE codigo = ?",valores_update)
			
		else:
			valores_update=[]
			for x in range(4):
				valores_update.append( self.entry_ropa[x+1].get_text() )
			#valores_update.append(1)
			#valores_update.append( self.pin_ropa.get_text() )
			valores_update.append( self.codigo_anterior )
			self_seccion_stock.liststore_ropa.set_value(iter,2,self.entry_ropa[1].get_text())
			self_seccion_stock.liststore_ropa.set_value(iter,3,self.entry_ropa[2].get_text())
			#self_seccion_stock.liststore_ropa.set_value(iter,4,int(self.pin_talle.get_text()))
			self_seccion_stock.liststore_ropa.set_value(iter,5,float(self.entry_ropa[3].get_text() ))
			self_seccion_stock.liststore_ropa.set_value(iter,6,float(self.entry_ropa[4].get_text()))
			#self_seccion_stock.liststore_ropa.set_value(iter,7,int(self.pin_ropa.get_text()) )

			cursor.execute("UPDATE ropa SET codigo=? , descripcion=?, costo=?, precio=? WHERE codigo = ?",valores_update)
		bbdd.commit()
		cursor.close()
		bbdd.close()
		self.window.destroy()
		self_ventana_principal.window.set_sensitive(True)


	def entrys_correctos_generales(self,widget):
		if self.codigo_generales_ok and self.costo_generales_ok and self.precio_generales_ok:
			self.botones[0].set_sensitive(True)
		else:
			self.botones[0].set_sensitive(False)

	def entrys_correctos_ropa(self,widget):
		if self.codigo_ropa_ok and self.costo_ropa_ok and self.precio_ropa_ok:
			self.botones[0].set_sensitive(True)
		else:
			self.botones[0].set_sensitive(False)

	def codigo_no_repetido(self,self_seccion_stock):
		repetido=False
		for x in range(len(self.liststore_elejido) ):
			if self.liststore_elejido[x][2] == self.entry_generales[1].get_text() and self.liststore_elejido[x][1] != self_seccion_stock.datos_seleccionados_productos[1]:
				repetido=True
				break
		if repetido:
			return True
		else:
			return False

	def codigo_no_repetidoROPA(self,self_seccion_stock):
		repetido=False
		for x in range(len(self.liststore_elejido) ):
			if self.liststore_elejido[x][2] == self.entry_ropa[1].get_text() and self.liststore_elejido[x][1] != self_seccion_stock.datos_seleccionados_productos[1]:
				repetido=True
				break
		if repetido:
			return True
		else:
			return False

	def validar_codigo_generales(self,widget,self_seccion_stock):

		if self.entry_generales[1].get_text() != "":
			if not self.codigo_no_repetido(self_seccion_stock):
				self.codigo_generales_ok=True
				self.label_cuit_incorrecto_generales.set_text("")
			else:
				self.codigo_generales_ok=False
				self.label_cuit_incorrecto_generales.set_text("Repetido.")
		else:
			self.codigo_generales_ok=False
			self.label_cuit_incorrecto_generales.set_text("Incorrecto.")


	def verificar_costo_generales(self,widget):
		if self.entry_generales[3].get_text() != "":
			try:
				float(self.entry_generales[3].get_text() )
				self.costo_generales_ok=True
				self.label_costo_incorrecto_generales.set_text("")
			except ValueError :
					self.label_costo_incorrecto_generales.set_text("Invalido.")
					self.costo_generales_ok=False
		else:
			self.csto_generales_ok=False
			self.label_costo_incorrecto_generales.set_text("Invalido.")

	def verificar_precio_generales(self,widget):
		if self.entry_generales[4].get_text() != "":
			try:
				float(self.entry_generales[4].get_text() )
				self.precio_generales_ok=True
				self.label_precio_incorrecto_generales.set_text("")
			except ValueError :
					self.label_precio_incorrecto_generales.set_text("Invalido.")
					self.precio_generales_ok=False
		else:
			self.precio_generales_ok=False
			self.label_precio_incorrecto_generales.set_text("Invalido.")


	def validar_codigo_ropa(self,widget,self_seccion_stock):
		self.liststore_elejido=self_seccion_stock.total_liststore_productos[2]
		if self.entry_ropa[1].get_text() != "":
			if not self.codigo_no_repetidoROPA(self_seccion_stock):
				self.codigo_ropa_ok=True
				self.label_cuit_incorrecto_ropa.set_text("")
			else:
				self.label_cuit_incorrecto_ropa.set_text("Repetido.")
				self.codigo_ropa_ok=False
		else:
			self.label_cuit_incorrecto_ropa.set_text("Incorrecto.")
			self.codigo_ropa_ok=False

	def verificar_costo_ropa(self,widget):
		if self.entry_ropa[3].get_text() != "":
			try:
				float(self.entry_ropa[3].get_text() )
				self.costo_ropa_ok=True
				self.label_costo_incorrecto_ropa.set_text("")
			except ValueError :
					self.label_costo_incorrecto_ropa.set_text("Invalido.")
					self.costo_ropa_ok=False
		else:
			self.costo_ropa_ok=False
			self.label_costo_incorrecto_ropa.set_text("Invalido.")

	def verificar_precio_ropa(self,widget):
		if self.entry_ropa[4].get_text() != "":
			try:
				float(self.entry_ropa[4].get_text() )
				self.precio_ropa_ok=True
				self.label_precio_incorrecto_ropa.set_text("")
			except ValueError :
					self.label_precio_incorrecto_ropa.set_text("Invalido.")
					self.precio_ropa_ok=False
		else:
			self.precio_ropa_ok=False
			self.label_precio_incorrecto_ropa.set_text("Invalido.")


	def cerrar(self,widget,event,self_ventana_principal):
		self.window.destroy()
		self_ventana_principal.window.set_sensitive(True)

	def cerrar_button(self,widget,self_ventana_principal):
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


		self.codigo_generales_ok,self.costo_generales_ok,self.precio_generales_ok=False,False,False
		self.codigo_ropa_ok,self.costo_ropa_ok,self.precio_ropa_ok=False,False,False

		self_ventana_principal.window.set_sensitive(False)
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		icono="../Images/fusa_icon.png"
		self.window.set_icon(gtk.gdk.pixbuf_new_from_file(icono) )
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_title("Modificar Producto")
		self.window.set_size_request(500,400)
		self.window.set_resizable(False)
		self.window.connect("delete-event",self.cerrar,self_ventana_principal)

		image_fondo=gtk.Image()
		#image_fondo.set_from_file("../Images/fondo_eliminar_producto.png")

		fixed=gtk.Fixed()
		fixed.add(image_fondo)
		self.window.add(fixed)

		atributos = pango.AttrList()
		atributos.insert(pango.AttrSize(12400,0,-1))
		atributos.insert(pango.AttrWeight(1200,0,-1))

		fuente_entrys="Sans 13"
									#generales
#############################################################################################################
		self.fixed_generales=gtk.Fixed()
		fixed.put(self.fixed_generales,90,20)

		titulo_labels_generales=("Tipo de Producto : ","Codigo : ","Descripcion : ","Costo : ","Precio : ")
		labels_cordenadaY_generales=(0,50,100,150,200)
		self.labels_generales=[]
		for x in range(5):
			self.labels_generales.append(gtk.Label(titulo_labels_generales[x]) )
			self.labels_generales[x].set_attributes(atributos)
			self.fixed_generales.put(self.labels_generales[x],-40,labels_cordenadaY_generales[x])


		self.label_cuit_incorrecto_generales=gtk.Label()
		self.label_cuit_incorrecto_generales.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_generales.put(self.label_cuit_incorrecto_generales,318,50)

		self.label_costo_incorrecto_generales=gtk.Label()
		self.label_costo_incorrecto_generales.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_generales.put(self.label_costo_incorrecto_generales,318,150)

		self.label_precio_incorrecto_generales=gtk.Label()
		self.label_precio_incorrecto_generales.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_generales.put(self.label_precio_incorrecto_generales,318,200)



		self.entry_generales=[]
		coordenadas_entryYgenerales=(-3,47,97,147,197)
		for x in range(5):
			self.entry_generales.append( gtk.Entry() )
			font_entry_generales = pango.FontDescription(fuente_entrys)
			self.entry_generales[x].modify_font(font_entry_generales)
			self.entry_generales[x].set_size_request(200,26)
			self.fixed_generales.put(self.entry_generales[x],110,coordenadas_entryYgenerales[x])
			if x ==0:
				self.entry_generales[x].set_property("editable",0)

		self.entry_generales[1].connect("changed",self.validar_codigo_generales,self_seccion_stock)
		self.entry_generales[3].connect("changed",self.verificar_costo_generales)
		self.entry_generales[4].connect("changed",self.verificar_precio_generales)

		self.entry_generales[1].connect("changed",self.entrys_correctos_generales)
		self.entry_generales[3].connect("changed",self.entrys_correctos_generales)
		self.entry_generales[4].connect("changed",self.entrys_correctos_generales)

		adj_generales=gtk.Adjustment(value=0, lower=1, upper=999,step_incr=1,page_incr=1,page_size=0)
		self.pin_generales=gtk.SpinButton(adjustment=adj_generales, climb_rate=1.0, digits=0)
		self.pin_generales.set_numeric(True)
		self.pin_generales.set_size_request(80,28)
		self.pin_generales.set_max_length(7)
		font_spin_generales = pango.FontDescription(fuente_entrys)
		self.pin_generales.modify_font(font_spin_generales)
		#self.fixed_generales.put(self.pin_generales,110,247)


									#ROPA
#############################################################################################################
		self.fixed_ropa=gtk.Fixed()
		fixed.put(self.fixed_ropa,90,20)

		titulo_labels_ropa=("Tipo de Producto : ","Codigo : ","Descripcion : ","Costo : ","Precio : ")
		labels_cordenadaY_ropa=(0,50,100,150,200)
		self.labels_ropa=[]
		for x in range(5):
			self.labels_ropa.append(gtk.Label(titulo_labels_ropa[x]) )
			self.labels_ropa[x].set_attributes(atributos)
			self.fixed_ropa.put(self.labels_ropa[x],-40,labels_cordenadaY_ropa[x])


		self.label_cuit_incorrecto_ropa=gtk.Label()
		self.label_cuit_incorrecto_ropa.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_ropa.put(self.label_cuit_incorrecto_ropa,318,50)

		self.label_costo_incorrecto_ropa=gtk.Label()
		self.label_costo_incorrecto_ropa.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_ropa.put(self.label_costo_incorrecto_ropa,318,150)

		self.label_precio_incorrecto_ropa=gtk.Label()
		self.label_precio_incorrecto_ropa.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_ropa.put(self.label_precio_incorrecto_ropa,318,200)



		self.entry_ropa=[]
		coordenadas_entryYropa=(-3,47,97,147,197)
		for x in range(5):
			self.entry_ropa.append( gtk.Entry() )
			font_entry_ropa = pango.FontDescription(fuente_entrys)
			self.entry_ropa[x].modify_font(font_entry_ropa)
			self.entry_ropa[x].set_size_request(200,26)
			self.fixed_ropa.put(self.entry_ropa[x],110,coordenadas_entryYropa[x])
			if x ==0:
				self.entry_ropa[x].set_property("editable",0)

		self.entry_ropa[1].connect("changed",self.validar_codigo_ropa,self_seccion_stock)
		self.entry_ropa[3].connect("changed",self.verificar_costo_ropa)
		self.entry_ropa[4].connect("changed",self.verificar_precio_ropa)

		self.entry_ropa[1].connect("changed",self.entrys_correctos_ropa)
		self.entry_ropa[3].connect("changed",self.entrys_correctos_ropa)
		self.entry_ropa[4].connect("changed",self.entrys_correctos_ropa)

		adj_ropa=gtk.Adjustment(value=0, lower=1, upper=999,step_incr=1,page_incr=1,page_size=0)
		self.pin_ropa=gtk.SpinButton(adjustment=adj_ropa, climb_rate=1.0, digits=0)
		self.pin_ropa.set_numeric(True)
		self.pin_ropa.set_size_request(80,28)
		self.pin_ropa.set_max_length(3)
		font_spin_ropa = pango.FontDescription(fuente_entrys)
		self.pin_ropa.modify_font(font_spin_ropa)
		#self.fixed_ropa.put(self.pin_ropa,110,247)


									#BOTONES
###############################################################################################################
		self.botones=[]
		imagenes=[]
		ruta_imagenes=("../Images/boton_aceptar.png","../Images/boton_cerrar.png")
		for x in range(2):
			imagenes.append(gtk.Image() )
			self.botones.append( gtk.Button() )
			self.botones[x].set_property("relief",2)
			self.botones[x].set_property("can-focus",0)
			self.botones[x].set_size_request(130,40)
			imagenes[x].set_from_file(ruta_imagenes[x])
			self.botones[x].add(imagenes[x] )

		fixed.put(self.botones[0],110,340)
		fixed.put(self.botones[1],260,340)

		self.botones[0].connect("clicked",self.aceptar_datos,self_seccion_stock,self_ventana_principal)

		self.botones[1].connect("clicked",self.cerrar_button,self_ventana_principal)

		self.window.show_all()
		self.botones[0].set_sensitive(False)
		self.fixed_generales.hide()
		self.fixed_ropa.hide()

		b=len(self_seccion_stock.datos_seleccionados_productos)
		self.fila_seleccionada=self_seccion_stock.datos_seleccionados_productos[b-1]

		if self_seccion_stock.tipo_producto !="ropa":
			self.entry_generales[0].set_text(self_seccion_stock.tipo_producto)
			self.entry_generales[1].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,2)) )
			self.entry_generales[2].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,3)) )
			self.entry_generales[3].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,4)) )
			self.entry_generales[4].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,5)) )
			self.fixed_generales.show()
			self.codigo_anterior=self.entry_generales[1].get_text()
		else:
			self.entry_ropa[0].set_text(self_seccion_stock.tipo_producto)
			self.entry_ropa[1].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,2) ) )
			self.entry_ropa[2].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,3) ) )
			self.entry_ropa[3].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,5) ) )
			self.entry_ropa[4].set_text(str(self.liststore_elejido.get_value(self.fila_seleccionada,6) ) )
			self.codigo_anterior=self.entry_ropa[1].get_text()
			self.fixed_ropa.show()
