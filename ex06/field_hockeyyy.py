from errno import EEXIST, ENEEDAUTH
from tkinter import CENTER
import pygame as pg
import sys
import random
from pygame.locals import *


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Player1: #player(画面左)
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((30, 200)) # Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc, color, Rect(10,10,30,200), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 30 #初期位置
        self.rct.centery = 450 #初期位置
        self.vx, self.vy = vxy
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
     
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_w]: #wキーで上
            self.rct.centery -= 1
        if key_states[pg.K_s]: #sキーで下
            self.rct.centery += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_w]: 
                self.rct.centery += 1
            if key_states[pg.K_s]: 
                self.rct.centery -= 1
        self.blit(scr)


class Player2: #player(画面右)
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((30, 200)) # Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.rect(self.sfc, color, Rect(10,10,30,200), size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 1580 #初期位置
        self.rct.centery = 450 #初期位置
        self.vx, self.vy = vxy
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
     
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_UP]: #upキーで上
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: #downキーで下
            self.rct.centery += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = 900
        self.rct.centery = 400
        self.vx, self.vy = vxy 

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen): 
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)     


class Score:
    def __init__(self, score, score2):
        self.font = pg.font.Font(None, 100)
        self.text = self.font.render(f'{score2}   -   {score}',True,(0,0,0) )

    def blit(self, scr:Screen):
        scr.sfc.blit(self.text,(scr.rct.width//2-100,50))

    def update(self, scr:Screen):
        self.blit(scr)

    
def main():
    clock = pg.time.Clock()
    scr = Screen("field_hockey", (1600, 900), "fig/t.jpeg")
    score,score2 = 0,0
    bkd = Bomb((255,0,0), 10, (+1,+1), scr)
    pl1 = Player1((255,255,0), 200, (1, 1), scr) 
    pl2 = Player2((255,0,255), 200, (1, 1), scr)
    while True:
        sb = Score(score, score2)
        if pl1.rct.colliderect(bkd.rct): #playerに当たったら
            bkd.vx *= -1 #反射
        if pl2.rct.colliderect(bkd.rct): #playerに当たったら
            bkd.vx *= -1 #反射
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        if bkd.rct.centerx < 10:
            score += 1
        if bkd.rct.centerx > scr.rct.width-10:
            score2 += 1
        if score >= 5 and score-score2 >= 2: #5点先取orデュースで2点差
            return
        elif score2 >= 5 and score2-score >= 2: #5点先取orデュースで2点差
            return
        scr.rct.width
        bkd.update(scr)
        pl1.update(scr)
        pl2.update(scr)
        sb.update(scr)
        pg.display.update()
        clock.tick(1000)


def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : 
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: 
        tate = -1 # 領域外
    return yoko, tate
    

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()