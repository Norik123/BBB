import time
from time import sleep
import wrap, random, math
from wrap import sprite, actions, world, sprite_text
from random import randint, choice

world_x = 600
world_y = 600
world.create_world(world_x, world_y, 680, 30)

hero = sprite.add("battle_city_tanks", 100, 100, "tank_player_size1_green1")
target = sprite.add("pacman", 10, 10, costume="player2", visible=False)
sprite.set_angle(target, 0)


@wrap.always(10000000)
def show():
    x = randint(1, 600)
    y = randint(1, 600)
    sprite.move_to(hero, x, y)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def change_costume(pos_x, pos_y, button):
    if sprite.is_collide_point(hero, pos_x, pos_y) or \
            sprite.is_collide_sprite(hero, target) and sprite.is_visible(target):
        if button == wrap.BUTTON_LEFT:
            sprite.set_costume_next(hero)


@wrap.on_mouse_move
def action(pos_x, pos_y):
    sprite.move_to(target, pos_x, pos_y)


@wrap.on_key_up(wrap.K_UP)
def sniper(key):
    if key == wrap.K_UP:
        x = sprite.get_width_percent(target)

        if not sprite.is_visible(target):
            sprite.set_width_percent(target, 50)
            sprite.set_height_percent(target, 50)
            sprite.show(target)


        elif x == 50:
            sprite.set_height_percent(target, 100)
            sprite.set_width_percent(target, 100)

        elif x == 100:
            sprite.set_height_percent(target, 150)
            sprite.set_width_percent(target, 150)

        elif x == 150:
            sprite.hide(target)

