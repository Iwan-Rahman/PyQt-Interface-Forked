from PyQt5 import QtWidgets as qw, uic
from MainWindow import Ui_MainWindow
from ComManager import Ui_ComManager
from graph import Ui_Graph

class ComWindow(qw.QDialog,Ui_ComManager):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.ConnectBtnP1.clicked.connect(self.connectPort)
    
  
  def connectPort1(self):
    self.PortInputP1.setEnabled(False)
    self.BaudInputP1.setEnabled(False)
    self.ByteSizeInputP1.setEnabled(False)
    self.ParityInputP1.setEnabled(False)
    self.StopBitInputP1.setEnabled(False)
    self.TimeoutInputP1.setEnabled(False)
  
  def disconnectPort1(self):
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
    self.PortInputP2.setEnabled(True)
    self.BaudInputP2.setEnabled(True)
    self.ByteSizeInputP2.setEnabled(True)
    self.ParityInputP2.setEnabled(True)
    self.StopBitInputP2.setEnabled(True)
    self.TimeoutInputP2.setEnabled(True)  

  def connectPort3(self):
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
    print(self.comWindow)
    if self.comWindow is None:
     self.comWindow = ComWindow()
    self.comWindow.show()

  
app = qw.QApplication([])
window = MainWindow()
window.show()
app.exec()