import serial
from PyQt5 import QtWidgets as qw, uic
from MainWindow import Ui_MainWindow
from ComManager import Ui_ComManager
from graph import Ui_Graph
from serialConnection import serial_connection
from ConnectionManager import Ui_ConnectionManager

class ConnectionWidget(qw.QWidget,Ui_ConnectionManager):
  def __init__(self):
    super().__init__()
    self.setupUi(self)

class ComWindow(qw.QDialog,Ui_ComManager):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
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
    self.initValues()
    self.refresh()

  def refresh(self):
    self.ports = serial_connection.get_ports()
    print(self.ports)

    # Reset Port 1 Input
    if serial_connection.connectedPorts[0] == None:
      self.PortInputP1.clear()
      if(len(self.ports) == 0):
        self.PortInputP1.insertItem(0,'No Ports Found')
        self.PortInputP1.setEnabled(False)
      else:
        self.PortInputP1.setEnabled(True)
        for x in self.ports:
          self.PortInputP1.addItem(x)

    # Reset Port 2 Input  
    if serial_connection.connectedPorts[1] == None:
      self.PortInputP2.clear()
      if(len(self.ports) == 0):
       self.PortInputP2.insertItem(0,'No Ports Found')
       self.PortInputP2.setEnabled(False)
      else:
        self.PortInputP2.setEnabled(True)
        for x in self.ports:
          self.PortInputP2.addItem(x)
    
    # Reset Port 3 Input 
    if serial_connection.connectedPorts[2] == None:
      self.PortInputP3.clear()
      if(len(self.ports) == 0):
        self.PortInputP3.insertItem(0,'No Ports Found')
        self.PortInputP3.setEnabled(False)
      else:
        self.PortInputP3.setEnabled(True)
        for x in self.ports:
          self.PortInputP3.addItem(x)   
  
  def initValues(self):
    self.DisconnectBtnP1.setEnabled(False)
    self.DisconnectBtnP2.setEnabled(False)
    self.DisconnectBtnP3.setEnabled(False)

  def connectPort1(self):
    self.StopBitInput = None
    for radioBtn in self.StopBitInputP1.findChildren(qw.QRadioButton):
      if radioBtn.isChecked():
        self.StopBitInput = radioBtn
        break
    try:
      serial_connection.connectCOM(
        0,
        str(self.PortInputP1.currentText()),
        int(self.BaudInputP1.currentText()),
        int(self.ByteSizeInputP1.value()),
        str(self.ParityInputP1.currentText()),
        int(self.StopBitInput.text()),
        int(self.TimeoutInputP1.value())
        )
      self.PortInputP1.setEnabled(False)
      self.BaudInputP1.setEnabled(False)
      self.ByteSizeInputP1.setEnabled(False)
      self.ParityInputP1.setEnabled(False)
      self.StopBitInputP1.setEnabled(False)
      self.TimeoutInputP1.setEnabled(False)
      self.ConnectBtnP1.setEnabled(False)
      self.DisconnectBtnP1.setEnabled(True)
    except Exception as e:
            reply = qw.QMessageBox.critical(
                self, 
                'Connection Error', 
                f'There was an error connecting to the port: {e}',
                qw.QMessageBox.Ok
            )

  def disconnectPort1(self):
    serial_connection.disconnectCOM(0)
    if(len(self.ports) != 0):
          self.PortInputP1.setEnabled(True)
    self.BaudInputP1.setEnabled(True)
    self.ByteSizeInputP1.setEnabled(True)
    self.ParityInputP1.setEnabled(True)
    self.StopBitInputP1.setEnabled(True)
    self.TimeoutInputP1.setEnabled(True)
    self.ConnectBtnP1.setEnabled(True)
    self.DisconnectBtnP1.setEnabled(False)

  def connectPort2(self):
    self.PortInputP2.setEnabled(False)
    self.BaudInputP2.setEnabled(False)
    self.ByteSizeInputP2.setEnabled(False)
    self.ParityInputP2.setEnabled(False)
    self.StopBitInputP2.setEnabled(False)
    self.TimeoutInputP2.setEnabled(False)
    self.ConnectBtnP2.setEnabled(False)
    self.DisconnectBtnP2.setEnabled(True)
  
  def disconnectPort2(self):
    if(len(self.ports) != 0):
      self.PortInputP2.setEnabled(True)
    self.BaudInputP2.setEnabled(True)
    self.ByteSizeInputP2.setEnabled(True)
    self.ParityInputP2.setEnabled(True)
    self.StopBitInputP2.setEnabled(True)
    self.TimeoutInputP2.setEnabled(True)  
    self.ConnectBtnP2.setEnabled(True)
    self.DisconnectBtnP2.setEnabled(False)

  def connectPort3(self):
    if(len(self.ports) != 0):
      self.PortInputP3.setEnabled(False)
    self.BaudInputP3.setEnabled(False)
    self.ByteSizeInputP3.setEnabled(False)
    self.ParityInputP3.setEnabled(False)
    self.StopBitInputP3.setEnabled(False)
    self.TimeoutInputP3.setEnabled(False)
    self.ConnectBtnP3.setEnabled(False)
    self.DisconnectBtnP3.setEnabled(True)
  
  def disconnectPort3(self):  
    self.PortInputP3.setEnabled(True)
    self.BaudInputP3.setEnabled(True)
    self.ByteSizeInputP3.setEnabled(True)
    self.ParityInputP3.setEnabled(True)
    self.StopBitInputP3.setEnabled(True)
    self.TimeoutInputP3.setEnabled(True)
    self.ConnectBtnP3.setEnabled(True)
    self.DisconnectBtnP3.setEnabled(False)

class MainWindow(qw.QMainWindow, Ui_MainWindow):
  def __init__(self, *args, obj=None, **kwargs):
    super(MainWindow,self).__init__(*args,**kwargs)
    self.setupUi(self)
    self.actionConnect.triggered.connect(self.openCOM)
    self.comWindow = None
    self.connectionManager = ConnectionWidget()
    self.horizontalLayout.replaceWidget(self.connectionWidget, self.connectionManager)
    self.connectionWidget.setParent(None)

  def openCOM(self):
    if self.comWindow is None:
     self.comWindow = ComWindow()
    self.comWindow.show()

  def closeEvent(self,event):
    reply = qw.QMessageBox.question(self, 'Quit', 'Are you sure you want to quit the application?',
        qw.QMessageBox.Yes | qw.QMessageBox.No, qw.QMessageBox.No)
    if reply == qw.QMessageBox.Yes:
      qw.QApplication.quit() # Proceed with the close event
    else:
      event.ignore()  # Ignore the close event, keep the window open

  
app = qw.QApplication([])
window = MainWindow()
window.show()
app.exec()