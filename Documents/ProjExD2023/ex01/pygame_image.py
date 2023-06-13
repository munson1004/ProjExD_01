import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    rbg_img= pg.transform.flip(bg_img,True,False)
    kk = pg.transform.rotozoom(kk_img, 10, 1.0)
    kkflip = []
    for i in range(10):
        kkflip.append(pg.transform.rotozoom(kk_img, i, 1.0))
    for i in range(9,1,-1):
        kkflip.append(pg.transform.rotozoom(kk_img, i, 1.0))
    tmr = 0
    x=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [0-x, 0])
        screen.blit(rbg_img, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kkflip[tmr%18],[300,200])
        pg.display.update()
        tmr += 1        
        x += 1
        if x>3200:
            x=0
        clock.tick(100)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()