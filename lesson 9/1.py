import time
from time import sleep
import wrap, random, math
from wrap import sprite,actions,world,sprite_text
from random import randint,choice

world_x = 500
world_y = 500
world.create_world(world_x, world_y,750,30)
world.set_back_color(27, 195, 255)

enemy=sprite.add("pacman",50,50,costume="enemy_blue_down1")
hero=sprite.add("pacman",200,50,costume="player2")


def say(player,text):
    x0= sprite.get_right(player)
    y0 = sprite.get_top(player)
    text0 = sprite.add_text(text, x0, y0 - 20,underline=True,font_size=30)
    actions.set_size_percent(text0, 200, 200, 300)
    actions.set_size_percent(text0, 100, 100, 300)
    sprite.hide(text0)

def act_hero(run_angle):
    say(hero,"ааааааа")
    actions.move_at_angle(hero,run_angle, 100, 1000)

def act_enemy():
    say(enemy,"держи его")
    x = sprite.get_x(hero)
    y = sprite.get_y(hero)
    actions.set_angle_to_point(enemy, x, y, 1000)
    actions.move_at_angle_dir(enemy, 100, 1000)


act_hero(100)
act_hero(200)
act_enemy()
