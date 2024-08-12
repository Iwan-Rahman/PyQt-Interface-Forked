from PyQt5 import QtWidgets as qw, QtCore as qc
from ConnectionManager import Ui_ConnectionManager
from graphics_window import GraphicsWindow

class ConnectionWidget(qw.QWidget, Ui_ConnectionManager):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.graphics_windows = {}
        self.window_counter = 0

    def open_graphics_window(self):
        self.window_counter += 1
        window_id = f'window_{self.window_counter}'
        
        new_window = GraphicsWindow()
        new_window.setWindowTitle(window_id)

        self.graphics_windows[window_id] = new_window
        new_window.show()
