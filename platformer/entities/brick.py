import arcade
import time
from platformer.constants import LEFT_FACING, RIGHT_FACING, TILE_SCALING
from platformer.entities.entity import Entity

class Brick(arcade.Sprite):
    """"""
    def __init__(self):
        super().__init__()
        self.scale = TILE_SCALING
        folder = "assets/images/sprites/blocks/"
        file_prefix = "brick"
        self.texture = arcade.load_texture(f"{folder}/{file_prefix}.png")


class BreakableBrick(Brick):
    """"""

    def __init__(self, center_x=0, center_y=0):

        super().__init__()
        self.center_x = center_x
        self.center_y = center_y


class SolidBrick(Brick):
    """"""

    def __init__(self, center_x=0, center_y=0):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y

class PointBrick(Brick):

    def __init__(self, points, center_x=0, center_y=0):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.points = points

    def reduce_point(self):
        self.points -= 1
    
    def is_done(self):
        return self.points == 0

