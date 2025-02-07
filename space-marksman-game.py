# SPACE MARKSMAN GAME USING PYGAME (final project)
# By: Aman Kumar Ray

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Marksman")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player spaceship properties
player_width = 50
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 5

# Enemy properties
enemy_width = 50
enemy_height = 40
enemy_speed = 2
enemies = []

# Bullet properties
bullet_width = 5
bullet_height = 10
bullet_speed = -7
bullets = []

# Score
score = 0

# Font for score
font = pygame.font.Font(None, 36)

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Add enemies
def add_enemy():
    x = random.randint(0, WIDTH - enemy_width)
    y = random.randint(-100, -40)
    enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

# Draw player spaceship
def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))

# Draw enemies
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

# Draw bullets
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, bullet)

# Move enemies
def move_enemies():
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

# Move bullets
def move_bullets():
    for bullet in bullets:
        bullet.y += bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

# Check collisions
def check_collisions():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

# Main game loop
running = True
enemy_spawn_timer = 0
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit number of bullets on screen
            bullets.append(pygame.Rect(player_x + player_width // 2, player_y, bullet_width, bullet_height))

    # Spawn enemies
    enemy_spawn_timer += 1
    if enemy_spawn_timer > 50:  # Spawn an enemy every 50 frames
        add_enemy()
        enemy_spawn_timer = 0

    # Move and draw everything
    move_enemies()
    move_bullets()
    check_collisions()
    draw_player(player_x, player_y)
    draw_enemies()
    draw_bullets()

    # Check for game over
    for enemy in enemies:
        if enemy.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            print("Game Over!")
            running = False

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()