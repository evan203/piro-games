from sense_hat import SenseHat
import math

class Ball:
    sense = SenseHat()
    
    red = [255, 0, 0]  # Red
    
    directions = ["pitch", "roll"]

    avg_pitch, avg_roll = normalize_orientation()

    gravity = 0.01
    terminal_v = 0.1
    dampening = 0.9
        
    ball_pos = [0.0, 0.0] #init position to center (x,y) 
    ball_v = [0.0, 0.0] #init velocity to 0 (x,y)

    #initialize at a spawn position and normalize orientation
    def __init__ (spawn):
        ball_pos = spawn
        normalize_orientation()
        


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
    

    def get_normal_orientation():
            # adjust orientation by average
            o = sense.get_orientation()
            o["pitch"] -= avg_pitch		
            o["pitch"] *= -1
            o["roll"] -= avg_roll
            return o
    
    def getMaxVel():
        return terminal_v
    def getPos():
        return [int(ball_pos[0]), int(ball_pos[1])]
    def getRawPos():
        return ball_pos

    def killPosYVel:
        if ball_v[1] > 0:
            vall_v[1] = 0
    def killNegYVel:
        if ball_v[1] < 0:
            vall_v[1] = 0
    def killPosXVel:
        if ball_v[0] > 0:
            vall_v[0] = 0
    def killNegXVel:
        if ball_v[0] < 0:
            vall_v[0] = 0

    
    # the function that actualy updates the player and is called from the GameManager
    def update():
            o = get_normal_orientation()
            for i in range(2):
                ball_pos[i] += ball_v[i]
                
                ball_v[i] += math.sin(math.radians(o[directions[i]]))*gravity
                ball_v[i] *= dampening
                
                if ball_v[i] > terminal_v:
                        ball_v[i] = terminal_v
                elif ball_v[i] < -1 * terminal_v:
                        ball_v[i] = -1 * terminal_v

                
                if ball_pos[i] >= 8:
                        ball_v[i] = 0
                        ball_pos[i] = 7.999
                elif ball_pos[i] < 0:
                        ball_v[i] = 0
                        ball_pos[i] = 0
