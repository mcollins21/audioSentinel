##################################################################
# AudioSentinel
#
# AudioSentinel is a python program that detects audio input/output
# drivers on devices.
#
# © Michael Collins 2024
##################################################################

import sys
from pyo import *
from src import midiUtils
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5.QtCore import QObject, pyqtSignal

class OutputRedirector(QObject):
    # Custom class to redirect output to a QTextEdit
    outputWritten = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

    def write(self, text):
        self.outputWritten.emit(str(text))

app = QApplication(sys.argv)

# Redirect stdout to the OutputRedirector
sys.stdout = OutputRedirector(app)

def driverInputSearch():
    server = Server().boot()
    midiUtils.deviceInput()

def driverOutputSearch():
    server = Server().boot()
    midiUtils.deviceOutputs()

window = QWidget()
window.setWindowTitle("Audio Device Scanner")

# input scanner button
scan_button = QPushButton("Scan Input Devices", window)
scan_button.clicked.connect(driverInputSearch)
scan_button.move(100, 50)

# output scanner button
scan_button = QPushButton("Scan Output Devices", window)
scan_button.clicked.connect(driverOutputSearch)
scan_button.move(100, 0)

# output window
output_text = QTextEdit(window)
output_text.move(50, 100)  # Adjust position as needed
output_text.setReadOnly(True)  # Make it read-only

# Connect the OutputRedirector signal to update the QTextEdit
sys.stdout.outputWritten.connect(output_text.append)

window.show()
sys.exit(app.exec_())
