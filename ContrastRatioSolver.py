import math

def calcComponent(rsrgb):
	color = rsrgb / 255
    if color <= 0.03928:
        return color / 12.92
    else:
        return math.pow(color / ((color + 0.055) / 1.055), 2.4)

def calcL(r, g, b):
    return 0.2126 * calcComponent(r) + 0.7152 * calcComponent(g) + 0.0722 * calcComponent(b)

def calcContrastRatio(l1, l2):
    return (l1 + 0.05) / (l2 + 0.05)

def calcL1(r, l2):

    return

def calcL2(r, l1):
    pass

