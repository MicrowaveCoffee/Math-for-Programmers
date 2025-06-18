import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))  # No OPENGL flag
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 128, 255))  # Blue screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()