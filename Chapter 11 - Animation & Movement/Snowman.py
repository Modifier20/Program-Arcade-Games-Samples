import pygame

# --- Defined Colours ---
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()                                               # Initalizes PyGame

size = (700, 500)                                           # Determines the Size of the PyGame Window
screen = pygame.display.set_mode(size)                      # Creates PyGame Window.

pygame.display.set_caption("PyGame Base Project")            # Set's The Title of The PyGame Window.

done = False                                                # Loops Until The User Clicks

clock = pygame.time.Clock()                                 # Manages How Fast The Screen Updates.

# --- Main Program Variables ---


# --- Main Program Loop ---
while not done:

    # --- Main Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)                                      # Fills The Background With White

    # --- Game Logic ---


    # --- Game Drawing ---
    

    pygame.display.flip()                                   # Updates The Screen With What We've Drawn

    clock.tick(20)                                          # Limits The FPS

pygame.quit()