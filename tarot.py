#!/usr/bin/env python3
import cairosvg
import glob
import re
import random
import io

def generate(path_to_assets, denom=5):
	with open(path_to_assets+'/cross.svg', 'r') as file:
		svg = file.read()
	tarot = glob.glob(path_to_assets+"/tarot/*")
	others = set(glob.glob(path_to_assets+"/*/*"))
	others = others - set(tarot)
	others = list(others)
	random.shuffle(tarot)
	random.shuffle(others)

	def takecard(m):
		if random.randint(0,denom) == 0:
			card = others.pop()
			print("================================")
			print("Tarot: ")
			print(tarot)
			print("--------------------------------")
			print("Others: ")
			print(others)
			print("--------------------------------")
			print("Non-tarot card: " + card)
			print("================================")
			return card
		card = tarot.pop()
		print("================================")
		print("Tarot: ")
		print(tarot)
		print("--------------------------------")
		print("Others: ")
		print(others)
		print("--------------------------------")
		print("Tarot card: " + card)
		print("================================")
		return card
	def rndsome(m):
		return random.choice(["rotate(0)", "rotate(180)"])
	def rndall(m):
		return random.choice(["rotate(0)", "rotate(0)", "rotate(90)", "rotate(180)", "rotate(180)", "rotate(270)"])

	svg = re.sub("#image#", takecard, svg)
	svg = re.sub("rotate\\(some\\)", rndsome, svg)
	svg = re.sub("rotate\\(all\\)", rndall, svg)
	fileobj = io.BytesIO()
	cairosvg.svg2png(bytestring=str.encode(svg), write_to=fileobj)
	fileobj.seek(0)
	return fileobj

if __name__ == "__main__":
	generated = generate("./imgs")
	with open('./output.png', 'wb') as file:
		file.write(generated.read())

