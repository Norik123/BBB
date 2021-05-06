import time
import wrap, random, math
from wrap import sprite,actions,world,sprite_text
from random import randint
from time import sleep

world_x = 500
world_y = 700
world.create_world(world_x, world_y,750,10)
world.set_back_color(27, 195, 255)

start_time=time.time()
a=sprite.add_text("ф",world_x/2,world_y/2)
mario=sprite.add("mario-1-small",480,30,costume="stand")
sprite.set_reverse_x(mario,True)

mario_speed=3

while True:
    sprite.move(mario,0,mario_speed)
    bot=sprite.get_bottom(mario)
    if bot>=world_y:
        sprite.move_bottom_to(mario,world_y)
        mario_speed=-3

    top=sprite.get_top(mario)
    if top<=0:
        sprite.move_top_to(mario,0)
        mario_speed=3

    middle_time=time.time()
    watch=int(middle_time-start_time)
    sprite_text.set_text(a,str(watch))
