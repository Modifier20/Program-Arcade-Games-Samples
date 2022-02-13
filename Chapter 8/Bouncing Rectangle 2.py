import pygame

# --- Defined Colours ---
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()                                               # Initalizes PyGame

size = (1440, 900)                                           # Determines the Size of the PyGame Window
screen = pygame.display.set_mode(size)                      # Creates PyGame Window.

pygame.display.set_caption("Bouncing Rectangle")            # Set's The Title of The PyGame Window.

done = False                                                # Loops Until The User Clicks

clock = pygame.time.Clock()                                 # Manages How Fast The Screen Updates.

# --- Main Program Variables ---
rect_x = 50                                                 # Position of Rectangle
rect_y = 50
rect_change_x = 10                                           # Vector Direction and Speed
rect_change_y = 6

# --- Main Program Loop ---
while not done:

    # --- Main Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(black)                                      # Fills The Background With White

    # --- Game Logic ---
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_x > 1389 or rect_x < 0:
        rect_change_x *= -1
    if rect_y > 849 or rect_y < 0:
        rect_change_y *= -1

    # --- Game Drawing ---
    pygame.draw.rect(screen, white, [rect_x,rect_y,50,50])
    

    pygame.display.flip()                                   # Updates The Screen With What We've Drawn

    clock.tick(20)                                          # Limits The FPS

pygame.quit()