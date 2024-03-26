import pygame 
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the snake and food initial positions
snake_size = 20
snake_speed = 25
snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0

food_x = round(random.randrange(0, window_width - snake_size) / 20) * 20
food_y = round(random.randrange(0, window_height - snake_size) / 20) * 20
# Define the score variable
score = 0

# Set up the game clock
clock = pygame.time.Clock()

# Define the game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0

    # Update the snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with the walls
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    # Check for collision with the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = round(random.randrange(0, window_width - snake_size) / 20) * 20
        food_y = round(random.randrange(0, window_height - snake_size) / 20) * 20

    # Clear the game window
    game_window.fill(black)

    # Draw the snake and food
    pygame.draw.rect(game_window, green, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(game_window, white, [snake_x, snake_y, snake_size, snake_size])

    # Update the game display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()

