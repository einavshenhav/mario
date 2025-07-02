import arcade
import time
from platformer.constants import TILE_SCALING

class Trigger(arcade.Sprite):
    
    def __init__(self, folder, file_prefix, scale=TILE_SCALING, center_x=0, center_y=0, object=None):
        super().__init__()
        self.scale = scale
        self.object = object
        self.texture = arcade.load_texture(f"{folder}/{file_prefix}.png")
        self.center_x = center_x
        self.center_y = center_y

    
    # this should call a method of self.object and mutate it according to how it should behave under collision
    def handle_collision(self):
        self.object.trigger()