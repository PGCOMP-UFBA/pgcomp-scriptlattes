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

from base_panel import BasePanel

class SingleProcessingTabPanel(BasePanel):
    def __init__(self, parent):
        super(SingleProcessingTabPanel, self).__init__(parent)
        
        self.ui.filechooser.clicked.connect(self.choose_file)
        self.ui.runner.clicked.connect(self.run)
        self.ui.openLink.clicked.connect(self.open_link)
        self.ui.openFolder.clicked.connect(self.open_folder)
        
        last_file = self.settings.value('lastFile', None)
        if last_file:
            self.ui.input.setPlainText(last_file)
            
        #self.output_folder = '/tmp/teste-01/'
        #self.output_folder = u'C:\\a paça\\exemplo\\teste-01\\'
        #self.ui.resultsWidget.setDisabled(False)
    
    def print_text(self):
        try:
            s = str(self.process.readAllStandardOutput())
        except:
            s = ""
        try:
            self.ui.out.insertPlainText( s )
        except:
            self.print_error("(String não capturada)")

    def print_error(self):
        s = str(self.process.readAllStandardError())
        msg = "<br><p style='color: red; font-weight: bold'>%s</p>" % s.replace('\n', '<br>')
        self.ui.errors.insertHtml(msg)

    def clearOutputs(self):
        self.ui.out.setPlainText('');
        self.ui.errors.setPlainText('');
        self.ui.statusbar.clearMessage()
    
    def open_link(self):
        path = self.get_output_folder() +  'index.html'
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(path, QtCore.QUrl.TolerantMode))
    
    def open_folder(self):
        path = self.get_output_folder()
        QtGui.QDesktopServices.openUrl(path)
    
    def enable_running(self):
        self.running = True
        self.ui.runner.setDisabled(True)
        self.ui.file_holder.setDisabled(True)
        self.ui.runner.setText('Aguarde, processando...')
        self.ui.statusbar.showMessage('Aguarde, processando...')
        self.ui.mainTabs.setTabEnabled(1, False)
    
    def disable_running(self):
        self.running = False
        self.ui.runner.setDisabled(False)
        self.ui.file_holder.setDisabled(False)
        self.ui.runner.setText('Executar')
        self.ui.statusbar.showMessage('Processo finalizado!')
        self.ui.mainTabs.setTabEnabled(1, True)
    
    def run(self):
        self.clearOutputs()
        self.ui.resultsWidget.setDisabled(True)
        
        self.current_file = self.ui.input.toPlainText()
        
        self.enable_running()
        
        self.process = QtCore.QProcess(self.parent)
        self.process.readyReadStandardOutput.connect(self.print_text)
        self.process.readyReadStandardError.connect(self.print_error)
        self.process.finished.connect(self.finished)
        self.process.start(self.parent.CMD,[self.current_file])

    def choose_file(self):
        last_file = self.settings.value('lastFile', None)
        if last_file:
            folder = os.path.abspath(os.path.join(last_file, os.pardir))
        else:
            folder = '.'
        filename = QtGui.QFileDialog.getOpenFileName(self.parent,
            "Abrir arquivo config", folder, "Text files (*.config)")
        if filename[0]:
            path = filename[0]
            self.settings.setValue('lastFile',  path)
            self.ui.input.setPlainText(path)


    def finished(self):
        self.disable_running()
        
        s = self.ui.out.toPlainText()
        # getting from output result folder
        results = re.findall(r"\>\'.*?\'\<", s)
        if results:
            self.output_folder = unicode(results[0][2:-2] + os.sep)
            self.ui.resultsWidget.setDisabled(False)