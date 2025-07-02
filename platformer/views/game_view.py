import arcade
import math
from platformer.views.view import View
from platformer.constants import MAP_HEIGHT, ASPECT_RATIO, TILE_SCALING, LAYER_NAME_WALLS, PLAYER_START_X, PLAYER_START_Y, LAYER_NAME_PLAYER, LAYER_NAME_BRICKS, LAYER_NAME_BRICK_TRIGGERS, OBJECT_LAYER_NAME_BRICKS, TRIGGER_MARGIN, PLAYER_MOVEMENT_SPEED, PLAYER_JUMP_SPEED
from platformer.entities.player import Player
from platformer.entities.brick import BreakableBrick, SolidBrick
from platformer.entities.trigger import Trigger

class GameView(View):
    def __init__(self):
        super().__init__()

        # Scene Object
        self.scene = None

        # Camera object
        self.camera = None

        self.player_sprite = None

        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False

        
    def setup(self):
        
        super().setup()

        # Name of map file to load
        map_name = "assets/maps/map1-1.tmx"

        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.
        layer_options = {
            LAYER_NAME_WALLS: {
                "use_spatial_hash": True,
            },
        }

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = Player()
        self.player_sprite.center_x = (
            self.tile_map.tiled_map.tile_size[0] * TILE_SCALING * PLAYER_START_X
        )
        self.player_sprite.center_y = (
            self.tile_map.tiled_map.tile_size[1] * TILE_SCALING * PLAYER_START_Y
        )
        self.scene.add_sprite(LAYER_NAME_PLAYER, self.player_sprite)

        self.scene.add_sprite_list(LAYER_NAME_BRICKS)
        self.scene.add_sprite_list(LAYER_NAME_BRICK_TRIGGERS)

        brick_layer = self.tile_map.object_lists[LAYER_NAME_BRICKS]
        for object in brick_layer:
            brick_type = object.type
            if brick_type == "breakable_brick":
                object_center_x = object.shape[0][0] + 4
                object_center_y = object.shape[0][1] - 4

                brick = BreakableBrick(center_x=object_center_x, center_y=object_center_y)
                self.scene.add_sprite(LAYER_NAME_BRICKS, brick)
                
                brick_trigger = Trigger(brick,
                                        "assets/images/sprites",
                                        "trigger",
                                        scale=TILE_SCALING,
                                        center_x=object.shape[0][0] + 4,
                                        center_y=object.shape[0][1] - 4 - TRIGGER_MARGIN)
                self.scene.add_sprite(LAYER_NAME_BRICK_TRIGGERS, brick_trigger)

            if brick_type == "solid_brick":
                object_center_x = object.shape[0][0] + 4
                object_center_y = object.shape[0][1] - 4

                brick = SolidBrick(center_x=object_center_x, center_y=object_center_y)
                self.scene.add_sprite(LAYER_NAME_BRICKS, brick)

                brick_trigger = Trigger(brick,
                                        "assets/images/sprites",
                                        "trigger",
                                        scale=TILE_SCALING,
                                        center_x=object.shape[0][0] + 4,
                                        center_y=object.shape[0][1] - 4 - TRIGGER_MARGIN)
                self.scene.add_sprite(LAYER_NAME_BRICK_TRIGGERS, brick_trigger)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            gravity_constant=0.5,
            walls=[self.scene["Ground"], self.scene[LAYER_NAME_BRICKS]],
        )

        # Set up the camera
        self.camera = arcade.Camera2D(
            arcade.types.Viewport(0,
                                  0,
                                  math.floor(MAP_HEIGHT * ASPECT_RATIO) * self.tile_map.tile_width * TILE_SCALING,
                                  MAP_HEIGHT * self.tile_map.tile_height * TILE_SCALING
                                 ),
        )

        # Set the viewport to match the window size
        self.camera.viewport_width = self.window.width
        self.camera.viewport_height = self.window.height

        self.left_border = self.camera.position[0]


    def on_show_view(self):
        self.window.background_color = arcade.color.CORNFLOWER_BLUE

    def on_draw(self):
        if not self.started:
            self.setup()
        
        # Clear screen to the background color
        self.clear()

        # Activate camera
        self.camera.use()

        # Draw scene
        self.scene.draw()


    def process_keychange(self):
        if not self.started:
            self.setup()

        # Process up/down
        if self.up_pressed:
            if (
                self.physics_engine.can_jump(y_distance=10)
            ):
                self.player_sprite.change_y = PLAYER_JUMP_SPEED

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        self.process_keychange()
    

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()


    def update_animations(self, delta_time: float):
        # Update Animations
        self.scene.update_animation(
            delta_time,
            [
                LAYER_NAME_PLAYER,
                LAYER_NAME_BRICKS,
            ],
        )

    def did_player_fall(self) -> bool: 
        return self.player_sprite.center_y < -100
    
    def on_update(self, delta_time):
        if not self.started:
            self.setup()

        self.physics_engine.update()

        # Update Animations
        self.update_animations(delta_time)

        if self.did_player_fall():
            arcade.exit()

        self.camera.position = arcade.Vec2(max(self.left_border,self.player_sprite.position[0]), self.camera.position[1])

        # All collisions
        player_collision_list = arcade.check_for_collision_with_list(
            self.player_sprite,
            self.scene[LAYER_NAME_BRICK_TRIGGERS],
        )

        # Check for collisions
        for collision in player_collision_list:
            if self.scene[LAYER_NAME_BRICK_TRIGGERS] in collision.sprite_lists:
                if isinstance(collision.object, BreakableBrick):
                    # Remove the block and the trigger from the scene
                    self.scene[LAYER_NAME_BRICKS].remove(collision.object)
                    self.scene[LAYER_NAME_BRICK_TRIGGERS].remove(collision)
                if isinstance(collision.object, SolidBrick):
                    # Change the texture of the brick
                    collision.object.texture = arcade.load_texture("assets/images/sprites/blocks/solid_brick.png")
                    self.scene[LAYER_NAME_BRICK_TRIGGERS].remove(collision)