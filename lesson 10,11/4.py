import time
from time import sleep
import wrap, random, math
from wrap import sprite, actions, world, sprite_text
from random import randint, choice

world_x = 600
world_y = 600
world.create_world(world_x, world_y, 680, 30)
world.set_back_color(44,211,255)

mario = sprite.add("mario-1-big", 300, 550, costume="stand")

@wrap.on_key_down(wrap.K_LEFT,wrap.K_RIGHT)
def move(key):
    if sprite.get_y(mario)==550:
        if key==wrap.K_LEFT:
            sprite.set_reverse_x(mario,True)

        if key==wrap.K_RIGHT:
            sprite.set_reverse_x(mario,False)
    else:
        return
    sprite.set_costume(mario, costume="walk1")
    actions.move_at_angle_dir(mario, 10,300)
    sprite.set_costume(mario, costume="walk2")
    actions.move_at_angle_dir(mario, 10,300)
    sprite.set_costume(mario, costume="walk3")
    actions.move_at_angle_dir(mario, 10, 300)
    sprite.set_costume(mario, costume="stand")

@wrap.on_key_down(wrap.K_SPACE,wrap.K_DOWN)
def action(key):
    if key==wrap.K_SPACE:
        sprite.set_costume(mario,costume="swim1")

    if key==wrap.K_DOWN:
        sprite.set_costume(mario,costume="stand")
        sprite.move_to(mario,300,550)
        if sprite.get_reverse_x(mario):
            sprite.set_angle(mario,-90)
        else:
            sprite.set_angle(mario,90)

@wrap.always
def fly(pos_x,pos_y):
    if sprite.get_costume(mario)=="swim1":
        a=sprite.calc_angle_by_point(mario,pos_x,pos_y)
        sprite.move_at_angle_point(mario,pos_x,pos_y,3)
        if sprite.get_reverse_x(mario):
            sprite.set_angle(mario,a-90)
        else:
            sprite.set_angle(mario,a+90)
