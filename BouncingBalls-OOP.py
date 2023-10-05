import pygame
import random

# Dictionary of common color names mapped to RGB values
COLORS = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "black": (0, 0, 0),
    "cyan": (100, 100, 150),
    "brown": (200, 60, 34)
    # Add more colors as needed
}

class MovingCircle:
    def __init__(self, screen, color_name, size, start_x, start_y): # removed controls
        self.screen = screen
        self.color = COLORS.get(color_name, (255, 255, 255))  # Default to white if color is not found
        self.size = size
        self.position = pygame.Vector2(start_x, start_y)
        self.active = True  # Flag to indicate if the player is active
        self.dt = 0
        self.velX = random.randint(700, 1000)*(random.choice([-1, 1]))
        self.velY = random.randint(700, 1000)*(random.choice([-1, 1]))
        self.LastHit = ""
    

    def move(self, dt, velX, velY):
        self.position.x += int(velX * dt) # when x is positive, it goes right  (- <) (+ >)
        self.position.y += int(velY * dt) # When y is negative, the object goes up (- ^) (+ ,)

    def draw(self):
        if self.active:
            pygame.draw.circle(self.screen, self.color, self.position, self.size)

    def check_collision(self, height, width):
        if self.position.x-self.size < 0 and self.LastHit != "L":
            self.LastHit = "L"
            self.velX *= -1
            self.color = random.choice(list(COLORS.keys()))
            print("L", self.color, self.position, self.velX, self.velY)
            self.position.x = self.size +2
        elif self.position.x+self.size > width and self.LastHit != "R":
            self.LastHit = "R"
            self.velX *= -1
            self.color = random.choice(list(COLORS.keys()))
            print("R", self.color, self.position, self.velX, self.velY)
            self.position.x = width - self.size -2
        if self.position.y+self.size > height and self.LastHit != "D":
            self.LastHit = "D"
            self.velY *= -1
            self.color = random.choice(list(COLORS.keys()))
            print("D", self.color, self.position, self.velX, self.velY)
            self.position.y = height - self.size -2
        elif self.position.y-self.size < 0 and self.LastHit != "U":
            self.LastHit = "U"
            self.velY *= -1
            self.color = random.choice(list(COLORS.keys()))
            print("U", self.color, self.position, self.velX, self.velY)
            self.position.y = self.size +2
# Pygame setup
pygame.init()
SCREEN_H = 720
SCREEN_W = 1280
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Manok Balls')

# Create player objects
player1 = MovingCircle(screen, "red", 40, random.randint(41, SCREEN_W-41), random.randint(41, SCREEN_H-41))
player2 = MovingCircle(screen, "blue", 40, random.randint(41, SCREEN_W-41), random.randint(41, SCREEN_H-41))
player3 = MovingCircle(screen, "yellow", 40, random.randint(41, SCREEN_W-41), random.randint(41, SCREEN_H-41))
player4 = MovingCircle(screen, "cyan", 40, random.randint(41, SCREEN_W-41), random.randint(41, SCREEN_H-41))
player5 = MovingCircle(screen, "blue", 40, random.randint(100, 1200), random.randint(100, 600))
player6 = MovingCircle(screen, "yellow", 40, random.randint(100, 1200), random.randint(100, 600))
player7 = MovingCircle(screen, "black", 40, random.randint(100, 1200), random.randint(100, 600))
player8 = MovingCircle(screen, "red", 40, random.randint(100, 1200), random.randint(100, 600))
player9 = MovingCircle(screen, "w", 40, random.randint(100, 1200), random.randint(100, 600))
player10 = MovingCircle(screen, "bl", 40, random.randint(100, 1200), random.randint(100, 600))

players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
#players = [player1]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 128, 128))

    for player in players:
        player.check_collision(720, 1280)
        player.move(player.dt, player.velX, player.velY)
        player.draw()
    pygame.display.flip()
    for player in players:
        player.dt = clock.tick(900) / 100
pygame.quit()
