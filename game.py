import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks!")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (50, 200, 50)
SPACE_COLOR = (10, 10, 30)  # Dark space-like background

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 80
player_speed = 8

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []

# Game loop variables
running = True
clock = pygame.time.Clock()
score = 0

while running:
    screen.fill(SPACE_COLOR)  # Set background color instead of image
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # Spawn obstacles randomly and ensure they don't align with player
    if random.randint(1, 40) == 1:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        while abs(obstacle_x - player_x) < player_size:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacles.append([obstacle_x, 0])
    
    # Move obstacles down
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
    
    # Remove off-screen obstacles
    obstacles = [ob for ob in obstacles if ob[1] < HEIGHT]
    
    # Collision detection
    for obstacle in obstacles:
        if (player_x < obstacle[0] + obstacle_width and player_x + player_size > obstacle[0] and
            player_y < obstacle[1] + obstacle_height and player_y + player_size > obstacle[1]):
            print(f"Game Over! Your Score: {score}")
            running = False
    
    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))
    
    # Increase speed over time
    score += 1
    if score % 500 == 0:
        obstacle_speed += 2.5
    
    # Refresh screen
    pygame.display.update()
    clock.tick(30)

pygame.quit()
