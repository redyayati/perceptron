import random
import pygame as pg 
pg.init()
width = 800
height = 800

window = pg.display.set_mode((width, height))
pg.display.set_caption('Perceptron Training')
clock = pg.time.Clock() 
running  = True

def sign(n) : 
    if n >= 0 : 
        return 1 
    else : return -1

f= sign(234)

class perceptron : 
    def __init__(self) : 
        self.weights = [0 for i in range(2)]
        for i in range(2) : 
            self.weights[i] = random.uniform(-1,1)
    def guess(self, inputs) : 
        sum = 0 
        for i in range(len(self.weights)) : 
            sum += inputs[i] * self.weights[i]
        output = sign(sum)
        return output
    def train(self, inputs, target) : 
        lr = .1
        guess = self.guess(inputs)
        error = target - guess 
        for i in range(len(self.weights)) : 
            self.weights[i] += error * inputs[i] * lr


class point : 
    def __init__(self) : 
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        # self.bias = 1
        if self.x > self.y : self.label = 1 
        else : self.label = -1
    def show(self) : 
        if self.label == 1 : col = 255,255,255
        else : col = 0,0,0
        pg.draw.circle(window,col, (self.x,self.y),6)

points = []
for i in range(200): 
    points.append(point())

p = perceptron()

print(p.weights)


while running : 

    window.fill((155,155,155))
    for pt in points : 
        pt.show()
    
    for pt in points : 
        inPut = pt.x,pt.y 
        target = pt.label
        guess = p.guess(inPut)
        if guess == target : col = 0,255,0
        else : col = 255,0,0
        pg.draw.circle(window , col , (pt.x,pt.y) , 4)
    # for pt in points : 
    #     inPut = pt.x,pt.y , pt.bias
    #     target = pt.label
        # p.train(inPut , target)
    # pg.draw.line(window,(0,255,0),(0,0), (width,height),2)

    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False 
            if event.key == pg.K_t : 
                for pt in points : 
                    inPut = pt.x,pt.y 
                    target = pt.label
                    p.train(inPut , target)
                # print("weights are : ",p.weights)
                # first = random.randint(0,100)
                # second = random.randint(0,100)
                # x1 , y1 = points[first].x , points[first].y
                # x2 , y2 = points[second].x , points[second].y
                # sum1 = x1*p.weights[0] + y1*p.weights[1]
                # sum2 = x2*p.weights[0] + y2*p.weights[1]
                # print("test points : ", (x1,y1,sum1, p.guess((x1,y1))) , (x2,y2,sum2, p.guess((x2,y2))))
            if event.key == pg.K_r : 
                points = []
                for i in range(200): 
                    points.append(point())
                p = perceptron()
            if event.key == pg.K_n : 
                points = []
                for i in range(200): 
                    points.append(point())
                
    pg.display.flip()
    clock.tick(60)
pg.quit()
