from platformer.constants import LEFT_FACING, RIGHT_FACING, TEXTURE_DELAY
from platformer.entities.entity import Entity


class Goomba(Entity):
    """Goomba Sprite"""

    def __init__(self, collision_sprite, center_x=0, center_y=0):

        folder = "assets/images/sprites/players/goomba"
        file_prefix = "goomba"

        # Set up parent class
        super().__init__(folder, file_prefix, moving_assets=2)
        self.collision_sprite = collision_sprite
        self.texture_delay = TEXTURE_DELAY
        self.scale = 0.33
        self.center_x=center_x
        self.center_y=center_y
        self.facing_direction = RIGHT_FACING


    def update_animation(self, delta_time: float = 1 / 60):
        if self.facing_direction == RIGHT_FACING:
            self.center_x += 0.1
        else:
            self.center_x -= 0.1
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.facing_direction == RIGHT_FACING:
            self.facing_direction = LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == LEFT_FACING:
            self.facing_direction = RIGHT_FACING

        # Walking animation
        if self.texture_delay == 0:
            self.cur_texture += 1
            if self.cur_texture > 1:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture][self.facing_direction]
            self.texture_delay = TEXTURE_DELAY

        else:
            self.texture_delay -= 1
