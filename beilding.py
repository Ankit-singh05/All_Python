import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 400
HEIGHT = 600
BOTTOM_MARGIN = 20
CATCH_BASE_Y = HEIGHT - BOTTOM_MARGIN
BALL_R = 12
STACK_W = 24
PLATFORM_W = 60
PLATFORM_SPEED = 8
FPS = 60

# Colors (Nokia monochrome vibe with shades)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
STACK_COLOR = (0, 220, 0)
STACK_OUTLINE = (50, 255, 50)
RED = (255, 50, 50)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drop Stack - Old Nokia Style! (Wobble Physics)")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont('monospace', 24, bold=True)
big_font = pygame.font.SysFont('monospace', 48, bold=True)

# Wobble physics variables
wobble_amplitude = 0.0
wobble_phase = 0.0
wobble_offset = 0.0
high_score = 0

# Game variables
def reset_game():
    global platform_x, stack_x, stack_h, balls, caught, fall_speed, spawn_interval, spawn_timer, game_over
    global wobble_amplitude, wobble_phase, wobble_offset
    platform_x = WIDTH // 2 - PLATFORM_W // 2
    stack_x = WIDTH // 2
    stack_h = 0
    balls = []
    caught = 0
    fall_speed = 3.0
    spawn_interval = 80
    spawn_timer = 0
    game_over = False
    wobble_amplitude = 0.0
    wobble_phase = 0.0
    wobble_offset = 0.0

reset_game()

def draw_platform():
    py = CATCH_BASE_Y + 12
    pygame.draw.line(screen, WHITE, (platform_x, py), (platform_x + PLATFORM_W, py), 6)

def draw_stack():
    if stack_h > 0:
        top_y = CATCH_BASE_Y - stack_h
        bottom_y = CATCH_BASE_Y
        half_w = STACK_W // 2
        # Polygon points for slanted/wobbling stack
        bl = (stack_x - half_w, bottom_y)
        br = (stack_x + half_w, bottom_y)
        tr = (stack_x + half_w + wobble_offset, top_y)
        tl = (stack_x - half_w + wobble_offset, top_y)
        points = [bl, br, tr, tl]
        # Fill
        pygame.draw.polygon(screen, STACK_COLOR, points)
        # Outline for crisp Nokia look
        pygame.draw.polygon(screen, WHITE, points, 2)

def draw_balls():
    for ball in balls:
        pygame.draw.circle(screen, WHITE, (int(ball['x']), int(ball['y'])), BALL_R)

def check_collisions():
    global stack_h, caught, wobble_amplitude
    i = 0
    while i < len(balls):
        ball = balls[i]
        bx = ball['x']
        by = ball['y']
        stack_top_y = CATCH_BASE_Y - stack_h
        # Effective top center accounting for wobble lean
        effective_top_x = stack_x + wobble_offset
        tolerance = (STACK_W // 2) + (BALL_R // 2)
        if by + BALL_R >= stack_top_y and abs(bx - effective_top_x) < tolerance:
            # Wobble impulse: stronger on shorter stacks for realism/fun
            impulse = 3.5 / (1 + stack_h / 250.0)
            wobble_amplitude += impulse
            stack_h += 24
            caught += 1
            del balls[i]
            continue
        i += 1

# Main game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                high_score = max(high_score, caught)
                reset_game()

    if not game_over:
        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            platform_x -= PLATFORM_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            platform_x += PLATFORM_SPEED
        platform_x = max(0, min(WIDTH - PLATFORM_W, platform_x))

        # Update stack_x to follow platform center
        stack_x = platform_x + PLATFORM_W // 2

        # Update wobble physics (always, but impulses only during game)
        wobble_phase += 0.4
        wobble_offset = wobble_amplitude * math.sin(wobble_phase)
        wobble_amplitude *= 0.96
        if wobble_amplitude < 0.2:
            wobble_amplitude = 0.0
            wobble_offset = 0.0

        # Dynamic difficulty
        level = caught // 10
        fall_speed = 3.0 + 0.25 * level
        spawn_interval = max(40, 80 - 3 * level)

        # Spawn balls
        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_timer = 0
            if len(balls) < 10:  # Limit falling balls
                balls.append({'x': random.randint(BALL_R + 20, WIDTH - BALL_R - 20), 'y': -BALL_R * 2})

        # Update balls
        i = 0
        while i < len(balls):
            balls[i]['y'] += fall_speed
            if balls[i]['y'] > HEIGHT + BALL_R:
                del balls[i]
            else:
                i += 1

        # Check collisions
        check_collisions()

        # Game over check
        stack_top_y = CATCH_BASE_Y - stack_h
        if stack_top_y <= 80:
            wobble_amplitude += 15.0  # Dramatic collapse wobble!
            game_over = True
            high_score = max(high_score, caught)

    else:
        # During game over, let wobble continue to decay dramatically
        wobble_phase += 0.6
        wobble_offset = wobble_amplitude * math.sin(wobble_phase)
        wobble_amplitude *= 0.94
        if wobble_amplitude < 0.2:
            wobble_amplitude = 0.0
            wobble_offset = 0.0

    # Draw everything
    draw_stack()
    draw_balls()
    draw_platform()

    # UI
    score_text = font.render(f"Score: {caught}", True, WHITE)
    high_text = font.render(f"High: {high_score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(high_text, (10, 40))

    if game_over:
        go_text = big_font.render("GAME OVER", True, RED)
        restart_text = font.render("Press SPACE to Restart", True, WHITE)
        screen.blit(go_text, (WIDTH // 2 - 140, HEIGHT // 2 - 40))
        screen.blit(restart_text, (WIDTH // 2 - 160, HEIGHT // 2 + 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()