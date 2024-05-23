import pygame
import math


class enemies(pygame.sprite.Sprite):
    def __init__(self, pos, type, image, path) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.type = type
        self.image = image
        self.rect = self.image.get_rect(center = pos)
        
        self.path_index = 0
        self.path = path

    def update(self, grid_width, grid_height, ENEMY_SPEED):
        if self.path_index < len(self.path):
            next_node = self.path[self.path_index]
            # Get the position of the next node
            next_pos_x = (next_node.x * grid_width) + (grid_width / 2)
            next_pos_y = (next_node.y * grid_height) + (grid_height / 2)
            # Calculate movement vector
            dx = next_pos_x - self.rect.centerx
            dy = next_pos_y - self.rect.centery
            # Calculate distance to next position
            distance = math.sqrt(dx ** 2 + dy ** 2)
            # Move the enemy
            if distance > ENEMY_SPEED:
                ratio = ENEMY_SPEED / distance
                dx *= ratio
                dy *= ratio
                self.rect.centerx += dx
                self.rect.centery += dy
            else:
                self.rect.centerx = next_pos_x
                self.rect.centery = next_pos_y
                self.path_index += 1

    def set_path(self, path):
        self.path = path
        self.path_index = 0

    def get_pos_x(self):
        ans = self.rect.center[0]/20
        return int(ans)
    
    def get_pos_y(self):
        ans = self.rect.center[1]/20
        return int(ans)
    

class normal(enemies):
    def __init__(self, pos, type, image, path):
        super().__init__(pos, type, image, path)
        self.type = "Normal"
        
        

class fast(enemies):
    pass

class strong(enemies):
    pass
