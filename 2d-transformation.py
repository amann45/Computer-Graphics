import pygame
import math
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw Line Example")
# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)

global x1,y1,x2,y2
x1,y1,x2,y2 = 100,100,400,300

def translation(x1,y1,x2,y2,tx,ty):
    x1 += tx
    y1 += ty
    x2 += tx
    y2 += ty
    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 5)
    
def scaling(x1,y1,x2,y2,sx,sy):
    x1 *= sx
    y1 *= sy
    x2 *= sx
    y2 *= sy
    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 5)

def rotation(x1,y1,x2,y2,angle):
    angle = math.radians(angle)
    x1_new = x1*math.cos(angle) - y1*math.sin(angle)
    y1_new = x1*math.sin(angle) + y1*math.cos(angle)
    x2_new = x2*math.cos(angle) - y2*math.sin(angle)
    y2_new = x2*math.sin(angle) + y2*math.cos(angle)
    pygame.draw.line(screen, BLACK, (x1_new, y1_new), (x2_new, y2_new), 5)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a red line (x1, y1, x2, y2, color)
    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 5)
    translation(x1,y1,x2,y2,50,50)
    scaling(x1,y1,x2,y2,5,5)
    rotation(x1,y2,x2,y2,45)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()