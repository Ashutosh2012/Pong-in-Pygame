import pygame
import opponent_paddle
import player_paddle
from player_paddle import Player
from opponent_paddle import Opponent
from ball import Ball

# Initializing pygame
pygame.init()

# Screen
W = 1280
H = 750
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Ping Pong by Ashutosh2012")

# Timer settings
timer = pygame.time.Clock()
fps = 60

# Font
font = pygame.font.Font("freesansbold.ttf", 32)

# Color
grey = (128, 128, 128)

# Player
player = Player()

# Opponent
opponent = Opponent()

# Ball
ball = Ball()

# Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")

# Run loop
run = True
while run:
    screen.fill((0, 0, 0))
    timer.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pressed = pygame.key.get_pressed()
        # Player up
        if pressed[pygame.K_w]:
            player.move_up()
        # Player down
        if pressed[pygame.K_s]:
            player.move_down()
        # Opponent up
        if pressed[pygame.K_x]:
            opponent.move_up()
        # Player down
        if pressed[pygame.K_v]:
            opponent.move_down()

    # Line
    pygame.draw.line(screen, grey, (W / 2, 0),(W / 2, H), 4)

    # Draw player paddle
    player.draw_player(screen, grey)

    # Draw opponent paddle
    opponent.draw_opponent(screen, grey)

    # Ball
    ball.draw_ball(screen, grey)
    ball.ball_movement(player.player, opponent.opponent, pong_sound)

    # Score
    #Score -- player
    if ball.ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player.score += 1
    #Score -- opponent
    if ball.ball.right >= W:
        pygame.mixer.Sound.play(pong_sound)
        opponent.score += 1

    # Show Score
    player_score = font.render(f'{player.score}', False, grey)
    screen.blit(player_score, (1024, 60))

    opponent_score = font.render(f'{opponent.score}', False, grey)
    screen.blit(opponent_score, (230, 60))

    pygame.display.flip()

pygame.quit()