import pygame as pg
# import settings as sett


class Button:
    def __init__(self, x, y, image):
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, [200, 100])
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = pg.Rect([x, y], [width, height])
        self.rect_col = pg.Rect([x, y], [width, height])

    def paint(self, window):
        window.blit(self.image, self.rect)
        self.rect_col.centerx = self.rect.centerx
        self.rect_col.centery = self.rect.centery
