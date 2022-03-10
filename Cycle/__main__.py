import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.player1 import Player1
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    P1 = Player1()
    P2 = Player1()
    P1.set_color(constants.GREEN)
    P1.set_position(Point(300, 300))
    P2.set_color(constants.RED)
    P2.set_position(Point(600, 300))
    cast.add_actor("player1", P1)
    cast.add_actor("player2", P2)
    P1 = cast.get_first_actor("player1")
    P2 = cast.get_first_actor("player2")

    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()