import pygame,sys
from pygame.locals import *

catx=10
caty=10
screen=0

def myquit():
    pygame.quit()
    sys.exit(0)

def check_input(events):
    global catx,caty,screen
    for event in events:
        if event.type==QUIT:
            myquit()
        else:
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    myquit()
                elif event.key==K_LEFT:
                    catx-=5
                    print("Move Rect left")
                elif event.key==K_RIGHT:
                    catx+=5
                    print("Move rect right")
                else:
                    print(event.key)
                    print(event.key)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
    pygame.display.update()

def main():
    global screen
    pygame.init()
    SCREEN_WIDTH=600
    SCREEN_HEIGHT=480
    window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Slither")
    screen=pygame.display.get_surface()

    pygame.display.update()

    while 1:
        check_input(pygame.event.get())
main()
