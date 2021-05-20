import time
from time import sleep
import wrap, random, math
from wrap import sprite, actions, world, sprite_text
from random import randint, choice

world_x = 600
world_y = 600
world.create_world(world_x, world_y, 650, 30)

tank1 = sprite.add("battle_city_tanks", 500, 100, "tank_player_size1_green1", False)
tank2 = sprite.add("battle_city_tanks", 50, 500, "tank_player_size1_yellow1", False)


def appear(player):
    x = sprite.get_x(player)
    y = sprite.get_y(player)
    star = sprite.add("battle_city_items", x, y, costume="effect_appearance1")
    sleep(0.5)
    sprite.set_costume_next(star)
    sleep(0.5)
    sprite.set_costume_next(star)
    sleep(0.5)
    sprite.set_costume_next(star)
    sleep(0.5)
    sprite.hide(star)
    sprite.show(player)


def move_left(player, dist, speed):
    sprite.set_angle_modif(player, -90)
    speed1 = dist / speed * 1000
    maxdist = sprite.get_left(player)
    if dist > maxdist:
        dist = maxdist
    actions.move_at_angle_dir(player, dist, speed1)


def move_down(player, dist, speed):
    sprite.set_angle_modif(player, 180)
    speed1 = dist / speed * 1000
    actions.move_at_angle_dir(player, dist, speed1)


def move_right(player, dist, speed):
    sprite.set_angle_modif(player, 90)
    speed1 = dist / speed * 1000
    r = sprite.get_right(player)
    way = world_x - r
    if dist > way:
        dist = way
    actions.move_at_angle_dir(player, dist, speed1)


def move_up(player, dist, speed):
    sprite.set_angle_modif(player, 0)
    speed1 = dist / speed * 1000
    actions.move_at_angle_dir(player, dist, speed1)


appear(tank1)
appear(tank2)

move_left(tank1, 1000, 5000)
move_down(tank1, 100, 100)

move_right(tank2, 1000, 5000)
move_up(tank2, 50, 100)
