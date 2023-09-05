from sense_hat import SenseHat
import time
import math
sense = SenseHat()
red = [255, 0, 0]  # Red
white = [255, 255, 255]  # White
directions = ["pitch", "roll"]

ball_pos = [3, 3] #init position to center (x,y) 
ball_v = [0, 0] #init velocity to 0 (x,y)


sense.clear()

gravity = 0.5
def normalize_orientation():
	pitch = 0
	roll = 0
	for i in range(100):
		o = sense.get_orientation()
		pitch += o["pitch"]
		roll += o["roll"]
	# collect 100 orientations and get the average pitch and roll
	pitch /= 100
	roll /= 100
	return pitch, roll
avg_pitch, avg_roll = normalize_orientation()

def get_normal_orientation():
	# adjust orientation by average
	o = sense.get_orientation()
	o["pitch"] -= avg_pitch		
	o["pitch"] *= -1
	o["roll"] -= avg_roll
	return o

def render(ball_pos):
	arr = [white] * 64 # make array of 64 zeros
	for i in range(8): # row
		for j in range (8): # column
			if ball_pos[0] == i and ball_pos[1] == j:
				arr[i+ 8*j] = red
	sense.set_pixels(arr)


while True:
	o = get_normal_orientation()
	for i in range(2):
		ball_v[i] += math.sin(math.radians(o[directions[i]]))*gravity
		print(f"{math.sin(math.radians(o[directions[i]]))*gravity}")
		ball_pos[i] += int(ball_v[i])
		if ball_pos[i] > 7 :
			ball_v[i] = 0
			ball_pos[i] = 7
		elif ball_pos[i] < 0:
			ball_v[i] = 0
			ball_pos[i] = 0
	print(f"{ball_v}")
	render(ball_pos)
