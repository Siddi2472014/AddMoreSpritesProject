import pygame

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Jump Game")

clock = pygame.time.Clock()
FPS = 60

# Load images
background_img = pygame.image.load("background.png").convert()
mario_img = pygame.image.load("mario.png").convert_alpha()
pipe_img = pygame.image.load("pipe.png").convert_alpha()

# Resize images
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
mario_img = pygame.transform.scale(mario_img, (60, 70))
pipe_img = pygame.transform.scale(pipe_img, (80, 120))

# Ground level
ground_y = HEIGHT - 70

# Mario settings
mario_width = 60
mario_height = 70
mario_x = 100
mario_y = ground_y - mario_height
velocity_y = 0
gravity = 0.8
jump_power =-20
on_ground = True
# Pipes on ground only
pipes = [pygame.Rect(500, ground_y - 120, 80, 120),pygame.Rect(850, ground_y - 120, 80, 120),pygame.Rect(1200, ground_y - 120, 80, 120),]
pipe_speed = 5
# Fonts
font = pygame.font.SysFont(None, 45)
big_font = pygame.font.SysFont(None, 90)
# Score
score = 0
# Game over
game_over = False
# Main loop
running = True
while running:
    clock.tick(FPS)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground:
                    velocity_y = jump_power
                    on_ground = False

    # Game logic
    if not game_over:

        # Gravity
        velocity_y += gravity
        mario_y += velocity_y
        # Ground collision
        if mario_y >= ground_y - mario_height:
            mario_y = ground_y - mario_height
            velocity_y = 0
            on_ground = True
        # Mario hitbox
        mario_rect = pygame.Rect(mario_x + 10,mario_y + 5,40,65)
        # Move pipes
        for pipe in pipes:
            pipe.x -= pipe_speed
            # Respawn pipes
            if pipe.right < 0:
                pipe.x = WIDTH + 400
                score += 1
            # Normal collision
            if mario_rect.colliderect(pipe):
                game_over = True
    # Draw background image
    screen.blit(background_img, (0, 0))
    # Draw pipes
    for pipe in pipes:
        screen.blit(pipe_img, (pipe.x, pipe.y))
    # Draw Mario
    screen.blit(mario_img, (mario_x, mario_y))
    # Score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    # Game Over text
    if game_over:
        game_over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text,(WIDTH // 2 - game_over_text.get_width() // 2,HEIGHT // 2 - 50))
    pygame.display.update()
pygame.quit()
# the hitboxes of mario were really weird so i clearly set a particular hitbox for mario and even then the hitboxes were weird so in the end i was forced to increase jump power instead of actually fixing the hitboxes, even after that too the hitboxes are weird but the pipes are jumpable, so in a way the game works, so say ur like 5-15 pixels on top of the pipes or near the pipes, it still counts as a hit, I really can't fix it, you can see for yourself, and the reason the first time I createed the same space invader game is because that's what was given in the instruction.