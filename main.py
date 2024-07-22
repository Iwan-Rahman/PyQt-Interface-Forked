import serial
from PyQt5 import QtWidgets as qw, uic
from MainWindow import Ui_MainWindow
from ComManager import Ui_ComManager
from graph import Ui_Graph
from serialConnection import *

class ComWindow(qw.QDialog,Ui_ComManager):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.refresh()
    self.refreshBtn = qw.QPushButton("Refresh")
    self.refreshBtn.setObjectName("Refresh")
    self.refreshBtn.clicked.connect(self.refresh)
    self.buttonBox.addButton(self.refreshBtn, qw.QDialogButtonBox.ActionRole)
    self.ConnectBtnP1.clicked.connect(self.connectPort1)
    self.DisconnectBtnP1.clicked.connect(self.disconnectPort1)
    self.ConnectBtnP2.clicked.connect(self.connectPort2)
    self.DisconnectBtnP2.clicked.connect(self.disconnectPort2)
    self.ConnectBtnP3.clicked.connect(self.connectPort3)
    self.DisconnectBtnP3.clicked.connect(self.disconnectPort3)

  def refresh(self):
    self.ports = get_ports()
    print(self.ports)
    self.PortInputP1.clear()
    self.PortInputP2.clear()
    self.PortInputP3.clear()
    if(len(self.ports) == 0):
      self.PortInputP1.insertItem(0,'No Ports Found')
      self.PortInputP2.insertItem(0,'No Ports Found')
      self.PortInputP3.insertItem(0,'No Ports Found')
      self.PortInputP1.setEnabled(False)
      self.PortInputP2.setEnabled(False)
      self.PortInputP3.setEnabled(False)
    else:
      self.PortInputP1.setEnabled(True)
      self.PortInputP2.setEnabled(True)
      self.PortInputP3.setEnabled(True)
      for x in self.ports:
        self.PortInputP1.addItem(x)
        self.PortInputP2.addItem(x)
        self.PortInputP3.addItem(x)   
      
  def connectPort1(self):
    self.PortInputP1.setEnabled(False)
    self.BaudInputP1.setEnabled(False)
    self.ByteSizeInputP1.setEnabled(False)
    self.ParityInputP1.setEnabled(False)
    self.StopBitInputP1.setEnabled(False)
    self.TimeoutInputP1.setEnabled(False)
  
  def disconnectPort1(self):
    if(len(self.ports) != 0):
          self.PortInputP1.setEnabled(True)
    self.BaudInputP1.setEnabled(True)
    self.ByteSizeInputP1.setEnabled(True)
    self.ParityInputP1.setEnabled(True)
    self.StopBitInputP1.setEnabled(True)
    self.TimeoutInputP1.setEnabled(True)

  def connectPort2(self):
    self.PortInputP2.setEnabled(False)
    self.BaudInputP2.setEnabled(False)
    self.ByteSizeInputP2.setEnabled(False)
    self.ParityInputP2.setEnabled(False)
    self.StopBitInputP2.setEnabled(False)
    self.TimeoutInputP2.setEnabled(False)
  
  def disconnectPort2(self):
    if(len(self.ports) != 0):
      self.PortInputP2.setEnabled(True)
    self.BaudInputP2.setEnabled(True)
    self.ByteSizeInputP2.setEnabled(True)
    self.ParityInputP2.setEnabled(True)
    self.StopBitInputP2.setEnabled(True)
    self.TimeoutInputP2.setEnabled(True)  

  def connectPort3(self):
    if(len(self.ports) != 0):
      self.PortInputP3.setEnabled(False)
    self.BaudInputP3.setEnabled(False)
    self.ByteSizeInputP3.setEnabled(False)
    self.ParityInputP3.setEnabled(False)
    self.StopBitInputP3.setEnabled(False)
    self.TimeoutInputP3.setEnabled(False)
  
  def disconnectPort3(self):  
    self.PortInputP3.setEnabled(True)
    self.BaudInputP3.setEnabled(True)
    self.ByteSizeInputP3.setEnabled(True)
    self.ParityInputP3.setEnabled(True)
    self.StopBitInputP3.setEnabled(True)
    self.TimeoutInputP3.setEnabled(True)


class MainWindow(qw.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, obj=None, **kwargs):
    super(MainWindow,self).__init__(*args,**kwargs)
    self.setupUi(self)

    self.actionConnect.triggered.connect(self.openCOM)
    self.comWindow = None

  def openCOM(self):
    if self.comWindow is None:
     self.comWindow = ComWindow()
    self.comWindow.show()

  
app = qw.QApplication([])
window = MainWindow()
window.show()
app.exec()