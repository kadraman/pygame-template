import pygame as pg

from .base_state import BaseState

from modules.display_utils import BackGround

import constants


class MainMenu(BaseState):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.active_index = 0
        self.options = ["Start Game", "Quit Game"]
        self.next_state = "GAME_PLAY"

        self.fancy_text_1 = None

    def startup(self, persistent):
        self.persist = persistent
        color = self.persist["screen_color"]
        self.screen_color = pg.Color(color)
        self.fancy_text_1 = self.persist["fancy_text_1"]
        persistent["fancy_text_1"] = self.fancy_text_1

    def render_text(self, index):
        color = pg.Color("red") if index == self.active_index else pg.Color("white")
        return self.default_font.render(self.options[index], True, color)

    def get_text_position(self, text, index):
        center = (self.screen_rect.center[0],
                  self.screen_rect.center[1] + (index * 50))
        return text.get_rect(center=center)

    def handle_action(self):
        if self.active_index == 0:
            self.done = True
        elif self.active_index == 1:
            self.quit = True

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.active_index = 1 if self.active_index <= 0 else 0
            elif event.key == pg.K_DOWN:
                self.active_index = 0 if self.active_index >= 1 else 1
            elif event.key == pg.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        background = BackGround(constants.DEFAULT_BACKGROUND, [0, 0])
        surface.fill([255, 255, 255])
        surface.blit(background.image, background.rect)

        self.fancy_text_1.draw(self.screen, constants.TITLE, 320, 75)

        for index, option in enumerate(self.options):
            text_render = self.render_text(index)
            surface.blit(text_render, self.get_text_position(
                text_render, index))

    def update(self, dt):
        self.fancy_text_1.update()
