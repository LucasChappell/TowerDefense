import pygame
from enemies import enemies, normal, fast, strong
from towers import towers, sniper, smg, rifle
pygame.init()

window_width = 1440
window_height = 960
black = (0,0,0)




gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tabletop Tower Defense")

columnLen = 72
rowLen = 48
grid= []
gridColumns = []
grid_width = window_width/columnLen
grid_height = window_height/rowLen
for i in range(columnLen):
    gridColumns.append([])
for i in range(rowLen):
    grid.append(gridColumns)

clock = pygame.time.Clock()

bg = pygame.image.load("images/gameBackground.jpg")



def draw():
    y = 0
    
    for row in range(rowLen):
        x = 0
        for column in range(columnLen):
            pygame.draw.rect(gameDisplay, black, [x, y, grid_width, grid_height], 1)
            x += grid_width
            
        y += grid_height
        


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
    

    