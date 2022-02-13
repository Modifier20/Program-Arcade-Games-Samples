import pygame

# --- Defined Colours ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()                                           # Initalizes PyGame

size = (700, 500)                                       # Determines the Size of the PyGame Window
screen = pygame.display.set_mode(size)                  # Creates PyGame Window.

pygame.display.set_caption("Bouncing Rectangle")        # Set's The Title of The PyGame Window.

done = False                                            # Loops Until The User Clicks

clock = pygame.time.Clock()                             # Manages How Fast The Screen Updates.

# --- Main Program Loop ---
while not done:

    # --- Main Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        screen.fill(WHITE)                              # Fills The Background With White

        pygame.display.flip()                           # Updates The Screen With What We've Drawn

        clock.tick(60)                                  # Limits The FPS to 60

pygame.quit()