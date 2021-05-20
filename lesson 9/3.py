import time
from time import sleep
import wrap, random, math
from wrap import sprite,actions,world,sprite_text
from random import randint,choice

world_x = 600
world_y = 600
world.create_world(world_x, world_y,680,30)

tank1 = sprite.add("battle_city_tanks", 500, 100, "tank_player_size1_green1", False)
tank2 = sprite.add("battle_city_tanks", 50, 500, "tank_player_size1_yellow1", False)

def appear(player):
    x=sprite.get_x(player)
    y=sprite.get_y(player)
    star=sprite.add("battle_city_items",x,y,costume="effect_appearance1")
    sleep(0.5)
    sprite.set_costume_next(star)
    sleep(0.5)
    sprite.set_costume_next(star)
    sleep(0.5)
    sprite.set_costume_next(star)
    sleep(0.5)
    sprite.hide(star)
    sprite.show(player)

def move_left(player,dist,speed):
    sprite.set_angle_modif(player,-90)
    actions.move_at_angle_dir(player,dist,speed)

def move_down(player,dist,speed):
    sprite.set_angle_modif(player,180)
    actions.move_at_angle_dir(player,dist,speed)

def move_right(player,dist,speed):
    sprite.set_angle_modif(player,90)
    actions.move_at_angle_dir(player,dist,speed)

def move_up(player,dist,speed):
    sprite.set_angle_modif(player,0)
    actions.move_at_angle_dir(player,dist,speed)

def fly_bullet(player,enemy,dist):
    x = sprite.get_x(player)
    y = sprite.get_y(player)
    x1 = sprite.get_x(enemy)
    y1 = sprite.get_y(enemy)
    bullet=sprite.add("battle_city_items",x, y, costume="bullet")
    sprite.set_angle_to_point(bullet,x1,y1)
    actions.move_at_angle_dir(bullet,dist,500)
    sleep(0.2)
    sprite.hide(bullet)

def explosion(player):
    sprite.hide(player)
    x = sprite.get_x(player)
    y = sprite.get_y(player)
    boom = sprite.add("battle_city_items", x, y, costume="effect_explosion1")
    sleep(0.5)
    sprite.set_costume_next(boom)
    sleep(0.5)
    sprite.set_costume_next(boom)
    sleep(0.5)
    sprite.hide(boom)



appear(tank1)
appear(tank2)

move_left(tank1, 200, 1000)
move_down(tank1, 100, 1000)

move_right(tank2, 250, 1000)
move_up(tank2, 50, 1000)

fly_bullet(tank2,tank1 ,200)
fly_bullet(tank1,tank2 ,250)

explosion(tank2)
appear(tank2)

fly_bullet(tank2,tank1, 250)
explosion(tank1)

move_left(tank2,150,1000)
appear(tank1)
move_right(tank1,150,1000)