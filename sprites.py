import os
import sys

import pygame

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
trees = pygame.sprite.Group()
portal_1 = pygame.sprite.Group()
portal_2 = pygame.sprite.Group()
portal_3 = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
stick_group = pygame.sprite.Group()
sword_group = pygame.sprite.Group()
npc_group = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(player_sprite)
        self.image = load_image("DeftSorceress.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.select_level_1_3 = False
        self.select_level_1_2 = False
        self.select_level_1_1 = False

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = 0
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = 0
        if pygame.sprite.spritecollideany(self, trees) or pygame.sprite.spritecollideany(self, npc_group):
            self.vx = 0
            self.vy = 0
        if pygame.sprite.spritecollideany(self, portal_1):
            self.select_level_1_1 = True
        if pygame.sprite.spritecollideany(self, portal_2):
            self.select_level_1_2 = True
        if pygame.sprite.spritecollideany(self, portal_3):
            self.select_level_1_3 = True


class FirstNpc(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(player_sprite)
        self.image = load_image("First npc.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Boss(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(player_sprite)
        self.image = load_image("Boss.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Sword(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(player_sprite)
        self.image = load_image("Sword.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Stick(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(player_sprite)
        self.image = load_image("Stick.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Tree(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(all_sprites)
        self.image = load_image("Big Green Tree.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Bush(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(all_sprites)
        self.image = load_image("bush.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Portal(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(all_sprites)
        self.image = load_image("portal.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y