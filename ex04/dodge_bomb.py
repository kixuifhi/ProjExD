import pygame as pg
import sys


def main():
    clock = pg.time.Clock()

    # 練習1
    pg.display.set_caption("逃げり!こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #Surface
    screen_rct = screen_sfc.get_rect()           #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")   #Surface
    bgimg_rct = bgimg_sfc.get_rect()             #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    #練習3
    kkimg_sfc = pg.image.load("fig/6.png")               #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0) #Surface
    kkimg_rct = kkimg_sfc.get_rect()                    #Rect
    kkimg_rct.center = 900,400

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()
        clock.tick(1000)
    

if __name__=="__main__":
    pg.init() #module 初期化
    main() 
    pg.quit() #初期化解除
    sys.exit()
