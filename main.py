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
        super().__init__(all_sprites)
        self.image = load_image("DeftSorceress.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = 0
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = 0
        if pygame.sprite.spritecollideany(self, trees):
            self.vx = 0
            self.vy = 0


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


class Thin_Tree(pygame.sprite.Sprite):
    def __init__(self, s1, s2, x, y):
        super().__init__(all_sprites)
        self.image = load_image("Thin Tree.png")
        self.image = pygame.transform.scale(self.image, (s1, s2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def level_1():
    bg = pygame.image.load('data/Grass.png')
    bg = pygame.transform.scale(bg, (800, 400))
    screen.blit(bg, (0, 0))
    player = Player(50, 50, 375, 300)
    tree = Tree(150, 150, 500, 150)
    tree3 = Tree(150, 150, 130, 140)
    tree2 = Tree(70, 70, 100, 300)
    tree4 = Thin_Tree(60, 100, 700, 100)
    tree5 = Thin_Tree(60, 100, 680, 170)
    tree6 = Thin_Tree(60, 100, 700, 300)
    all_sprites.add(tree)
    trees.add(tree)
    all_sprites.add(tree2)
    trees.add(tree2)
    all_sprites.add(tree3)
    trees.add(tree3)
    all_sprites.add(tree4)
    trees.add(tree4)
    return player


def main():
    game_state = "start_menu"
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
    player = level_1()

    def draw_start_menu():
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('My Game', True, (255, 255, 255))
        start_button = font.render('Start', True, (255, 255, 255))
        screen.blit(title,
                    (screen.get_width() / 2 - title.get_width() / 2, screen.get_height() / 2 - title.get_height() / 2))
        screen.blit(start_button, (
            screen.get_width() / 2 - start_button.get_width() / 2,
            screen.get_height() / 2 + start_button.get_height() / 2))
        pygame.display.update()

    running = True
    fps = 60
    clock = pygame.time.Clock()
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
        if game_state == "start_menu":
            draw_start_menu()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                player_x = 200
                player_y = 400
                game_state = "game"
                game_over = False

        if game_state == "game":
                bg = pygame.image.load('data/Grass.png')
                bg = pygame.transform.scale(bg, (800, 400))
                screen.blit(bg, (0, 0))
                all_sprites.draw(screen)
                all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
