import pygame as pg

import constants


class Explosion(pg.sprite.Sprite):
    def __init__(self, sprites, center, size):
        super(Explosion, self).__init__()
        self.timer = 0
        self.interval = 2
        self.number_of_images = constants.SS_EXPLOSION_IMAGES
        self.images = sprites.load_strip([
            constants.SS_EXPLOSION_X,
            constants.SS_EXPLOSION_Y,
            constants.SS_EXPLOSION_WIDTH,
            constants.SS_EXPLOSION_HEIGHT], self.number_of_images, -1)

        # scale explosion images to size of enemy images
        for index, image in enumerate(self.images):
            self.images[index] = pg.transform.scale(image, (size[0], size[1]))

        self.surface = self.images[0]
        self.rect = self.surface.get_rect(center=center)
        self.image_index = 0

    def get_event(self, event):
        pass

    def update(self, pressed_keys):
        self.timer += 1
        if self.timer % self.interval == 0:
            self.image_index += 1

        if self.image_index >= self.number_of_images:
            self.kill()

    def get_surface(self):
        return self.images[self.image_index]
