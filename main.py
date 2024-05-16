import pygame

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
PLAYER_WIDTH = 300
PLAYER_HEIGHT = 300

# Load images
background = pygame.image.load("WhatsApp Image 2024-04-12 at 10.10.14.jpeg")
player = pygame.image.load("RUL.png")

# Scale images
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.transform.scale(player, (PLAYER_WIDTH, PLAYER_HEIGHT))

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

    # Check collision with screen edges
    if player_x <= 0 or player_x + PLAYER_WIDTH >= SCREEN_WIDTH:
        # If player hits the left or right wall, reverse the horizontal velocity
        player_velocity_x *= -1

    # Drawing code
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
