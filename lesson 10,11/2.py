import time
from time import sleep
import wrap, random, math
from wrap import sprite, actions, world, sprite_text
from random import randint, choice

world_x = 600
world_y = 600
world.create_world(world_x, world_y, 680, 30)

hero = sprite.add("battle_city_tanks", 450, 300, "tank_player_size1_green1")
mario = sprite.add("mario-1-small", 150, 150, costume="stand")


@wrap.on_key_down(wrap.K_UP, wrap.K_DOWN)
def action_costumes(pos_x, pos_y, key):
    if sprite.is_collide_point(hero, pos_x, pos_y):
        spr = hero
    elif sprite.is_collide_point(mario, pos_x, pos_y):
        spr = mario
    else:
        return

    if key == wrap.K_UP:
        sprite.set_costume_next(spr)
    else:
        sprite.set_costume_prev(spr)


@wrap.on_key_down(wrap.K_LEFT, wrap.K_RIGHT)
def rotate(pos_x, pos_y, key):
    if sprite.is_collide_point(hero, pos_x, pos_y):
        spr = hero
    elif sprite.is_collide_point(mario, pos_x, pos_y):
        spr = mario
    else:
        return

    a = sprite.get_angle(spr)
    if key == wrap.K_RIGHT:
        sprite.set_angle(spr, a + 15)
    else:
        sprite.set_angle(spr, a - 15)


@wrap.on_mouse_down(wrap.BUTTON_WHEELUP, wrap.BUTTON_WHEELDOWN)
def growing(pos_x, pos_y, button):
    if sprite.is_collide_point(hero, pos_x, pos_y):
        spr = hero
    elif sprite.is_collide_point(mario, pos_x, pos_y):
        spr = mario
    else:
        return


    if button == wrap.BUTTON_WHEELUP:
        sprite.set_size_percent_of(spr, 101)
    else:
        sprite.set_size_percent_of(spr, 99)
