from sense_hat import SenseHat
from time import sleep
from random import randint


#from random import randint
#num = randint(0,10)

#from random import uniform
#num = uniform(0,10)

#from random import choice
#deck = ['Ace', 'King', 'Queen', 'Jack']
#card = choice(deck)


sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

sense.show_letter("s", pick_random_colour())
sleep(1)
sense.show_letter("i", pick_random_colour())
sleep(1)
sense.show_letter("x", pick_random_colour())
sleep(1)
sense.show_letter("v", pick_random_colour())
sleep(1)
sense.show_letter("o", pick_random_colour())
sleep(1)

sense.clear()
