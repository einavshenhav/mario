import arcade
import time
from platformer.constants import LEFT_FACING, RIGHT_FACING, TILE_SCALING
from platformer.entities.entity import Entity

class Brick(arcade.Sprite):
    """"""
    def __init__(self, folder, file_prefix):
        super().__init__()
        self.scale = TILE_SCALING
        self.texture = arcade.load_texture(f"{folder}/{file_prefix}.png")


class BreakableBrick(Brick):
    """"""

    def __init__(self, center_x=0, center_y=0):

        folder = "assets/images/sprites/blocks/"
        file_prefix = "brick"
        super().__init__(folder, file_prefix)
        self.texture = arcade.load_texture("assets/images/sprites/blocks/brick.png")

        self.center_x = center_x
        self.center_y = center_y
    

