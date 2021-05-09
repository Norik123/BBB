import time
from time import sleep
import wrap, random, math
from wrap import sprite,actions,world,sprite_text
from random import randint,choice

world_x = 500
world_y = 650
world.create_world(world_x, world_y,750,10)
world.set_back_color(27, 195, 255)

start_time=time.time()
a=sprite.add_text("ф",world_x/2,world_y/2)
mario=sprite.add("mario-1-small",480,30,costume="stand")
sprite.set_reverse_x(mario,True)
mario_speed=randint(5,23)

enemy=sprite.add("mario-enemies",20,30,costume="turtle_stand")
sprite.set_reverse_x(enemy,True)
enemy_speed=randint(5,12)
target=0

while True:
    sprite.move(mario,0,mario_speed)
    bot=sprite.get_bottom(mario)
    sprite.move(enemy, 0, enemy_speed)
    bot1 = sprite.get_bottom(enemy)

    if bot>=world_y:
        sprite.move_bottom_to(mario,world_y)
        mario_speed=-randint(5,23)
    if bot1>=world_y:
        sprite.move_bottom_to(enemy,world_y)
        enemy_speed=-randint(5,12)

    top=sprite.get_top(mario)
    top1 = sprite.get_top(enemy)

    if top<=0:
        sprite.move_top_to(mario,0)
        mario_speed=randint(5,23)
    if top1<=0:
        sprite.move_top_to(enemy,0)
        enemy_speed=randint(5,12)

    target=target+1
    middle_time=time.time()
    watch=int(middle_time-start_time)
    sprite_text.set_text(a,str(watch))

    if target==15:
        target=0
        hammerx=sprite.get_right(enemy)
        hammery=sprite.get_top(enemy)
        mariox=sprite.get_x(mario)
        marioy=sprite.get_y(mario)


        hammer=sprite.add("mario-enemies",hammerx,hammery,costume="turtle_hammer")
        actions.move_to(hammer,mariox/3,marioy,1000)
        sprite.set_angle_modif(hammer,120)

        actions.move_to(hammer,(mariox/3)*2,marioy,1000)
        sprite.set_angle_modif(hammer,240)

        actions.move_to(hammer,mariox,marioy,1000)
        sprite.set_angle_modif(hammer, 360)

        collide=sprite.is_collide_sprite(hammer,mario)

        if collide==True:
            break

actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,120)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,240)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,360)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,120)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,240)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,360)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,120)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,240)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,360)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,120)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,240)
actions.move_at_angle(mario,180,50,500)
sprite.set_angle_modif(mario,360)