import pgzrun
import pygame
import random

HEIGHT = 540
WIDTH = 960

# Initial score and missed count
score = 0
missed = 0

# Create the chicken actor and set its initial position
chicken = Actor("chickenbasic", (382, 272))
wallpaper = Actor("background", (480, 270))

# Resize the background to fit the entire window
wallpaper.width = WIDTH
wallpaper.height = HEIGHT

# Define difficulty and timer variables
difficulty_factor = 1  # Controls the difficulty of the game
reset_time = 0.12  # Time (in seconds) before the chicken resets position if not clicked
time_left = reset_time  # Timer countdown

# Initialize the pygame mixer for background music
pygame.mixer.init()

# Load and play the background music
pygame.mixer.music.load(r"C:\oyun\music\chicken-song.mp3")
pygame.mixer.music.play(-1, 0.0)  # Play looped (-1 for infinite loop)

def update(dt):
    global time_left, missed
    # Decrease the timer countdown
    time_left -= dt
    
    # If time runs out, the chicken "disappears" (reset its position)
    if time_left <= 0:
        missed += 1  # Increment missed count
        reset_chicken()
        time_left = reset_time  # Reset the timer

def draw():
    global time_left, missed
    # Clear the screen and redraw everything
    screen.clear()

    # Draw the background to cover the whole screen
    wallpaper.draw()

    # Draw the chicken at its current position
    chicken.draw()

    # Draw the score and missed count on the screen
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30, color="white")
    screen.draw.text(f"Missed: {missed}", topleft=(10, 40), fontsize=30, color="white")
    screen.draw.text(f"Time left: {int(time_left)}", topleft=(10, 70), fontsize=30, color="white")

def on_mouse_down(pos, button):
    global score, difficulty_factor
    # Check if the chicken was clicked
    if chicken.collidepoint(pos):
        # Player caught the chicken, increment the score
        score += 5
        # Make the chicken harder to catch by increasing difficulty
        difficulty_factor += 0.1  # Increase the difficulty slightly
        reset_chicken()  # Move chicken to a new position
        global time_left
        time_left = reset_time  # Reset the timer

def reset_chicken():
    # The chicken's new position will be within the updated difficulty limits
    x_pos = random.randint(0, WIDTH - int(chicken.width * difficulty_factor))  # Smaller area
    y_pos = random.randint(0, HEIGHT - int(chicken.height * difficulty_factor))  # Smaller area
    chicken.pos = (x_pos, y_pos)  # Set the new position of the chicken

pgzrun.go()
