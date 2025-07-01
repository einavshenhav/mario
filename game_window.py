import arcade
from views.game_view import GameView
from platformer.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)

        self.views = {}

        self.views["game_view"] = GameView()


