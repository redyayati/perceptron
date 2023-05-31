from nn import NeuralNetwork
import random

import pygame as pg 
pg.init()
width = 800
height = 500

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Title of window')
clock = pg.time.Clock() 
running  = True

resolution = 10 
rows = int(height / resolution)
cols = int(width / resolution)

training_data = [[[1,0],1] , [[1,1],0] , [[0,1],1] , [[0,0],0]]

nn = NeuralNetwork(2,3,1)

def train(n):
    for i in range(500) : 
        for i  in range(len(training_data)) : 
            test = random.choice(training_data)
            # test = training_data[i]
            inputs = test[0]
            target = [test[1]]
            n.train(inputs, target)
    print("trained")

train(nn)

print(nn.predict([1,0]))

# nn2 = NeuralNetwork(2,3,1)
nn2 = nn.copy()
print(nn2.predict([0,0]))



while running : 
    screen.fill((255,255,255))
    for i in range(rows) : 
        for j in range(cols):
            xpos = j * resolution
            ypos = i * resolution
            xVal = j * resolution/width
            yVal = i * resolution/height
            col = nn2.predict([xVal,yVal])
            col = col[0]
            col = int(col * 255)
            pg.draw.rect(screen, (col , col ,col), (xpos,ypos,resolution, resolution))

    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False 
            if event.key == pg.K_t : 
                # nn2 = nn.copy()
                train(nn2)
            if event.key == pg.K_r : 
                nn2 = nn.copy()
    pg.display.flip()
    clock.tick(60)
pg.quit()
