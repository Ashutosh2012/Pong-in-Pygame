import pygame

# Initializing pygame
pygame.init()

class Player():
    def __init__(self):
        # Settings
        self.W = 1280
        self.H = 750
        self.player = pygame.Rect(self.W / 2 + 600, self.H / 2, 15, 100)
        self.speed = 8
        self.score = 0

    def move_up(self):
        # Move up
        self.player.y -= self.speed

        # Collision
        if self.player.top <= 0:
            self.player.top = 0

    def move_down(self):
        # Move down
        self.player.y += self.speed

        # Collision
        if self.player.bottom >= self.H:
            self.player.bottom = self.H

    def draw_player(self, screen, color):
        # Drawing the rect
        pygame.draw.rect(screen, color, self.player)
