import pygame as pg 
pg.init()
width = 800
height = 500

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Title of window')
clock = pg.time.Clock() 
running  = True





while running : 
    screen.fill((255,255,255))


    for event in pg.event.get() : 
        if event.type == pg.QUIT : 
            running = False 
        elif event.type == pg.KEYDOWN : 
            if event.key == pg.K_ESCAPE : 
                running = False 
    pg.display.flip()
    clock.tick(60)
pg.quit()
