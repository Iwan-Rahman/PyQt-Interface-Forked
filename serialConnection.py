import serial
import serial.tools.list_ports

def get_ports():

    ports = serial.tools.list_ports.comports()
    ports = [com[0] for com in ports]
    return ports