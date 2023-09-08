from sense_hat import SenseHat

class Level:
        sense = SenseHat()
        
        levelnum

        levelarr

        hole = [255,0,0]
	wall = [0,0,0]
	goal = [255,0,255]
	
        
	def __init__():
		levelarr = sense.load_image("levels/level1.png")
		levelnum = 1
		
        def getLevelNum():
            return levelnum
	def getLevelArr():
		return levelarr
	def isHole(x, y):
		return levelarr[y*8+x] == hole
	def isWall(x, y):
		return levelarr[y*8+x] == wall
	def isGoal(x, y):
		return levelarr[y*8+x] == goal
	def spawnCoords():
		for i, color in enumerate(levelarr):
			if color == [0,0,255]:
				return [i%8, int(i/8)]

	def nextLevel():
		levelnum += 1
		levelarr = sense.load_image("levels/level" + levelnum + ".png")
	def restart():
		levelnum = 1
		levelarr = sense.load_image("levels/level1.png")
