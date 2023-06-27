# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FilePath
                                 A QGIS plugin
 This plugin copies the file path of the selected layer
 ***************************************************************************/
"""

from PyQt5.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QToolBar
from qgis.core import QgsProject, Qgis
from PyQt5.Qt import QApplication
import os
# Initialize Qt resources from file resources.py
from .resources import *

class FilePath:

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        # Specify the absolute path of the icon
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")

        # Create action that will start plugin configuration
        self.action = QAction(QIcon(icon_path), "Copy file path", self.iface.mainWindow())
        self.action.triggered.connect(self.copy_layer_path)

        # Create a new toolbar named "File Path Toolbar" and add the action to it
        self.toolbar = self.iface.addToolBar("File Path Toolbar")
        self.toolbar.setObjectName("FilePathToolbar")
        self.toolbar.addAction(self.action)

        # Also, add action to the plugin menu
        self.iface.addPluginToMenu("&File Path", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&File Path", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        # Remove the toolbar when the plugin is unloaded
        del self.toolbar

    def copy_layer_path(self):
        # Get the current layer
        layer = self.iface.activeLayer()

        if layer is None:
            self.iface.messageBar().pushMessage("Error", "No layer selected", level=Qgis.Warning)
            return

        # Get the layer source
        layer_path = layer.source()

        # Copy the layer source to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(layer_path)

        self.iface.messageBar().pushMessage("Success", "Layer path copied to clipboard", level=Qgis.Success)
