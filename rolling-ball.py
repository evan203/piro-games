from sense_hat import SenseHat
import time
import level
import math
sense = SenseHat()
red = [255, 0, 0]  # Red
white = [255, 255, 255]  # White
directions = ["pitch", "roll"]

ball_pos = [3, 3] #init position to center (x,y) 
ball_v = [0, 0] #init velocity to 0 (x,y)


sense.clear()

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
level_obj = level.Level(sense)
def render(ball_pos):
	int_ball_pos = [0] * 2
	for i in range (2): 
		int_ball_pos[i] = int(ball_pos[i])
	arr = level_obj.returnlevelarr()

	for i in range(8): # row
		for j in range (8): # column
			if int_ball_pos[0] == i and int_ball_pos[1] == j:
				arr[i+ 8*j] = red
	sense.set_pixels(arr)

gravity = 0.05
terminal_v = 1

while True:
	o = get_normal_orientation()
	for i in range(2):
		ball_v[i] += math.sin(math.radians(o[directions[i]]))*gravity
		if ball_v[i] > terminal_v:
			ball_v[i] = terminal_v
		elif ball_v[i] < -1 * terminal_v:
			ball_v[i] = -1 * terminal_v
		ball_pos[i] += ball_v[i]
		if ball_pos[i] > 7 :
			ball_v[i] = 0
			ball_pos[i] = 7
		elif ball_pos[i] < 0:
			ball_v[i] = 0
			ball_pos[i] = 0
	#print(f"{ball_v}")
	render(ball_pos)
	time.sleep(0.01)
