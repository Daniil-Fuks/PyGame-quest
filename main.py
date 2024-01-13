import sys

import pygame

from sprites import Player, FirstNpc, Border, Tree, Bush, Portal, Boss, Stick, Sword
from sprites import player_sprite, trees, npc_group, portal_1, portal_2, portal_3, all_sprites, sword_group, stick_group

pygame.init()
pygame.display.set_caption("PyGame Quest")
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
current_level = "start_menu"


def switch_level(level):
    global current_level
    current_level = level


def level_1():
    running = True
    fps = 60
    clock = pygame.time.Clock()
    player = Player(35, 50, 375, 300)
    player_sprite.add(player)
    npc_1 = FirstNpc(50, 50, 500, 200)
    Border(0, 0, width, 0)
    Border(0, height, width, height)
    Border(0, 0, 0, height)
    Border(width, 0, width, height)
    tree = Tree(150, 150, 590, 190)
    tree2 = Tree(150, 150, 70, 230)
    b1 = Bush(35, 35, 50, 200)
    b2 = Bush(60, 60, 230, 310)
    b3 = Bush(50, 50, 200, 200)
    b4 = Bush(50, 50, 520, 320)
    b5 = Bush(50, 50, 560, 280)
    b6 = Bush(50, 50, 700, 320)
    b7 = Bush(35, 35, 745, 190)
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
    all_sprites.add(npc_1)
    npc_group.add(npc_1)

    def kill_all():
        player.kill()
        tree.kill()
        tree2.kill()
        portal.kill()
        portal2.kill()
        portal3.kill()
        b1.kill()
        b2.kill()
        b3.kill()
        b4.kill()
        b5.kill()
        b6.kill()
        b7.kill()
        npc_1.kill()

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
            if player.select_level_1_1:
                running = False
                screen.fill((255, 0, 0))
                kill_all()
                level_1_1()
                switch_level("lvl2")
        if not player.select_level_1_1:
            bg = pygame.image.load('data/Grass.png')
            bg = pygame.transform.scale(bg, (800, 400))
            screen.blit(bg, (0, 0))
            player_sprite.draw(screen)
            player_sprite.update()
            all_sprites.draw(screen)
            all_sprites.update()
            clock.tick(fps)
            pygame.display.flip()


def level_1_1():
    bg = pygame.image.load('data/Grass.png')
    all_sprites.draw(screen)
    running = True
    fps = 60
    clock = pygame.time.Clock()
    player = Player(35, 50, 375, 300)
    player_sprite.add(player)
    all_sprites.add(player)
    main_boss = Boss(250, 250, 550, 50)
    all_sprites.add(main_boss)
    npc_group.add(main_boss)
    sword = Sword(70, 70, 50, 100)
    all_sprites.add(sword)
    sword_group.add(sword)
    stick = Stick(50, 50, 50, 300)
    stick_group.add(stick)
    all_sprites.add(stick)
    sword_group.add(stick)
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
            if player.select_level_1_1:
                switch_level(None)
                running = False
        bg = pygame.transform.scale(bg, (800, 400))
        screen.blit(bg, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        clock.tick(fps)
        pygame.display.flip()


def start_game():
    global current_level

    def draw_start_menu():
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('Calibri', 40)
        title = font.render('Игра-квест', True, (255, 255, 255))
        start_button = font.render('Нажите пробел, чтобы начать игру', True, (255, 255, 255))
        screen.blit(title,
                    (screen.get_width() / 2 - title.get_width() / 2, screen.get_height() / 2 - title.get_height() / 2))
        screen.blit(start_button, (
            screen.get_width() / 2 - start_button.get_width() / 2,
            screen.get_height() / 2 + start_button.get_height() / 2))
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if current_level == "start_menu":
            draw_start_menu()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                switch_level(level_1())
                running = False


if __name__ == "__main__":
    sys.exit(start_game())
