# Sierpinski Triangle Fractal Generator
# 08-03-13

import pygame, sys
from pygame.locals import *

screenWidth = 600                           # Width(px) of screen
screenHeight = 350                          # Height(px) of screen
sideLength = 300                            # Length (px) of triangle side
centX = screenWidth//2                      # Upper x coord of bounding triangle
centY = 0 + (screenHeight-sideLength)//2    # Upper y coord of bounding triangle

screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("Sierpinski Triangle")


def fractalLoop():
    print("Sierpinski Triangle:")

    screen.fill((255,255,255))

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                image = pygame.display.get_surface()
                n_image = pygame.transform.rotozoom(image, 180, 2)
                screen.blit(n_image, (0,0))
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    screen.fill((255,255,255))
                    
        depth = raw_input("Enter a level: ")
        depth = int(depth, base=10)
        draw(centX,centY, sideLength, depth)
        
        pygame.time.Clock().tick(30)
        pygame.display.flip()
    # Exit 
    pygame.quit()
    System.exit()


def draw(cx,cy,length,count):
    # Draw bounding triangle
    pygame.draw.polygon(screen,(0,0,0),
                        [(cx,cy),(cx-length, cy+length)],1)
    pygame.draw.polygon(screen,(0,0,0),
                        [(cx,cy),(cx+length,cy+length)],1)
    pygame.draw.polygon(screen,(0,0,0),
                        [(cx-length, cy+length),(cx+length,cy+length)],1)
    # Draw sub-triangles
    if (count > 0):
        recDraw(cx,cy,length,count)


def recDraw(cx, cy, length, count):
    pygame.draw.polygon(screen,(255,0,0),
                [(cx-length//2,cy+length//2),(cx+length//2, cy+length//2)],1) 
    pygame.draw.polygon(screen,(0,255,0),
                [(cx-length//2,cy+length//2),(cx,cy+length)],1)
    pygame.draw.polygon(screen,(0,0,255),
                [(cx+length//2,cy+length//2),(cx,cy+length)],1)
    
    if count > 1:
        count -= 1
        recDraw(cx,cy,length//2,count)
        recDraw(cx-length//2, cy+length//2,length//2,count) # Divide down-left
        recDraw(cx+length//2, cy+length//2,length//2,count) # Divide down-right
        
pygame.init()

# Draw Sierpinski Triangles
fractalLoop()
