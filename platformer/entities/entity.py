import arcade

from platformer.constants import CHARACTER_SCALING, RIGHT_FACING


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.Texture.flip_horizontally(arcade.load_texture(filename))
    ]


class Entity(arcade.Sprite):
    def __init__(self, folder, file_prefix, moving_assets=2):
        super().__init__()

        # Default to facing right
        self.facing_direction = RIGHT_FACING

        # Used for image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        self.animations = {}

        self.idle_texture_pair = load_texture_pair(f"{folder}/{file_prefix}_idle.png")

        # Load textures for walking
        self.walk_textures = []
        for i in range(moving_assets):
            texture = load_texture_pair(f"{folder}/{file_prefix}_walk{i}.png")
            self.walk_textures.append(texture)

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]