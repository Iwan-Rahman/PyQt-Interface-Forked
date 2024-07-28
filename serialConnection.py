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

    def reconnect(self):
        try:
            self.ser = serial.Serial(
                self.ser.port,
                self.ser.baudrate,
                self.ser.bytesize,
                self.ser.parity,
                self.ser.stopbits,
                self.ser.timeout,
            )
        except:
            pass

    def stop(self):
        self.ser = None

    def run(self):
        while self.ser != None:
            try:
                arduinoData_string = self.ser.readline().decode("ascii").strip()
                print(arduinoData_string)
                arduinoData_float = float(arduinoData_string)
                self.signals.data.emit(arduinoData_float)
            except ValueError:
                print(f"Invalid data: {arduinoData_string}")
                self.signals.sync.emit()
                time.sleep(1)
                self.reconnect
                continue
            except serial.SerialException:
                print("Port Disconnected")
                self.signals.failed.emit()
                time.sleep(1)
                self.reconnect()
                continue
            except Exception as e:
                print(f"Error: {e}")


class SerialConnection(QObject):
    def __init__(self):
        super().__init__()
        self.connectedPorts = {0: None, 1: None, 2: None}
        self.connectedWorkers = {}
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
            timeout=timeout,
        )
        self.start_reading_thread(portNo)

    def disconnectCOM(self, portNo):
        if self.connectedPorts[portNo] is not None:
            self.connectedPorts[portNo].close()
            self.connectedPorts[portNo] = None
            self.connectedWorkers[portNo].stop()
        else:
            print(f"No connection found on port {portNo}")

    def getSerialByteSize(self, byteSizeInput):
        byteSize = {
            5: serial.FIVEBITS,
            6: serial.SIXBITS,
            7: serial.SEVENBITS,
            8: serial.EIGHTBITS,
        }
        return byteSize.get(byteSizeInput, None)

    def getSerialParity(self, parityInput):
        parity = {
            "None": serial.PARITY_NONE,
            "Even": serial.PARITY_EVEN,
            "Odd": serial.PARITY_ODD,
            "Mark": serial.PARITY_MARK,
            "Space": serial.PARITY_SPACE,
        }
        return parity.get(parityInput, None)

    def getSerialStopBit(self, stopbitInput):
        stopbit = {1: serial.STOPBITS_ONE, 2: serial.STOPBITS_TWO}
        return stopbit.get(stopbitInput, None)

    def start_reading_thread(self, portNo):
        self.connectedWorkers[portNo] = SerialWorker(self.connectedPorts[portNo])
        try:
            self.connectedWorkers[portNo].signals.data.connect(
                self.data_received
            )  # Connect signal to slot
        except Exception as e:
            print(e)
        self.threadpool.start(self.connectedWorkers[portNo])

    @pyqtSlot(float)
    def data_received(self, data):
        print(f"Data received: {data}")


# Create a singleton instance
serial_connection = SerialConnection()
