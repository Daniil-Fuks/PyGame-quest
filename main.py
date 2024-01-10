import os
import sys

import pygame

pygame.init()
pygame.display.set_caption("PyGame Quest")
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
trees = pygame.sprite.Group()
portal_1 = pygame.sprite.Group()
portal_2 = pygame.sprite.Group()
portal_3 = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
game_state = "start_menu"


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
        global game_state
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = 0
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = 0
        if pygame.sprite.spritecollideany(self, trees):
            self.vx = 0
            self.vy = 0
        if pygame.sprite.spritecollideany(self, portal_1):
            self.select_level_1_1 = True
            game_state = 'level_1_3'
        if pygame.sprite.spritecollideany(self, portal_2):
            self.select_level_1_2 = True
            game_state = 'level_1_3'
        if pygame.sprite.spritecollideany(self, portal_3):
            self.select_level_1_3 = True
            game_state = 'level_1_3'


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


current_level = None


def switch_level(level):
    global current_level
    current_level = level


def level_1():
    running = True
    fps = 60
    clock = pygame.time.Clock()
    player = Player(50, 50, 375, 300)
    player_sprite.add(player)
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
    tree = Tree(150, 150, 590, 190)
    tree2 = Tree(150, 150, 70, 230)
    Bush(35, 35, 50, 200)
    Bush(60, 60, 230, 310)
    Bush(50, 50, 200, 200)
    Bush(50, 50, 520, 320)
    Bush(50, 50, 560, 280)
    Bush(50, 50, 700, 320)
    Bush(35, 35, 745, 190)
    portal = Portal(100, 100, 360, -10)
    portal2 = Portal(100, 100, 700, 60)
    portal3 = Portal(100, 100, 0, 60)
    portal_1.add(portal)
    portal_2.add(portal2)
    portal_3.add(portal3)
    all_sprites.add(tree)
    trees.add(tree)
    all_sprites.add(tree2)
    trees.add(tree2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.vy = -5
                if event.key == pygame.K_a:
                    player.vx = -5
                if event.key == pygame.K_s:
                    player.vy = 5
                if event.key == pygame.K_d:
                    player.vx = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.vy = 0
                if event.key == pygame.K_a:
                    player.vx = 0
                if event.key == pygame.K_s:
                    player.vy = 0
                if event.key == pygame.K_d:
                    player.vx = 0
        bg = pygame.image.load('data/Grass.png')
        bg = pygame.transform.scale(bg, (800, 400))
        screen.blit(bg, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        player_sprite.draw(screen)
        player_sprite.update()
        clock.tick(fps)
        pygame.display.flip()


def start_game():
    def draw_start_menu():
        screen.fill((255, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('My Game', True, (255, 255, 255))
        start_button = font.render('Start', True, (255, 255, 255))
        screen.blit(title,
                    (screen.get_width() / 2 - title.get_width() / 2, screen.get_height() / 2 - title.get_height() / 2))
        screen.blit(start_button, (
            screen.get_width() / 2 - start_button.get_width() / 2,
            screen.get_height() / 2 + start_button.get_height() / 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            switch_level(level_1())


if __name__ == "__main__":
    sys.exit(start_game())
