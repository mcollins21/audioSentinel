# contains code for midi utilities components

from pyo import *

def deviceCount():
    devices = pm_count_devices()
    print(devices)

def deviceInput():
    inputs = pm_get_input_devices()
    print(inputs)

def deviceOutputs():
    outputs = pm_get_output_devices()
    print(outputs)
