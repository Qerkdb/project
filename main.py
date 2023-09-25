from PIL import Image, ImageDraw
import re
import subprocess
from subprocess import PIPE, STDOUT, CREATE_NO_WINDOW
import os
import time


def add_zone(image, x1, y1, x2, y2, color, transparency):
	draw = ImageDraw.Draw(image)
	highlight = Image.new('RGBA', image.size, (255, 255, 255, 0))
	draw = ImageDraw.Draw(highlight)
	draw.rectangle([x1, y1, x2, y2], fill=color + (transparency,))
	image = Image.alpha_composite(image.convert('RGBA'), highlight)
	return image


def id_file():
	file_path = 'scripts/file.txt'
	with open(file_path, 'r') as file:
		for line in file:
			matches = re.findall(r'(\w+)=(\d+)', line)
			for match in matches:
				text, number = match
				bands.append((text, int(number)))
	return bands

def coord_file():
	file_path = 'map/bands.txt'
	with open(file_path, 'r') as file:
		for line in file:
			matches = re.findall(r'\((\d+), (\d+), (\d+), (\d+), (\d+)\)', line)
			if matches:
				values = tuple(map(int, matches[0]))
				gangzone.append(values)

	return gangzone

def color_file():
	file_path = 'map/color.txt'
	with open(file_path, 'r') as file:
		for line in file:
			matches = re.findall(r'\((\d+), (\d+), (\d+), (\d+)', line)
			if matches:
				values = tuple(map(int, matches[0]))
				color.append(values)

	return color


def ghetto_card():
	image = Image.open('map/map.png')
	for zone in gangzone:
		for band in bands:
			id, x1, y1, x2, y2 = zone
			name, ids = band
			
			print(x1,y1)

			if name == "nw" and ids == id:
				image = add_zone(image, x1, y1, x2, y2, (144, 93, 93), 120)
			elif name == 'ballas' and ids == id:
				image = add_zone(image, x1, y1, x2, y2, (176,48,157), 170)
			elif name == 'rifa' and ids == id:
				image = add_zone(image, x1, y1, x2, y2, (115,116,200), 170)
			elif name == 'grove' and ids == id:
				image = add_zone(image, x1, y1, x2, y2, (35,122,53), 120)
			elif name == 'aztec' and ids == id:
				image = add_zone(image, x1, y1, x2, y2, (47,200,175), 120)
			elif name == 'vagos' and ids == id:
				image = add_zone(image, x1, y1, x2, y2, (183,187,64), 120)

	image.save('map_server.png')
	image.close()

#==================================================================================================================


server = [
	'0',
	'185.169.134.3', #1
	'185.169.134.4', #2
	'185.169.134.43',#3
	'185.169.134.44',#4
	'185.169.134.45',#5
	'185.169.134.5',#6
	'185.169.134.59',#7
	'185.169.134.61',#8
	'185.169.134.107',#9
	'185.169.134.109',#10
	'185.169.134.166',#11
	'185.169.134.171',#12
	'185.169.134.172',#13
	'185.169.134.173',#14
	'185.169.134.174',#15
	'80.66.82.191',#16
	'80.66.82.190',#17
	'80.66.82.188',#18
	'80.66.82.168',#19
	"80.66.82.159", #20
	'80.66.82.200', #21
	'80.66.82.144', #22
	'80.66.82.132', #23
	'80.66.82.128', #24
	'80.66.82.113', #25
	'80.66.82.82' #26
]

s = int(input('Введите сервер:'))
command = ["RakSAMP Lite.exe", "-n", "Nick", "-h", server[s], "-p", "7777", "-z"]
process = subprocess.run(command, creationflags=subprocess.CREATE_NO_WINDOW)

while True:
    ves = "scripts/file.txt"
    
    if os.path.exists(ves):
        if os.path.getsize(ves) > 100:
            time.sleep(3)
            bands = []
            id_file()
            gangzone = []
            coord_file()
            color = []
            color_file()
            ghetto_card()
            print('Карта готова!')
            break
    else:
        time.sleep(1)


