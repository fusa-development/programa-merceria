#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
from seccion_stock import *

class acerca_de:
	def __init__(self):
		about_dialog = gtk.AboutDialog()
		about_dialog.set_destroy_with_parent(True)
		about_dialog.set_name('Merceria Katy\nV. 1.11')
		#about_dialog.set_version('1.0')
		about_dialog.set_authors(['Fusa Desarollos\nE-mail:fusadesarrollos@gmail.com'])
		about_dialog.run()
		about_dialog.destroy()


class win_stock():

	def salir_boton(self,widget):
		self.window.destroy()

	def mostrar_acerda_de(self,widget):
		acerca_de()

	def __init__(self):
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_size_request(1280,690)
		self.window.set_title("Menu Stock")
		icono="../Images/fusa_icon.png"
		self.window.set_icon(gtk.gdk.pixbuf_new_from_file(icono) )
		self.window.set_resizable(False)

		salir_menubar = gtk.MenuItem("Salir")
		opciones = gtk.MenuItem("Opciones")
		ayuda=gtk.MenuItem("Ayuda")

		contenedor_salir = gtk.Menu()
		item_salir = gtk.MenuItem("Salir del Programa")
		contenedor_salir.append(item_salir)
		salir_menubar.set_submenu(contenedor_salir)

		menu_item_opciones=[]
		contenedor_opciones = gtk.Menu()
		menu_item_opciones.append( gtk.MenuItem("Administrar Base De Datos") )
		contenedor_opciones.append(menu_item_opciones[0])
		opciones.set_submenu(contenedor_opciones)

		contenedor_ver_registros=gtk.Menu()
		item_ver_registro_stock=gtk.MenuItem("Control de Productos")
		contenedor_ver_registros.append(item_ver_registro_stock)

		contenedor_administrar_BD=gtk.Menu()
		self.item_administrar_BDproducto=gtk.MenuItem("Productos")
		contenedor_administrar_BD.append(self.item_administrar_BDproducto)

		menu_item_opciones[0].set_submenu(contenedor_administrar_BD)


		contenedor_ayuda=gtk.Menu()
		item_acerca_de=gtk.MenuItem("Acerca de")
		contenedor_ayuda.append(item_acerca_de)
		ayuda.set_submenu(contenedor_ayuda)

		self.vbox = gtk.VBox(False, 0)
		self.window.add(self.vbox)
		self.menu_bar = gtk.MenuBar()
		self.menu_bar.append (salir_menubar)
		self.menu_bar.append (opciones)
		self.menu_bar.append (ayuda)

		self.vbox.pack_start(self.menu_bar,False,True, 0)

		dibujar_stock(self)

		separador_inferior=gtk.HSeparator()
		self.vbox.pack_start(separador_inferior, False, False,2)

		self.button_salir=gtk.Button()
		image_salir=gtk.Image()
		image_salir.set_from_file("../Images/cerrar1.png")
		self.button_salir.add(image_salir)
		self.button_salir.set_size_request(115,50)
		self.button_salir.connect("clicked",self.salir_boton)
		self.button_salir.set_property("can-focus",0)
		self.button_salir.set_property("relief",2)

		botonera_inferior=gtk.HButtonBox()
		botonera_inferior.set_property("layout-style",4)

		botonera_inferior.pack_start(self.button_salir,False,False,1)

		self.vbox.pack_start(botonera_inferior,True, False,0)

		item_acerca_de.connect("activate",self.mostrar_acerda_de)

		item_salir.connect("activate",self.salir_boton)

		self.window.show_all()

if __name__ == '__main__':
	win_stock()
	gtk.main()
