#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk

class indicar_BD:
	def __init__(self,object,entry_new_BD):
		self.ruta_archivo_db=""
		object.set_sensitive(False)
		self.dialog = gtk.FileChooserDialog("Indicar Ruta",
											None,
											gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
											(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
											gtk.STOCK_SAVE, gtk.RESPONSE_OK))
		self.dialog.set_default_response(gtk.RESPONSE_OK)
		#self.dialog.set_current_name(" ")
		response = self.dialog.run()
		if response == gtk.RESPONSE_OK:
			print self.dialog.get_current_folder()


		object.set_sensitive(True)
		self.dialog.destroy()
