#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygtk
pygtk.require ("2.0")
import gtk
import sqlite3 as bdapi
import pango
import csv

from bbdd.leer_ruta_BD import leer_ruta

class consultas_stk():

	def delete_event(self,widget,event,object):
		object.set_sensitive(True)
		
	def salir (self, widget,object):
		object.set_sensitive(True)
		self.window.destroy()

	def mostrar(self,widget,data):
		cod = self.entry.get_text() 
		self.liststore.clear()
		self.bbdd=bdapi.connect(leer_ruta())
		self.cursor=self.bbdd.cursor()
		bandera = False
		if cod != "":
			if cod[0] in self.codigos_repetidos:
				self.cursor2=self.bbdd.cursor()
			if cod[0] == "M" or cod[0] == "m":
				self.cursor.execute(" SELECT * FROM merceria WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco
			elif cod[0] == "L" or cod[0] =="l":
				bandera = True
				self.cursor.execute(" SELECT * FROM lana WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco
				self.cursor2.execute(" SELECT * FROM ropa WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco
			elif cod[0] == "R" or cod[0] =="r":
				bandera = True
				self.cursor.execute(" SELECT * FROM regaleria WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco
				self.cursor2.execute(" SELECT * FROM ropa WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco
			elif cod[0] == "J" or cod[0] =="j":
				self.cursor.execute(" SELECT * FROM jugueteria WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco
			elif cod[0] == "S" or cod[0] =="s":
				self.cursor.execute(" SELECT * FROM santeria WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco
			elif cod[0] == "B" or cod[0] =="b":
				self.cursor.execute(" SELECT * FROM bijouterie WHERE codigo LIKE '"+cod+"%'") #imprime cuando el nombre sea = a lo qe busco  
			if not bandera:
				if cod[0].upper() == "M":
					for tupla in self.cursor.fetchall():
						if tupla[9]:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),float(tupla[6]),float(tupla[7]) ,int(tupla[8]),"Si",True])
						else:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),float(tupla[6]),float(tupla[7]) ,int(tupla[8]),"No",False])
					self.bbdd.commit()
					self.cursor.close()
				else:
					for tupla in self.cursor.fetchall():
						if tupla[9]:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),"Si",True])
						else:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),"No",False])
					self.bbdd.commit()
					self.cursor.close()
			else:
				if cod[0].upper() == "L":
					for tupla in self.cursor.fetchall():
						if tupla[9]:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),float(tupla[6]),float(tupla[7]) ,int(tupla[8]),"Si",True])
						else:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),float(tupla[6]),float(tupla[7]) ,int(tupla[8]),"No",False])
					self.bbdd.commit()
					self.cursor.close()
					for tupla in self.cursor2.fetchall():  
						if tupla[10]:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[4]),float(tupla[5]),float(tupla[6]),int(tupla[7]),int(tupla[8]) ,int(tupla[9]),"Si",True])
						else:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[4]),float(tupla[5]),float(tupla[6]),int(tupla[7]),int(tupla[8]) ,int(tupla[9]),"No",False])
				else:
					for tupla in self.cursor.fetchall():
						if tupla[9]:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),"Si",True])
						else:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[3]),float(tupla[4]),float(tupla[5]),int(tupla[6]),int(tupla[7]) ,int(tupla[8]),"No",False])
					self.bbdd.commit()
					for tupla in self.cursor2.fetchall():  
						if tupla[10]:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[4]),float(tupla[5]),float(tupla[6]),int(tupla[7]),int(tupla[8]) ,int(tupla[9]),"Si",True])
						else:
							self.liststore.append(["", int(tupla[0]),tupla[1],tupla[2],float(tupla[4]),float(tupla[5]),float(tupla[6]),int(tupla[7]),int(tupla[8]) ,int(tupla[9]),"No",False])
					self.bbdd.commit()
				self.cursor.close()
				self.cursor2.close()
			self.bbdd.close()
			
	def buscar(self,cod):
		datos = []
		self.cursor2 = None
		self.bbdd=bdapi.connect(leer_ruta())
		self.cursor=self.bbdd.cursor()
		if cod[0][0] in self.codigos_repetidos:
			self.cursor2=self.bbdd.cursor()
		cod[0]=cod[0].upper()
		if cod[0][0].upper() == "M":
				self.cursor.execute(" SELECT * FROM merceria WHERE codigo = ?",cod) 
		elif cod[0][0].upper() == "L":
			bandera = True
			self.cursor.execute(" SELECT * FROM lana WHERE codigo = ?",cod) 
			self.cursor2.execute(" SELECT * FROM ropa WHERE codigo = ?",cod)
		elif cod[0][0].upper() == "R":
			bandera = True
			self.cursor.execute(" SELECT * FROM regaleria WHERE codigo = ? ",cod)
			self.cursor2.execute(" SELECT * FROM ropa WHERE codigo = ?",cod) 
		elif cod[0][0].upper() == "J":
			self.cursor.execute(" SELECT * FROM jugueteria WHERE codigo = ? ",cod) 
		elif cod[0][0].upper() == "S":
			self.cursor.execute(" SELECT * FROM santeria WHERE codigo = ?",cod)
		elif cod[0][0].upper() == "B":
			self.cursor.execute(" SELECT * FROM bijouterie WHERE codigo = ?",cod)
		self.bbdd.commit()
		if self.cursor2 != None:
			tupla = self.cursor2.fetchone()
			self.cursor2.close()
			if tupla == None:
				tupla = self.cursor.fetchone()
				self.cursor.close()
		else:
			tupla = self.cursor.fetchone()
			self.cursor.close()
		self.bbdd.close()
		if tupla != None:
			for x in tupla:
				datos.append(x)
			return datos
		else:
			return False
			
	def verificar_codigo(self,widget,event):
		self.codigo = []
		self.codigo.append(self.entry.get_text())
		self.datos = self.buscar(self.codigo)
		if self.datos == False:
			print "Codigo increiblemente inexistente"
		else:
			self.entry_descripcion.set_text(self.datos[2])
			self.entry_cantidad.set_property("is focus",1)
			
	def cargar(self,widget,self_seccion_stock):
		self.bbdd=bdapi.connect(leer_ruta())
		self.cursor=self.bbdd.cursor()
		cod = self.codigo
		if cod[0][0] in self.codigos_repetidos:
			self.cursor2=self.bbdd.cursor()
		cod[0]=cod[0].upper()
		if cod[0][0]=="M"or cod[0][0:2] == "LA" or cod[0][0] == "J"or cod[0][0] == "S" or cod[0][0:2] == "RE" or cod[0][0] == "B":
			cantidad = self.datos[7]-float(self.entry_cantidad.get_text())
			if cantidad<=self.datos[8]:
				values = (cantidad,True,cod[0])
			else:
				values = (cantidad,False,cod[0])
		else:
			cantidad = self.datos[8]-int(self.entry_cantidad.get_text())
			if cantidad<=self.datos[9]:
				values = (cantidad,True,cod[0])
			else:
				values = (cantidad,False,cod[0])
		if cod[0][0] == "M":
			self.cursor.execute(" UPDATE merceria SET stk_disp = ?, aviso = ? WHERE codigo = ?",values)
			for x in range(len(self_seccion_stock.liststore_merceria)):
				if self_seccion_stock.liststore_merceria[x][2] == self.datos[1]:
					self_seccion_stock.liststore_merceria[x][8] = values[0]
					self_seccion_stock.liststore_merceria[x][11]= values[1]
		elif cod[0][0] == "L":
			self.cursor.execute(" UPDATE lana SET stk_disp = ?, aviso = ?  WHERE codigo = ?",values) 
			self.cursor2.execute(" UPDATE ropa SET stk_disp = ?, aviso = ?  WHERE codigo = ?",values)
			if cod[0][0:2]=="LA":
				for x in range(len(self_seccion_stock.liststore_lana)):
					if self_seccion_stock.liststore_lana[x][2] == self.datos[1]:
						self_seccion_stock.liststore_lana[x][8] = values[0]
						self_seccion_stock.liststore_lana[x][11]= values[1]
			else:
				for x in range(len(self_seccion_stock.liststore_ropa)):
					if self_seccion_stock.liststore_ropa[x][2] == self.datos[1]:
						self_seccion_stock.liststore_ropa[x][9] = values[0]
						self_seccion_stock.liststore_ropa[x][12]= values[1]
		elif cod[0][0] == "R":
			self.cursor.execute(" UPDATE regaleria SET stk_disp = ?, aviso = ?  WHERE codigo = ? ",values)
			self.cursor2.execute(" UPDATE ropa SET stk_disp = ?, aviso = ? WHERE codigo = ?",values) 
			if cod[0][0:2] == "RE":
				for x in range(len(self_seccion_stock.liststore_regaleria)):
					if self_seccion_stock.liststore_regaleria[x][2] == self.datos[1]:
						self_seccion_stock.liststore_regaleria[x][8] = values[0]
						self_seccion_stock.liststore_regaleria[x][11]= values[1]
			else:
				for x in range(len(self_seccion_stock.liststore_ropa)):
					if self_seccion_stock.liststore_ropa[x][2] == self.datos[1]:
						self_seccion_stock.liststore_ropa[x][9] = values[0]
						self_seccion_stock.liststore_ropa[x][12]= values[1]
		elif cod[0][0] == "J":
			self.cursor.execute(" UPDATE jugueteria SET stk_disp = ?, aviso = ? WHERE codigo = ? ",values) 
			for x in range(len(self_seccion_stock.liststore_jugueteria)):
				if self_seccion_stock.liststore_jugueteria[x][2] == self.datos[1]:
					self_seccion_stock.liststore_jugueteria[x][8] = values[0]
					self_seccion_stock.liststore_jugueteria[x][11]= values[1]
		elif cod[0][0] == "S":
			self.cursor.execute(" UPDATE santeria SET stk_disp = ?, aviso = ?  WHERE codigo = ?",values)
			for x in range(len(self_seccion_stock.liststore_santeria)):
				if self_seccion_stock.liststore_santeria[x][2] == self.datos[1]:
					self_seccion_stock.liststore_santeria[x][8] = values[0]
					self_seccion_stock.liststore_santeria[x][11]= values[1]
		elif cod[0][0] == "B":
			self.cursor.execute(" UPDATE bijouterie SET stk_disp = ?, aviso = ?  WHERE codigo = ?",values)
			for x in range(len(self_seccion_stock.liststore_bijouterie)):
				if self_seccion_stock.liststore_bijouterie[x][2] == self.datos[1]:
					self_seccion_stock.liststore_bijouterie[x][8] = values[0]
					self_seccion_stock.liststore_bijouterie[x][11]= values[1]
		self.bbdd.commit()
		self.cursor.close()
		self.bbdd.close()
		self.entry.set_text("")
		self.entry_cantidad.set_text("")
		self.entry_descripcion.set_text("")
		self.entry.set_property("is focus",1)
		
		
			
	def setear_filas(self):
		cell = self.lista_columnas[8]
		cellpb = self.lista_columnas[9]
		self.lista_columnas[0].set_attributes(cellpb, stock_id=0, cell_background_set=11)
		self.lista_columnas[1].set_attributes(cell, text=2,cell_background_set=11)
		self.lista_columnas[2].set_attributes(cell, text=3,cell_background_set=11)
		self.lista_columnas[3].set_attributes(cell, text=4,cell_background_set=11)
		self.lista_columnas[4].set_attributes(cell, text=5,cell_background_set=11)
		self.lista_columnas[5].set_attributes(cell, text=7,cell_background_set=11)
		self.lista_columnas[6].set_attributes(cell, text=8,cell_background_set=11)
		self.lista_columnas[7].set_attributes(cell, text=9,cell_background_set=11)

	def __init__(self,widget,self_seccion_stock,self_ventana_principal):
		self.codigo = []
		self.codigos_repetidos = ["l","L","r","R"]
		object = self_ventana_principal.window
		object.set_sensitive(False)
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_size_request(1131,600)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_title("Busqueda de productos")
		self.window.set_resizable(False)
		self.window.connect("delete-event",self.delete_event,object)
		self.fixed=gtk.Fixed()

		img = gtk.Image()

		self.fixed.add(img)
		self.window.add(self.fixed)

		atributos = pango.AttrList()
		atributos.insert(pango.AttrSize(12400,0,-1))
		atributos.insert(pango.AttrWeight(1200,0,-1))

		label_codigo = gtk.Label("Codigo : ")
		label_descripcion = gtk.Label("Descripcion : ")
		label_cantidad = gtk.Label("Cantidad : ")

		label_codigo.set_attributes(atributos)
		label_descripcion.set_attributes(atributos)
		label_cantidad.set_attributes(atributos)


		fuente_entrys="Sans 13"
		font_entry= pango.FontDescription(fuente_entrys)

		self.entry = gtk.Entry()
		self.entry_descripcion = gtk.Entry()
		self.entry_cantidad = gtk.Entry()

		self.entry.modify_font(font_entry)
		self.entry_descripcion.modify_font(font_entry)
		self.entry_cantidad.modify_font(font_entry)

		self.fixed.put(self.entry,150,20)
		self.fixed.put(self.entry_descripcion,480,20)
		self.fixed.put(self.entry_cantidad,750,20)

		self.fixed.put(label_codigo,80,25)
		self.fixed.put(label_descripcion,370,25)
		self.fixed.put(label_cantidad,660,25)

		self.button_ma = gtk.Button()
		self.button_ma.set_property("relief",2)
		imagen_boton_cerrar=gtk.Image()
		imagen_boton_cerrar.set_from_file("../Images/boton_cerrar.png")
		self.button_ma.add(imagen_boton_cerrar)
		self.fixed.put(self.button_ma,990,550)

		#agrego a una lista informacion de la bd
		
		self.button_ma.connect("clicked",self.salir,object)
		self.entry.connect("changed",self.mostrar,'codigo')
		self.entry.connect("activate",self.verificar_codigo,'codigo')
		self.entry_cantidad.connect("activate",self.cargar,self_seccion_stock)


#--------------------------------------------------------------------------------------------------------------
		self.scroll_win = gtk.ScrolledWindow()
		self.scroll_win.set_policy(gtk.POLICY_AUTOMATIC,gtk.POLICY_AUTOMATIC)
		self.scroll_win.set_size_request(1111,470)
		self.fixed.put(self.scroll_win,10,70)

		self.liststore=gtk.ListStore(str,int,str,str,float,float,str,str,str,str,str,'gboolean')
		self.treeview=gtk.TreeView(self.liststore)
		rules_hint=self.treeview.get_rules_hint()
		self.treeview.set_rules_hint(True)

		self.scroll_win.add(self.treeview)

		self.columnpb = gtk.TreeViewColumn("")
		self.column1 = gtk.TreeViewColumn("Codigo")
		self.column2 = gtk.TreeViewColumn("Descripcion")
		self.column3 = gtk.TreeViewColumn("Costo")
		self.column4 = gtk.TreeViewColumn("Precio")
		self.column5 = gtk.TreeViewColumn("Stock inicial")
		self.column6 = gtk.TreeViewColumn("Stock disponible")
		self.column7 = gtk.TreeViewColumn("punto de reposicion")
		self.column8 = gtk.TreeViewColumn("Reponer")

		self.treeview.append_column(self.columnpb)
		self.treeview.append_column(self.column1)
		self.treeview.append_column(self.column2)
		self.treeview.append_column(self.column3)
		self.treeview.append_column(self.column4)
		self.treeview.append_column(self.column5)
		self.treeview.append_column(self.column6)
		self.treeview.append_column(self.column7)
		
		self.cell = gtk.CellRendererText()
		self.cellpb = gtk.CellRendererPixbuf()
		
		self.cell.set_property("cell background", "#71ACE2")
		self.cell.set_property('size', 14000)#solo le da el tamaño a las celdas xd
		self.cell.set_property('weight', 700)#seria el "grosor" de la fuente :P
		self.cellpb.set_property("cell background", "#71ACE2")
		
		self.columnpb.pack_start(self.cellpb,True)
		self.column1.pack_start(self.cell, True)
		self.column2.pack_start(self.cell, True)
		self.column3.pack_start(self.cell, True)
		self.column4.pack_start(self.cell, True)
		self.column5.pack_start(self.cell, True)
		self.column6.pack_start(self.cell, True)
		self.column7.pack_start(self.cell, True)

		self.treeview.set_search_column(1)
		self.treeview.set_search_column(2)
		self.treeview.set_search_column(3)
		self.treeview.set_search_column(4)
		self.treeview.set_search_column(5)
		self.treeview.set_search_column(6)
		self.treeview.set_search_column(7)

		self.column1.set_sort_column_id(2)
		self.column2.set_sort_column_id(3)
		self.column3.set_sort_column_id(4)
		self.column4.set_sort_column_id(5)
		self.column5.set_sort_column_id(6)
		self.column6.set_sort_column_id(7)
		self.column7.set_sort_column_id(8)

		self.columnpb.set_expand(True)
		self.column1.set_expand(True)
		self.column2.set_expand(True)
		self.column3.set_expand(True)
		self.column4.set_expand(True)
		self.column5.set_expand(True)
		self.column6.set_expand(True)
		self.column7.set_expand(True)

		self.column1.set_resizable(True)
		self.column2.set_resizable(True)
		self.column3.set_resizable(True)
		self.column4.set_resizable(True)
		self.column5.set_resizable(True)
		self.column6.set_resizable(True)
		self.column7.set_resizable(True)

		self.lista_columnas = []
		self.lista_columnas.append(self.columnpb)
		self.lista_columnas.append(self.column1)
		self.lista_columnas.append(self.column2)
		self.lista_columnas.append(self.column3)
		self.lista_columnas.append(self.column4)
		self.lista_columnas.append(self.column5)
		self.lista_columnas.append(self.column6)
		self.lista_columnas.append(self.column7)

		self.lista_columnas.append(self.cell)
		self.lista_columnas.append(self.cellpb)

		self.setear_filas()	
		
		self.window.show_all()
