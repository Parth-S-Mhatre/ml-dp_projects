import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame from CMD")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game loop
clock = pygame.time.Clock()
running = True

print("Pygame window opened! Press ESC or close window to exit.")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Fill screen with white
    screen.fill(WHITE)
    
    # Draw a red circle that follows mouse
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, RED, mouse_pos, 20)
    
    # Draw a blue rectangle in center
    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100))
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit
pygame.quit()
sys.exit()