# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FilePath
                                 A QGIS plugin
 This plugin copies the file path of the selected layer
 ***************************************************************************/

 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load FilePath class from file FilePath.py
    from .FilePath import FilePath
    return FilePath(iface)
