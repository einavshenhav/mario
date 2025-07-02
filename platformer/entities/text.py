import arcade
from platformer.constants import COIN_SCALING, COIN_TEXTURE_DELAY
from platformer.entities.entity import Entity

class Coin(arcade.Sprite):
    """"""
    def __init__(self, center_x=0, center_y=0):
        super().__init__()
        self.scale = 1
        self.center_x = center_x
        self.center_y = center_y


    def update_animation(self, delta_time: float = 1 / 60):
        if self.texture_delay == 0:
            self.cur_texture_index += 1
            if self.cur_texture_index > 3:
                self.cur_texture_index = 0
            self.texture = self.textures[self.cur_texture_index]
            self.texture_delay = COIN_TEXTURE_DELAY
        else:
            self.texture_delay -= 1
            
