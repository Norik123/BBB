import time
from time import sleep
import wrap, random, math
from wrap import sprite,actions,world,sprite_text
from random import randint,choice

world_x = 600
world_y = 600
world.create_world(world_x, world_y,680,30)


hero1=sprite.add("battle_city_tanks", 500, 100, "tank_player_size1_green1")
base=sprite.add("battle_city_items",300,300,costume="base",visible=False)


@wrap.on_key_always(wrap.K_RIGHT,wrap.K_d)
def move_right(key):
    a=sprite.get_angle(hero1)
    sprite.set_angle(hero1,a+3)

@wrap.on_key_always(wrap.K_LEFT,wrap.K_a)
def move_left(key):
    a=sprite.get_angle(hero1)
    sprite.set_angle(hero1,a-3)

@wrap.on_key_always(wrap.K_UP,wrap.K_w)
def go(key):
    sprite.move_at_angle_dir(hero1,3)

@wrap.on_key_always(wrap.K_DOWN,wrap.K_s)
def back(key):
    sprite.move_at_angle_dir(hero1,-3)

@wrap.always(30)
def rotate():
    if sprite.is_visible(base):
        x=sprite.get_x(base)
        y=sprite.get_y(base)
        sprite.set_angle_to_point(hero1,x,y)
        sprite.move_at_angle_dir(hero1,3)


@wrap.on_mouse_down
def show(button):
    if button==wrap.BUTTON_LEFT:
        sprite.show(base)

    if button==wrap.BUTTON_RIGHT:
        sprite.show(base)
        angle=sprite.get_angle(base)
        sprite.set_angle(base,angle+45)

@wrap.on_mouse_up
def show():
    sprite.hide(base)


@wrap.on_mouse_move
def base_move(pos_x,pos_y):
    sprite.move_to(base,pos_x,pos_y)

@wrap.on_close
def game():
    pass