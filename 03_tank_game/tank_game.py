x = 100
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{x}, {y}'

import pgzrun
import random

width=800
height= 6900

tank = Actor('tank_blue')
tank.y = 575
tank.x = 400
tank.angle = 90

background = Actor('grass')

walls = []
# for x in range(16):
#     for y in range(20):
#         wall = Actor('wall')
#         wall.x = x * 50 + 25
#         wall.y = y * 50 + 25
#         walls.append(wall)
# print(walls)
for x in range(16):
    for y in range(10):
        if random.randint(0, 100) < 50:
            wall = Actor('wall')
            wall.x = x * 50 + 25
            wall.y = y * 50 + 25 + 50
            walls.append(wall)

bullets = []
bullet_holdoff = 0


def update():
    global bullet_holdoff
    # tank.angle += 1
    # screen.fill((0,0,0))
    # Save the original position of the tank
    original_x = tank.x
    original_y = tank.y
    # print(original_x, original_x)

    # Move the tank if keys are pressed
    if keyboard.left:
        tank.x = tank.x - 2
        tank.angle = 180
    elif keyboard.right:  # I use elif and not if to not go in diagonal directions!
        tank.x = tank.x + 2
        tank.angle = 0
    elif keyboard.up:
        tank.y = tank.y - 2
        tank.angle = 90
    elif keyboard.down:
        tank.y = tank.y + 2
        tank.angle = 270

    # return tank to original position if colliding with wall
    if tank.collidelist(walls) != -1:
        # print(tank.collidelist(walls))
        tank.x = original_x
        tank.y = original_y
    
    # We prevent the tank from exit the screen
    # if tank.x < 0 or tank.x > 800 or tank.y < 0 or tank.y > 600: # it goes out for 25 pixels
    if tank.x < 25 or tank.x > 800 - 25 or tank.y < 25 or tank.y > 600 - 25: # it goes out for 25 pixels
        tank.x = original_x
        tank.y = original_y

    if bullet_holdoff == 0:
        if keyboard.space:
            bullet = Actor('laserblue02')
            bullet.angle = tank.angle
            bullet.x = tank.x
            bullet.y = tank.y
            bullets.append(bullet)
            bullet_holdoff = 30
    else:
        bullet_holdoff = bullet_holdoff -1
    print(bullet_holdoff)

    for bullet in bullets:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        elif bullet.angle == 90:
            bullet.y = bullet.y -5
        elif bullet.angle == 180:
            bullet.x = bullet.x -5
        elif bullet.angle == 270:
            bullet.y = bullet.y + 5
    
    for bullet in bullets:
        wall_index = bullet.collidelist(walls)
        if wall_index != -1:
            del walls[wall_index]
            bullets.remove(bullet)
        # Remove the bullet that reaches the edge of ghe screen.
        if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
            bullets.remove(bullet)


def draw():
    background.draw()
    for wall in walls:
        wall.draw()
    tank.draw()
    for bullet in bullets:
        bullet.draw()





pgzrun.go() # Must be last line

# sono arrivato a tank cannon