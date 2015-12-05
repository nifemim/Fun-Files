import math

## See http://www.w3.org/TR/WCAG20/#meaning

def convertRGBColorComponentToLSpace(csrgb):
	color = csrgb / 255
	if color <= 0.03928:
		return color / 12.92
	else:
		return math.pow((color + 0.055) / 1.055, 2.4)

def calcL(rsrgb, gsrgb, bsrgb):
	return 0.2126 * convertRGBColorComponentToLSpace(rsrgb) + 0.7152 * convertRGBColorComponentToLSpace(gsrgb) + 0.0722 * convertRGBColorComponentToLSpace(bsrgb)

# Calculates the contrast ratio between the relative luminances l1 and l2 of two colors
def calcContrastRatio(l1, l2):
	return (l1 + 0.05) / (l2 + 0.05)

# Calculates the L value for the lighter of the two colors
def calcL1(r, l2):
	return ((l2 + 0.05) * r) - 0.05

# Calculates the L value for the darker of the two colors
def calcL2(r, l1):
	return ((l1 + 0.05) / r) - 0.05

def convertLColorComponentToRGBSpace(csl):
	test = csl * 12.92
	if test <= 0.03928:
		return test * 255
	else:
		return ((math.pow(csl, 1 / 2.4) * 1.055) - 0.055) * 255

def pickOutGreenRGBSpace(l, rsrgb, bsrgb):
	greenLSpace =  (l - (0.2126 * convertRGBColorComponentToLSpace(rsrgb) + 0.0722 * convertRGBColorComponentToLSpace(bsrgb))) / 0.7152

	return convertLColorComponentToRGBSpace(greenLSpace)

def solveForDarkerGreenComponentRGBSpace(r, l1, fixedDarkerBlueRGB, fixedDarkerRedRGB):
	l2 = calcL2(r, l1)

	return pickOutGreenRGBSpace(l2, fixedDarkerBlueRGB, fixedDarkerRedRGB)
