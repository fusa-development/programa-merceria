#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk

class BD_no_especificada:

	def delete_event(self,widget,event,self_ventana_principal):
		self.aviso.destroy()
		self_ventana_principal.window.set_sensitive(True)

	def aceptar(self,widget,self_ventana_principal):
		self_ventana_principal.window.set_sensitive(True)
		self.aviso.destroy()

	def __init__(self,self_ventana_principal):
		self_ventana_principal.window.set_sensitive(False)
		self.aviso = gtk.Dialog(title="Mensaje", parent=None, flags=0, buttons=None)
		self.aviso.set_size_request(200,100)
		self.aviso.set_resizable(False)
		self.aviso.connect("delete_event", self.delete_event,self_ventana_principal)
		self.button = gtk.Button("Aceptar")
		label = gtk.Label("La Base de Datos NO\nha sido especificada")
		self.aviso.vbox.pack_start(label,0)
		self.aviso.action_area.pack_start(self.button, 0)
		self.button.connect("clicked",self.aceptar,self_ventana_principal)

		label.show()
		self.button.show()
		self.aviso.show()
