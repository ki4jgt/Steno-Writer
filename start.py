#!/usr/bin/env python3

import pyglet
pyglet.options["debug_gl"] = False
pyglet.options["shadow_window"] = False
from pyglet.window import key
from os import path, listdir
from sys import argv
from pyglet.gl import *
from json import loads, dumps

title = "Steno-Writer 16.02"

keys = []

sav = False
m = "Save"
index = 0

w = pyglet.window.Window(640, 490, resizable = True, caption = title, vsync = False)

#w.push_handlers(pyglet.window.event.WindowEventLogger())
# ^ For testing ONLY

path = path.dirname(path.realpath(__file__))
pyglet.font.add_file(path + "/Resources/UbuntuMono-R.ttf")
uMono = pyglet.font.load("Ubuntu Mono")
icon = pyglet.image.load(path + "/Resources/icon.png")
w.set_icon(icon)

on = pyglet.resource.image("keys/1.png")
off = pyglet.resource.image("keys/0.png")

p = ""

class settings():
	
	global w, path
	
	def __call__(self):
		pass
		
	def __init__(self):
		try:
			fob = open(path + "/conf", "r")
			self.settings = loads(fob.read())
			fob.close()
		except:
			fob = open(path + "/conf", "w")
			fob.write("""{"show_keys":1, "fullscreen":0}""")
			fob.close()
			self.settings = {"show_keys":True, "fullscreen":False}
	
	def update(self, setting):
		if setting in self.settings:
			if self.settings[setting] == 0:
				self.settings[setting] = 1
			else:
				self.settings[setting] = 0
		else:
			self.settings[setting] = 1
		fob = open(path + "/conf", "w")
		fob.write(dumps(self.settings))
		fob.close()
		w.set_fullscreen(self.settings["fullscreen"])
			

settings = settings()

w.set_fullscreen(settings.settings["fullscreen"])

if len(argv) > 1:
	try:
		if argv[1][-5:] == ".swrf":
			argv[1] = argv[1][:-5]
		w.set_caption(title + ": " + argv[1])
		audio = pyglet.media.load(argv[1])
		player = pyglet.media.Player()
		player.queue(audio)
		player.seek(0.01)
	except:
		print("NOT A VALID FILE TYPE")
	try:
		fob = open(argv[1] + ".swrf", "rb")
		plist = fob.read().decode().split("\r\n")
		fob.close()
	except:
		print("FILE NOT PROPERLY FORMATTED")
	try:
		player.seek(loads(plist[-1])["stop-time"])
		for line in plist[:-1]:
			p = p + line + "\r\n"
		p = p[:-2]
	except:
		pass

def rectCheck(lista, listb, listc):
	if listc[0] >= lista[0] and listc[0] <= listb[0] and listc[1] >= lista[1] and listc[1] <= listb[1]:
		return True
	else:
		return False

def pl(i):
	global p
	if len(p.split("\r\n")) >= i:
		return p.split("\r\n")[-i][-int(w.width / 20):].replace("\t", "    ")
	else:
		return ""

def find(num, l):
	count = 0
	for item in l:
		if item == num:
			return count;
		count += 1
	return -1
	
def save(dt):
	global p, player, sav, m
	if len(argv) > 1 and len(p) > 0:
		if p[0] == " ":
			p = p[1:]
		fob = open(argv[1] + ".swrf", "wb")
		fob.write((p.replace("\r\n ", "\r\n").replace("...", ". . . ") + "\r\n" + dumps({"stop-time":player.time})).encode())
		fob.close()
	sav = True
	m = "Saved"

@w.event
def on_draw():
	global player, audio, sav, m, index
	glColor3f(1.0, 1.0, 1.0)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glClearColor(0.02, 0.02, 0.02, 1.0)
	off.height = 75
	off.width = 50
	on.height = 75
	on.width = 50
	on.anchor_x = on.width / 2
	on.anchor_y = on.height / 2
	off.anchor_x = off.width / 2
	off.anchor_y = off.height / 2
	w.clear()
	if settings.settings["show_keys"]:
		#T
		off.blit((w.width / 2) - 215, 270)
		if key.W in keys:
			on.blit((w.width / 2) - 215, 270)
		#K
		off.blit((w.width / 2) - 215, 190)
		if key.S in keys:
			on.blit((w.width / 2) - 215, 190)
		#P
		off.blit((w.width / 2) - 160, 270)
		if key.E in keys:
			on.blit((w.width / 2) - 160, 270)
		#W
		off.blit((w.width / 2) - 160, 190)
		if key.D in keys:
			on.blit((w.width / 2) - 160, 190)
		#H
		off.blit((w.width / 2) - 105, 270)
		if key.R in keys:
			on.blit((w.width / 2) - 105, 270)
		#R
		off.blit((w.width / 2) - 105, 190)
		if key.F in keys:
			on.blit((w.width / 2) - 105, 190)
		#F
		off.blit((w.width / 2) + 55, 270)
		if key.U in keys:
			on.blit((w.width / 2) + 55, 270)
		#R
		off.blit((w.width / 2) + 55, 190)
		if key.J in keys:
			on.blit((w.width / 2) + 55, 190)
		#P
		off.blit((w.width / 2) + 110, 270)
		if key.I in keys:
			on.blit((w.width / 2) + 110, 270)
		#B
		off.blit((w.width / 2) + 110, 190)
		if key.K in keys:
			on.blit((w.width / 2) + 110, 190)
		#L
		off.blit((w.width / 2) + 165, 270)
		if key.O in keys:
			on.blit((w.width / 2) + 165, 270)
		#G
		off.blit((w.width / 2) + 165, 190)
		if key.L in keys:
			on.blit((w.width / 2) + 165, 190)
		#T
		off.blit((w.width / 2) + 220, 270)
		if key.P in keys:
			on.blit((w.width / 2) + 220, 270)
		#S
		off.blit((w.width / 2) + 220, 190)
		if key.SEMICOLON in keys:
			on.blit((w.width / 2) + 220, 190)
		#D
		off.blit((w.width / 2) + 275, 270)
		if key.BRACKETLEFT in keys:
			on.blit((w.width / 2) + 275, 270)
		#Z
		off.blit((w.width / 2) + 275, 190)
		if key.APOSTROPHE in keys:
			on.blit((w.width / 2) + 275, 190)
		#A
		off.blit((w.width / 2) - 135, 105)
		if key.C in keys:
			on.blit((w.width / 2) - 135, 105)
		#O
		off.blit((w.width / 2) - 80, 105)
		if key.V in keys:
			on.blit((w.width / 2) - 80, 105)
		#E
		off.blit((w.width / 2) + 30, 105)
		if key.N in keys:
			on.blit((w.width / 2) + 30, 105)
		#U
		off.blit((w.width / 2) + 85, 105)
		if key.M in keys:
			on.blit((w.width / 2) + 85, 105)
		#S
		off.height = 156
		on.height = 156
		on.anchor_y = on.height / 2
		off.anchor_y = off.height / 2
		off.blit((w.width / 2) - 270, 230)
		if key.Q in keys or key.A in keys:
			on.blit((w.width / 2) - 270, 230)
		#*
		off.height = 156
		off.width = 100
		on.height = 156
		on.width = 100
		on.anchor_x = on.width / 2
		on.anchor_y = on.height / 2
		off.anchor_x = off.width / 2
		off.anchor_y = off.height / 2
		off.blit((w.width / 2) - 25, 230)
		if key.T in keys or key.Y in keys or key.G in keys or key.H in keys:
			on.blit((w.width / 2) - 25, 230)
		cindex = 0
		while cindex < index:
			pyglet.text.Label(pl(cindex + 1), font_name='Ubuntu Mono', font_size = 28, x = w.width / 2, y = ((w.height + 310) / 2) + (50 * cindex), anchor_x = 'center', anchor_y = 'center').draw()
			cindex += 1
	else:
		cindex = 0
		while cindex < index:
			pyglet.text.Label(pl(cindex + 1), font_name='Ubuntu Mono', font_size = 28, x = w.width / 2, y = (w.height / 2) + (50 * cindex), anchor_x = 'center', anchor_y = 'center').draw()
			cindex += 1
	if len(argv) > 1:
		glColor3f(1.0, 1.0, 1.0)
		glLineWidth(7.0)
		glBegin(GL_LINES)
		glVertex2f(5, 13)
		glVertex2f(w.width - 110, 13)
		glEnd()
		glColor3f(0.5, 0.5, 0.5)
		glLineWidth(5.0)
		glBegin(GL_LINES)
		glVertex2f(6, 13)
		glVertex2f(w.width - 111, 13)
		glEnd()
		glColor3f(0.5, 0.0, 0.0)
		glLineWidth(5.0)
		glBegin(GL_LINES)
		glVertex2f(6, 13)
		glVertex2f(int((((player.time / audio.duration) * 100) * (w.width - 111)) / 100), 13)
		glEnd()
		pyglet.text.Label(str(int(player.time / 60)).zfill(2) + ":" + str(int(player.time % 60)).zfill(2) + "/" + str(int(audio.duration / 60)).zfill(2) + ":" + str(int(audio.duration % 60)).zfill(2), font_name='Ubuntu Mono', font_size = 12, x = w.width - 5, y = 15, anchor_x = 'right', anchor_y = 'center').draw()
		if sav:
			glColor3f(0.0, 1.0, 0.0)
		else:
			glColor3f(1.0, 0.0, 0.0)
		glBegin(GL_POLYGON)
		glVertex2f(w.width - 100, 25)
		glVertex2f(w.width - 100, 50)
		glVertex2f(w.width - 5, 50)
		glVertex2f(w.width - 5, 25)
		glEnd()
		pyglet.text.Label(m, font_name='Ubuntu Mono', font_size = 15, x = w.width - (95 / 2), y = 40, anchor_x = 'center', anchor_y = 'center').draw()

@w.event
def on_mouse_press(x, y, button, mods):
	if rectCheck([w.width - 100, 25], [w.width - 5, 50], [x, y]):
		save(1)
		
@w.event
def on_key_press(sym, mods):
	global keys, p, sav, m
	sav = False
	m = "Save"
	if sym == key.F11:
		settings.update("fullscreen")
	if sym == key.F2:
		settings.update("show_keys")
	if sym == key.TAB:
		p = p + "\t"
	if sym not in keys:
		keys.append(sym)

@w.event
def on_key_release(sym, mods):
	global keys
	if sym in keys:
		del keys[find(sym, keys)]
		
@w.event
def on_text(t):
	global p
	if t == "\r":
		t = "\r\n"
	p = p + t

@w.event
def on_text_motion(m):
	global p
	if m == key.BACKSPACE:
		p = p[:len(p) - 1]
	if len(argv) > 1:
		if m == key.UP:
			if player.playing:
				player.pause()
			else:
				player.play()
		if m == key.DOWN:
			p = p + " [" + str(int(player.time / 3600)).zfill(2) + ":" +  str(int((player.time % 3600) / 60)).zfill(2) + ":" + str(int((player.time % 3600) % 60)).zfill(2) + "] "
		if m == key.LEFT:
			player.seek(player.time - 3)
		if m == key.RIGHT:
			player.seek(player.time + 3)

@w.event
def on_resize(w, h):
	global index
	if settings.settings["show_keys"]:
		index = int((h - ((h + 310) / 2)) / 50)
	else:
		index = int(h - (h / 2) / 50)

@w.event
def on_close():
	save(1)

def update(dt):
	pass

pyglet.clock.schedule_interval(update, 1 / 2)
pyglet.clock.schedule_interval(save, 30)

pyglet.app.run()
