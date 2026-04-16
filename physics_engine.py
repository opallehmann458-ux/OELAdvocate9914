import pygame
import math

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vx = 5  # Velocity in x direction
        self.vy = 5  # Velocity in y direction

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.vx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.vx = 5
        self.vy = 5

class Net:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Ball Bouncing Simulation')
    clock = pygame.time.Clock()

    ball = Ball(WIDTH // 2, HEIGHT // 2, 20, (255, 0, 0))
    net = Net(WIDTH // 2 - 50, HEIGHT - 30, 100, 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.move()

        # Check if ball hits the net
        if net.rect.collidecircle((ball.x, ball.y), ball.radius):
            ball.vy *= -1
            ball.y = net.rect.top - ball.radius

        screen.fill((0, 0, 0))  # Clear the screen
        ball.draw(screen)
        net.draw(screen)
        pygame.display.flip()  # Update the display

        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()