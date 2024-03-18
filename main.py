import pygame
pygame.init()

window_width = 1440
window_height = 960

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tabletop Tower Defense")

clock = pygame.time.Clock()

bg = pygame.image.load("images/gameBackground.jpg")

def draw():
    pass


stopped = False
while not stopped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
        
        print(event)
    
    gameDisplay.blit(bg, (0,0))

    pygame.display.update()
    clock.tick(60)

    