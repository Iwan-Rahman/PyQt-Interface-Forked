import serial
import serial.tools.list_ports

def get_ports():

    ports = serial.tools.list_ports.comports()
    ports = [com[0] for com in ports]
    return ports


def connectCOM(com, baud, data, parity, stop, timeout):
    serialByteSize = getSerialByteSize(data)
    serialParity = getSerialParity(parity)
    serialStopBits = getSerialStopBit(stop)
    print(str(serialByteSize))
    print(str(serialParity))
    print(str(serialStopBits))
    ser = serial.Serial(com, baudrate = baud,bytesize=serialByteSize,parity=serialParity,stopbits=serialStopBits, timeout=timeout)
    while 1:
        arduinoData = ser.readline().decode('ascii')
        print(arduinoData)


    
def getSerialByteSize(byteSizeInput):
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

def getSerialParity(parityInput):
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

def getSerialStopBit(stopbitInput):
    stopbit = None
    match stopbitInput:
        case 1:
            stopbit = serial.STOPBITS_ONE
        case 2:
            stopbit = serial.STOPBITS_TWO
    return stopbit
