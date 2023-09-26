import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)

    B3_img = pg.image.load("fig/3.png")
    B3_img = pg.transform.flip(B3_img, True, False)
    B3_img2 = pg.transform.rotozoom(B3_img, 10, 1.0)
    B3_imgs = [B3_img, B3_img2]
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%6400
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(bg_img2, [4800-x, 0])
        screen.blit(bg_img, [6400-x, 0])

        screen.blit(B3_imgs[tmr%2], [300,200])
        pg.display.update()
        tmr += 10
      
        clock.tick(40)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()