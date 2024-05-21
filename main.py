import pygame, random

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200

BUBBLE_WIDTH = 100
BUBBLE_HEIGHT = 100

# Load images
background = pygame.image.load("WhatsApp Image 2024-04-12 at 10.10.14.jpeg")
player = pygame.image.load("RUL.png")
bad_b = pygame.image.load("עיצוב_ללא_שם-removebg-preview (1).png ")
good_b = pygame.image.load("WhatsApp_Image_2024-04-09_at_17.31.12-removebg-preview.png")
# Scale images
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.transform.scale(player, (PLAYER_WIDTH, PLAYER_HEIGHT))
bad_b = pygame.transform.scale(bad_b, (BUBBLE_WIDTH, BUBBLE_HEIGHT))
good_b = pygame.transform.scale(good_b, (BUBBLE_WIDTH, BUBBLE_HEIGHT))
Bubbles = good_b, bad_b

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Say No to Social Anxiety")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player attributes
player_x = 50
player_y = SCREEN_HEIGHT // 2
player_velocity_y = 0
player_velocity_x = 5  # Initial horizontal speed
jump_strength = -10
gravity = 0.5

# function


# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_velocity_y = jump_strength

    # Update player position
    player_y += player_velocity_y
    player_velocity_y += gravity
    player_x += player_velocity_x

    player_x = max(0, min(player_x, SCREEN_WIDTH - 200))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - 200))

    # Check collision with screen edges
    if player_x <= 0 or player_x + PLAYER_WIDTH >= SCREEN_WIDTH:
        # If player hits the left or right wall, reverse the horizontal velocity
        player_velocity_x *= -1

    # Drawing code
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))
    screen.blit(bad_b, (0, 0))
    screen.blit(good_b, (0, 0))

    # making the object appear randomly
    # Randomize the position of bad bubble
    bad_bubble_x = random.randint(0, SCREEN_WIDTH - BUBBLE_WIDTH)
    bad_bubble_y = random.randint(0, SCREEN_HEIGHT - BUBBLE_HEIGHT)
    screen.blit(bad_b, (bad_bubble_x, bad_bubble_y))

    # Randomize the position of good bubble
    good_bubble_x = random.randint(0, SCREEN_WIDTH - BUBBLE_WIDTH)
    good_bubble_y = random.randint(0, SCREEN_HEIGHT - BUBBLE_HEIGHT)
    screen.blit(good_b, (good_bubble_x, good_bubble_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()