import pgzrun
import random

WIDTH = 800
HEIGHT = 600

color = 0
x_pos = 0
y_pos = 0

ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

gem = Actor('gemgreen.png')
gem.x = 350
gem.y = 0

score = 0

game_over = False

def update(): # 60 frames per seconds by default
    if keyboard.left:
        global color
        global score
        global game_over

        ship.x = ship.x -5
    if keyboard.right:
        ship.x = ship.x + 5
    color = random.randint(1, 250)
    # print(color)
    # gem.x = random.randint(0, 800)
    # gem.y = random.randint(0, 600)
    # gem.y = gem.y + 4
    gem.y = gem.y + 4 + score / 5 
    if gem.y > 600:
        # gem.x = random.randint(20, 780)
        # gem.y = 0
        game_over = True
    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1
        print(score)
    # if ship.colliderect(gem):
    #     gem.y = 0


def draw():
    # screen.clear()
    # screen.fill([color, color, color]) # this also clear the screen
    screen.fill((80, 0, 70))
    # if game_over == True:
    if game_over:
        screen.draw.text('Game Over', (360,300), color = (255,255,255), fontsize = 60)
        screen.draw.text('Final Score: ' + str(score), (360,350), color=(255,255,255), fontsize = 60)
    else:
        gem.draw()
        ship.draw()
        screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize = 30)
    
    
    
    # screen.draw.text(f'Score: {score}', (15,10), 
    #                  color=(255,255,255), 
    #                  fontsize = 30)


def on_mouse_move(pos, rel, buttons):
    # rel provides the change in position since the last mouse move (rel[0] for x)
    ship.x = pos[0] # pos[0] is for x and pos[1] is for y
    # ship.y = pos[1]
   

pgzrun.go() # Must be last line