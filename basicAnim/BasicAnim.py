# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:37:46 2024

@author: Michael Scott

"""


def main():
    import pygame
    pygame.init()
    
    boxRight = True
    boxUp = True
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Press Space to switch direction")

    background = pygame.Surface(screen.get_size())
    background = pygame.image.load("sursa.png")
    background = background.convert()
    background = pygame.transform.scale(background, (640 , 480))
    
    box = pygame.Surface((25, 25))
    box = pygame.image.load("horn_man.png")
    box = box.convert_alpha()
    box = pygame.transform.scale(box, (100 , 100))
    
    box_x = 0
    box_y = 200
    
    clock = pygame.time.Clock()
    keepGoing = True

    keySwitch = False

    while keepGoing:
        
        keys = pygame.key.get_pressed()
        
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        if boxRight:
            box_x += 5
        else:
            box_x -= 5
        
        if boxUp:
            box_y -= 5
        else:
            box_y += 5
        
        if box_x > screen.get_width() - 100:
            boxRight = False
        if box_y > screen.get_height() - 100:
            boxUp = True
        if box_x < 0:
            boxRight = True
        if box_y < 0:
            boxUp = False
        if keys[pygame.K_SPACE]:
            if keySwitch == False:
                if boxRight:
                    boxRight = False
                elif boxRight == False:
                    boxRight = True
            keySwitch = True
        else:
            keySwitch = False
        
        
        screen.blit(background, (0, 0))
        screen.blit(box, (box_x,box_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
