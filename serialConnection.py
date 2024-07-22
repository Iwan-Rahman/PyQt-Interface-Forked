import serial
import serial.tools.list_ports

class SerialConnection:
    def __init__(self):
        self.connectedPorts = {0: None, 1: None, 2: None}

    def get_ports(self):
        ports = serial.tools.list_ports.comports()
        ports = [com[0] for com in ports]
        return ports

    def connectCOM(self, portNo, com, baud, data, parity, stop, timeout):
        serialByteSize = self.getSerialByteSize(data)
        serialParity = self.getSerialParity(parity)
        serialStopBits = self.getSerialStopBit(stop)
        print(str(serialByteSize))
        print(str(serialParity))
        print(str(serialStopBits))
        print(portNo)
        print(self.connectedPorts[portNo])
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

# Create a singleton instance
serial_connection = SerialConnection()
