﻿# -*- coding: utf-8 -*-
import sys
from tcaxPy import *

try:
	input = sys.argv[1]
except:
	print('Error: none input image file!')
	sys.exit()
output = input
width = 1280
height = 720
ass_header = """[Script Info]\r
; This script is generated by png2ass powered by TCAX 1.2.0\r
; Welcome to TCAX forum http://tcax.org\r
ScriptType: v4.00+\r
Collisions:Normal\r
PlayResX:{width}\r
PlayResY:{height}\r
Timer:100.0000\r
\r
[V4+ Styles]\r
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\r
Style: TCMS,Arial,30,&H00FF0000,&HFFFF0000,&H000000FF,&HFF000000,0,0,0,0,100,100,0,0,0,1,0,5,15,15,10,1\r
Style: TCPS,Arial,1,&HFFFFFFFF,&HFFFFFFFF,&HFFFFFFFF,&HFFFFFFFF,0,0,0,0,100,100,0,0,0,0,0,7,0,0,0,1\r
\r
[Events]\r
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\r
\r""".format(width=width, height=height)

data = {
	val_OutFile : output,
	val_AssHeader : ass_header,
	val_ResolutionX : width,
	val_ResolutionY : height,
}

def png2ass():
	file_name = GetVal(val_OutFile) + '.ass'
	ass_header = GetVal(val_AssHeader)
	ASS_FILE = CreateAssFile(file_name, ass_header)
	ASS_BUF = []
	PIX = ImagePix((input))
	dx = (GetVal(val_ResolutionX) - PIX[1][0]) / 2 - PIX[0][0]	# x middle of the screen
	dy = (GetVal(val_ResolutionY) - PIX[1][1]) / 2 - PIX[0][1]   # y middle of the screen

	## -- pix convert start
	initPosX = dx + PIX[0][0]
	initPosY = dy + PIX[0][1]
	for h in range(PIX[1][1]):
		posY = initPosY + h
		for w in range(PIX[1][0]):
			posX = initPosX + w
			idx  = 4 * (h * PIX[1][0] + w)
			pixR = PIX[2][idx + 0]
			pixG = PIX[2][idx + 1]
			pixB = PIX[2][idx + 2]
			pixA = PIX[2][idx + 3]
			if pixA != 0:
				ass_main(ASS_BUF, SubL(0, 1000, 0, Pix_Style), pos(posX, posY) + color1(FmtRGB(pixR, pixG, pixB)) + alpha1(255 - pixA), PixPt())
	## -- pix convert end
	
	WriteAssFile(ASS_FILE, ASS_BUF)	 # write the buffer in memory to the file
	FinAssFile(ASS_FILE)

if __name__ == "__main__":
	tcaxPy_InitData(data)
	png2ass()