import pygame
import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        points.append((x1, y1))

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

x1, y1 = 50, 100
x2, y2 = 400, 300

points = bresenham(x1, y1, x2, y2)

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Bresenham Line - Pygame")

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw pixels
    for x, y in points:
        screen.set_at((x, y), (255, 0, 0))

    pygame.display.flip()

pygame.quit()


x_vals = [p[0] for p in points]
y_vals = [p[1] for p in points]

plt.figure()
plt.plot(x_vals, y_vals, 'ro')
plt.title("Bresenham Line - Matplotlib")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().invert_yaxis()  # match screen coordinates
plt.grid(True)
plt.show()