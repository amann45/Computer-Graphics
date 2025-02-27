import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodging ball game")

# Load background image
background = pygame.image.load("3d_background1.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK=(0,0,0,)

# Game Variables
ball_x, ball_y = 100, HEIGHT // 2
ball_velocity = 0
gravity = 0.5
ball_strength = -8

pipes = []
obstacles = []
pipe_width = 60
gap = 150
pipe_speed = 3
score = 0

font = pygame.font.Font(None, 36)

def create_pipe():
    """ Creates a new pipe with a random obstacle in the gap """
    pipe_y = random.randint(100, HEIGHT - 200)
    pipes.append({"x": WIDTH, "y": pipe_y})

    # Randomly place an obstacle in the gap
    if random.random() < 0.5:  # 50% chance of obstacle
        obs_y = pipe_y + random.randint(30, gap - 30)
        obstacles.append({"x": WIDTH + pipe_width // 2, "y": obs_y})

def move_pipes():
    """ Moves pipes and obstacles left """
    global pipes, obstacles, score
    for pipe in pipes:
        pipe["x"] -= pipe_speed
    for obs in obstacles:
        obs["x"] -= pipe_speed

    if pipes and pipes[0]["x"] < -pipe_width:
        pipes.pop(0)
        if obstacles and obstacles[0]["x"] < -pipe_width:
            obstacles.pop(0)
        score += 1  # Increase score when passing pipes

def draw_pipes():
    """ Draws pipes and obstacles """
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe["x"], 0, pipe_width, pipe["y"]))  # Top pipe
        pygame.draw.rect(screen, GREEN, (pipe["x"], pipe["y"] + gap, pipe_width, HEIGHT - pipe["y"] - gap))  # Bottom pipe

    for obs in obstacles:
        pygame.draw.circle(screen, RED, (obs["x"], obs["y"]), 10)  # Random obstacle

def check_collision():
    """ Checks if the ball collides with pipes, obstacles, or ground """
    if ball_y > HEIGHT or ball_y < 0:
        return True

    for pipe in pipes:
        if ball_x + 30 > pipe["x"] and ball_x < pipe["x"] + pipe_width:
            if ball_y < pipe["y"] or ball_y > pipe["y"] + gap:
                return True  # Collision with pipe

    for obs in obstacles:
        if (ball_x + 15 - obs["x"]) **2 + (ball_y + 15 - obs["y"]) **2 < 20 ** 2:
            return True  # Collision with obstacle

    return False

def draw_text(text, x, y):
    """ Draws text on the screen """
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def main():
    """ Main game loop """
    global ball_y, ball_velocity
    clock = pygame.time.Clock()
    running = True
    create_pipe()

    while running:
        screen.blit(background, (0, 0))  # Draw background

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ball_velocity = ball_strength  # Ball flaps up

        # Ball physics
        ball_velocity += gravity
        ball_y += ball_velocity

        # Pipe movement and generation
        move_pipes()
        if pipes and pipes[-1]["x"] < WIDTH - 200:
            create_pipe()

        # Draw elements
        pygame.draw.circle(screen, BLACK, (ball_x, int(ball_y)), 15)  # Ball
        draw_pipes()
        draw_text(f"Score: {score}", 10, 10)

        # Collision check
        if check_collision():
            draw_text("GAME OVER", WIDTH // 2 - 70, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            break

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()