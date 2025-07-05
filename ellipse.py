import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Algorithm")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0 )
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Function to draw the circle using midpoint algorithm
def draw_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry
    p1 = round(ry * ry - rx * rx * ry + 0.25 * rx * rx) 
    # dx = 2 * ry * ry * x
    # dy = 2 * rx * rx * y
    while (ry * ry * x) <= (rx * rx * y ):
        if(p1 < 0):
          
            p1 = p1 + (2 * ry * ry * x) + ry * ry
        else:

            y = y-1
            p1 = p1 + (2 * ry * ry * x) - (2 * rx * rx * y )+ ry * ry
        x += 1
        screen.set_at(( x + xc , y + yc) , RED) 
        screen.set_at((x + xc , -y + yc) , GREEN) 
        screen.set_at((-x + xc , y + yc) , BLUE) 
        screen.set_at((-x + xc , -y + yc) , WHITE) 

    p2 = round(ry * ry *(x + 1/2) ** 2  + rx * rx * (y-1) ** 2 - rx * rx * ry * ry)
    while y != 0:
        if(p2 >  0):
            p2 = p2 -  (2 * rx * rx * y )+ rx * rx
        else:
            x = x+1
            p2 = p2 + (2 * ry * ry * x) - (2 * rx * rx * y )+ rx * rx
            
        y = y-1
        screen.set_at(( x + xc , y + yc) , RED) 
        screen.set_at((x + xc , -y + yc) , RED) 
        screen.set_at((-x + xc , y + yc) , RED) 
        screen.set_at((-x + xc , -y + yc) , RED) 

        

# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_ellipse(200, 200, 100, 50)
        # pygame.draw.circle(screen, RED, (400, 400), 100, 50)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()