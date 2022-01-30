import pygame as pg

from .base_state import BaseState

from modules.display_utils import BackGround, FancyText

import constants


class SplashScreen(BaseState):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.title = self.default_font.render(constants.TITLE, True, pg.Color("blue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.persist["screen_color"] = pg.Color("black")
        self.persist["background"] = BackGround(constants.DEFAULT_BACKGROUND, [0, 0])
        self.next_state = "MAIN_MENU"
        self.time_active = 0

        self.fancy_text_1 = FancyText(constants.DEFAULT_FONT, constants.TITLE_FONT_SIZE, [20, 20, 150])
        self.fancy_text_1.color_direction = [0, 0, 1]
        self.fancy_text_1.color_speed = 5

    def startup(self, persistent):
        self.persist = persistent
        color = self.persist["screen_color"]
        self.screen_color = color
        background = self.persist["background"]
        self.background = background
        persistent["fancy_text_1"] = self.fancy_text_1

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            self.done = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.done = True

    def draw(self, surface):
        surface.fill([255, 255, 255])
        surface.blit(self.background.image, self.background.rect)
        self.fancy_text_1.draw(self.screen, constants.TITLE, 320, 75)

    def update(self, dt):
        self.time_active += dt * 1000
        # move to main menu automatically
        if self.time_active >= 2000:
            self.done = True
        self.fancy_text_1.update()

