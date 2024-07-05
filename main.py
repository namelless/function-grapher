import sys
import math
import pygame

pygame.init()

display = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
t = 0
while True:
    display.fill((0, 0, 0))
    points = []
    for x in range(-10,display.get_width()+10):
        #change the function used
        func = math.sin
        point = [x,func(math.radians(x+t))*display.get_height()/6+display.get_height()/2]
        points.append(point)
        #the line below is for drawing the points as circles
        #pygame.draw.circle(display, (255,0,0),point,2)
    #the line below is for drawing the points as a line note: the tan funcioned cant be mapped using a line since it extends to infinity
    pygame.draw.lines(display, (255,0,0),0,points,5)
    
    #controls the speed
    t += 1
    #add a line to the middle of the graph
    #pygame.draw.line(display, (255,255,255),(0, display.get_height()/2),(display.get_width(), display.get_height()/2),2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()    
    clock.tick(60)
    