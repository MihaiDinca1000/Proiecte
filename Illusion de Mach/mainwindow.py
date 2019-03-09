#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import uic
from PyQt4 import QtCore, QtGui
import sys

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow1.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
    
        #Color slider
        self.ui.slider_2.setValue(0)
        self.ui.slider_2.valueChanged.connect(self.getSquareColor)
        
        #Menu button
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionHelp.triggered.connect(self.howToUse)
        
        #Display Color change
    def getSquareColor(self):
        value = self.ui.slider_2.value()
        self.ui.label_4.setText(str(value))
        
        if value == 0:
            self.ui.square_2.setStyleSheet("background-color: #FFFFFF")  
        else:
            if value == 10:
                self.ui.square_2.setStyleSheet("background-color: #E0E0E0") 
            else:
                if value == 20:
                    self.ui.square_2.setStyleSheet("background-color: #C0C0C0")
                else:
                    if value == 30:
                        self.ui.square_2.setStyleSheet("background-color: #808080")
                    else:
                        if value == 40:
                            self.ui.square_2.setStyleSheet("background-color: #404040")
                        else:
                            if value == 50:
                                self.ui.square_2.setStyleSheet("background-color: #000000") 
                                
        #Help button
    def howToUse(self):
        appName = "Interface - Illusion de Mach"

        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle(self.tr("Help"))
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setText("<br><br>" +
                       appName + ":" +
                       "<br>" +
                       "<u>Utilisez le curseur pour ajuste <font color=red>l'intensite </font>du couleur du carre noir.</u><br>" + 
                       "Il alternera entre differentes <u>nuances de gris</u>." + "<br>" +
                       "A la fin il va affiche un <b>carre noir</b>." + "<br>" + 
                       "Voir la difference entre le deux carres.")

        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
        
        #About button
    def about(self):
        appName = "Interface - Illusion de Mach"
        version = "1.0"
        website = "http://illusion-mach/"
        email = "illusion.mach@imach.com"
        tyMsg = "Merci pour utiliser cette application!"

        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle(self.tr("About"))
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setTextFormat(QtCore.Qt.RichText)
        msgBox.setText("<br><br>" +
                       appName +
                       " v" +
                       version +
                       "<br>" + 
                       "&copy;2017 Tudor Mihai U.<br><br>" +
                       "<a href='{0}'>{0}</a><br><br>".format(website) +
                       "<a href='mailto:{0}'>{0}</a><br><br>".format(email) + tyMsg)

        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
        
        #Exit button
    def exit(self):
        choice = QtGui.QMessageBox.question(self, 'Quitter', "Vous etes sur le point de quitter le programme, etes-vous sur?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def __del__ ( self ):
        self.ui = None

