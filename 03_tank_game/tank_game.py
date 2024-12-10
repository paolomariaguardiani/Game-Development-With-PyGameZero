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

enemy = Actor('tank_red')
enemy.y = 25
enemy.x = 400
enemy.angle = 270
enemy.move_count = 0

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
enemy_bullets = []

enemies = []
for i in range(3):
    enemy = Actor('tank_red')
    enemy.y = 25
    enemy.x = i * 200 + 100
    enemy.angle = 270
    enemy.move_count = 0
    enemies.append(enemy)

bullet_holdoff = 0

game_over = False

def update():
    global bullet_holdoff, game_over
    # tank.angle += 1
    # screen.fill((0,0,0))

    # This part is for the tank
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


    # This part is for the bullet
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
    # print(bullet_holdoff)

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
        enemy_index = bullet.collidelist(enemies)
        if enemy_index != -1:
            del enemies[enemy_index]
            bullets.remove(bullet)
        
    
    # This part is for the enemy
    for enemy in enemies:
        choice = random.randint(0, 2)
        if enemy.move_count > 0:
            enemy.move_count = enemy.move_count -1

            original_x = enemy.x
            original_y = enemy.y
            if enemy.angle == 0:
                enemy.x = enemy.x + 2
            elif enemy.angle == 90:
                enemy.y = enemy.y -2
            elif enemy.angle == 180:
                enemy.x = enemy.x -2
            elif enemy.angle == 270:
                enemy.y = enemy.y + 2

            if enemy.collidelist(walls) != -1:
                enemy.x = original_x
                enemy.y = original_y
                enemy.move_count = 0
            if enemy.x < 0 or enemy.x > 800 or enemy.y < 0 or enemy.y > 600:
                enemy.x = original_x
                enemy.y = original_y
                enemy.move_count = 0


        elif choice == 0:
            enemy.move_count = 20
            # print('move')
        elif choice == 1:
            # print('turn')
            enemy.angle = random.randint(0, 3) * 90
        else:
            # print('shoot')
            bullet = Actor('laserred02')
            bullet.angle = enemy.angle
            bullet.x = enemy.x
            bullet.y = enemy.y
            enemy_bullets.append(bullet)

        for bullet in enemy_bullets:
            if bullet.angle == 0:
                bullet.x = bullet.x + 5
            elif bullet.angle == 90:
                bullet.y = bullet.y - 5
            elif bullet.angle == 180:
                bullet.x = bullet.x - 5
            elif bullet.angle == 270:
                bullet.y = bullet.y + 5

        for bullet in enemy_bullets:
            wall_index = bullet.collidelist(walls)
            if wall_index != -1:
                del walls[wall_index]
                enemy_bullets.remove(bullet)
            if bullet.x < 0 or bullet.x > 800 or bullet.y < 0 or bullet.y > 600:
                enemy_bullets.remove(bullet)
            if bullet.colliderect(tank):
                game_over = True


def draw():
    if len(enemies) == 0:
        screen.fill((0,0,0))
        screen.draw.text('You Win!', (260,250), color=(255,255,255), fontsize = 100)
    elif game_over:
        screen.fill((0,0,0))
        screen.draw.text('You Lose!', (260,250), color=(255,255,255), fontsize=100)
    else:
        background.draw()
        tank.draw()
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw( )
        for bullet in enemy_bullets:
            bullet.draw()
        for wall in walls:
            wall.draw()





pgzrun.go() # Must be last line

# sono arrivato a tank cannon