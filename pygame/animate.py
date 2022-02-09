#usr/bin/python

"""
invader.py
"""

import pygame, sys

pygame.init()

screen = pygame.display.set_mode([225,150])

r = pygame.Color("red")
w = pygame.Color("white")

frame1 = [
    [w,w,r,r,r,r,r,w,w],
    [w,w,r,w,r,w,r,w,w],
    [w,w,r,w,r,w,r,w,w],
    [w,r,r,r,w,r,r,r,w],
    [r,w,w,r,r,r,w,w,r],
    [r,r,w,w,w,w,w,r,r],
    ]

frame2 = [
    [w,r,r,r,r,r,r,r,w],
    [w,r,r,w,r,w,r,r,w],
    [w,w,r,r,r,r,r,w,w],
    [w,r,w,w,w,w,w,r,w],
    [r,w,w,r,r,r,w,w,r],
    [r,r,r,r,r,r,r,r,r],
    ]

#for y, row in enumerate(data):
#    for x, color in enumerate(row):
#        rect = pygame.Rect(x*25,y*25,25,25)
#        screen.fill(color, rect=rect)

#pygame.display.update()


def draw_frame(surface, data):
  for y, row in enumerate(data):
    for x, colour in enumerate(row):
      rect = pygame.Rect(x*25,y*25, 25, 25)
      screen.fill(colour, rect=rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    draw_frame(screen, frame1)
    pygame.display.update()
    pygame.time.wait(500)
    draw_frame(screen, frame2)
    pygame.display.update()
    pygame.time.wait(500)
