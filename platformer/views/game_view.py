import arcade
from platformer.views.view import View
from platformer.constants import TILE_SCALING, LAYER_NAME_GROUND

class GameView(View):
    def __init__(self):
        super().__init__()

        # Scene Object
        self.scene = None

        

    def setup(self):
        
        super().setup()

        # Name of map file to load
        map_name = "assets/maps/level1.tmx"

        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.
        layer_options = {
            LAYER_NAME_GROUND: {
                "use_spatial_hash": True,
            },
        }

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        
    def on_show_view(self):
        self.window.background_color = arcade.color.CORNFLOWER_BLUE

    def on_draw(self):
        if not self.started:
            self.setup()
        self.scene.draw()