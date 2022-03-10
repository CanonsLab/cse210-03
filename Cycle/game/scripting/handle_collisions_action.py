from game.casting.player1 import Player1
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        Player1 = cast.get_first_actor("player1")
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        Player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        head = Player1.get_segments()[0]
        head2 = player2.get_segments()[0]
        segments = Player1.get_segments()[1:]
        segments2 = player2.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()) or head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
            

        for segment2 in segments2:
            if head2.get_position().equals(segment2.get_position()) or head.get_position().equals(segment2.get_position()):
                self._is_game_over = True
        
         
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            Player1 = cast.get_first_actor("player1")
            Player2 = cast.get_first_actor("player2")
            segments = Player1.get_segments()
            segments2 = Player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            Player1.set_color(constants.WHITE)
            Player2.set_color(constants.WHITE)
            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)