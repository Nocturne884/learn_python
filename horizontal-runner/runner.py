import sys
import pygame


WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
FPS = 60


def handle_input(x, y, speed):
    """Return updated (x, y) based on arrow key input."""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    return x, y


def clamp_position(x, y):
    """Keep the player rectangle fully on screen."""
    x = max(0, min(x, WIDTH - PLAYER_SIZE))
    y = max(0, min(y, HEIGHT - PLAYER_SIZE))
    return x, y


def draw(screen, x, y):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (int(x), int(y), PLAYER_SIZE, PLAYER_SIZE))
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    # Starting position (centered)
    player_x = (WIDTH - PLAYER_SIZE) / 2
    player_y = (HEIGHT - PLAYER_SIZE) / 2
    player_speed = 5  # pixels per frame

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player_x, player_y = handle_input(player_x, player_y, player_speed)
        player_x, player_y = clamp_position(player_x, player_y)
        draw(screen, player_x, player_y)
        clock.tick(FPS)

    pygame.quit()
    sys.exit(0)


if __name__ == "__main__":
    main()
