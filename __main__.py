import arcade
from game_window import GameWindow

def main() -> None:
    window = GameWindow()
    window.show_view(window.views["game_view"])
    arcade.run()

if __name__ == "__main__":
    main()