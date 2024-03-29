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
damage_group = pygame.sprite.Group()


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


def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, s1, s2, x, y):
        super().__init__(player_sprite)
        self.screen = screen
        self.image = load_image("player/1.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.hp = 100
        self.select_level_1_3 = False
        self.select_level_1_2 = False
        self.select_level_1_1 = False
        self.select_sword = False
        self.select_stick = False

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = 0
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = 0
        if pygame.sprite.spritecollideany(self, trees) or pygame.sprite.spritecollideany(self, npc_group):
            self.vx = 0
            self.vy = 0
        if pygame.sprite.spritecollideany(self, damage_group):
            self.hp -= 100
        if pygame.sprite.spritecollideany(self, portal_1):
            self.select_level_1_1 = True
        if pygame.sprite.spritecollideany(self, portal_2):
            self.select_level_1_2 = True
        if pygame.sprite.spritecollideany(self, portal_3):
            self.select_level_1_3 = True
        if pygame.sprite.spritecollideany(self, sword_group):
            self.select_sword = True
            self.select_stick = False
        if pygame.sprite.spritecollideany(self, stick_group):
            self.select_stick = True
            self.select_sword = False


class FirstNpc(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(player_sprite)
        self.image = load_image("First npc.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Boss(pygame.sprite.Sprite):
    def __init__(self, screen, s1, s2, x, y):
        super().__init__(npc_group)
        self.image = load_image('Boss/03_demon_cleave/demon_cleave_1.png')
        self.screen = screen
        self.animation_count = 0
        self.boss_sprite = [
            load_image('Boss/03_demon_cleave/demon_cleave_1.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_2.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_3.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_4.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_5.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_6.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_7.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_8.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_9.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_10.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_11.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_12.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_13.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_14.png'),
            load_image('Boss/03_demon_cleave/demon_cleave_15.png')
        ]
        self.rect = self.image.get_rect()
        self.hp = 600
        self.rect.x = x
        self.rect.y = y

    def animation(self):
        self.image.set_alpha(0)
        if self.animation_count + 1 >= 60:
            self.animation_count = 0
        self.screen.blit(self.boss_sprite[self.animation_count // 8], (self.rect.x, self.rect.y))
        self.animation_count += 1


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


class FireBall(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(all_sprites)
        self.image = load_image("Fire ball.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class FireBallLeft(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(all_sprites)
        self.image = load_image("Fire ball.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.image, self.rect = rot_center(self.image, 90, x, y)
        self.rect.x = x
        self.rect.y = y