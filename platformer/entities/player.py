from platformer.constants import LEFT_FACING, RIGHT_FACING
from platformer.entities.entity import Entity


class Player(Entity):
    """Player Sprite"""

    def __init__(self):

        folder = "assets/images/sprites/players/mario"
        file_prefix = "mario"

        # Set up parent class
        super().__init__(folder, file_prefix, moving_assets=3)


    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.facing_direction == RIGHT_FACING:
            self.facing_direction = LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == LEFT_FACING:
            self.facing_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 2:
            self.cur_texture = 0
        self.texture = self.walk_textures[self.cur_texture][self.facing_direction]
