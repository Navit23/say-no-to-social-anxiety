import pygame
import random

# Initialize Pygame
pygame.init()

ls_screen = pygame.image.load("WhatsApp Image 2024-04-11 at 16.55.49.jpeg")
wi_screen = pygame.image.load("WhatsApp Image 2024-04-12 at 13.10.36.jpeg")
background = pygame.image.load("WhatsApp Image 2024-04-12 at 10.10.14.jpeg")
player =

# Set up screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("say no to social anxiety")



# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Drawing code could go here
    #blit
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
