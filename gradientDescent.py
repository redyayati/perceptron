import pygame as pg 
from pygame.math import Vector2
pg.init()
width = 600
height = 600

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Title of window')
clock = pg.time.Clock() 
running  = True

data = []
m = 1 
b = 0 

def drawLine() : 
    global m , b
    x1 = 0 
    y1 = m*x1 + b 
    x2 = 1
    y2 = m*x2 + b 

    x1 = x1* width 
    y1 = (1-y1) * height
    x2 = x2* width 
    y2 = (1-y2) * height

    pg.draw.line(screen , (0,250,250), (x1,y1),(x2,y2),2)

def mousePressed(): 
    mx,my = pg.mouse.get_pos()
    x = mx / width
    y = -my/height + 1 
    point = Vector2(x,y)
    data.append(point)

def linearRegression() : 
    global m , b
    xsum = 0 
    ysum = 0
    n = len(data)  
    for point in data : 
        xsum += point.x
        ysum += point.y 
    xmean = xsum / n
    ymean = ysum / n 

    num = 0
    den = 0
    for point in data : 
        x , y = point
        num += (x - xmean) * (y - ymean)
        den += (x - xmean) * (x - xmean)
    m = num / den
    b = ymean - m * xmean

def gradietDescent() : 
    global m,b
    learning_rate = .1
    for point in data : 
        x ,y = point 
        
        guess = m * x + b 
        
        error = y - guess

        m += error * x * learning_rate 
        b += error * learning_rate

while running : 
    
    screen.fill((155,155,155))
    for point in data : 
        x = point.x * width 
        y = (1-point.y) * height
        pg.draw.circle(screen , (255,255,255), (int(x),int(y)),6)
        pg.draw.circle(screen , (0,0,0), (int(x),int(y)),7,1)
    if len(data) > 1 : 
        gradietDescent()
        drawLine()

    for event in pg.event.get() : 
        if event.type == pg.MOUSEBUTTONDOWN : 
            mousePressed()
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False 
            if event.key == pg.K_r : 
                data = [] 
    pg.display.flip()
    clock.tick(60)
pg.quit()
