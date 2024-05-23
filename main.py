import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from enemies import enemies, normal, fast, strong
from towers import Tower, Sniper, SMG, Rifle, Base
import math
pygame.init()

window_width = 1440
window_height = 960
hoverBlack = (0,0,0,130)
black = (0,0,0, 255)
clear = (0,0,0,100)
ENEMY_SPEED = 2
points = 100
grid_square_size = 20  
columnLen = 72
rowLen = 48
selected_tower = None
round = 0
tower_dragging = False
stopped = False
path_calculated = False
roundGoing = False


gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tabletop Tower Defense")
clearSurface = pygame.Surface((window_width, window_height))
clearSurface.set_alpha(60)


grid= []
gridColumns = []
grid_width = window_width/columnLen
grid_height = window_height/rowLen
for i in range(columnLen):
    gridColumns.append([])
for i in range(rowLen):
    grid.append(gridColumns)

clock = pygame.time.Clock()

spritesheet = pygame.image.load("images/rifle_shoot.pdf").convert_alpha()


sprite_rects = [
    pygame.Rect(0, 0, 128, 128), 

]

sprites = []
for rect in sprite_rects:
    sprite = spritesheet.subsurface(rect)
    sprites.append(sprite)


tower1_icon = pygame.image.load("images/rifle.png")
tower2_icon = pygame.image.load("images/smg.png")
tower3_icon = pygame.image.load("images/sniper.png")


def adjust_points(amount):
    global points
    points += amount

def check_round():
    pass


def place_tower(mouse_pos):
    global selected_tower
    if tower_dragging and 0 <= mouse_pos[0] < window_width and 0 <= mouse_pos[1] < window_height:
        grid_x = int(mouse_pos[0] // grid_width)
        grid_y = int(mouse_pos[1] // grid_height)
        if matrix[grid_y][grid_x] == 1:
            if selected_tower == "tower1":
                tower = Rifle((grid_x * grid_width) + 10, (grid_y * grid_height) + 10)
            elif selected_tower == "tower2":
                tower = SMG((grid_x * grid_width) + 10, (grid_y * grid_height) + 10)
            elif selected_tower == "tower3":
                tower = Sniper((grid_x * grid_width) + 10, (grid_y * grid_height) + 10)
            allies_group.add(tower)
            matrix[grid_y][grid_x] = 2

def recalculate_path_for_enemies():
  
    global path
    start = map.node(0, 0)
    end = map.node(base.get_pos_x(), base.get_pos_y())
    finder = AStarFinder()
    path, runs = finder.find_path(start, end, map)
    for enemy in normal_group:
        enemy.set_path(path)


matrix = [[1] * columnLen for _ in range(rowLen)]
obstacle_positions = []
start_num = 71
for i in range(50):
    
    obstacle_positions.append((start_num, 12))
    start_num -= 1
start_num = 71
for i in range(50):
    
    obstacle_positions.append((start_num, 36))
    start_num -= 1
for x, y in obstacle_positions:
    matrix[y][x] = 0


base_image = pygame.image.load("images/biggerbase.png").convert_alpha()
base = Base((1320, 480) , base_image)
allies_group = pygame.sprite.Group()
allies_group.add(base)

map = Grid(matrix = matrix)

start = map.node(0,0)

end = map.node(base.get_pos_x(), base.get_pos_y())

finder = AStarFinder()
path,runs = finder.find_path(start,end,map)
bg = pygame.image.load("images/gameBackground.jpg")

normal_image = pygame.image.load("images/normal.png").convert_alpha()
normal_group = pygame.sprite.Group()
normal_enemy = normal((0, 0), "Normal", normal_image, path)

normal_group.add(normal_enemy)





def draw_tower_icons():
    bg_rect = pygame.Rect(10, window_height - 155, 200, 150)
    pygame.draw.rect(gameDisplay, (50, 50, 100), bg_rect)
    font = pygame.font.Font(None, 24)
    

    tower1_label = font.render("Rifle - 100", True, (255, 255, 255))
    tower2_label = font.render("SMG - 150", True, (255, 255, 255))
    tower3_label = font.render("Sniper - 200", True,(255, 255, 255))
    
    gameDisplay.blit(tower1_icon, (20, window_height - 150))
    gameDisplay.blit(tower1_label, (60, window_height - 145))
    
    gameDisplay.blit(tower2_icon, (20, window_height - 90))
    gameDisplay.blit(tower2_label, (60, window_height - 85))

    gameDisplay.blit(tower3_icon, (20, window_height - 30))
    gameDisplay.blit(tower3_label,(60, window_height - 25))


tower1_icon_rect = tower1_icon.get_rect(topleft=(20, window_height - 150))
tower2_icon_rect = tower2_icon.get_rect(topleft=(20, window_height-90))
tower3_icon_rect = tower3_icon.get_rect(topleft=(20, window_height-30))



def draw_points():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Points: {points}", True, (100, 100, 255))
    text_rect = text.get_rect()
    text_rect.topright = (window_width - 20, 20) 
    gameDisplay.blit(text, text_rect)

play_image = pygame.image.load("images/play.png")
play_rect = play_image.get_rect(topleft = (window_width - 70, window_height - 50))

def draw_play():
     
    background_rect = pygame.Rect(window_width - 75, window_height - 55, 30, 30)
    pygame.draw.rect(gameDisplay, (50, 50, 100), background_rect)
    gameDisplay.blit(play_image, (window_width - 70, window_height - 50))   
   
def draw(pos):

    clearSurface.blit(bg, (0, 0))
    
    y = 0
    for row in range(rowLen):
        x = 0
        for column in range(columnLen):
            if matrix[row][column] == 0: 
                pygame.draw.rect(gameDisplay, black, [x, y, grid_width, grid_height], 0)
            elif x <= pos[0] < x + grid_width and y <= pos[1] < y + grid_height:
                pygame.draw.rect(clearSurface, hoverBlack, [x, y, grid_width, grid_height], 0)
            x += grid_width
        y += grid_height
    gameDisplay.blit(clearSurface, (0,0))
    normal_group.draw(gameDisplay)
    allies_group.draw(gameDisplay)
    base.draw_health_bar(gameDisplay)
    draw_tower_icons()
    draw_points()
    draw_play()
    draw_tower_drag()
    pygame.display.flip()
        
def handle_tower_selection(event):
    global selected_tower
    global tower_dragging 
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if tower1_icon_rect.collidepoint(mouse_pos):
            selected_tower = "tower1"
            tower_dragging = True  
        elif tower2_icon_rect.collidepoint(mouse_pos):
            selected_tower = "tower2"
            tower_dragging = True  
        if tower3_icon_rect.collidepoint(mouse_pos):
            selected_tower = "tower3"
            tower_dragging = True


def draw_tower_drag():
    mouse_pos = pygame.mouse.get_pos()
    if selected_tower and tower_dragging:
        if selected_tower == "tower1":
            tower_rect = tower1_icon.get_rect(topleft=mouse_pos)
        elif selected_tower == "tower2":
            tower_rect = tower2_icon.get_rect(topleft=mouse_pos)
        elif selected_tower == "tower3":
            tower_rect = tower3_icon.get_rect(topleft=mouse_pos)
        tower_rect.x -= tower_rect.x % grid_width
        tower_rect.y -= tower_rect.y % grid_height
        if selected_tower == "tower1":
            gameDisplay.blit(tower1_icon, tower_rect.topleft)
        elif selected_tower == "tower2":
            gameDisplay.blit(tower2_icon, tower_rect.topleft)
        elif selected_tower == "tower3":
            gameDisplay.blit(tower3_icon, tower_rect.topleft)
    

def handle_mouse_up(event):
   
    global selected_tower
    global tower_dragging
    if selected_tower and event.type == pygame.MOUSEBUTTONUP:
        mouse_pos = pygame.mouse.get_pos()
        if selected_tower == "tower1":
            if points < 100:
                tower_dragging = False
                return
        elif selected_tower == "tower2":
            if points < 150:
                tower_dragging = False
                return
        elif selected_tower == "tower3":
            if points < 200:
                tower_dragging = False
                return
        place_tower(mouse_pos)
        if selected_tower == "tower1":
            adjust_points(-100)
        elif selected_tower == "tower2":
            adjust_points(-150)
        elif selected_tower == "tower3":
            adjust_points(-200)
        selected_tower = None

def enemy_health():
    global roundGoing
    for enemy in normal_group:
        if enemy.health <= 0:
            enemy.kill()
    if len(normal_group) == 0:
        roundGoing = False
def move_enemies(path):
    for enemy in normal_group:
        if enemy.path_index < len(path):
            next_pos = path[enemy.path_index]
            next_pos_x = (next_pos.x * grid_width) + (grid_width / 2)
            next_pos_y = (next_pos.y * grid_height) + (grid_height / 2)
            dx = next_pos_x - enemy.rect.centerx
            dy = next_pos_y - enemy.rect.centery
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if matrix[int(next_pos.y)][int(next_pos.x)] != 1:
                start = map.node(int(enemy.rect.centerx // grid_width), int(enemy.rect.centery // grid_height))
                end = map.node(base.get_pos_x() // grid_square_size, base.get_pos_y() // grid_square_size)
                new_path, runs = finder.find_path(start, end, map)
                if len(new_path) > 0:
                    path[:] = new_path  
                    enemy.path_index = 0  

            if distance > ENEMY_SPEED:
                ratio = ENEMY_SPEED / distance
                dx *= ratio
                dy *= ratio
                enemy.rect.centerx += dx
                enemy.rect.centery += dy
            else:
                enemy.rect.centerx = next_pos_x
                enemy.rect.centery = next_pos_y
                enemy.path_index += 1
        else:
            start = map.node(int(enemy.rect.centerx // grid_width), int(enemy.rect.centery // grid_height))
            end = map.node(base.get_pos_x() // grid_square_size, base.get_pos_y() // grid_square_size)
            new_path, runs = finder.find_path(start, end, map)
            if len(new_path) > 0:
                enemy.path_index = 0  
                for enemy in normal_group:
                    enemy.set_path(new_path)

            

while not stopped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_tower_selection(event)
            mouse_pos = pygame.mouse.get_pos()
            if play_rect.collidepoint(mouse_pos):
                roundGoing = True
                round += 1
        elif event.type == pygame.MOUSEBUTTONUP:
            handle_mouse_up(event)
    if roundGoing:
            move_enemies(path)   
   
    pos = pygame.mouse.get_pos()
    gameDisplay.blit(bg, (0,0))
    draw(pos)
    clock.tick(60)
    pygame.display.update()
