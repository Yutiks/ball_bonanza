import pygame as pg

# DISPLAY -->
HEIGHT = 900
WIDTH = 1475

# BACKGROUND-->
BACKGROUND = pg.image.load("images/background.png")
BACKGROUND = pg.transform.smoothscale(BACKGROUND, [WIDTH, HEIGHT])

# BALLS -->
BROWN_BALL = pg.image.load("images/brown_ball.PNG")
GREEN_BALL = pg.image.load("images/green_ball.PNG")
PINK_BALL = pg.image.load("images/pink_ball.PNG")
RED_BALL = pg.image.load("images/red_ball.PNG")
YELLOW_BALL = pg.image.load("images/yellow_ball.PNG")

FINAL_SIZE = 500

# BUTTONS -->
YES_BUTTON = "images/yes_button.jpg"
NO_BUTTON = "images/no_button.jpg"

# MENU-->
LOSS_SCREEN = pg.image.load("images/loss.jpg")
LOSS_SCREEN = pg.transform.smoothscale(LOSS_SCREEN, [WIDTH, HEIGHT])
WIN_SCREEN = pg.image.load("images/win.jpg")
WIN_SCREEN = pg.transform.smoothscale(WIN_SCREEN, [WIDTH, HEIGHT])

PLAY_AGAIN = "images/play_again.PNG"
