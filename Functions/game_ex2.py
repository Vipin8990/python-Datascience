import pgzrun

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',(WIDTH//2, HEIGHT//2))

title = 'IRON-MAN GAME'

def draw():
    screen.fill('white')
    screen.draw.text(title,center=(WIDTH//2,30),fontsize=60, 
        color='black', align='center',shadow=(.2,2),scolor='red')

    p.draw()

def p_move():
    '''' function to move player'''
    if keyboard.right:
        p.x += 3
    elif keyboard.left:
        p.x -= 3
        p.angle = -10
    elif keyboard.up:
        p.y -= 3
    elif keyboard.down:
        p.y += 3
        p.angle = 10
    else:
        p.angle = -20
    
def handle_boundary():
    if p.x > WIDTH:
        p.x = 0
    if p.x < 0:
        p.x = WIDTH
    if p.y > HEIGHT:
        p.y = 0
    if p.y < 0:
        p.y = HEIGHT

def update():
    p_move() # function call 
    handle_boundary() # function call
    print(p.x, p.y, p.angle)

pgzrun.go()