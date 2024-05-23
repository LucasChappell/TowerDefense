import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, damage, range, fire_rate) -> None:
        pygame.sprite.Sprite.__init__(self) 
        self.damage = damage
        self.range = range
        self.fire_rate = fire_rate
        self.image = pygame.image.load('images/rifle.png')
        

class Sniper(Tower):
    def __init__(self, posx, posy) -> None:
        super().__init__(damage=25, range=100, fire_rate=1)
        self.image = pygame.image.load("images/sniper.png")
        self.rect = self.image.get_rect(center = (posx, posy))
        

class SMG(Tower):
    def __init__(self, posx, posy) -> None:
        super().__init__(damage=5, range=50, fire_rate=5)
        self.image = pygame.image.load("images/smg.png")
        self.rect = self.image.get_rect(center = (posx, posy))

class Rifle(Tower):
    def __init__(self, posx, posy) -> None:
        super().__init__(damage=10, range=75, fire_rate=3)
        self.image = pygame.image.load("images/rifle.png")
        self.rect = self.image.get_rect(center = (posx, posy))
class Base(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.health = 100  
        self.max_health = 100  

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            
    def get_pos_x(self):
        ans = self.rect.center[0]/20
        return int(ans)
    
    def get_pos_y(self):
        ans = self.rect.center[1]/20

        return int(ans)


    def draw_health_bar(self, surface):
        bar_length = 100
        bar_height = 10
        fill = (self.health / self.max_health) * bar_length
        outline_rect = pygame.Rect(self.rect.left, self.rect.top - 20, bar_length, bar_height)
        fill_rect = pygame.Rect(self.rect.left, self.rect.top - 20, fill, bar_height)
        pygame.draw.rect(surface, (255, 0, 0), fill_rect)
        pygame.draw.rect(surface, (0, 255, 0), outline_rect, 2)