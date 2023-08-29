from sense_hat import SenseHat
sense = SenseHat()

sense.clear()
while True:
	o = sense.get_orientation()
	pitch = o["pitch"]
	roll = o["roll"]
	print("pitch {0} roll {1}".format(pitch, roll))
