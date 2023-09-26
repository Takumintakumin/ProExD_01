import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    B3_img = pg.image.load("fig/3.png")
    B3_img = pg.transform.flip(B3_img, True, False)
    B3_img2 = pg.transform.rotozoom(B3_img, 10, 1.0)
    B3_imgs = [B3_img, B3_img2]
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(B3_imgs[tmr%2], [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()