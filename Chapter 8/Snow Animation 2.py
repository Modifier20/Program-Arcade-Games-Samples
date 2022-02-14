import pygame
import random

# --- Defined Colours ---
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()                                               # Initalizes PyGame

size = (1440, 900)                                           # Determines the Size of the PyGame Window
screen = pygame.display.set_mode(size)                      # Creates PyGame Window.

pygame.display.set_caption("Snow Animation")            # Set's The Title of The PyGame Window.

done = False                                                # Loops Until The User Clicks

clock = pygame.time.Clock()                                 # Manages How Fast The Screen Updates.

# --- Main Program Variables ---
star_list = []
for i in range(50):
    x = random.randint(0,1440)
    y = random.randint(0,900)
    star_list.append([x, y])

# --- Main Program Loop ---
while not done:

    # --- Main Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)                                      # Fills The Background With White

    # --- Game Logic ---
    

    # --- Game Drawing ---
    for item in star_list:
        item[1] += 1
        pygame.draw.circle(screen, white, item, 2)

        if item[1] > 900:
            item[1] = random.randrange(-20, -5)
            item[0] = random.randrange(1440)

    pygame.display.flip()                                   # Updates The Screen With What We've Drawn

    clock.tick(20)                                          # Limits The FPS

pygame.quit()