import pygame as pg
import balls
import random
import settings as sett
import pygame.freetype
import player_ball
import button as butt

pg.init()
pg.mixer.init()


class Game:
    def __init__(self):
        self.game_process = 1
        self.display = pg.display.set_mode([sett.WIDTH, sett.HEIGHT])
        self.clock = pg.time.Clock()
        self.background = sett.BACKGROUND
        # self.menu_picture =
        # self.menu_picture =
        self.loss_screen = sett.LOSS_SCREEN
        self.win_screen = sett.WIN_SCREEN
        self.size_increase = 0
        self.player_ball = player_ball.PlayerBall(200)
        self.ball_spawn = pg.USEREVENT
        pg.time.set_timer(self.ball_spawn, 3000)
        self.balls = []
        self.font = pg.freetype.Font("fonts/gaming_font.otf", 40)
        self.menu = "game"
        self.yes_button = butt.Button(450, 780, sett.YES_BUTTON)
        self.no_button = butt.Button(850, 780, sett.NO_BUTTON)
        self.play_again = butt.Button(650, 680, sett.PLAY_AGAIN)

    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.game_process = 0
            if self.menu == "game":
                if event.type == pg.MOUSEMOTION:
                    self.player_ball.mouse_x, self.player_ball.mouse_y = event.pos
                if event.type == self.ball_spawn:
                    speed_y_above = random.randint(4, 8)
                    speed_y_below = random.randint(-8, -4)
                    random_size = random.randint(50, 200)
                    ball_ = balls.Ball(random.randint(0, sett.WIDTH - 50), -50, random_size, speed_y_above)
                    self.balls.append(ball_)
                    ball_ = balls.Ball(random.randint(0, sett.WIDTH - 50), sett.HEIGHT + 50, random_size, speed_y_below)
                    self.balls.append(ball_)
            if self.menu == "loss" or self.menu == "win":
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if event.button == 1 and self.yes_button.rect.collidepoint(pg.mouse.get_pos()):
                        self.balls = []
                        self.menu = "game"
                    elif self.no_button.rect.collidepoint(pg.mouse.get_pos()):
                        self.game_process = 0

    def paint(self):
        if self.menu == "game":
            text_to_render = str(f"size:{self.player_ball.size}/{sett.FINAL_SIZE}")
            self.display.blit(self.background, [0, 0])
            self.player_ball.paint(self.display)
            for ball_paint in self.balls:
                ball_paint.paint(self.display)
            self.font.render_to(self.display, [sett.WIDTH - 230, 10], text_to_render, [255, 255, 255])
        if self.menu == "loss":
            self.display.blit(self.loss_screen, [0, 0])
            self.yes_button.paint(self.display)
            self.no_button.paint(self.display)
            self.play_again.paint(self.display)
        if self.menu == "win":
            self.display.blit(self.win_screen, [0, 0])
            self.play_again.paint(self.display)
            self.yes_button.paint(self.display)
            self.no_button.paint(self.display)

    def movement(self):
        if self.menu == "game":
            pg.mouse.set_visible(False)
            self.player_ball.control()
            for ball in self.balls:
                ball.movement()
            for ball in self.balls:
                if ball.rect_col.colliderect(self.player_ball.rect) and ball.size < self.player_ball.size:
                    self.size_increase = ball.size // 10
                    self.balls.remove(ball)
                    self.player_ball.update_size(self.size_increase)
                if ball.rect_col.colliderect(self.player_ball.rect) and ball.size > self.player_ball.size:
                    self.menu = "loss"
                if ball.rect.y > sett.HEIGHT + 100:
                    ball.rect.y = -50
                elif ball.rect.y < -100:
                    ball.rect.y = sett.HEIGHT + 50
                if ball.rect.x > sett.WIDTH + 100:
                    ball.rect.x = - 50
            if self.menu == "loss":
                pg.mouse.set_visible(True)
                self.player_ball.size = 199
                self.size_increase = 1
                self.player_ball.update_size(self.size_increase)
            if self.player_ball.size >= 500:
                self.menu = "win"
            if self.menu == "win":
                pg.mouse.set_visible(True)
                self.player_ball.size = 199
                self.size_increase = 1
                self.player_ball.update_size(self.size_increase)

    def start(self):
        while self.game_process == 1:
            self.paint()
            self.events()
            self.movement()
            pg.display.update()
            self.clock.tick(60)


game = Game()
game.start()
