import serial
from PyQt5 import QtWidgets as qw, QtCore as qc
from MainWindow import Ui_MainWindow
from ComManager import Ui_ComManager
from graph import Ui_Graph
from serialConnection import serial_connection
from ConnectionManager import Ui_ConnectionManager


class ConnectionWidget(qw.QWidget, Ui_ConnectionManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ComWindow(qw.QDialog, Ui_ComManager):
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

    def refreshPort(self, portNo, port):
        if serial_connection.connectedPorts[portNo] is None:
            port.clear()
            if len(self.ports) == 0:
                port.insertItem(0, "No Ports Found")
                port.setEnabled(False)
            else:
                port.setEnabled(True)
                for x in self.ports:
                    port.addItem(x)

    def refresh(self):
        self.ports = serial_connection.get_ports()
        print(self.ports)
        self.refreshPort(0, self.PortInputP1)  # Refresh Port 1 Input
        self.refreshPort(1, self.PortInputP2)  # Refrest Port 2 Input
        self.refreshPort(2, self.PortInputP3)  # Refresh Port 3 Input

    def initValues(self):
        self.DisconnectBtnP1.setEnabled(False)
        self.DisconnectBtnP2.setEnabled(False)
        self.DisconnectBtnP3.setEnabled(False)

    def connectPort(
        self,
        portNo,
        portInput,
        baudInput,
        byteSizeInput,
        parityInput,
        stopBitInput,
        timeoutInput,
        connectBtn,
        disconnectBtn,
    ):
        stopBit = None
        for radioBtn in stopBitInput.findChildren(qw.QRadioButton):
            if radioBtn.isChecked():
                stopBit = radioBtn
                break
        try:
            serial_connection.connectCOM(
                portNo,
                str(portInput.currentText()),
                int(baudInput.currentText()),
                int(byteSizeInput.value()),
                str(parityInput.currentText()),
                int(stopBit.text()),
                int(timeoutInput.value()),
            )
            portInput.setEnabled(False)
            baudInput.setEnabled(False)
            byteSizeInput.setEnabled(False)
            parityInput.setEnabled(False)
            stopBitInput.setEnabled(False)
            timeoutInput.setEnabled(False)
            connectBtn.setEnabled(False)
            disconnectBtn.setEnabled(True)
            self.updateConnectionDisplay(portNo)
        except Exception as e:
            reply = qw.QMessageBox.critical(
                self,
                "Connection Error",
                "There was an error connecting to the port",
                qw.QMessageBox.Ok,
            )

    def disconnectPort(
        self,
        portNo,
        PortInput,
        BaudInput,
        ByteSizeInput,
        ParityInput,
        StopBitInput,
        TimeoutInput,
        ConnectBtn,
        DisconnectBtn,
    ):
        serial_connection.disconnectCOM(portNo)
        if len(self.ports) != 0:
            PortInput.setEnabled(True)
        BaudInput.setEnabled(True)
        ByteSizeInput.setEnabled(True)
        ParityInput.setEnabled(True)
        StopBitInput.setEnabled(True)
        TimeoutInput.setEnabled(True)
        ConnectBtn.setEnabled(True)
        DisconnectBtn.setEnabled(False)
        
        # Start a timer to call removeConnectionDisplay after a short delay
        qc.QTimer.singleShot(50, lambda: self.removeConnectionDisplay(portNo))

   
    def connectPort1(self):
        self.connectPort(
            0,
            self.PortInputP1,
            self.BaudInputP1,
            self.ByteSizeInputP1,
            self.ParityInputP1,
            self.StopBitInputP1,
            self.TimeoutInputP1,
            self.ConnectBtnP1,
            self.DisconnectBtnP1,
        )

    def connectPort2(self):
        self.connectPort(
            1,
            self.PortInputP2,
            self.BaudInputP2,
            self.ByteSizeInputP2,
            self.ParityInputP2,
            self.StopBitInputP2,
            self.TimeoutInputP2,
            self.ConnectBtnP2,
            self.DisconnectBtnP2,
        )

    def connectPort3(self):
        self.connectPort(
            2,
            self.PortInputP3,
            self.BaudInputP3,
            self.ByteSizeInputP3,
            self.ParityInputP3,
            self.StopBitInputP3,
            self.TimeoutInputP3,
            self.ConnectBtnP3,
            self.DisconnectBtnP3,
        )

    def disconnectPort1(self):
        self.disconnectPort(
            0,
            self.PortInputP1,
            self.BaudInputP1,
            self.ByteSizeInputP1,
            self.ParityInputP1,
            self.StopBitInputP1,
            self.TimeoutInputP1,
            self.ConnectBtnP1,
            self.DisconnectBtnP1,
        )

    def disconnectPort2(self):
        self.disconnectPort(
            1,
            self.PortInputP2,
            self.BaudInputP2,
            self.ByteSizeInputP2,
            self.ParityInputP2,
            self.StopBitInputP2,
            self.TimeoutInputP2,
            self.ConnectBtnP2,
            self.DisconnectBtnP2,
        )

    def disconnectPort3(self):
        self.disconnectPort(
            2,
            self.PortInputP3,
            self.BaudInputP3,
            self.ByteSizeInputP3,
            self.ParityInputP3,
            self.StopBitInputP3,
            self.TimeoutInputP3,
            self.ConnectBtnP3,
            self.DisconnectBtnP3,
        )

    def updateConnectionDisplay(self, portNo):
        if portNo == 0:
            syncLbl = connection_manager.syncP1lbl
        elif portNo == 1:
            syncLbl = connection_manager.syncP2lbl
        elif portNo == 2:
            syncLbl = connection_manager.syncP3lbl

        worker = serial_connection.connectedWorkers.get(portNo)
        if worker:
            worker.signals.data.connect(lambda data: self.updateConnection(syncLbl, 'Live'))
            worker.signals.sync.connect(lambda: self.updateConnection(syncLbl, 'Unsynced'))
            worker.signals.failed.connect(lambda: self.updateConnection(syncLbl, 'Failed'))

    def removeConnectionDisplay(self, portNo):
        if portNo == 0:
            syncLbl = connection_manager.syncP1lbl
        elif portNo == 1:
            syncLbl = connection_manager.syncP2lbl
        elif portNo == 2:
            syncLbl = connection_manager.syncP3lbl
        syncLbl.clear()

    def updateConnection(self, syncLbl, status):
        syncLbl.setText(status)

class MainWindow(qw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionConnect.triggered.connect(self.openCOM)
        self.comWindow = None
        self.connectionManager = connection_manager
        self.horizontalLayout.replaceWidget(
            self.connectionWidget, self.connectionManager
        )
        self.connectionWidget.setParent(None)

    def openCOM(self):
        if self.comWindow is None:
            self.comWindow = ComWindow()
        self.comWindow.show()

    def closeEvent(self, event):
        reply = qw.QMessageBox.question(
            self,
            "Quit",
            "Are you sure you want to quit the application?",
            qw.QMessageBox.Yes | qw.QMessageBox.No,
            qw.QMessageBox.No,
        )
        if reply == qw.QMessageBox.Yes:
            qw.QApplication.quit()  # Proceed with the close event
        else:
            event.ignore()  # Ignore the close event, keep the window open

if __name__ == "__main__":
    app = qw.QApplication([])
    connection_manager = ConnectionWidget()  # Move this here
    window = MainWindow()
    window.show()
    app.exec()
