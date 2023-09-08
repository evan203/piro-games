from sense_hat import SenseHat
import time
import copy
import level
import math
sense = SenseHat()
red = [255, 0, 0]  # Red
white = [255, 255, 255]  # White
directions = ["pitch", "roll"]

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
ball_pos = level_obj.spawnCoords() #init position to center (x,y) 
ball_v = [0, 0] #init velocity to 0 (x,y)
def render(ball_pos):
	int_ball_pos = [0] * 2
	for i in range (2): 
		int_ball_pos[i] = int(ball_pos[i])
	arr = copy.deepcopy(level_obj.returnlevelarr())

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
		
		#ball_pos[i] += ball_v[i]
		if ball_pos[i] > 7 :
			ball_v[i] = 0
			ball_pos[i] = 7
		elif ball_pos[i] < 0:
			ball_v[i] = 0
			ball_pos[i] = 0
	#print(f"{ball_v}")
	future_coords = [ball_pos[0]+ball_v[0], ball_pos[1]+ball_v[1]]
	for i in range (2):
		future_coords[i] = int(future_coords[i])
	if level_obj.isWall(future_coords[0], future_coords[1]):
		for i in range(2):
			ball_v[i] = 0
	else:
		for i in range(2):
			ball_pos[i] += ball_v[i]
	# if future_coords goes diag
	j = 0
	for i in range (2):
		if future_coords[i] - int(ball_pos[i]) > 1:
			j += 1
	if j > 1:# if it's diagonal
		wall_x_coord= [future_coord[0], int(ball_pos[1])]
		wall_y_coord= [int(ball_pos[0]), future_coord[1]]
		x_is_wall = level_obj.isWall(wall_x_coord)
		y_is_wall = level_obj.isWall(wall_y_code)
		# if both are walls
		if x_is_wall and y_is_wall:
			ball_v[0] = 0
			ball_v[1] = 0
		# if x is a wall
		elif x_is_wall:
			# go in y
			ball_pos_y += ball_v[1]
		# if y is a wall
		elif y_is_wall:
			# go in x
			ball_pos_x += ball_v[0]
	render(ball_pos)
	if level_obj.isGoal(future_coords[0], future_coords[1]):
		level_obj.nextLevel()
		for i in range (2):
			ball_v[i] = 0
			ball_pos = level_obj.spawnCoords() 
	time.sleep(0.01)
