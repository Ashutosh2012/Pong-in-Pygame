import pygame

# Initializing pygame
pygame.init()

class Ball:
    def __init__(self):
        self.W = 1280
        self.H = 750
        self.ball = pygame.Rect(self.W / 2 - 9, self.H / 2, 20, 20)
        self.speed_x = 7
        self.speed_y = 7

    def draw_ball(self, screen, color):
        # Drawing the rect
        pygame.draw.ellipse(screen, color, self.ball)

    def restart(self):
        self.ball.center = (self.W / 2, self.H / 2)

    def ball_movement(self, player, opponent, pong_sound):
        # Moving the ball
        self.ball.x += self.speed_x
        self.ball.y += self.speed_y

        # Collision detection and appropriate movement also sounds
        # Collision detection of sides
        if self.ball.top <= 0 or self.ball.bottom >= self.H:
            pygame.mixer.Sound.play(pong_sound)
            self.speed_y *= -1
        if self.ball.left <= 0 or self.ball.right >= self.W:
            pygame.mixer.Sound.play(pong_sound)
            self.speed_x *= -1

        # Collision detection of rects
        if self.ball.colliderect(player) or self.ball.colliderect(opponent):
            pygame.mixer.Sound.play(pong_sound)
            self.speed_x *= -1
