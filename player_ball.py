import pygame as pg
import settings as sett


class PlayerBall:
    def __init__(self, size):
        self.image = pg.image.load("images/blue_ball.PNG").convert_alpha()
        self.size = size
        self.image = pg.transform.smoothscale(self.image, [self.size, self.size])
        width, height = self.image.get_size()
        self.mouse_x, self.mouse_y = pg.mouse.get_pos()
        self.rect = pg.Rect([sett.HEIGHT, sett.WIDTH], [width, height])
        self.rect_col = pg.Rect([sett.HEIGHT, sett.WIDTH], [width // 1.5, height // 1.5])

    def paint(self, display):
        display.blit(self.image, self.rect)

    def control(self):
        self.rect.center = pg.mouse.get_pos()
        self.rect_col.centerx = self.rect.centerx
        self.rect_col.centery = self.rect.centery

    def update_size(self, size_increase):
        self.size += size_increase
        self.image = pg.transform.smoothscale(self.image, [self.size, self.size])
        width, height = self.image.get_size()
        self.rect.size = (width, height)
        self.rect_col.size = (width // 1.5, height // 1.5)
