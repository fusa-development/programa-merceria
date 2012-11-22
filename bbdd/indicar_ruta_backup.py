#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gtk
import pygtk
import csv

import shutil

from leer_ruta_BD import *
from dividir_hora import *

class indicar_ruta_backup:
	def __init__(self,object):
		self.ruta_archivo_db=""
		object.set_sensitive(False)
		self.dialog = gtk.FileChooserDialog("Indicar Ruta",
											None,
											gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
											(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
											gtk.STOCK_SAVE, gtk.RESPONSE_OK))
		self.dialog.set_default_response(gtk.RESPONSE_OK)
		response = self.dialog.run()
		if response == gtk.RESPONSE_OK:
			nueva_ruta=self.dialog.get_current_folder()
			shutil.copyfile(leer_ruta(),str(nueva_ruta)+"/MERCERIA_Backup_"+dividir_hora()+str(".db")  )

		object.set_sensitive(True)
		self.dialog.destroy()
