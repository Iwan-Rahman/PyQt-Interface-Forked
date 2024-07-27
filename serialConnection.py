import serial
import serial.tools.list_ports
import time
from PyQt5.QtCore import *

class SerialSignals(QObject):
    live = pyqtSignal()
    sync = pyqtSignal()
    failed = pyqtSignal()
    data = pyqtSignal(float)

class SerialWorker(QRunnable):
    def __init__(self, serial, *args, **kwargs):
        super(SerialWorker, self).__init__()
        self.ser = serial
        self.signals = SerialSignals()

    def run(self):
        try:
            while True:
                arduinoData_string = self.ser.readline().decode('ascii').strip()
                arduinoData_float = float(arduinoData_string)
                self.signals.data.emit(arduinoData_float)
        except ValueError:
            print(f"Invalid data: {arduinoData_string}")
            self.signals.sync.emit()
        except serial.SerialException:
            print('Port Disconnected')
            self.signals.failed.emit()
        except Exception as e:
            print(f"Error: {e}")

class SerialConnection(QObject):
    def __init__(self):
        super().__init__()
        self.connectedPorts = {0: None, 1: None, 2: None}
        self.threadpool = QThreadPool()
    def get_ports(self):
        ports = serial.tools.list_ports.comports()
        ports = [com[0] for com in ports]
        return ports

    def connectCOM(self, portNo, com, baud, data, parity, stop, timeout):
        serialByteSize = self.getSerialByteSize(data)
        serialParity = self.getSerialParity(parity)
        serialStopBits = self.getSerialStopBit(stop)
        if self.connectedPorts[portNo] is not None:
            print("Port already connected")
            return
        self.connectedPorts[portNo] = serial.Serial(
            com,
            baudrate=baud,
            bytesize=serialByteSize,
            parity=serialParity,
            stopbits=serialStopBits,
            timeout=timeout
        )
        self.start_reading_thread(portNo)

    def disconnectCOM(self, portNo):
        if self.connectedPorts[portNo] is not None:
            self.connectedPorts[portNo].close()
            self.connectedPorts[portNo] = None
        else:
            print(f"No connection found on port {portNo}")

    def getSerialByteSize(self, byteSizeInput):
        byteSize = None
        match byteSizeInput:
            case 5:
                byteSize = serial.FIVEBITS
            case 6:
                byteSize = serial.SIXBITS
            case 7:
                byteSize = serial.SEVENBITS
            case 8:
                byteSize = serial.EIGHTBITS
        return byteSize

    def getSerialParity(self, parityInput):
        parity = None
        match parityInput:
            case 'None':
                parity = serial.PARITY_NONE
            case 'Even':
                parity = serial.PARITY_EVEN
            case 'Odd':
                parity = serial.PARITY_ODD
            case 'Mark':
                parity = serial.PARITY_MARK
            case 'Space':
                parity = serial.PARITY_SPACE
        return parity

    def getSerialStopBit(self, stopbitInput):
        stopbit = None
        match stopbitInput:
            case 1:
                stopbit = serial.STOPBITS_ONE
            case 2:
                stopbit = serial.STOPBITS_TWO
        return stopbit

    def start_reading_thread(self, portNo):
        worker = SerialWorker(self.connectedPorts[portNo])
        try:
            worker.signals.data.connect(self.data_received)  # Connect signal to slot
        except Exception as e:
            print(e)
        self.threadpool.start(worker)

    @pyqtSlot(float)
    def data_received(self, data):
        print(f"Data received: {data}")

# Create a singleton instance
serial_connection = SerialConnection()