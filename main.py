import os
import sys

import pygame

pygame.init()
Moving_Up = False
Moving_Down = False
Moving_Right = False
Moving_Left = False
pygame.display.set_caption("PyGame Quest")
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


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
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = load_image("DeftSorceress.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 100
        self.vx = 0
        self.vy = 0

    def move(self, direction):
        if direction == "w":
            self.vy = -5
        if direction == "s":
            self.vy = 5
        if direction == "a":
            self.vx = -5
        if direction == "d":
            self.vx = 5

    def update(self):
        self.rect = self.rect.move(self.vx, 0)
        self.rect = self.rect.move(0, self.vy)


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


def main():
    global Moving_Up, Moving_Left, Moving_Right, Moving_Down
    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)
    player = Player(20, 100, 100)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill((255, 255, 255))
        event_key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.move('w')
                if event.key == pygame.K_a:
                    player.move('a')
                if event.key == pygame.K_s:
                    player.move('s')
                if event.key == pygame.K_d:
                    player.move('d')
            if event.type == pygame.KEYUP:
                player.vx = 0
                player.vy = 0

        all_sprites.draw(screen)
        all_sprites.update()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
