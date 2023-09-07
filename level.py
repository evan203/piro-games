
class Level:

	def __init__(self, sense):
		self.sense = sense
		self.levelarr = sense.load_image("levels/level1.png")
		self.levelnum = 1
		self.hole = [255,0,0]
		self.wall = [0,0,0]
		self.goal = [255,0,255]

	def returnlevelarr(self):
		return self.levelarr
	def isHole(self, x, y):
		return self.levelarr[y*8+x] == self.hole
	def isWall(self, x, y):
		return self.levelarr[y*8+x] == self.wall
	def isGoal(self, x, y):
		return self.levelarr[y*8+x] == self.goal
	def spawnCoords(self):
		for i, color in enumerate(self.levelarr):
			if color == [0,0,255]:
				return [i%8, int(i/8)]

	def nextLevel(self):
		self.levelnum += 1
		self.levelarr = self.sense.load_image("levels/level{}.png".format(self.levelnum))
	def restart(self):
		self.levelnum = 1
		self.levelarr = self.sense.load_image("levels/level1.png")
