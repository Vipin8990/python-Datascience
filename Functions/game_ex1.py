import pgzrun # pgzurn are used to import game files
HEIGHT = 300
WIDTH = 800

p = Actor('ironman',(100, 100))
c = Actor('cookie')

def draw():
    screen.clear()
    #screen.fill('white') to fill the color in background   
    p.draw() # to draw the picture
    c.draw()
    #print('drawing')

def update():
    #print('updating')
    p.x += 1
    p.angle = -10 
    if p.x > WIDTH:
        p.x = 0
    print(p.x, p.y)
    


pgzrun.go() # press ctrl + j for open the terminal to run the program



