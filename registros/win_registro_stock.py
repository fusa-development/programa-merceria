#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk
import csv
import time

class win_registro_stock():

	def calcular(self,widget):
		self.texto = []
		self.texto.append(self.entry_tipo_producto.get_text())
		self.texto.append(self.entry_ganancia.get_text())
		self.texto.append(self.entry_cantidad_bruta.get_text())
		if None not in self.texto or "" not in self.texto:
			total = float(self.texto[2])*(float(self.texto[1])/100)
			self.entry_ganancia_neta.set_text(str(total))
			self.texto.append(total)
			self.texto.append(float(self.texto[2])-total)
			self.entry_para_reposicion.set_text(str(self.texto[4]))
			
	def limpiar(self,widget=None):
		self.entry_tipo_producto.set_text("")
		self.entry_ganancia.set_text("")
		self.entry_cantidad_bruta.set_text("")
		self.entry_ganancia_neta.set_text("")
		self.entry_para_reposicion.set_text("")
		
	def cargar(self,widget):
		manejador=open("./registros/registros.csv","a")
		manejador_csv=csv.writer(manejador)
		self.texto.append(time.ctime())
		manejador_csv.writerow(self.texto)
		manejador.close()
		print self.texto
		self.liststore.append([self.texto[0],int(self.texto[1]),float(self.texto[2]),float(self.texto[3]),float(self.texto[4]),self.texto[5]])
		self.limpiar()

	def leer(self):
		manejador=open("./registros/registros.csv","r")
		manejador_csv=csv.reader(manejador)
		for fila in manejador_csv:
			if fila != []:
				self.liststore.append([fila[0],int(fila[1]),float(fila[2]),float(fila[3]),float(fila[4]),fila[5] ])
		manejador.close()
		

	def focus1(self,widget,event = None):
		self.entry_ganancia.set_property("is focus",1)
		
	def focus2(self,widget,event = None):
		self.entry_cantidad_bruta.set_property("is focus",1)
		
	def delete_event(self,widget,eventdata= None):
		self.window.destroy()

	def cerrar(self,widget):
		self.window.destroy()


	def __init__(self,widget,self_ventana_principal):
		
		object = self_ventana_principal.window
		icono="../Images/fusa_icon.png"
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.connect("delete_event",self.delete_event)
		self.window.set_title("Registros STOCK")
		self.window.set_size_request(860,550)
		self.window.set_icon(gtk.gdk.pixbuf_new_from_file(icono) )

		caja=gtk.VBox()

		button_limpiar=gtk.Button("Limpiar") #hacer mensaje si quiere limpiar!!!!!!!!!!!!
		self.entry_tipo_producto = gtk.Entry()
		self.entry_ganancia = gtk.Entry()
		self.entry_cantidad_bruta = gtk.Entry()
		self.entry_ganancia_neta = gtk.Entry()
		self.entry_para_reposicion = gtk.Entry()
		button_limpiar.set_property("can-focus",0)
		caja_labels= gtk.HBox(True,0)
		lista_lbl = []
		nombre_lbl=("Tipo Producto","Ganancia","Cantidad Bruta","Ganancia neta","P/ reposicion")
		lbl1 = gtk.Label(nombre_lbl[0])
		lbl2 = gtk.Label(nombre_lbl[1])
		lbl3 = gtk.Label(nombre_lbl[2])
		lbl4 = gtk.Label(nombre_lbl[3])
		lbl5 = gtk.Label(nombre_lbl[4])
		lista_lbl.append(lbl1)
		lista_lbl.append(lbl2)
		lista_lbl.append(lbl3)
		lista_lbl.append(lbl4)
		lista_lbl.append(lbl5)
		for x in lista_lbl:
			caja_labels.pack_start(x,True,False,)
		caja_entry = gtk.HButtonBox()
		caja_entry.set_layout(3)
		caja_entry.pack_start(self.entry_tipo_producto,True,True,0)
		caja_entry.pack_start(self.entry_ganancia,True,True,0)
		caja_entry.pack_start(self.entry_cantidad_bruta,True,True,0)
		caja_entry.pack_start(self.entry_ganancia_neta,True,True,0)
		caja_entry.pack_start(self.entry_para_reposicion,True,True,0)
		caja_buttons = gtk.HButtonBox()
		caja_buttons.set_layout(5)
		self.button_limpiar = gtk.Button("Limpiar")
		self.button_aceptar = gtk.Button("Aceptar")
		caja_buttons.add(self.button_limpiar)
		caja_buttons.add(self.button_aceptar)

		caja.pack_start(caja_labels,True,False, 0)
		caja.pack_start(caja_entry,True,False, 0)
		caja.pack_start(caja_buttons,True,False,0)
		self.scroll_win = gtk.ScrolledWindow()
		self.scroll_win.set_size_request(0,430)
		self.scroll_win.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		caja.pack_start(self.scroll_win,True,False, 0)

		self.liststore=gtk.ListStore(str,int,float,float,float,str)
		self.treeview=gtk.TreeView(self.liststore)
		self.scroll_win.add(self.treeview)

		riles_hint = self.treeview.get_rules_hint()
		self.treeview.set_rules_hint(True)
		self.cell = gtk.CellRendererText()
		nombre_columnas=("Tipo Producto","Ganancia","Cantidad Bruta","Ganancia neta","P/ reposicion","Fecha")
		columnas_registro=[]
		for x in range(6):
			columnas_registro.append( gtk.TreeViewColumn(nombre_columnas[x]) )
			self.treeview.append_column(columnas_registro[x])
			columnas_registro[x].pack_start(self.cell, True)
			columnas_registro[x].add_attribute(self.cell,"text",x)
			self.treeview.set_search_column(x)
			columnas_registro[x].set_sort_column_id(x)
			columnas_registro[x].set_expand(True)
			columnas_registro[x].set_resizable(True)

		button_cerrar=gtk.Button("Cerrar")
		button_cerrar.set_property("can-focus",0)
		button_cerrar.connect("clicked",self.cerrar)

		caja_button1= gtk.HButtonBox()
		caja_button1.set_layout(4)
		caja_button1.add(button_cerrar)
		caja.pack_start(caja_button1,True,False, 0)
		self.entry_tipo_producto.connect("activate",self.focus1)
		self.entry_tipo_producto.connect("focus-out-event",self.focus1)
		self.entry_ganancia.connect("activate",self.focus2)
		self.entry_ganancia.connect("focus-out-event",self.focus2)
		self.entry_cantidad_bruta.connect("activate",self.calcular)
		self.entry_cantidad_bruta.connect("focus-out-event",self.calcular)
		self.button_limpiar.connect("clicked",self.limpiar)
		self.button_aceptar.connect("clicked",self.cargar)
		self.leer()
		self.window.add(caja)
		self.window.show_all()
