import pygame
pygame.init()

window_width = 1440
window_height = 960
black = (0,0,0)

gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tabletop Tower Defense")

clock = pygame.time.Clock()

bg = pygame.image.load("images/gameBackground.jpg")

def draw():
    pygame.draw.rect(gameDisplay, black, [450, 200, 1200, 10], 0)


stopped = False
while not stopped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
        
        print(event)
    
    gameDisplay.blit(bg, (0,0))
    draw()
    pygame.display.update()
    clock.tick(60)

    