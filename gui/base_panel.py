#!/usr/bin/python
# encoding: utf-8
#
#  GUI/Windows version
#  Copyright 2014: Roberto Faga Jr
#
#  http://github.com/rfaga/scriptlattesgui
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util,
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import sys
from PySide import QtCore, QtGui

import os
import re
import string

class BasePanel(object):
    def __init__(self, parent):
        self.settings = QtCore.QSettings("ScriptLattes", "ScriptLattesGUI")
        self.ui = parent.ui
        self.parent = parent
        self.running = False
        
    def get_output_folder(self, output_folder=None):
        if not output_folder:
            output_folder = self.output_folder
        if 'win' in sys.platform.lower():
            return 'file:///' + output_folder.replace('\\', '/')
        else:
            return 'file://' + output_folder