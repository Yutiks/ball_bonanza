import pygame as pg
import random
import settings as sett


class Ball:
    def __init__(self, x, y, size, speed_y):
        self.size = size
        self.image = random.choice([sett.RED_BALL, sett.PINK_BALL, sett.BROWN_BALL, sett.GREEN_BALL, sett.YELLOW_BALL])
        self.image = pg.transform.smoothscale(self.image, [self.size, self.size])
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pg.Rect([x, y], [width, height])
        self.speed_x = random.randint(-2, 2)
        self.speed_y = speed_y
        self.rect_col = pg.Rect([x, y], [width // 1.5, height // 1.5])

    def paint(self, display):
        display.blit(self.image, self.rect)

    def movement(self):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        self.rect_col.centerx = self.rect.centerx
        self.rect_col.centery = self.rect.centery
