import sys

import pygame

from sprites import Player, FirstNpc, Border, Tree, Bush, Portal, Boss, Stick, Sword, FireBall
from sprites import player_sprite, trees, npc_group, portal_1, portal_2, portal_3, all_sprites, sword_group, \
    stick_group, damage_group

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Игра-квест")
s1 = pygame.mixer.Sound("data/Sakura-Girl-Peach-chosic.com_.mp3")
s2 = pygame.mixer.Sound("data/Boss fight.mp3")
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
current_level = "start_menu"


def switch_level(level):
    global current_level
    current_level = level


def level_1():
    s1.play()
    running = True
    fps = 60
    clock = pygame.time.Clock()
    player = Player(screen, 35, 50, 375, 300)
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
                    player.left = False
                    player.right = True
                if event.key == pygame.K_a:
                    player.vx = -5
                    player.left = True
                    player.right = False
                if event.key == pygame.K_s:
                    player.vy = 5
                    player.left = True
                    player.right = False
                if event.key == pygame.K_d:
                    player.vx = 5
                    player.left = False
                    player.right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.vy = 0
                    player.left = False
                    player.right = False
                if event.key == pygame.K_a:
                    player.vx = 0
                    player.left = False
                    player.right = False
                if event.key == pygame.K_s:
                    player.vy = 0
                    player.left = False
                    player.right = False
                if event.key == pygame.K_d:
                    player.vx = 0
                    player.left = False
                    player.right = False
            if player.select_level_1_1:
                s1.stop()
                s2.play(-1)
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
    timer = 0
    bg = pygame.image.load('data/background 2.png')
    all_sprites.draw(screen)
    weapon = None
    running = True
    fps = 60
    clock = pygame.time.Clock()
    player = Player(screen, 35, 50, 375, 300)
    player_sprite.add(player)
    all_sprites.add(player)
    main_boss = Boss(screen, 250, 250, 600, 50)
    npc_group.add(main_boss)
    all_sprites.add(main_boss)
    sword = Sword(70, 70, 50, 100)
    all_sprites.add(sword)
    sword_group.add(sword)
    stick = Stick(50, 50, 50, 300)
    stick_group.add(stick)
    all_sprites.add(stick)
    sword_group.add(stick)
    f_1 = FireBall(30, 40, 700, -50)
    f_2 = FireBall(30, 40, 550, -150)
    f_3 = FireBall(30, 40, 400, -250)
    f_4 = FireBall(30, 40, 350, -350)
    f_5 = FireBall(30, 40, 200, -450)
    f_6 = FireBall(30, 40, 50, -550)
    all_sprites.add(f_1)
    damage_group.add(f_1)
    all_sprites.add(f_2)
    damage_group.add(f_2)
    all_sprites.add(f_3)
    damage_group.add(f_3)
    all_sprites.add(f_4)
    damage_group.add(f_4)
    all_sprites.add(f_5)
    damage_group.add(f_5)
    all_sprites.add(f_6)
    damage_group.add(f_6)

    def boss_fight():
        pygame.draw.rect(screen, (255, 0, 0), (100, 10, main_boss.hp, 30))
        if timer > 175:
            fire_attack_1()

    def fire_attack_1():
        f_1.rect = f_1.rect.move(0, 3)
        f_2.rect = f_2.rect.move(0, 3)
        f_3.rect = f_3.rect.move(0, 3)
        f_4.rect = f_4.rect.move(0, 3)
        f_5.rect = f_5.rect.move(0, 3)
        f_6.rect = f_6.rect.move(0, 3)

    while running:
        timer += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(player.hp)
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.vy = -5
                    player.left = False
                    player.right = True
                if event.key == pygame.K_a:
                    player.vx = -5
                    player.left = True
                    player.right = False
                if event.key == pygame.K_s:
                    player.vy = 5
                    player.left = True
                    player.right = False
                if event.key == pygame.K_d:
                    player.vx = 5
                    player.left = False
                    player.right = True
                if event.key == pygame.K_SPACE and pygame.sprite.spritecollideany(player, npc_group):
                    if weapon == "stick" and main_boss.hp > 0:
                        main_boss.hp -= 50
                    elif weapon == 'sword' and main_boss.hp > 0:
                        main_boss.hp -= 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.vy = 0
                    player.left = False
                    player.right = False
                if event.key == pygame.K_a:
                    player.vx = 0
                    player.left = False
                    player.right = False
                if event.key == pygame.K_s:
                    player.vy = 0
                    player.left = False
                    player.right = False
                if event.key == pygame.K_d:
                    player.vx = 0
                    player.left = False
                    player.right = False

        def kill_sprites():
            player.kill()
            sword.kill()
            stick.kill()
            main_boss.kill()
            f_1.kill()
            f_2.kill()
            f_3.kill()
            f_4.kill()
            f_5.kill()
            f_6.kill()

        def kill_weapon():
            sword.kill()
            stick.kill()

        bg = pygame.transform.scale(bg, (800, 400))
        screen.blit(bg, (0, 0))
        if player.select_sword:
            weapon = "sword"
            boss_fight()
            kill_weapon()
        if player.select_stick:
            weapon = "stick"
            boss_fight()
            kill_weapon()
        if player.hp <= 0:
            screen.fill((255, 0, 0))
            kill_sprites()
            running = False
            end_screen("lose")
        if main_boss.hp <= 0:
            screen.fill((255, 0, 0))
            kill_sprites()
            running = False
            end_screen("win")
        main_boss.animation()
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


def end_screen(game_state):
    running = True
    font = pygame.font.SysFont('Calibri', 22)
    if game_state == "win":
        s2.stop()
        while running:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        switch_level(level_1())
                        running = False
            screen.fill((0, 0, 0))
            title = font.render('Поздравляем, вы выиграли!', True, (255, 255, 255))
            start_button = font.render('Нажите пробел, чтобы начать игру заново', True, (255, 255, 255))
            screen.blit(title,
                        (screen.get_width() / 2 - title.get_width() / 2,
                         screen.get_height() / 2 - title.get_height() / 2))
            screen.blit(start_button, (
                screen.get_width() / 2 - start_button.get_width() / 2,
                screen.get_height() / 2 + start_button.get_height() / 2))
            pygame.display.update()
    if game_state == "lose":
        s2.stop()
        while running:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        switch_level(level_1())
                        running = False
            screen.fill((0, 0, 0))
            title = font.render('К сожалению, вы Проиграли:(', True, (255, 255, 255))
            start_button = font.render('Нажите пробел, чтобы начать игру заново', True, (255, 255, 255))
            screen.blit(title,
                        (screen.get_width() / 2 - title.get_width() / 2,
                         screen.get_height() / 2 - title.get_height() / 2))
            screen.blit(start_button, (
                screen.get_width() / 2 - start_button.get_width() / 2,
                screen.get_height() / 2 + start_button.get_height() / 2))
            pygame.display.update()


if __name__ == "__main__":
    sys.exit(start_game())
