#!/usr/bin/python
# encoding: utf-8
#
#  GUI/Windows version
#  Copyright 2014: Roberto Faga Jr e Dorival Piedade Neto
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
from gui.main_window import Ui_MainWindow

import os
import re
import string

from gui.single_panel import SingleProcessingTabPanel
from gui.multiple_panel import MultipleProcessingTabPanel


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)

        # definir executavel do scriptLattes
        if 'win' in sys.platform.lower():
            self.CMD = 'scriptLattes.exe'
        else:
            self.CMD = './scriptLattes.py'
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)
        self.single = SingleProcessingTabPanel(self)
        self.multiple = MultipleProcessingTabPanel(self)
        self.setWindowIcon(QtGui.QIcon('gui/logo.png'))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
