#!/usr/bin/env python3

import pyglet
from pyglet.window import key
from os import path
from sys import argv
from pyglet.gl import *

keys = []

w = pyglet.window.Window(605, 490, caption = "Steno-Writer 15")

p = path.dirname(path.realpath(__file__))
pyglet.font.add_file(p + "/Resources/UbuntuMono-R.ttf")
uMono = pyglet.font.load("Ubuntu Mono")

on = pyglet.resource.image("keys/1.png")
off = pyglet.resource.image("keys/0.png")

p = ""

if len(argv) > 1:
	try:
		audio = pyglet.media.load(argv[1])
		player = pyglet.media.Player()
		player.queue(audio)
		fob = open(argv[1] + ".txt", "r")
		p = fob.read()
		fob.close()
	except:
		print("NOT A VALID FILE TYPE")

def pl():
	global p
	return p.split("\r\n")[-1][-30:]

def find(num, l):
	count = 0
	for item in l:
		if item == num:
			return count;
		count += 1
	return -1
	
def save(dt):
	global p
	if len(argv) > 1 and len(p) > 0:
		if p[0] == " ":
			p = p[1:]
		fob = open(argv[1] + ".txt", "w")
		fob.write(p.replace("\r\n ", "\r\n").replace("...", ". . . "))
		fob.close()

@w.event
def on_draw():
	global player, audio
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
	#T
	off.blit(85, (w.height / 2) + 24)
	if key.W in keys:
		on.blit(85, (w.height / 2) + 24)
	#K
	off.blit(85, (w.height / 2) - 57)
	if key.S in keys:
		on.blit(85, (w.height / 2) - 57)
	#P
	off.blit(140, (w.height / 2) + 24)
	if key.E in keys:
		on.blit(140, (w.height /2) + 24)
	#W
	off.blit(140, (w.height / 2) - 57)
	if key.D in keys:
		on.blit(140, (w.height / 2) - 57)
	#H
	off.blit(195, (w.height /2) + 24)
	if key.R in keys:
		on.blit(195, (w.height /2) + 24)
	#R
	off.blit(195, (w.height / 2) - 57)
	if key.F in keys:
		on.blit(195, (w.height / 2) - 57)
	#F
	off.blit(355, (w.height / 2) + 24)
	if key.U in keys:
		on.blit(355, (w.height / 2) + 24)
	#R
	off.blit(355, (w.height / 2) - 57)
	if key.J in keys:
		on.blit(355, (w.height / 2) - 57)
	#P
	off.blit(410, (w.height / 2) + 24)
	if key.I in keys:
		on.blit(410, (w.height / 2) + 24)
	#B
	off.blit(410, (w.height / 2) - 57)
	if key.K in keys:
		on.blit(410, (w.height / 2) - 57)
	#L
	off.blit(465, (w.height / 2) + 24)
	if key.O in keys:
		on.blit(465, (w.height / 2) + 24)
	#G
	off.blit(465, (w.height / 2) - 57)
	if key.L in keys:
		on.blit(465, (w.height / 2) - 57)
	#T
	off.blit(520, (w.height / 2) + 24)
	if key.P in keys:
		on.blit(520, (w.height / 2) + 24)
	#S
	off.blit(520, (w.height / 2) - 57)
	if key.SEMICOLON in keys:
		on.blit(520, (w.height / 2) - 57)
	#D
	off.blit(575, (w.height / 2) + 24)
	if key.BRACKETLEFT in keys:
		on.blit(575, (w.height / 2) + 24)
	#Z
	off.blit(575, (w.height / 2) - 57)
	if key.APOSTROPHE in keys:
		on.blit(575, (w.height / 2) - 57)
	#A
	off.blit(165, (w.height / 2) - 138)
	if key.C in keys:
		on.blit(165, (w.height / 2) - 138)
	#O
	off.blit(220, (w.height / 2) - 138)
	if key.V in keys:
		on.blit(220, (w.height / 2) - 138)
	#E
	off.blit(330, (w.height / 2) - 138)
	if key.N in keys:
		on.blit(330, (w.height / 2) - 138)
	#U
	off.blit(385, (w.height / 2) - 138)
	if key.M in keys:
		on.blit(385, (w.height / 2) - 138)
	#S
	off.height = 156
	on.height = 156
	on.anchor_y = on.height / 2
	off.anchor_y = off.height / 2
	off.blit(30, (w.height / 2) - 15)
	if key.Q in keys or key.A in keys:
		on.blit(30, (w.height / 2) - 15)
	#*
	off.height = 156
	off.width = 100
	on.height = 156
	on.width = 100
	on.anchor_x = on.width / 2
	on.anchor_y = on.height / 2
	off.anchor_x = off.width / 2
	off.anchor_y = off.height / 2
	off.blit(275, (w.height / 2) - 15)
	if key.T in keys or key.Y in keys or key.G in keys or key.H in keys:
		on.blit(275, (w.height / 2) - 15)
	pyglet.text.Label(pl(), font_name='Ubuntu Mono', font_size = 28, x = w.width / 2, y = w.height - 100, anchor_x = 'center', anchor_y = 'center').draw()
	if len(argv) > 1:
		glColor3f(1.0, 1.0, 1.0)
		glLineWidth(7.0)
		glBegin(GL_LINES)
		glVertex2f(5, 13)
		glVertex2f(492, 13)
		glEnd()
		glColor3f(0.5, 0.5, 0.5)
		glLineWidth(5.0)
		glBegin(GL_LINES)
		glVertex2f(6, 13)
		glVertex2f(491, 13)
		glEnd()
		glColor3f(0.5, 0.0, 0.0)
		glLineWidth(5.0)
		glBegin(GL_LINES)
		glVertex2f(6, 13)
		glVertex2f(int((((player.time / audio.duration) * 100) * 491) / 100), 13)
		glEnd()
		pyglet.text.Label(str(int(player.time / 60)).zfill(2) + ":" + str(int(player.time % 60)).zfill(2) + "/" + str(int(audio.duration / 60)).zfill(2) + ":" + str(int(audio.duration % 60)).zfill(2), font_name='Ubuntu Mono', font_size = 12, x = w.width - 5, y = 15, anchor_x = 'right', anchor_y = 'center').draw()
		
@w.event
def on_key_press(sym, mods):
	global keys
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
		if len(argv) > 1:
			save(1)
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

def update(dt):
	pass

pyglet.clock.schedule_interval(update, 1 / 3)
pyglet.clock.schedule_interval(save, 30)

pyglet.app.run()
