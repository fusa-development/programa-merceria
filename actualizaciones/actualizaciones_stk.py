#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygtk
pygtk.require ('2.0')
import gtk
import sqlite3 as bdapi
from win_stock_zapateria import *

class actualizaciones_stk():
	
	
	def delete_event(self,widget, event ,object):
		object.set_sensitive(True)
		
	def salir (self, widget, window,lista,object):
		self.setear_filas(lista)
		object.set_sensitive(True)
		window.destroy()
	
	def setear_filas(self,lista_columnas):
		cell = lista_columnas[13]
		cellpb = lista_columnas[14]
		lista_columnas[0].set_attributes(cellpb, stock_id=0,cell_background_set=13)
		lista_columnas[1].set_attributes(cell, text=1,cell_background_set=13)
		lista_columnas[2].set_attributes(cell, text=2,cell_background_set=13)
		lista_columnas[3].set_attributes(cell, text=3,cell_background_set=13)
		lista_columnas[4].set_attributes(cell, text=4,cell_background_set=13)
		lista_columnas[5].set_attributes(cell, text=5,cell_background_set=13)
		lista_columnas[6].set_attributes(cell, text=6,cell_background_set=13)
		lista_columnas[7].set_attributes(cell, text=7,cell_background_set=13)
		lista_columnas[8].set_attributes(cell, text=8,cell_background_set=13)
		lista_columnas[9].set_attributes(cell, text=9,cell_background_set=13)
		lista_columnas[10].set_attributes(cell, text=10,cell_background_set=13)
		lista_columnas[11].set_attributes(cell, text=11,cell_background_set=13)

	def rep_no(self, widget, data, liststore):
		data.set_sensitive(False)
		id = self.datos[0]
		print "estoy aca"
		bbdd=bdapi.connect('stock_robert.db')
		cursor=bbdd.cursor()
		cursor.execute("UPDATE stock_zapateria SET swich=?, aviso=? WHERE id = ?", (False,False,id))
		liststore.set_value(self.iter, 11, "No")
		liststore.set_value(self.iter, 12, "No")
		liststore.set_value(self.iter, 13, False)
		bbdd.commit()
		cursor.close()
		bbdd.close()

	def rep(self, widget, data, id, liststore):
		data.set_sensitive(True)
		print "ahora aca"
		bbdd=bdapi.connect('stock_robert.db')
		cursor=bbdd.cursor()
		if self.datos[5] < self.datos[6]:
			cursor.execute("UPDATE stock_zapateria SET swich=?, aviso=? WHERE id = ?", (True,True,id))
			liststore.set_value(self.iter, 12, "Si")
			liststore.set_value(self.iter, 13, True)
		else:
			cursor.execute("UPDATE stock_zapateria SET swich=?, aviso=? WHERE id = ?", (True,False,id))
			liststore.set_value(self.iter, 12, "No")
			liststore.set_value(self.iter, 13, False)
		liststore.set_value(self.iter, 11, "Si")
		bbdd.commit()
		cursor.close()
		bbdd.close()
		
	def act_cantidad(self,widget,value,entry, liststore):
		bbdd=bdapi.connect('stock_robert.db')
		cursor=bbdd.cursor()
		value[0] += int(entry.get_text())
		if value[0] <= self.datos[9]:
			print "entre para true"
			cursor.execute("UPDATE stock_zapateria SET stock_actual=?, aviso=? WHERE id = ?", (value[0],True,value[1]))
			liststore.set_value(self.iter, 12, "Si")
			liststore.set_value(self.iter, 13, True)
		else:
			print "entre para false"
			cursor.execute("UPDATE stock_zapateria SET stock_actual=?, aviso=? WHERE id = ?", (value[0],False,value[1]))
			liststore.set_value(self.iter, 12, "No")
			liststore.set_value(self.iter, 13, False)
		liststore.set_value(self.iter, 9, value[0])
		entry.set_text("")
		self.datos[8] = value[0]
		bbdd.commit()
		cursor.close()
		bbdd.close()
		
	def cambiar_punto_rep(self, widget, entry, liststore):
		text = int(entry.get_text())
		value = self.datos[0]
		bbdd=bdapi.connect('stock_robert.db')
		cursor=bbdd.cursor()
		if self.datos[8] <= text:
			cursor.execute("UPDATE stock_zapateria SET punto_reposicion=?, aviso=? WHERE id = ?", (text,True,value))
			liststore.set_value(self.iter, 12, "Si")
			liststore.set_value(self.iter, 13, True)
		else:
			cursor.execute("UPDATE stock_zapateria SET punto_reposicion=?, aviso=? WHERE id = ?", (text,False,value))
			liststore.set_value(self.iter, 12, "No")
			liststore.set_value(self.iter, 13, False)
		liststore.set_value(self.iter, 10, text)
		self.datos[9] = text
		entry.set_text("")
		bbdd.commit()
		cursor.close()
		bbdd.close()

	def __init__(self, datos_seleccionados, liststore, lista_columnas, object):
	
		object.set_sensitive(False)
		print datos_seleccionados
		self.datos = datos_seleccionados
		self.value = []

		self.value.append(datos_seleccionados[8])
		self.value.append(datos_seleccionados[0])
		
		self.iter = datos_seleccionados[12]
		
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(350, 250)
		self.window.set_title("Actualizar")
		self.window.connect("delete-event",self.delete_event,object)
		self.fixed = gtk.Fixed()
		
		hbox = gtk.HBox(gtk.FALSE, 10)
		self.btn_stk = gtk.Button("Actualizar")
		self.btn_pnt_rep = gtk.Button("Cambiar Pnt Rep")
		self.btn_ma = gtk.Button("Menu anterior")
		self.btn_stk.set_size_request(130,30)
		self.btn_pnt_rep.set_size_request(130,30)
		self.entry_stk = gtk.Entry()
		self.entry_pnt_rep = gtk.Entry()
		lbl_rep = gtk.Label("Avisar reposicion")
		self.btn_rep = gtk.RadioButton(None, "Si")
		self.btn_norep = gtk.RadioButton(self.btn_rep, "No")
		hbox.pack_start(self.btn_rep, gtk.TRUE, gtk.TRUE, 10)
		hbox.pack_start(self.btn_norep, gtk.TRUE, gtk.TRUE, 10)
		self.btn_norep.connect("clicked",self.rep_no, self.btn_pnt_rep, liststore)
		self.btn_rep.connect("clicked", self.rep, self.btn_pnt_rep, datos_seleccionados[0], liststore)
		self.btn_stk.connect("clicked", self.act_cantidad, self.value, self.entry_stk , liststore)
		self.btn_pnt_rep.connect("clicked",self.cambiar_punto_rep,self.entry_pnt_rep, liststore)
		self.btn_ma.connect("clicked", self.salir, self.window, lista_columnas, object)
		
		self.fixed.put(self.btn_stk,10,50)
		self.fixed.put(self.btn_pnt_rep,10,80)
		self.fixed.put(self.btn_ma,230,200)
		self.fixed.put(self.entry_stk,150,50)
		self.fixed.put(self.entry_pnt_rep,150,80)
		self.fixed.put(lbl_rep,115,120)
		self.fixed.put(hbox,110,150)
		self.window.add(self.fixed)
		
		if datos_seleccionados[10] == "Si":
			self.btn_rep.set_active(gtk.TRUE)
		else:
			self.btn_norep.set_active(gtk.TRUE)
			
		self.window.show_all()
		


	def main(self):
		gtk.main()
		return 0

if __name__ == '__main__':
	act = actualizaciones_stk()
	act.main()
