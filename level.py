from sense_hat import SenseHat

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

	def returnlevelarr():
		return levelarr
	def isHole(x, y):
		return levelarr[y*8+x] == hole
	def isWall(x, y):
		return levelarr[y*8+x] == wall
	def isGoal(x, y):
		return levelarr[y*8+x] == goal
	def spawnCoords():
		for i in range(64):
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
