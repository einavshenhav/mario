import arcade
from views.view import View

class GameView(View):
    def __init__(self):
        super().__init__()

    def setup(self):
        super().setup()
        
    def on_show_view(self):
        self.window.background_color = arcade.color.CORNFLOWER_BLUE

    def on_draw(self):
        self.clear()