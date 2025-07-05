import pygame
import math
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1024, 600))
pygame.display.set_caption("cycling")
clock = pygame.time.Clock()

x = 0
speed = 5

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
    
def animate(x):
     
    pygame.draw.circle(screen,RED,(100+x,500),50,0)
    pygame.draw.circle(screen,RED,(300+x,500),50,0)
    
    pygame.draw.line(screen,BLACK,(100+x,500),(200+x,500),5)
    pygame.draw.line(screen,BLACK,(100+x,500),(150+x,400),5)
    pygame.draw.line(screen,BLACK,(200+x,500),(250+x,400),5)
    pygame.draw.line(screen,BLACK,(150+x,400),(250+x,400),5)
    pygame.draw.line(screen,BLACK,(200+x,500),(140+x,380),5)
    pygame.draw.line(screen,BLACK,(130+x,380),(150+x,380),5)
    pygame.draw.line(screen,BLACK,(120+x,500),(160+x,500),5)
    pygame.draw.line(screen,BLACK,(300+x,500),(230+x,350),5)
    pygame.draw.line(screen,BLACK,(230+x,350),(250+x,330),5)
    

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    pygame.draw.line(screen,BLACK,(0,550),(1024,550),5)
    animate(x)
    x += speed
    if x > 1024:  # Reset position when it goes off-screen
        x = -300
    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()