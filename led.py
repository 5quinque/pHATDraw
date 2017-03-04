#!/usr/bin/env python

import sys
import json
import time

import scrollphat

if len(sys.argv) != 3:
	print("\nProblem")
	sys.exit(0)

data = json.loads(sys.argv[1])
brightness = int(sys.argv[2])

scrollphat.set_brightness(brightness)
for d in data:
	print data[d]
	scrollphat.set_pixel(data[d][0], data[d][1], True)

#for d in data:
#	scrollphat.set_pixel(d[0], d[1], True)

scrollphat.update()

sys.exit(0)

#x = int(sys.argv[1])
#y = int(sys.argv[2])

#print x, y

if y <= 4 and x <= 10:
	print("\nWe good");

scrollphat.set_brightness(2)

print scrollphat.buffer_len()

#scrollphat.set_pixel(0,0, True)
scrollphat.set_pixel(x,y, True)
scrollphat.update()

#for y in range(5):
#	for x in range(11):
#		scrollphat.set_pixel(x,y, True)
#		scrollphat.update()
#		time.sleep(0)

