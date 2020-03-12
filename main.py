import pygame

# init pygame
pygame.init()

# create window
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
# set title of it
pygame.display.set_caption("Donjon")

# ==========================================
#   VARIABLES
# ==========================================

# running true : the window is running / false : the window doesn't run anymore
running = True

# Main loop which updates all parts of the game
while running:

    # update window
    pygame.display.flip()

    # get events
    for e in pygame.event.get():

        # if cross is pressed
        if e.type == pygame.QUIT:
            # set running to False
            running = False
            # close window
            pygame.quit()

        # if window resizable
        if e.type == pygame.VIDEORESIZE:
            # recreate window with new dimensions
            screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
