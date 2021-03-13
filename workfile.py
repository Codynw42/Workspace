import pygame
import os


FPS = 60
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1400, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TEMPLE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Temple_Time.jpeg')), (WIDTH, HEIGHT))



def draw_surface():
    WIN.fill((WHITE))
    WIN.blit(TEMPLE, (0, 0))
    pygame.display.update()
    


def mainloop():                     
    
    clock = pygame.time.Clock()
    run = True                                 #The FIRST thing you always do when youre making a pygame, is write out this main function. 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():       #The second thing you do, is check if the player has quit the game to end the loop with this function.
            if event.type == pygame.QUIT:
                run = False           
                pygame.quit()                                   #Without a main loop, python would not be able to draw the window, it would start and stop immediately. 

        
        draw_surface()
        
        


if __name__ == "__main__":
    mainloop()                                
        