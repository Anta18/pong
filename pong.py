import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
FPS = 300

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKBLUE = (0, 0, 139)


# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anta's Pong Game")

clock = pygame.time.Clock()
# Paddle 1
paddle1_x = 50
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2

# Paddle 2
paddle2_x = WIDTH - 50 - PADDLE_WIDTH
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2


# Ball
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_velocity_x = 300
ball_velocity_y = 300 
# Initialize player scores
score1 = 0
score2 = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= 2
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += 2
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= 2
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += 2

    ball_x += ball_velocity_x / FPS
    ball_y += ball_velocity_y / FPS

    # Ball collision with walls
    if ball_y + BALL_RADIUS > HEIGHT or ball_y - BALL_RADIUS < 0:
        ball_velocity_y = -ball_velocity_y

    if ball_x - BALL_RADIUS < 0:
        # Player 2 scores a point
        score2 += 1
        pygame.time.wait(500)
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_velocity_x = -ball_velocity_x

    elif ball_x + BALL_RADIUS > WIDTH:
        # Player 1 scores a point
        score1 += 1
        pygame.time.wait(500)
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_velocity_x = -ball_velocity_x

    # Ball collision with paddles
    if (
        paddle1_x + PADDLE_WIDTH > ball_x > paddle1_x
        and paddle1_y + PADDLE_HEIGHT > ball_y > paddle1_y
    ):
        ball_velocity_x = -ball_velocity_x

    if (
        paddle2_x < ball_x + BALL_RADIUS < paddle2_x + PADDLE_WIDTH
        and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT
    ):
        ball_velocity_x = -ball_velocity_x

        # Ball out of bounds

    # Clear the screen
    screen.fill(DARKBLUE)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)
    for i in range(0, HEIGHT, HEIGHT // 10):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2, i, 2, HEIGHT // 20))
    font = pygame.font.Font(None, 36)  # Font for the score display

    # Draw player 1's score
    score_text1 = font.render("Player 1: " + str(score1), True, WHITE)
    screen.blit(score_text1, (20, 20))

    # Draw player 2's score
    score_text2 = font.render("Player 2: " + str(score2), True, WHITE)
    screen.blit(score_text2, (WIDTH - score_text2.get_width() - 20, 20))

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
