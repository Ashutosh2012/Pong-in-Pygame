import pygame

# Initializing pygame
pygame.init()

class Opponent:
    def __init__(self):
        self.W = 1280
        self.H = 750
        self.opponent = pygame.Rect(self.W / 2 - 600, self.H / 2, 15, 100)
        self.speed = 8
        self.score = 0

    def move_up(self):
        # Move up
        self.opponent.y -= self.speed

        # Collision
        if self.opponent.top <= 0:
            self.opponent.top = 0

    def move_down(self):
        # Move down
        self.opponent.y += self.speed

        # Collision
        if self.opponent.bottom >= self.H:
            self.opponent.bottom = self.H

    def draw_opponent(self, screen, color):
        # Drawing the rect
        pygame.draw.rect(screen, color, self.opponent)