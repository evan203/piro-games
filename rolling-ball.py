from sense_hat import SenseHat
import time
import math
sense = SenseHat()
red = [255, 0, 0]  # Red
white = [255, 255, 255]  # White

ball_pos = [3, 3] #init position to center (x,y) 
ball_v = [0, 0] #init velocity to 0 (x,y)


sense.clear()

gravity = 4

def render(ball_pos):
	arr = [white] * 64 # make array of 64 zeros
	for i in range(8): # row
		for j in range (8): # column
			if ball_pos[0] == i and ball_pos[1] == j:
				arr[i+ 8*j] = red
	sense.set_pixels(arr)


O = [0 , 0]
while True:
	o = sense.get_orientation()
	O[0] = math.radians(o["pitch"]) # float in degrees converted to radians
	O[1] = math.radians(o["roll"]) # float in degrees converted to radians
	for i in range(2):
		ball_v[i] += int(math.sin(O[i])*gravity)
		ball_pos[i] += ball_v[i]
		if ball_pos[i] > 7 :
			ball_v[i] = 0
			ball_pos[i] = 7
		elif ball_pos[i] < 0:
			ball_v[i] = 0
			ball_pos[i] = 0
	render(ball_pos)
	
	time.sleep(0.2)


