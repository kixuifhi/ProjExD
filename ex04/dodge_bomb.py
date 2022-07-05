import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()

    # 練習1 スクリーンと背景
    pg.display.set_caption("逃げり!こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #Surface
    screen_rct = screen_sfc.get_rect()           #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #Surface
    bgimg_rct = bgimg_sfc.get_rect()             #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    #練習3 こうかとん
    kkimg_sfc = pg.image.load("fig/8.png")               #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect()                    #Rect
    kkimg_rct.center = 900,400
    
    #練習5 爆弾
    bmimg_sfc = pg.Surface((20, 20)) # Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10,10), 10)
    bmimg_rct = bmimg_sfc.get_rect() #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        #練習4
        key_states = pg.key.get_pressed()  #辞書
        if key_states[pg.K_UP] == True:    #y座標を-1
            kkimg_rct.centery -= 1
        if key_states[pg.K_DOWN] == True:  #y座標を+1
            kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True:  #x座標を-1
            kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True: #x座標を+1
            kkimg_rct.centerx += 1
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        
        #練習5
        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        pg.display.update()
        clock.tick(1000)
    

if __name__=="__main__":
    pg.init() #module 初期化
    main() 
    pg.quit() #初期化解除
    sys.exit()
