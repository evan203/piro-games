from sense_hat import SenseHat
import time

import Level
import Ball

class GameManager:
    sense = SenseHat()

    levelManager

    frameRate = 60
    
    
    def __init__():
        levelManager = Level()
        update()


    def playLevel():
        player
        
        transition(levelManager.getLevelNum)
        player = Ball(levelManager.spawnCoords())

        while isAlive(player) and (not beatLevel(player)):
            render(player)
            player.update()

            if hitWallTop(player):
                player.killPosYVel()
            if hitWallBottom(player):
                player.killNegYVel()
            if hitWallRigh(player):
                player.killPosXVel()
            if hitWallLeft(player):
                player.killNegXVel()
            
            time.sleep(1.0 / frameRate)
        render(player)
        
        if (isAlive(player)):
            levelManager.nextLevel()
        else:
            levelManager.restart()
            defeatScreen()

        playLevel()


    def hitWallTop(player):
        pos = player.getRawPos()
        return levelManager.isWall(int(pos[0]), int(pos[1] + player.getMaxVel()))
    def hitWallBottom(player):
        pos = player.getRawPos()
        return levelManager.isWall(int(pos[0]), int(pos[1] - player.getMaxVel()))
    def hitWallRight(player):
        pos = player.getRawPos()
        return levelManager.isWall(int(pos[0] + player.getMaxVel()), int(pos[1]))
    def hitWallLeft(player):
        pos = player.getRawPos()
        return levelManager.isWall(int(pos[0] - player.getMaxVel()), int(pos[1]))

    def isAlive(player):
        pos = player.getPos()
        return not levelManager.isHole(pos[0], pos[1])
    def beatLevel(player):
        pos = player.getPos()
        return levelManager.isGoal(pos[0], pos[1])


    def render(player):
        ballPos = player.getPos()
        
        frameArr = []
        levelLayout = levelManager.getLevelArr()
        
        for i in range(len(levelLayout)):
            frameArr[i] = levelLayout[i]
        frameArr[ballPos[0] + (8 * ballPos[1])] = [255, 0, 0] # make player a red pixel

        sense.set_pixels(frameArr)
    

    def transition(num):
        sense.show_message("Entering Level " + num)
    def defeatScreen():
        sense.show_message("You Died!!!")
