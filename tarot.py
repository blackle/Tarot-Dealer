#!/usr/bin/env python3
import os
import cairosvg
import glob
import re
import random
import io

def generate(path_to_assets, denom=5):
	with open(path_to_assets+'/cross.svg', 'r') as file:
		svg = file.read()
	tarot = [os.path.normpath(i) for i in glob.glob(path_to_assets+"/tarot/*")]
	others = set([os.path.normpath(i) for i in glob.glob(path_to_assets+"/*/*")])
	others = list(others - set(tarot))
	random.shuffle(tarot)
	random.shuffle(others)

	def takecard(m):
		if random.randint(0,denom) == 0:
			return others.pop()
		return tarot.pop()
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

