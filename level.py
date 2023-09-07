
class Level:
	levelnum = 1
	hole = [255,0,0]
	wall = [0,0,0]
	goal = [255,0,255]
	levelarr = []
	sense = SenseHat()

	def __init__():
		levelarr = loadLevelToArr("/levels/level1.png")
		print(levelarr)

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

	def nextLevel():
		levelnum += 1
		levelarr = loadLevelToArr("/levels/level"+level+".png")
	def restart():
		levelnum = 1
		levelarr = loadLevelToArr("/levels/level1.png")

	def loadLevelToArr(file):
		return sense.load_image(file)
