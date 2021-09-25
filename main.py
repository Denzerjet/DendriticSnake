#importing pygame and sys (not sure what sys does)
import sys, pygame
#initializes all functions of pygame
pygame.init()

#you set size = 320, 240 because python is gamer and width = 320 and height = 240
size = width, height = 320, 240
#more python-esque initialization
speed = [2, 2]
black = 0, 0, 0

#you create a display of size size
screen = pygame.display.set_mode(size)
#load image into the thing and (make an area that encompasses it for manip?)
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

#infinite loop where u check if the user wants to exit
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #if the ball exits from the top or bottom reverse it's direction appropriately
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    #fill the screen with black, transfer the ball and ballrect drawings over from their storage locations
    #to the display
    screen.fill(black)
    screen.blit(ball, ballrect)
    #only draw completed drawings, don't draw things that are in the process of being drawn
    #(imagine flipping through a notebook of images that blend together to make an animation)
    pygame.display.flip()