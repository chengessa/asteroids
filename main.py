import pygame
from constants import *

def main():

    # SET UP DISPLAY
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #PRINT BOOTUP INFO
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    #DRAW THE GAME
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
