import gtk
import pygtk
import pango
import sqlite3 as bdapi
import csv

from bbdd.leer_ruta_BD import leer_ruta


class agregar_producto:

##################################################################################################################
##################################################################################################################

	def calcular_id(self,total_liststore_productos,numero_liststore):
		largo=len(total_liststore_productos[numero_liststore])
		if largo >0:
			id=(total_liststore_productos[numero_liststore][largo-1][1])+1
		else:
			id=1
		return id
#-----------------------------------------------------------------------------------------------------------------
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

#-----------------------------------------------------------------------------------------------------------------

	def aceptar_datos(self,widget,total_liststore_productos):
		model = self.combobox.get_model()
		index = self.combobox.get_active()
		bbdd=bdapi.connect(leer_ruta() )
		cursor=bbdd.cursor()

		if model[index][0] =="Lana":
			numero_liststore=1
			codigo=self.letra_inicio_codigo[0]+self.entry_lana[0].get_text()
			descripcion=self.entry_lana[1].get_text()
			costo=self.entry_lana[2].get_text()
			precio=self.entry_lana[3].get_text()

			ganancia=float(self.pin_lana[0].get_value() )
			cantidad_inicial=float(self.pin_lana[1].get_value() )
			cantidad_disponible=float(self.pin_lana[2].get_value() )
			punto_reposicion=float (self.pin_lana[3].get_text() )

			total_liststore_productos[1].append([None,int(self.calcular_id(total_liststore_productos,numero_liststore)),codigo,descripcion,float(costo),float(precio),float(ganancia),float(cantidad_inicial),float(cantidad_disponible),int(punto_reposicion), self.calcular_reponer(cantidad_disponible,punto_reposicion) , self.calcular_pintar(cantidad_disponible,punto_reposicion) ])
			cursor.execute(" INSERT INTO  lana (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",( codigo,descripcion,costo,precio,ganancia,cantidad_inicial,cantidad_disponible,punto_reposicion, self.calcular_pintar(cantidad_disponible,punto_reposicion) ) )
			self.label_informar_cargado_lana.set_text("PRODUCTO AGREGADO")
			for x in range(4):
				self.entry_lana[x].set_editable(False)
				self.pin_lana[x].set_editable(False)

		elif model[index][0] =="Merceria":
			numero_liststore=0
			codigo=self.letra_inicio_codigo[1]+self.entry_merceria[0].get_text()
			descripcion=self.entry_merceria[1].get_text()
			costo=float(self.entry_merceria[2].get_text() )
			precio=float (self.entry_merceria[3].get_text() )

			ganancia=float( self.pin_merceria[0].get_value() )
			cantidad_inicial=float( self.pin_merceria[1].get_value() )
			cantidad_disponible=float ( self.pin_merceria[2].get_value() )
			punto_reposicion=self.pin_merceria[3].get_text()
			total_liststore_productos[0].append([None,int(self.calcular_id(total_liststore_productos,numero_liststore)),codigo,descripcion,float(costo),float(precio),ganancia,cantidad_inicial,cantidad_disponible,int(punto_reposicion), self.calcular_reponer(cantidad_disponible,punto_reposicion) , self.calcular_pintar(cantidad_disponible,punto_reposicion) ])
			cursor.execute(" INSERT INTO  merceria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",( (codigo),descripcion,costo,precio,ganancia,cantidad_inicial,cantidad_disponible,punto_reposicion, self.calcular_pintar(cantidad_disponible,punto_reposicion) ) )
			self.label_informar_cargado_merceria.set_text("PRODUCTO AGREGADO")

			for x in range(4):
				self.entry_merceria[x].set_editable(False)
				self.pin_merceria[x].set_editable(False)

		elif model[index][0] =="Regaleria":
			numero_liststore=3
			codigo=self.letra_inicio_codigo[2]+self.entry_regaleria[0].get_text()
			descripcion=self.entry_regaleria[1].get_text()
			costo=self.entry_regaleria[2].get_text()
			precio=self.entry_regaleria[3].get_text()

			ganancia=self.pin_regaleria[0].get_text()
			cantidad_inicial=self.pin_regaleria[1].get_text()
			cantidad_disponible=self.pin_regaleria[2].get_text()
			punto_reposicion=self.pin_regaleria[3].get_text()
			total_liststore_productos[3].append([None,int(self.calcular_id(total_liststore_productos,numero_liststore)),codigo,descripcion,float(costo),float(precio),int(ganancia),int(cantidad_inicial),int(cantidad_disponible),int(punto_reposicion), self.calcular_reponer(cantidad_disponible,punto_reposicion) , self.calcular_pintar(cantidad_disponible,punto_reposicion) ])
			cursor.execute(" INSERT INTO  regaleria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",( (codigo),descripcion,costo,precio,ganancia,cantidad_inicial,cantidad_disponible,punto_reposicion, self.calcular_pintar(cantidad_disponible,punto_reposicion) ) )
			self.label_informar_cargado_regaleria.set_text("PRODUCTO AGREGADO")
			for x in range(4):
				self.entry_regaleria[x].set_editable(False)
				self.pin_regaleria[x].set_editable(False)

		elif model[index][0] =="Santeria":
			numero_liststore=5
			codigo=self.letra_inicio_codigo[3]+self.entry_santeria[0].get_text()
			descripcion=self.entry_santeria[1].get_text()
			costo=self.entry_santeria[2].get_text()
			precio=self.entry_santeria[3].get_text()

			ganancia=self.pin_santeria[0].get_text()
			cantidad_inicial=self.pin_santeria[1].get_text()
			cantidad_disponible=self.pin_santeria[2].get_text()
			punto_reposicion=self.pin_santeria[3].get_text()
			total_liststore_productos[5].append([None,int(self.calcular_id(total_liststore_productos,numero_liststore)),codigo,descripcion,float(costo),float(precio),int(ganancia),int(cantidad_inicial),int(cantidad_disponible),int(punto_reposicion), self.calcular_reponer(cantidad_disponible,punto_reposicion) , self.calcular_pintar(cantidad_disponible,punto_reposicion) ])
			cursor.execute(" INSERT INTO  santeria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",( (codigo),descripcion,costo,precio,ganancia,cantidad_inicial,cantidad_disponible,punto_reposicion, self.calcular_pintar(cantidad_disponible,punto_reposicion) ) )
			self.label_informar_cargado_santeria.set_text("PRODUCTO AGREGADO")
			for x in range(4):
				self.entry_santeria[x].set_editable(False)
				self.pin_santeria[x].set_editable(False)

		elif model[index][0] =="Ropa":
			numero_liststore=2
			model_cobre=self.combobox_ropas.get_model()
			index_cobre = self.combobox_ropas.get_active()
			tipo_ropa=model_cobre[index_cobre][0]

			codigo=tipo_ropa+self.entry_ropa[0].get_text()
			descripcion=self.entry_ropa[1].get_text()
			costo=self.entry_ropa[2].get_text()
			precio=self.entry_ropa[3].get_text()

			talle=1
			ganancia=self.pin_ropa[0].get_text()
			cantidad_inicial=self.pin_ropa[1].get_text()
			cantidad_disponible=self.pin_ropa[2].get_text()
			punto_reposicion=self.pin_ropa[3].get_text()
			total_liststore_productos[2].append([None,int(self.calcular_id(total_liststore_productos,numero_liststore)),codigo,descripcion,int(talle),float(costo),float(precio),int(ganancia),int(cantidad_inicial),int(cantidad_disponible),int(punto_reposicion), self.calcular_reponer(cantidad_disponible,punto_reposicion) , self.calcular_pintar(cantidad_disponible,punto_reposicion) ])
			cursor.execute(" INSERT INTO  ropa (codigo, descripcion, talle,costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?,?)",( (codigo),descripcion,talle,costo,precio,ganancia,cantidad_inicial,cantidad_disponible,punto_reposicion, self.calcular_pintar(cantidad_disponible,punto_reposicion) ) )
			self.label_informar_cargado_ropa.set_text("PRODUCTO AGREGADO")
			for x in range(4):
				self.entry_ropa[x].set_editable(False)
				self.pin_ropa[x].set_editable(False)

		elif model[index][0] =="Bijouterie":
			numero_liststore=6
			codigo=self.letra_inicio_codigo[4]+self.entry_bijouterie[0].get_text()
			descripcion=self.entry_bijouterie[1].get_text()
			costo=self.entry_bijouterie[2].get_text()
			precio=self.entry_bijouterie[3].get_text()

			ganancia=self.pin_bijouterie[0].get_text()
			cantidad_inicial=self.pin_bijouterie[1].get_text()
			cantidad_disponible=self.pin_bijouterie[2].get_text()
			punto_reposicion=self.pin_bijouterie[3].get_text()
			total_liststore_productos[6].append([None,int(self.calcular_id(total_liststore_productos,numero_liststore)),codigo,descripcion,float(costo),float(precio),int(ganancia),int(cantidad_inicial),int(cantidad_disponible),int(punto_reposicion), self.calcular_reponer(cantidad_disponible,punto_reposicion) , self.calcular_pintar(cantidad_disponible,punto_reposicion) ])
			cursor.execute(" INSERT INTO  bijouterie (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",( (codigo),descripcion,costo,precio,ganancia,cantidad_inicial,cantidad_disponible,punto_reposicion, self.calcular_pintar(cantidad_disponible,punto_reposicion) ) )
			self.label_informar_cargado_bijouterie.set_text("PRODUCTO AGREGADO")
			for x in range(4):
				self.entry_bijouterie[x].set_editable(False)
				self.pin_bijouterie[x].set_editable(False)

		elif model[index][0] =="Jugueteria":
			numero_liststore=4
			codigo=self.letra_inicio_codigo[5]+self.entry_jugueteria[0].get_text()
			descripcion=self.entry_jugueteria[1].get_text()
			costo=self.entry_jugueteria[2].get_text()
			precio=self.entry_jugueteria[3].get_text()

			ganancia=self.pin_jugueteria[0].get_text()
			cantidad_inicial=self.pin_jugueteria[1].get_text()
			cantidad_disponible=self.pin_jugueteria[2].get_text()
			punto_reposicion=self.pin_jugueteria[3].get_text()
			total_liststore_productos[4].append([None,int(self.calcular_id(total_liststore_productos,numero_liststore)),codigo,descripcion,float(costo),float(precio),int(ganancia),int(cantidad_inicial),int(cantidad_disponible),int(punto_reposicion), self.calcular_reponer(cantidad_disponible,punto_reposicion) , self.calcular_pintar(cantidad_disponible,punto_reposicion) ])
			cursor.execute(" INSERT INTO  jugueteria (codigo, descripcion, costo, precio, ganancia,stk_ini, stk_disp, pnt_rep,aviso) VALUES(?,?,?,?,?,?,?,?,?)",( (codigo),descripcion,costo,precio,ganancia,cantidad_inicial,cantidad_disponible,punto_reposicion, self.calcular_pintar(cantidad_disponible,punto_reposicion) ) )
			self.label_informar_cargado_jugueteria.set_text("PRODUCTO AGREGADO")
			for x in range(4):
				self.entry_jugueteria[x].set_editable(False)
				self.pin_jugueteria[x].set_editable(False)

		self.botones_totales[0].set_sensitive(False)
		bbdd.commit()
		cursor.close()
		bbdd.close()

##################################################################################################################
##################################################################################################################

	def elejir_producto(self,widget):#segun el producto que elijio muestra 
		model = self.combobox.get_model()
		index = self.combobox.get_active()
		self.botones_totales[1].set_sensitive(True)

		if model[index][0]=="Lana":
			self.fixed_lana.show()
			if self.label_informar_cargado_lana.get_text()=="" and self.codigo_lana_valido and self.costo_lana_valido and self.precio_lana_valido :
				self.botones_totales[0].set_sensitive(True)
			else:
				self.botones_totales[0].set_sensitive(False)
		else:
			self.fixed_lana.hide()

		if model[index][0]=="Merceria":
			self.fixed_merceria.show()
			if self.label_informar_cargado_merceria.get_text()=="" and self.codigo_merceria_valido and self.costo_merceria_valido and self.precio_merceria_valido :
				self.botones_totales[0].set_sensitive(True)
			else:
				self.botones_totales[0].set_sensitive(False)
		else:
			self.fixed_merceria.hide()

		if model[index][0]=="Regaleria":
			self.fixed_regaleria.show()
			if self.label_informar_cargado_regaleria.get_text()=="" and self.codigo_regaleria_valido and self.costo_regaleria_valido and self.precio_regaleria_valido :
				self.botones_totales[0].set_sensitive(True)
			else:
				self.botones_totales[0].set_sensitive(False)
		else:
			self.fixed_regaleria.hide()
		if model[index][0]=="Santeria":
			self.fixed_santeria.show()
			if self.label_informar_cargado_santeria.get_text()=="" and self.codigo_santeria_valido and self.costo_santeria_valido and self.precio_santeria_valido:
				self.botones_totales[0].set_sensitive(True)
			else:
				self.botones_totales[0].set_sensitive(False)
		else:
			self.fixed_santeria.hide()
		if model[index][0]=="Ropa":
			self.fixed_ropa.show()
			if self.label_informar_cargado_ropa.get_text()=="" and self.codigo_ropa_valido and self.costo_ropa_valido and self.precio_ropa_valido:
				self.botones_totales[0].set_sensitive(True)
			else:
				self.botones_totales[0].set_sensitive(False)
		else:
			self.fixed_ropa.hide()
		if model[index][0]=="Bijouterie":
			self.fixed_bijouterie.show()
			if self.label_informar_cargado_bijouterie.get_text()=="" and self.codigo_bijouterie_valido and self.costo_bijouterie_valido and self.precio_bijouterie_valido:
				self.botones_totales[0].set_sensitive(True)
			else:
				self.botones_totales[0].set_sensitive(False)
		else:
			self.fixed_bijouterie.hide()
		if model[index][0]=="Jugueteria":
			self.fixed_jugueteria.show()
			if self.label_informar_cargado_jugueteria.get_text()=="" and self.codigo_jugueteria_valido and self.costo_jugueteria_valido and self.precio_jugueteria_valido:
				self.botones_totales[0].set_sensitive(True)
			else:
				self.botones_totales[0].set_sensitive(False)
		else:
			self.fixed_jugueteria.hide()




##################################################################################################################
##################################################################################################################


#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

	def entrys_completados_lana(self,widget):
		if self.codigo_lana_valido and self.costo_lana_valido and self.precio_lana_valido:
			self.botones_totales[0].set_sensitive(True)
		else:
			self.botones_totales[0].set_sensitive(False)

	def entrys_completados_merceria(self,widget):
		if self.codigo_merceria_valido and self.costo_merceria_valido and self.precio_merceria_valido:
			self.botones_totales[0].set_sensitive(True)
		else:
			self.botones_totales[0].set_sensitive(False)

	def entrys_completados_regaleria(self,widget):
		if self.codigo_regaleria_valido and self.costo_regaleria_valido and self.precio_regaleria_valido:
			self.botones_totales[0].set_sensitive(True)
		else:
			self.botones_totales[0].set_sensitive(False)

	def entrys_completados_santeria(self,widget):
		if self.codigo_santeria_valido and self.costo_santeria_valido and self.precio_santeria_valido:
			self.botones_totales[0].set_sensitive(True)
		else:
			self.botones_totales[0].set_sensitive(False)

	def entrys_completados_ropa(self,widget):
		if self.codigo_ropa_valido and self.costo_ropa_valido and self.precio_ropa_valido:
			self.botones_totales[0].set_sensitive(True)
		else:
			self.botones_totales[0].set_sensitive(False)

	def entrys_completados_bijouterie(self,widget):
		if self.codigo_bijouterie_valido and self.costo_bijouterie_valido and self.precio_bijouterie_valido:
			self.botones_totales[0].set_sensitive(True)
		else:
			self.botones_totales[0].set_sensitive(False)

	def entrys_completados_jugueteria(self,widget):
		if self.codigo_jugueteria_valido and self.costo_jugueteria_valido and self.precio_jugueteria_valido:
			self.botones_totales[0].set_sensitive(True)
		else:
			self.botones_totales[0].set_sensitive(False)

#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


	def codigo_no_repetido(self,liststore_elejido,numero_entry_totales_codigo,inicio_letras_codigo):
		repetido=False
		for x in range(len(liststore_elejido) ):
			if liststore_elejido[x][2] == self.letra_inicio_codigo[inicio_letras_codigo]+self.entry_totales_codigo[numero_entry_totales_codigo].get_text():
				repetido=True
				break
		if repetido:
			return True
		else:
			return False

	def codigo_no_repetido_ROPA(self,liststore_elejido,numero_entry_totales_codigo):
		repetido=False
		model = self.combobox_ropas.get_model()
		active = self.combobox_ropas.get_active()
		for x in range(len(liststore_elejido) ):
			if liststore_elejido[x][2] == model[active][0]+self.entry_totales_codigo[numero_entry_totales_codigo].get_text():
				repetido=True
				break
		if repetido:
			return True
		else:
			return False


#------------------------------VALIDACION LANA-------------------------------------------------------------------------

	def verificar_codigos_lana(self,widget,total_liststore_productos):
		numero_entry_totales_codigo=0
		inicio_letras_codigo=0
		liststore_elejido=total_liststore_productos[1]
		if self.entry_lana[0].get_text() != "":
			if not self.codigo_no_repetido(liststore_elejido,numero_entry_totales_codigo,inicio_letras_codigo):
				self.label_codigo_incorrecto_lana.set_text("")
				self.codigo_lana_valido=True
			else:
				self.codigo_lana_valido=False
				self.label_codigo_incorrecto_lana.set_text("Repetido.")
		else:
			self.codigo_lana_valido=False
			self.label_codigo_incorrecto_lana.set_text("Incorrecto.")

	def verificar_costo_lana(self,widget):
		if self.entry_lana[2].get_text() != "":
			try:
				float(self.entry_lana[2].get_text() )
				self.costo_lana_valido=True
				self.label_costo_incorrecto_lana.set_text("")
			except ValueError :
					self.label_costo_incorrecto_lana.set_text("Costo Invalido.")
					self.costo_lana_valido=False
		else:
			self.costo_lana_valido=False
			self.label_costo_incorrecto_lana.set_text("Costo Invalido.")

	def verificar_precio_lana(self,widget):
		if self.entry_lana[3].get_text() != "":
			try:
				float(self.entry_lana[3].get_text() )
				self.precio_lana_valido=True
				self.label_precio_incorrecto_lana.set_text("")
			except ValueError :
					self.label_precio_incorrecto_lana.set_text("Precio Invalido.")
					self.precio_lana_valido=False
		else:
			self.precio_lana_valido=False
			self.label_precio_incorrecto_lana.set_text("Costo Invalido.")


#------------------------------VALIDACION MERCERIA-------------------------------------------------------------------------

	def verificar_codigos_merceria(self,widget,total_liststore_productos):
		numero_entry_totales_codigo=1
		inicio_letras_codigo=1
		liststore_elejido=total_liststore_productos[0]
		if self.entry_merceria[0].get_text() != "":
			if not self.codigo_no_repetido(liststore_elejido,numero_entry_totales_codigo,inicio_letras_codigo):
				self.label_codigo_incorrecto_merceria.set_text("")
				self.codigo_merceria_valido=True
			else:
				self.codigo_merceria_valido=False
				self.label_codigo_incorrecto_merceria.set_text("Repetido.")
		else:
			self.codigo_merceria_valido=False
			self.label_codigo_incorrecto_merceria.set_text("Incorrecto.")

	def verificar_costo_merceria(self,widget):
		if self.entry_merceria[2].get_text() != "":
			try:
				float(self.entry_merceria[2].get_text() )
				self.costo_merceria_valido=True
				self.label_costo_incorrecto_merceria.set_text("")
			except ValueError :
					self.label_costo_incorrecto_merceria.set_text("Costo Invalido.")
					self.costo_merceria_valido=False
		else:
			self.costo_merceria_valido=False
			self.label_costo_incorrecto_merceria.set_text("Costo Invalido.")

	def verificar_precio_merceria(self,widget):
		if self.entry_merceria[3].get_text() != "":
			try:
				float(self.entry_merceria[3].get_text() )
				self.precio_merceria_valido=True
				self.label_precio_incorrecto_merceria.set_text("")
			except ValueError :
					self.label_precio_incorrecto_merceria.set_text("Precio Invalido.")
					self.precio_merceria_valido=False
		else:
			self.precio_merceria_valido=False
			self.label_precio_incorrecto_merceria.set_text("Precio Invalido.")

#------------------------------VALIDACION REGALERIA-------------------------------------------------------------------------

	def verificar_codigos_regaleria(self,widget,total_liststore_productos):
		numero_entry_totales_codigo=2
		inicio_letras_codigo=2
		liststore_elejido=total_liststore_productos[3]
		if self.entry_regaleria[0].get_text() != "":
			if not self.codigo_no_repetido(liststore_elejido,numero_entry_totales_codigo,inicio_letras_codigo):
				self.label_codigo_incorrecto_regaleria.set_text("")
				self.codigo_regaleria_valido=True
			else:
				self.codigo_regaleria_valido=False
				self.label_codigo_incorrecto_regaleria.set_text("Repetido.")
		else:
			self.codigo_regaleria_valido=False
			self.label_codigo_incorrecto_regaleria.set_text("Incorrecto.")

	def verificar_costo_regaleria(self,widget):
		if self.entry_regaleria[2].get_text() != "":
			try:
				float(self.entry_regaleria[2].get_text() )
				self.costo_regaleria_valido=True
				self.label_costo_incorrecto_regaleria.set_text("")
			except ValueError :
					self.label_costo_incorrecto_regaleria.set_text("Costo Invalido.")
					self.costo_regaleria_valido=False
		else:
			self.costo_regaleria_valido=False
			self.label_costo_incorrecto_regaleria.set_text("Costo Invalido.")

	def verificar_precio_regaleria(self,widget):
		if self.entry_regaleria[3].get_text() != "":
			try:
				float(self.entry_regaleria[3].get_text() )
				self.precio_regaleria_valido=True
				self.label_precio_incorrecto_regaleria.set_text("")
			except ValueError :
					self.label_precio_incorrecto_regaleria.set_text("Precio Invalido.")
					self.precio_regaleria_valido=False
		else:
			self.precio_regaleria_valido=False
			self.label_precio_incorrecto_regaleria.set_text("Precio Invalido.")

#------------------------------VALIDACION SANTERIA-------------------------------------------------------------------------

	def verificar_codigos_santeria(self,widget,total_liststore_productos):
		numero_entry_totales_codigo=3
		inicio_letras_codigo=3
		liststore_elejido=total_liststore_productos[5]
		if self.entry_santeria[0].get_text() != "":
			if not self.codigo_no_repetido(liststore_elejido,numero_entry_totales_codigo,inicio_letras_codigo):
				self.label_codigo_incorrecto_santeria.set_text("")
				self.codigo_santeria_valido=True
			else:
				self.codigo_santeria_valido=False
				self.label_codigo_incorrecto_santeria.set_text("Repetido.")
		else:
			self.codigo_regaleria_valido=False
			self.label_codigo_incorrecto_santeria.set_text("Incorrecto.")

	def verificar_costo_santeria(self,widget):
		if self.entry_santeria[2].get_text() != "":
			try:
				float(self.entry_santeria[2].get_text() )
				self.costo_santeria_valido=True
				self.label_costo_incorrecto_santeria.set_text("")
			except ValueError :
					self.label_costo_incorrecto_santeria.set_text("Costo Invalido.")
					self.costo_santeria_valido=False
		else:
			self.costo_santeria_valido=False
			self.label_costo_incorrecto_santeria.set_text("Costo Invalido.")

	def verificar_precio_santeria(self,widget):
		if self.entry_santeria[3].get_text() != "":
			try:
				float(self.entry_santeria[3].get_text() )
				self.precio_santeria_valido=True
				self.label_precio_incorrecto_santeria.set_text("")
			except ValueError :
					self.label_precio_incorrecto_santeria.set_text("Precio Invalido.")
					self.precio_santeria_valido=False
		else:
			self.precio_santeria_valido=False
			self.label_precio_incorrecto_santeria.set_text("Precio Invalido.")

#------------------------------VALIDACION ROPA-------------------------------------------------------------------------

	def verificar_codigos_ropa(self,widget,total_liststore_productos):
		numero_entry_totales_codigo=4
		liststore_elejido=total_liststore_productos[2]
		if self.entry_ropa[0].get_text() != "":
			if not self.codigo_no_repetido_ROPA(liststore_elejido,numero_entry_totales_codigo):
				self.label_codigo_incorrecto_ropa.set_text("")
				self.codigo_ropa_valido=True
			else:
				self.codigo_ropa_valido=False
				self.label_codigo_incorrecto_ropa.set_text("Repetido.")
		else:
			self.codigo_ropa_valido=False
			self.label_codigo_incorrecto_ropa.set_text("Incorrecto.")

	def verificar_costo_ropa(self,widget):
		if self.entry_ropa[2].get_text() != "":
			try:
				float(self.entry_ropa[2].get_text() )
				self.costo_ropa_valido=True
				self.label_costo_incorrecto_ropa.set_text("")
			except ValueError :
					self.label_costo_incorrecto_ropa.set_text("Costo Invalido.")
					self.costo_ropa_valido=False
		else:
			self.costo_ropa_valido=False
			self.label_costo_incorrecto_ropa.set_text("Costo Invalido.")

	def verificar_precio_ropa(self,widget):
		if self.entry_ropa[3].get_text() != "":
			try:
				float(self.entry_ropa[3].get_text() )
				self.precio_ropa_valido=True
				self.label_precio_incorrecto_ropa.set_text("")
			except ValueError :
					self.label_precio_incorrecto_ropa.set_text("Precio Invalido.")
					self.precio_ropa_valido=False
		else:
			self.precio_ropa_valido=False
			self.label_precio_incorrecto_ropa.set_text("Precio Invalido.")

#------------------------------VALIDACION bijouterie-------------------------------------------------------------------------

	def verificar_codigos_bijouterie(self,widget,total_liststore_productos):
		numero_entry_totales_codigo=5
		inicio_letras_codigo=4
		liststore_elejido=total_liststore_productos[6]
		if self.entry_bijouterie[0].get_text() != "":
			if not self.codigo_no_repetido(liststore_elejido,numero_entry_totales_codigo,inicio_letras_codigo):
				self.label_codigo_incorrecto_bijouterie.set_text("")
				self.codigo_bijouterie_valido=True
			else:
				self.codigo_bijouterie_valido=False
				self.label_codigo_incorrecto_bijouterie.set_text("Repetido.")
		else:
			self.codigo_bijouterie_valido=False
			self.label_codigo_incorrecto_bijouterie.set_text("Incorrecto.")

	def verificar_costo_bijouterie(self,widget):
		if self.entry_bijouterie[2].get_text() != "":
			try:
				float(self.entry_bijouterie[2].get_text() )
				self.costo_bijouterie_valido=True
				self.label_costo_incorrecto_bijouterie.set_text("")
			except ValueError :
					self.label_costo_incorrecto_bijouterie.set_text("Costo Invalido.")
					self.costo_bijouterie_valido=False
		else:
			self.costo_bijouterie_valido=False
			self.label_costo_incorrecto_bijouterie.set_text("Costo Invalido.")

	def verificar_precio_bijouterie(self,widget):
		if self.entry_bijouterie[3].get_text() != "":
			try:
				float(self.entry_bijouterie[3].get_text() )
				self.precio_bijouterie_valido=True
				self.label_precio_incorrecto_bijouterie.set_text("")
			except ValueError :
					self.label_precio_incorrecto_bijouterie.set_text("Precio Invalido.")
					self.precio_bijouterie_valido=False
		else:
			self.precio_bijouterie_valido=False
			self.label_precio_incorrecto_bijouterie.set_text("Precio Invalido.")


#------------------------------VALIDACION JUGUETERIA-------------------------------------------------------------------------

	def verificar_codigos_jugueteria(self,widget,total_liststore_productos):
		numero_entry_totales_codigo=6
		inicio_letras_codigo=5
		liststore_elejido=total_liststore_productos[4]
		if self.entry_jugueteria[0].get_text() != "":
			if not self.codigo_no_repetido(liststore_elejido,numero_entry_totales_codigo,inicio_letras_codigo):
				self.label_codigo_incorrecto_jugueteria.set_text("")
				self.codigo_jugueteria_valido=True
			else:
				self.codigo_jugueteria_valido=False
				self.label_codigo_incorrecto_jugueteria.set_text("Repetido.")
		else:
			self.codigo_jugueteria_valido=False
			self.label_codigo_incorrecto_jugueteria.set_text("Incorrecto.")

	def verificar_costo_jugueteria(self,widget):
		if self.entry_jugueteria[2].get_text() != "":
			try:
				float(self.entry_jugueteria[2].get_text() )
				self.costo_jugueteria_valido=True
				self.label_costo_incorrecto_jugueteria.set_text("")
			except ValueError :
					self.label_costo_incorrecto_jugueteria.set_text("Costo Invalido.")
					self.costo_jugueteria_valido=False
		else:
			self.costo_jugueteria_valido=False
			self.label_costo_incorrecto_jugueteria.set_text("Costo Invalido.")

	def verificar_precio_jugueteria(self,widget):
		if self.entry_jugueteria[3].get_text() != "":
			try:
				float(self.entry_jugueteria[3].get_text() )
				self.precio_jugueteria_valido=True
				self.label_precio_incorrecto_jugueteria.set_text("")
			except ValueError :
					self.label_precio_incorrecto_jugueteria.set_text("Precio Invalido.")
					self.precio_jugueteria_valido=False
		else:
			self.precio_jugueteria_valido=False
			self.label_precio_incorrecto_jugueteria.set_text("Precio Invalido.")

##################################################################################################################
##################################################################################################################

	def limpiar_datos(self,widget):
		model = self.combobox.get_model()
		index = self.combobox.get_active()

		if model[index][0] =="Lana":
			for x in range(4):
				self.entry_lana[x].set_text("")
				self.pin_lana[x].set_value(1)
				self.entry_lana[x].set_editable(True)
				self.pin_lana[x].set_editable(True)
			self.label_informar_cargado_lana.set_text("")
			self.label_codigo_incorrecto_lana.set_text("")
			self.label_precio_incorrecto_lana.set_text("")
			self.label_costo_incorrecto_lana.set_text("")
			self.entry_lana[0].set_property("is-focus",1)

		elif model[index][0] =="Merceria":
			for x in range(4):
				self.entry_merceria[x].set_text("")
				self.pin_merceria[x].set_value(1)
				self.entry_merceria[x].set_editable(True)
				self.pin_merceria[x].set_editable(True)
			self.label_informar_cargado_merceria.set_text("")
			self.label_codigo_incorrecto_merceria.set_text("")
			self.label_precio_incorrecto_merceria.set_text("")
			self.label_costo_incorrecto_merceria.set_text("")
			self.entry_merceria[0].set_property("is-focus",1)

		elif model[index][0] =="Regaleria":
			for x in range(4):
				self.entry_regaleria[x].set_text("")
				self.pin_regaleria[x].set_value(1)
				self.entry_regaleria[x].set_editable(True)
				self.pin_regaleria[x].set_editable(True)
			self.label_informar_cargado_regaleria.set_text("")
			self.label_codigo_incorrecto_regaleria.set_text("")
			self.label_precio_incorrecto_regaleria.set_text("")
			self.label_costo_incorrecto_regaleria.set_text("")
			self.entry_regaleria[0].set_property("is-focus",1)

		elif model[index][0] =="Santeria":
			for x in range(4):
				self.entry_santeria[x].set_text("")
				self.pin_santeria[x].set_value(1)
				self.entry_santeria[x].set_editable(True)
				self.pin_santeria[x].set_editable(True)
			self.label_informar_cargado_santeria.set_text("")
			self.label_codigo_incorrecto_santeria.set_text("")
			self.label_precio_incorrecto_santeria.set_text("")
			self.label_costo_incorrecto_santeria.set_text("")
			self.entry_santeria[0].set_property("is-focus",1)

		elif model[index][0] =="Ropa":
			for x in range(4):
				self.entry_ropa[x].set_text("")
				self.pin_ropa[x].set_value(1)
				self.entry_ropa[x].set_editable(True)
				self.pin_ropa[x].set_editable(True)
			self.label_informar_cargado_ropa.set_text("")
			self.label_codigo_incorrecto_ropa.set_text("")
			self.label_precio_incorrecto_ropa.set_text("")
			self.label_costo_incorrecto_ropa.set_text("")
			self.entry_ropa[0].set_property("is-focus",1)

		elif model[index][0] =="Bijouterie":
			for x in range(4):
				self.entry_bijouterie[x].set_text("")
				self.pin_bijouterie[x].set_value(1)
				self.entry_bijouterie[x].set_editable(True)
				self.pin_bijouterie[x].set_editable(True)
			self.label_informar_cargado_bijouterie.set_text("")
			self.label_codigo_incorrecto_bijouterie.set_text("")
			self.label_precio_incorrecto_bijouterie.set_text("")
			self.label_costo_incorrecto_bijouterie.set_text("")
			self.entry_bijouterie[0].set_property("is-focus",1)

		elif model[index][0] =="Jugueteria":
			for x in range(4):
				self.entry_jugueteria[x].set_text("")
				self.pin_jugueteria[x].set_value(1)
				self.entry_jugueteria[x].set_editable(True)
				self.pin_jugueteria[x].set_editable(True)
			self.label_informar_cargado_jugueteria.set_text("")
			self.label_codigo_incorrecto_jugueteria.set_text("")
			self.label_precio_incorrecto_jugueteria.set_text("")
			self.label_costo_incorrecto_jugueteria.set_text("")
			self.entry_jugueteria[0].set_property("is-focus",1)

##################################################################################################################
##################################################################################################################


	def cerrar(self,widget,event,ventana_principal):
		self.window.destroy()
		ventana_principal.set_sensitive(True)

	def cerrar_button(self,widget,ventana_principal):
		self.window.destroy()
		ventana_principal.set_sensitive(True)


	def __init__(self,ventana_principal,total_liststore_productos):
		ventana_principal.set_sensitive(False)
		self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		icono="../Images/fusa_icon.png"
		self.window.set_icon(gtk.gdk.pixbuf_new_from_file(icono) )
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_title("Agregar Producto")
		self.window.set_size_request(490,650)
		self.window.set_resizable(False)
		self.window.connect("delete-event",self.cerrar,ventana_principal)

		image_fondo=gtk.Image()
		#image_fondo.set_from_file("../Images/fondo_agregar_producto.png")

		fixed=gtk.Fixed()
		fixed.add(image_fondo)
		self.window.add(fixed)

		atributos = pango.AttrList()
		atributos.insert(pango.AttrSize(12400,0,-1))
		atributos.insert(pango.AttrWeight(1200,0,-1))

		label_tipo_producto=gtk.Label("Tipo de Producto : ")
		label_tipo_producto.set_attributes(atributos)
		fixed.put(label_tipo_producto,60,10)

		self.combobox = gtk.combo_box_new_text()
		self.combobox.append_text('Lana')
		self.combobox.append_text('Merceria')
		self.combobox.append_text('Regaleria')
		self.combobox.append_text('Santeria')
		self.combobox.append_text('Ropa')
		self.combobox.append_text('Bijouterie')
		self.combobox.append_text('Jugueteria')
		fixed.put(self.combobox,225,5)

		fuente_entrys="Sans 13"
		self.letra_inicio_codigo=("LA-","M-","RE-","SA-","BI-","J-")
								#LANA
#############################################################################################################
		self.fixed_lana=gtk.Fixed()
		fixed.put(self.fixed_lana,110,40)

		self.label_informar_cargado_lana=gtk.Label("")
		self.label_informar_cargado_lana.set_attributes(atributos)
		self.label_informar_cargado_lana.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_lana.put(self.label_informar_cargado_lana,45,450)

		titulo_labels_lana=("Codigo : ","Descripcion : ","Costo : ","Precio : ","Ganancia : ","Cantidad Inicial: ","Cantidad Disponible : ","Punto Reposicion : ")
		labels_cordenadaY_lana=(25,75,125,175,225,275,325,375)
		self.labels_lana=[]
		for x in range(8):
			self.labels_lana.append(gtk.Label(titulo_labels_lana[x]) )
			self.labels_lana[x].set_attributes(atributos)
			self.fixed_lana.put(self.labels_lana[x],-50,labels_cordenadaY_lana[x])

		self.entry_lana=[]
		coordenadas_entryYlana=(21,71,121,171)

		Label_LA=gtk.Label("LA-")
		Label_LA.set_attributes(atributos)
		self.fixed_lana.put(Label_LA,115,22)

		for x in range(4):
			self.entry_lana.append( gtk.Entry() )
			font_entry_lana = pango.FontDescription(fuente_entrys)
			self.entry_lana[x].modify_font(font_entry_lana)
			self.entry_lana[x].set_size_request(150,26)
			if x ==0:
				self.fixed_lana.put(self.entry_lana[x],145,coordenadas_entryYlana[x])
			else:
				self.fixed_lana.put(self.entry_lana[x],115,coordenadas_entryYlana[x])

		self.entry_lana[0].connect("changed",self.verificar_codigos_lana,total_liststore_productos)
		self.entry_lana[2].connect("changed",self.verificar_costo_lana)
		self.entry_lana[3].connect("changed",self.verificar_precio_lana)

		self.entry_lana[0].connect("changed",self.entrys_completados_lana)
		self.entry_lana[2].connect("changed",self.entrys_completados_lana)
		self.entry_lana[3].connect("changed",self.entrys_completados_lana)


		self.pin_lana=[]
		adj_lana=[]
		coordenadasY_lana=(221,271,321,371)
		for x in range(3):
			adj_lana.append( gtk.Adjustment(value=0, lower=1, upper=9999999,step_incr=0.1,page_incr=0.1,page_size=0) )
			self.pin_lana.append ( gtk.SpinButton(adjustment=adj_lana[x], climb_rate=0.1, digits=3) )
			self.pin_lana[x].set_numeric(True)
			self.pin_lana[x].set_size_request(100,28)
			font_spin_lana = pango.FontDescription(fuente_entrys)
			self.pin_lana[x].modify_font(font_spin_lana)
			self.fixed_lana.put(self.pin_lana[x],115,coordenadasY_lana[x])

		adj_lana.append( gtk.Adjustment(value=0, lower=1, upper=9999999,step_incr=1,page_incr=1,page_size=0) )
		self.pin_lana.append ( gtk.SpinButton(adjustment=adj_lana[3], climb_rate=1.0, digits=0) )
		#self.pin_lana[3].set_numeric(True)
		self.pin_lana[3].set_size_request(80,28)
		self.pin_lana[3].set_max_length(7)
		font_spin_lana = pango.FontDescription(fuente_entrys)
		self.pin_lana[3].modify_font(font_spin_lana)
		self.fixed_lana.put(self.pin_lana[3],115,371)

		label_porcentaje_lana=gtk.Label("%")
		label_porcentaje_lana.modify_font(font_spin_lana)
		self.fixed_lana.put(label_porcentaje_lana,200,225)

		self.label_codigo_incorrecto_lana=gtk.Label()
		self.label_codigo_incorrecto_lana.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_costo_incorrecto_lana=gtk.Label()
		self.label_costo_incorrecto_lana.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_precio_incorrecto_lana=gtk.Label()
		self.label_precio_incorrecto_lana.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))


		self.fixed_lana.put(self.label_codigo_incorrecto_lana,296,22)
		self.fixed_lana.put(self.label_costo_incorrecto_lana,266,123)
		self.fixed_lana.put(self.label_precio_incorrecto_lana,266,173)


										#MERCERIA
##################################################################################################################
		self.fixed_merceria=gtk.Fixed()
		fixed.put(self.fixed_merceria,110,40)

		self.label_informar_cargado_merceria=gtk.Label()
		self.label_informar_cargado_merceria.set_attributes(atributos)
		self.label_informar_cargado_merceria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_merceria.put(self.label_informar_cargado_merceria,45,450)

		titulo_labels_merceria=("Codigo : ","Descripcion : ","Costo : ","Precio : ","Ganancia : ","Cantidad Inicial: ","Cantidad Disponible : ","Punto Reposicion : ")
		labels_cordenadaY_merceria=(25,75,125,175,225,275,325,375)
		self.labels_merceria=[]
		for x in range(8):
			self.labels_merceria.append(gtk.Label(titulo_labels_merceria[x]) )
			self.labels_merceria[x].set_attributes(atributos)
			self.fixed_merceria.put(self.labels_merceria[x],-50,labels_cordenadaY_merceria[x])


		Label_ME=gtk.Label("M-")
		Label_ME.set_attributes(atributos)
		self.fixed_merceria.put(Label_ME,121,22)


		self.entry_merceria=[]
		coordenadas_entryYmerceria=(21,71,121,171)
		for x in range(4):
			self.entry_merceria.append( gtk.Entry() )
			font_entry_merceria = pango.FontDescription(fuente_entrys)
			self.entry_merceria[x].modify_font(font_entry_merceria)
			self.entry_merceria[x].set_size_request(150,26)
			if x==0:
				self.fixed_merceria.put(self.entry_merceria[x],145,coordenadas_entryYmerceria[x])
			else:
				self.fixed_merceria.put(self.entry_merceria[x],115,coordenadas_entryYmerceria[x])

		self.entry_merceria[0].connect("changed",self.verificar_codigos_merceria,total_liststore_productos)
		self.entry_merceria[2].connect("changed",self.verificar_costo_merceria)
		self.entry_merceria[3].connect("changed",self.verificar_precio_merceria)

		self.entry_merceria[0].connect("changed",self.entrys_completados_merceria)
		self.entry_merceria[2].connect("changed",self.entrys_completados_merceria)
		self.entry_merceria[3].connect("changed",self.entrys_completados_merceria)


		self.pin_merceria=[]
		adj_merceria=[]
		coordenadasY_spin_merceria=(221,271,321,371)
		for x in range(3):
			adj_merceria.append( gtk.Adjustment(value=0, lower=1, upper=999999,step_incr=0.1,page_incr=0.1,page_size=0) )
			self.pin_merceria.append ( gtk.SpinButton(adjustment=adj_merceria[x], climb_rate=0.1, digits=3) )
			self.pin_merceria[x].set_numeric(True)
			self.pin_merceria[x].set_size_request(100,28)
			font_spin_merceria = pango.FontDescription(fuente_entrys)
			self.pin_merceria[x].modify_font(font_spin_merceria)
			self.fixed_merceria.put(self.pin_merceria[x],115,coordenadasY_spin_merceria[x])

		adj_merceria.append( gtk.Adjustment(value=0, lower=1, upper=9999,step_incr=1,page_incr=1,page_size=0) )
		self.pin_merceria.append ( gtk.SpinButton(adjustment=adj_merceria[3], climb_rate=1.0, digits=0) )
		self.pin_merceria[3].set_numeric(True)
		self.pin_merceria[3].set_size_request(80,28)
		self.pin_merceria[3].set_max_length(7)
		font_spin_merceria = pango.FontDescription(fuente_entrys)
		self.pin_merceria[3].modify_font(font_spin_merceria)
		self.fixed_merceria.put(self.pin_merceria[3],115,coordenadasY_spin_merceria[3])


		self.label_codigo_incorrecto_merceria=gtk.Label()
		self.label_codigo_incorrecto_merceria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_costo_incorrecto_merceria=gtk.Label()
		self.label_costo_incorrecto_merceria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_precio_incorrecto_merceria=gtk.Label()
		self.label_precio_incorrecto_merceria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))


		self.fixed_merceria.put(self.label_codigo_incorrecto_merceria,296,22)
		self.fixed_merceria.put(self.label_costo_incorrecto_merceria,266,123)
		self.fixed_merceria.put(self.label_precio_incorrecto_merceria,266,173)

		label_porcentaje_merceria=gtk.Label("%")
		label_porcentaje_merceria.modify_font(font_spin_merceria)
		self.fixed_merceria.put(label_porcentaje_merceria,200,225)


								#REGALERIA
#############################################################################################################
		self.fixed_regaleria=gtk.Fixed()
		fixed.put(self.fixed_regaleria,110,40)

		self.label_informar_cargado_regaleria=gtk.Label()
		self.label_informar_cargado_regaleria.set_attributes(atributos)
		self.label_informar_cargado_regaleria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_regaleria.put(self.label_informar_cargado_regaleria,45,450)

		titulo_labels_regaleria=("Codigo : ","Descripcion : ","Costo : ","Precio : ","Ganancia : ","Cantidad Inicial: ","Cantidad Disponible : ","Punto Reposicion : ")
		labels_cordenadaY_regaleria=(25,75,125,175,225,275,325,375)
		self.labels_regaleria=[]
		for x in range(8):
			self.labels_regaleria.append(gtk.Label(titulo_labels_regaleria[x]) )
			self.labels_regaleria[x].set_attributes(atributos)
			self.fixed_regaleria.put(self.labels_regaleria[x],-50,labels_cordenadaY_regaleria[x])

		Label_RE=gtk.Label("RE-")
		Label_RE.set_attributes(atributos)
		self.fixed_regaleria.put(Label_RE,115,22)

		self.entry_regaleria=[]
		coordenadas_entryYregaleria=(21,71,121,171)
		for x in range(4):
			self.entry_regaleria.append( gtk.Entry() )
			font_entry_regaleria = pango.FontDescription(fuente_entrys)
			self.entry_regaleria[x].modify_font(font_entry_regaleria)
			self.entry_regaleria[x].set_size_request(150,26)
			if x ==0:
				self.fixed_regaleria.put(self.entry_regaleria[x],145,coordenadas_entryYregaleria[x])
			else:
				self.fixed_regaleria.put(self.entry_regaleria[x],115,coordenadas_entryYregaleria[x])

		self.entry_regaleria[0].connect("changed",self.verificar_codigos_regaleria,total_liststore_productos)
		self.entry_regaleria[2].connect("changed",self.verificar_costo_regaleria)
		self.entry_regaleria[3].connect("changed",self.verificar_precio_regaleria)

		self.entry_regaleria[0].connect("changed",self.entrys_completados_regaleria)
		self.entry_regaleria[2].connect("changed",self.entrys_completados_regaleria)
		self.entry_regaleria[3].connect("changed",self.entrys_completados_regaleria)

		self.pin_regaleria=[]
		adj_regaleria=[]
		coordenadasY_regaleria=(221,271,321,371)
		for x in range(4):
			adj_regaleria.append( gtk.Adjustment(value=0, lower=1, upper=9999,step_incr=1,page_incr=1,page_size=0) )
			self.pin_regaleria.append ( gtk.SpinButton(adjustment=adj_regaleria[x], climb_rate=1.0, digits=0) )
			self.pin_regaleria[x].set_numeric(True)
			self.pin_regaleria[x].set_size_request(80,28)
			self.pin_regaleria[x].set_max_length(7)
			font_spin_regaleria = pango.FontDescription(fuente_entrys)
			self.pin_regaleria[x].modify_font(font_spin_regaleria)
			self.fixed_regaleria.put(self.pin_regaleria[x],115,coordenadasY_regaleria[x])


		self.label_codigo_incorrecto_regaleria=gtk.Label()
		self.label_codigo_incorrecto_regaleria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_costo_incorrecto_regaleria=gtk.Label()
		self.label_costo_incorrecto_regaleria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_precio_incorrecto_regaleria=gtk.Label()
		self.label_precio_incorrecto_regaleria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))


		self.fixed_regaleria.put(self.label_codigo_incorrecto_regaleria,296,22)
		self.fixed_regaleria.put(self.label_costo_incorrecto_regaleria,266,123)
		self.fixed_regaleria.put(self.label_precio_incorrecto_regaleria,266,173)

		label_porcentaje_regaleria=gtk.Label("%")
		label_porcentaje_regaleria.modify_font(font_spin_regaleria)
		self.fixed_regaleria.put(label_porcentaje_regaleria,200,225)

										#SANTERIA
#################################################################################################################
		self.fixed_santeria=gtk.Fixed()
		fixed.put(self.fixed_santeria,110,40)

		self.label_informar_cargado_santeria=gtk.Label()
		self.label_informar_cargado_santeria.set_attributes(atributos)
		self.label_informar_cargado_santeria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_santeria.put(self.label_informar_cargado_santeria,45,450)

		titulo_labels_santeria=("Codigo : ","Descripcion : ","Costo : ","Precio : ","Ganancia : ","Cantidad Inicial: ","Cantidad Disponible : ","Punto Reposicion : ")
		labels_cordenadaY_santeria=(25,75,125,175,225,275,325,375)
		self.labels_santeria=[]
		for x in range(8):
			self.labels_santeria.append(gtk.Label(titulo_labels_santeria[x]) )
			self.labels_santeria[x].set_attributes(atributos)
			self.fixed_santeria.put(self.labels_santeria[x],-50,labels_cordenadaY_santeria[x])

		Label_SA=gtk.Label("SN-")
		Label_SA.set_attributes(atributos)
		self.fixed_santeria.put(Label_SA,115,22)

		self.entry_santeria=[]
		coordenadas_entryYsanteria=(21,71,121,171)
		for x in range(4):
			self.entry_santeria.append( gtk.Entry() )
			font_entry_motores = pango.FontDescription(fuente_entrys)
			self.entry_santeria[x].modify_font(font_entry_motores)
			self.entry_santeria[x].set_size_request(150,26)
			if x ==0:
				self.fixed_santeria.put(self.entry_santeria[x],145,coordenadas_entryYsanteria[x])
			else:
				self.fixed_santeria.put(self.entry_santeria[x],115,coordenadas_entryYsanteria[x])

		self.entry_santeria[0].connect("changed",self.verificar_codigos_santeria,total_liststore_productos)
		self.entry_santeria[2].connect("changed",self.verificar_costo_santeria)
		self.entry_santeria[3].connect("changed",self.verificar_precio_santeria)

		self.entry_santeria[0].connect("changed",self.entrys_completados_santeria)
		self.entry_santeria[2].connect("changed",self.entrys_completados_santeria)
		self.entry_santeria[3].connect("changed",self.entrys_completados_santeria)

		coordenadasY_santeria=(221,271,321,371)
		self.pin_santeria=[]
		adj_santeria=[]
		font_spin_santeria= pango.FontDescription(fuente_entrys)
		for x in range(4):
			adj_santeria.append( gtk.Adjustment(value=0, lower=1, upper=9999,step_incr=1,page_incr=1,page_size=0) )
			self.pin_santeria.append ( gtk.SpinButton(adjustment=adj_santeria[x], climb_rate=1.0, digits=0) )
			self.pin_santeria[x].set_numeric(True)
			self.pin_santeria[x].set_size_request(80,28)
			self.pin_santeria[x].set_max_length(7)
			self.pin_santeria[x].modify_font(font_spin_santeria)
			self.fixed_santeria.put(self.pin_santeria[x],115,coordenadasY_santeria[x])


		self.label_codigo_incorrecto_santeria=gtk.Label()
		self.label_codigo_incorrecto_santeria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_costo_incorrecto_santeria=gtk.Label()
		self.label_costo_incorrecto_santeria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_precio_incorrecto_santeria=gtk.Label()
		self.label_precio_incorrecto_santeria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))


		self.fixed_santeria.put(self.label_codigo_incorrecto_santeria,296,22)
		self.fixed_santeria.put(self.label_costo_incorrecto_santeria,266,123)
		self.fixed_santeria.put(self.label_precio_incorrecto_santeria,266,173)


		label_porcentaje_santeria=gtk.Label("%")
		label_porcentaje_santeria.modify_font(font_spin_santeria)
		self.fixed_santeria.put(label_porcentaje_santeria,200,225)
										#ROPA
#################################################################################################################
		self.fixed_ropa=gtk.Fixed()
		fixed.put(self.fixed_ropa,110,40)

		self.label_informar_cargado_ropa=gtk.Label()
		self.label_informar_cargado_ropa.set_attributes(atributos)
		self.label_informar_cargado_ropa.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_ropa.put(self.label_informar_cargado_ropa,45,460)

		titulo_labels_ropa=("Codigo : ","Descripcion : ","Costo : ","Precio : ","Ganancia : ","Cantidad Inicial: ","Cantidad Disponible : ","Punto Reposicion : ")
		labels_cordenadaY_ropa=(25,75,125,175,225,275,325,375)
		self.labels_ropa=[]
		for x in range(8):
			self.labels_ropa.append(gtk.Label(titulo_labels_ropa[x]) )
			self.labels_ropa[x].set_attributes(atributos)
			self.fixed_ropa.put(self.labels_ropa[x],-50,labels_cordenadaY_ropa[x])


		self.combobox_ropas = gtk.combo_box_new_text()
		self.combobox_ropas.set_size_request(60,33)
		var_ropas=("RC-","RP-","LE-")
		for x in range (len(var_ropas) ):
			self.combobox_ropas.append_text(var_ropas[x])
		self.combobox_ropas.set_active(0)

		self.fixed_ropa.put(self.combobox_ropas,115,18)

		self.entry_ropa=[]
		coordenadas_entryYropa=(21,71,121,171)
		font_entry_ropa = pango.FontDescription(fuente_entrys)
		for x in range(4):
			self.entry_ropa.append( gtk.Entry() )
			self.entry_ropa[x].modify_font(font_entry_ropa)
			self.entry_ropa[x].set_size_request(150,26)
			if x==0:
				self.entry_ropa[x].set_size_request(120,27)
				self.fixed_ropa.put(self.entry_ropa[x],175,coordenadas_entryYropa[x])
			else:
				self.fixed_ropa.put(self.entry_ropa[x],115,coordenadas_entryYropa[x])

		self.entry_ropa[0].connect("changed",self.verificar_codigos_ropa,total_liststore_productos)
		self.entry_ropa[2].connect("changed",self.verificar_costo_ropa)
		self.entry_ropa[3].connect("changed",self.verificar_precio_ropa)

		self.entry_ropa[0].connect("changed",self.entrys_completados_ropa)
		self.entry_ropa[2].connect("changed",self.entrys_completados_ropa)
		self.entry_ropa[3].connect("changed",self.entrys_completados_ropa)

		coordenadasY_ropa=(221,271,321,371)
		self.pin_ropa=[]
		adj_ropa=[]
		font_spin_ropa= pango.FontDescription(fuente_entrys)
		for x in range(4):
			adj_ropa.append( gtk.Adjustment(value=0, lower=1, upper=9999,step_incr=1,page_incr=1,page_size=0) )
			self.pin_ropa.append ( gtk.SpinButton(adjustment=adj_ropa[x], climb_rate=1.0, digits=0) )
			self.pin_ropa[x].set_numeric(True)
			self.pin_ropa[x].set_size_request(80,28)
			self.pin_ropa[x].set_max_length(7)

			self.pin_ropa[x].modify_font(font_spin_ropa)
			self.fixed_ropa.put(self.pin_ropa[x],115,coordenadasY_ropa[x])


		self.label_codigo_incorrecto_ropa=gtk.Label()
		self.label_codigo_incorrecto_ropa.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_costo_incorrecto_ropa=gtk.Label()
		self.label_costo_incorrecto_ropa.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_precio_incorrecto_ropa=gtk.Label()
		self.label_precio_incorrecto_ropa.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.fixed_ropa.put(self.label_codigo_incorrecto_ropa,296,22)
		self.fixed_ropa.put(self.label_costo_incorrecto_ropa,266,123)
		self.fixed_ropa.put(self.label_precio_incorrecto_ropa,266,173)

		label_porcentaje_ropa=gtk.Label("%")
		label_porcentaje_ropa.modify_font(font_spin_ropa)
		self.fixed_ropa.put(label_porcentaje_ropa,200,225)
										#bijouterie
#################################################################################################################
		self.fixed_bijouterie=gtk.Fixed()
		fixed.put(self.fixed_bijouterie,110,40)

		self.label_informar_cargado_bijouterie=gtk.Label()
		self.label_informar_cargado_bijouterie.set_attributes(atributos)
		self.label_informar_cargado_bijouterie.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_bijouterie.put(self.label_informar_cargado_bijouterie,45,450)

		titulo_labels_bijouterie=("Codigo : ","Descripcion : ","Costo : ","Precio : ","Ganancia : ","Cantidad Inicial: ","Cantidad Disponible : ","Punto Reposicion : ")
		labels_cordenadaY_bijouterie=(25,75,125,175,225,275,325,375)
		self.labels_bijouterie=[]
		for x in range(8):
			self.labels_bijouterie.append(gtk.Label(titulo_labels_bijouterie[x]) )
			self.labels_bijouterie[x].set_attributes(atributos)
			self.fixed_bijouterie.put(self.labels_bijouterie[x],-50,labels_cordenadaY_bijouterie[x])

		Label_BI=gtk.Label("BI-")
		Label_BI.set_attributes(atributos)
		self.fixed_bijouterie.put(Label_BI,115,22)

		self.entry_bijouterie=[]
		coordenadas_entryYbijouterie=(21,71,121,171)
		font_entry_bijouterie = pango.FontDescription(fuente_entrys)
		for x in range(4):
			self.entry_bijouterie.append( gtk.Entry() )
			self.entry_bijouterie[x].modify_font(font_entry_bijouterie)
			self.entry_bijouterie[x].set_size_request(150,26)
			if x == 0:
				self.fixed_bijouterie.put(self.entry_bijouterie[x],145,coordenadas_entryYbijouterie[x])
			else:
				self.fixed_bijouterie.put(self.entry_bijouterie[x],115,coordenadas_entryYbijouterie[x])

		self.entry_bijouterie[0].connect("changed",self.verificar_codigos_bijouterie,total_liststore_productos)
		self.entry_bijouterie[2].connect("changed",self.verificar_costo_bijouterie)
		self.entry_bijouterie[3].connect("changed",self.verificar_precio_bijouterie)

		self.entry_bijouterie[0].connect("changed",self.entrys_completados_bijouterie)
		self.entry_bijouterie[2].connect("changed",self.entrys_completados_bijouterie)
		self.entry_bijouterie[3].connect("changed",self.entrys_completados_bijouterie)

		coordenadasY_bijouterie=(221,271,321,371)
		self.pin_bijouterie=[]
		adj_bijouterie=[]
		font_spin_bijouterie= pango.FontDescription(fuente_entrys)
		for x in range(4):
			adj_bijouterie.append( gtk.Adjustment(value=0, lower=1, upper=9999,step_incr=1,page_incr=1,page_size=0) )
			self.pin_bijouterie.append ( gtk.SpinButton(adjustment=adj_bijouterie[x], climb_rate=1.0, digits=0) )
			self.pin_bijouterie[x].set_numeric(True)
			self.pin_bijouterie[x].set_size_request(80,28)
			self.pin_bijouterie[x].set_max_length(7)

			self.pin_bijouterie[x].modify_font(font_spin_bijouterie)
			self.fixed_bijouterie.put(self.pin_bijouterie[x],115,coordenadasY_bijouterie[x])


		self.label_codigo_incorrecto_bijouterie=gtk.Label()
		self.label_codigo_incorrecto_bijouterie.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_costo_incorrecto_bijouterie=gtk.Label()
		self.label_costo_incorrecto_bijouterie.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_precio_incorrecto_bijouterie=gtk.Label()
		self.label_precio_incorrecto_bijouterie.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))


		self.fixed_bijouterie.put(self.label_codigo_incorrecto_bijouterie,296,22)
		self.fixed_bijouterie.put(self.label_costo_incorrecto_bijouterie,266,123)
		self.fixed_bijouterie.put(self.label_precio_incorrecto_bijouterie,266,173)


		label_porcentaje_bijouterie=gtk.Label("%")
		label_porcentaje_bijouterie.modify_font(font_spin_bijouterie)
		self.fixed_bijouterie.put(label_porcentaje_bijouterie,200,225)

										#JUGUETERIA
#################################################################################################################
		self.fixed_jugueteria=gtk.Fixed()
		fixed.put(self.fixed_jugueteria,110,40)

		self.label_informar_cargado_jugueteria=gtk.Label()
		self.label_informar_cargado_jugueteria.set_attributes(atributos)
		self.label_informar_cargado_jugueteria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))
		self.fixed_jugueteria.put(self.label_informar_cargado_jugueteria,45,450)

		titulo_labels_jugueteria=("Codigo : ","Descripcion : ","Costo : ","Precio : ","Ganancia : ","Cantidad Inicial: ","Cantidad Disponible : ","Punto Reposicion : ")
		labels_cordenadaY_jugueteria=(25,75,125,175,225,275,325,375)
		self.labels_jugueteria=[]
		for x in range(8):
			self.labels_jugueteria.append(gtk.Label(titulo_labels_jugueteria[x]) )
			self.labels_jugueteria[x].set_attributes(atributos)
			self.fixed_jugueteria.put(self.labels_jugueteria[x],-50,labels_cordenadaY_jugueteria[x])

		Label_J=gtk.Label("J-")
		Label_J.set_attributes(atributos)
		self.fixed_jugueteria.put(Label_J,125,23)

		self.entry_jugueteria=[]
		coordenadas_entryYjugueteria=(21,71,121,171)
		font_entry_jugueteria = pango.FontDescription(fuente_entrys)
		for x in range(4):
			self.entry_jugueteria.append( gtk.Entry() )
			self.entry_jugueteria[x].modify_font(font_entry_jugueteria)
			self.entry_jugueteria[x].set_size_request(150,26)
			if x==0:
				self.fixed_jugueteria.put(self.entry_jugueteria[x],145,coordenadas_entryYjugueteria[x])
			else:
				self.fixed_jugueteria.put(self.entry_jugueteria[x],115,coordenadas_entryYjugueteria[x])

		self.entry_jugueteria[0].connect("changed",self.verificar_codigos_jugueteria,total_liststore_productos)
		self.entry_jugueteria[2].connect("changed",self.verificar_costo_jugueteria)
		self.entry_jugueteria[3].connect("changed",self.verificar_precio_jugueteria)

		self.entry_jugueteria[0].connect("changed",self.entrys_completados_jugueteria)
		self.entry_jugueteria[2].connect("changed",self.entrys_completados_jugueteria)
		self.entry_jugueteria[3].connect("changed",self.entrys_completados_jugueteria)


		coordenadasY_jugueteria=(221,271,321,371)
		self.pin_jugueteria=[]
		adj_jugueteria=[]
		font_spin_jugueteria= pango.FontDescription(fuente_entrys)
		for x in range(4):
			adj_jugueteria.append( gtk.Adjustment(value=0, lower=1, upper=9999,step_incr=1,page_incr=1,page_size=0) )
			self.pin_jugueteria.append ( gtk.SpinButton(adjustment=adj_jugueteria[x], climb_rate=1.0, digits=0) )
			self.pin_jugueteria[x].set_numeric(True)
			self.pin_jugueteria[x].set_size_request(80,28)
			self.pin_jugueteria[x].set_max_length(7)

			self.pin_jugueteria[x].modify_font(font_spin_jugueteria)
			self.fixed_jugueteria.put(self.pin_jugueteria[x],115,coordenadasY_jugueteria[x])


		self.label_codigo_incorrecto_jugueteria=gtk.Label()
		self.label_codigo_incorrecto_jugueteria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_costo_incorrecto_jugueteria=gtk.Label()
		self.label_costo_incorrecto_jugueteria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))

		self.label_precio_incorrecto_jugueteria=gtk.Label()
		self.label_precio_incorrecto_jugueteria.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#FF0000'))


		self.fixed_jugueteria.put(self.label_codigo_incorrecto_jugueteria,296,22)
		self.fixed_jugueteria.put(self.label_costo_incorrecto_jugueteria,266,123)
		self.fixed_jugueteria.put(self.label_precio_incorrecto_jugueteria,266,173)

		label_porcentaje_jugueteria=gtk.Label("%")
		label_porcentaje_jugueteria.modify_font(font_spin_jugueteria)
		self.fixed_jugueteria.put(label_porcentaje_jugueteria,200,225)

									#BOTONES
###############################################################################################################
		self.botones_totales=[]
		imagenes=[]
		coordenadas_botonesX=(120,250,360)
		coordenadas_botonesY=(550,550,600)
		ruta_imagenes=("../Images/boton_aceptar.png","../Images/boton_limpiar.png","../Images/boton_cerrar.png")
		for x in range(3):
			imagenes.append(gtk.Image() )
			self.botones_totales.append( gtk.Button() )
			self.botones_totales[x].set_property("relief",2)
			self.botones_totales[x].set_property("can-focus",0)
			self.botones_totales[x].set_size_request(120,40)
			imagenes[x].set_from_file(ruta_imagenes[x])
			self.botones_totales[x].add(imagenes[x] )
			if x!=2:
				self.botones_totales[x].set_sensitive(False)
			fixed.put(self.botones_totales[x],coordenadas_botonesX[x],coordenadas_botonesY[x])

		self.combobox.connect('changed', self.elejir_producto)
		self.botones_totales[0].connect("clicked",self.aceptar_datos,total_liststore_productos)
		self.botones_totales[1].connect("clicked",self.limpiar_datos)
		self.botones_totales[2].connect("clicked",self.cerrar_button,ventana_principal)

		self.entry_totales_codigo=(self.entry_lana[0],self.entry_merceria[0],self.entry_regaleria[0],self.entry_santeria[0],self.entry_ropa[0],self.entry_bijouterie[0],self.entry_jugueteria[0]) #para verificar codigo repetido

		(self.codigo_lana_valido,self.codigo_merceria_valido,self.codigo_regaleria_valido,self.codigo_santeria_valido,self.codigo_ropa_valido,self.codigo_bijouterie_valido,self.codigo_jugueteria_valido)=(False,False,False,False,False,False,False)#|
																																																														#-para desbloquear boton aceptar
		(self.costo_lana_valido,self.costo_merceria_valido,self.costo_regaleria_valido,self.costo_santeria_valido,self.costo_ropa_valido,self.costo_bijouterie_valido,self.costo_jugueteria_valido)=(False,False,False,False,False,False,False)       #|
		(self.precio_lana_valido,self.precio_merceria_valido,self.precio_regaleria_valido,self.precio_santeria_valido,self.precio_ropa_valido,self.precio_bijouterie_valido,self.precio_jugueteria_valido)=(False,False,False,False,False,False,False)#|

		self.window.show_all()

		self.fixed_lana.hide()
		self.fixed_merceria.hide()
		self.fixed_regaleria.hide()
		self.fixed_santeria.hide()
		self.fixed_ropa.hide()
		self.fixed_bijouterie.hide()
		self.fixed_jugueteria.hide()
