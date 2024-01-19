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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QHBoxLayout
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

def driverDeviceCount():
    server = Server().boot()
    midiUtils.deviceCount()

window = QWidget()
window.setWindowTitle("Audio Device Scanner")

window.setFixedSize(300, 300)

layout = QHBoxLayout()
window.setLayout(layout)  # Set the layout for the window
"""
# Add buttons to the layout
layout.addWidget(scan_button)
layout.addWidget(scan_button, stretch=1)  # Add spacing between buttons
layout.addWidget(scan_button)
"""

# device count button
scan_button = QPushButton("Device Count", window)
scan_button.clicked.connect(driverDeviceCount)
scan_button.move(100, 20)

# input scanner button
scan_button = QPushButton("Input", window)
scan_button.clicked.connect(driverInputSearch)
scan_button.move(100, 60)

# output scanner button
scan_button = QPushButton("Output", window)
scan_button.clicked.connect(driverOutputSearch)
scan_button.move(100, 100)

# output window
output_text = QTextEdit(window)
output_text.setGeometry(50, 140, 200, 150)  # Adjusted size and position
output_text.setReadOnly(True)  # Make it read-only

# Connect the OutputRedirector signal to update the QTextEdit
sys.stdout.outputWritten.connect(output_text.append)

window.show()
sys.exit(app.exec_())

