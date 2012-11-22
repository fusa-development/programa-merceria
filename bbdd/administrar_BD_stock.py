#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk
import pango

from buscar_BD import *
from indicar_ruta_BD import *
from indicar_ruta_backup import *

class administrar_BD_stock:

	def realizar_backup(self,widget):
		indicar_ruta_backup(self.window)

	def cerrar(self,widget,event,self_ventana_principal):
		self_ventana_principal.window.set_sensitive(True)

	def cerrar_boton(self,widget,self_ventana_principal):
		self.window.destroy()
		self_ventana_principal.window.set_sensitive(True)


	def __init__(self,self_seccion_stock,self_ventana_principal):
		self_ventana_principal.window.set_sensitive(False)
		icono="../Images/fusa_icon.png"
		self.window=gtk.Window()
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_resizable(False)
		self.window.set_title("Administrar Base De Datos Stock")
		self.window.set_icon(gtk.gdk.pixbuf_new_from_file(icono) )
		self.window.set_size_request(620,400)
		self.window.connect("delete_event",self.cerrar,self_ventana_principal)

		image_fondo=gtk.Image()
		#image_fondo.set_from_file("../Images/fondo_amdBD.png")

		fixed_principal=gtk.Fixed()
		fixed_principal.add(image_fondo)
		self.window.add(fixed_principal)

		atributos = pango.AttrList()
		atributos.insert(pango.AttrSize(11000,0,-1))
		atributos.insert(pango.AttrWeight(1200,0,-1))

		label=gtk.Label()
		label.set_markup("<b>Base de Datos Stock</b>")
		label.set_use_markup(True)
		frame=gtk.Frame()
		frame.set_label_widget(label)
		frame.set_property("shadow-type",4)
		frame.set_size_request(600,310)
		fixed_principal.put(frame,10,30)
		fixed_frame=gtk.Fixed()
		frame.add(fixed_frame)

		self.button_backup=gtk.Button("Realizar Backup")

		self.radio_crear=gtk.RadioButton(None,"Crear")
		self.radio_crear.set_property("tooltip-text","Crear una nueva Base de Datos")
		self.radio_especificar=gtk.RadioButton(self.radio_crear,"Especificar")
		self.radio_especificar.set_property("tooltip-text","Buscar una Base de Datos existente")
		self.radio_otras=gtk.RadioButton(self.radio_crear,"Backup")
		self.radio_otras.set_property("tooltip-text","Indique el lugar donde desea \nrealizar el Backup")

		fixed_frame.put(self.button_backup,410,70)

		self.button_cerrar=gtk.Button("Cerrar")
		#self.button_cerrar.set_property("relief",2)
		self.button_cerrar.set_size_request(90,40)

		fixed_principal.put(self.button_cerrar,520,355)
		fixed_frame.put(self.radio_crear,40,30)
		fixed_frame.put(self.radio_especificar,250,30)
		fixed_frame.put(self.radio_otras,400,30)

		self.button_buscar=gtk.Button("Buscar...")
		fixed_frame.put(self.button_buscar,260,70)

		self.vbox = gtk.VBox(False, 0)

		label_nombre=gtk.Label("Nombre : ")
		self.entry_new_BD=gtk.Entry(12)

		self.hcaja_crear=gtk.HBox()
		self.hcaja_crear.set_size_request(200,40)
		self.hcaja_crear.set_property("homogeneous",0)
		self.hcaja_crear.pack_start(label_nombre,False,True,1)
		self.hcaja_crear.pack_start(self.entry_new_BD,True,True,1)
		self.vbox.pack_start(self.hcaja_crear,False,True,1)

		fixed_ruta=gtk.Fixed()
		self.frame_ruta=gtk.Frame("Ruta de Archivo")
		self.frame_ruta.set_property("shadow-type",4)
		self.frame_ruta.set_size_request(200,130)
		self.frame_ruta.add(fixed_ruta)

		self.radio_predeterminada=gtk.RadioButton(None,"Predeterminada")
		self.radio_indicar=gtk.RadioButton(self.radio_predeterminada,"Indicar")
		self.radio_indicar.set_property("tooltip-text","Especifique la ruta donde desea\nalojar la nueva Base de Datos")
		self.button_indicar=gtk.Button("Indicar Ruta")
		self.button_indicar.set_size_request(90,25)

		fixed_ruta.put(self.radio_predeterminada,20,10)
		fixed_ruta.put(self.radio_indicar,20,60)
		fixed_ruta.put(self.button_indicar,100,60)

		self.vbox.pack_start(self.frame_ruta,False,True,1)

		self.aceptar_BD=gtk.Button("Aceptar")
		self.vbox.pack_start(self.aceptar_BD,False,True,1)

		fixed_frame.put(self.vbox,40,70)

		self.button_buscar.connect("clicked",self.buscarBD,self_seccion_stock)
		self.button_indicar.connect("clicked",self.indicarBD)

		self.radio_crear.connect("toggled",self.elijio_crear)
		self.radio_especificar.connect("toggled",self.elijio_especificar)
		self.radio_otras.connect("toggled",self.elijio_otras)

		self.radio_predeterminada.connect("toggled",self.desactivar_indicar)
		self.radio_indicar.connect("toggled",self.activar_indicar)

		self.entry_new_BD.connect("changed",self.entry_teclas)

		self.button_backup.connect("clicked",self.realizar_backup)

		self.button_cerrar.connect("clicked",self.cerrar_boton,self_ventana_principal)

		self.button_buscar.set_sensitive(False)
		self.button_indicar.set_sensitive(False)
		self.aceptar_BD.set_sensitive(False)
		self.frame_ruta.set_sensitive(False)
		self.hcaja_crear.set_sensitive(False)

		self.button_cerrar.set_property("is-focus",1)
		self.radio_otras.set_active(True)

		self.window.show_all()

	def indicarBD(self,widget):
		indicar_BD(self.window,self.entry_new_BD)

	def buscarBD(self,widget,self_seccion_stock):
		buscar_BD(self.window,self_seccion_stock)

	def entry_teclas(self,widget):
		if self.entry_new_BD.get_text()=="":
			self.aceptar_BD.set_sensitive(False)
			self.frame_ruta.set_sensitive(False)
		else:
			self.aceptar_BD.set_sensitive(True)
			self.frame_ruta.set_sensitive(True)

	def desactivar_indicar(self,windget):
		self.button_indicar.set_sensitive(False)
		self.hcaja_crear.set_sensitive(True)

	def activar_indicar(self,windget):
		self.button_indicar.set_sensitive(True)

	def activar_area_crear(self):
		self.hcaja_crear.set_sensitive(True)
		self.vbox.set_sensitive(True)

	def desactivar_area_crear(self):
		self.vbox.set_sensitive(False)
		self.hcaja_crear.set_sensitive(False)

	def activar_area_espeficiar(self):
		self.button_buscar.set_sensitive(True)

	def desactivar_area_especificar(self):
		self.button_buscar.set_sensitive(False)

	def activar_area_otras(self):
		self.button_backup.set_sensitive(True)

	def desactivar_area_otras(self):
		self.button_backup.set_sensitive(False)


	def elijio_especificar(self,widget):
		self.desactivar_area_crear()
		self.desactivar_area_otras()
		self.activar_area_espeficiar()

	def elijio_crear(self,widget):
		self.desactivar_area_otras()
		self.desactivar_area_especificar()
		self.activar_area_crear()

	def elijio_otras(self,widget):
		self.desactivar_area_crear()
		self.desactivar_area_especificar()
		self.activar_area_otras()
