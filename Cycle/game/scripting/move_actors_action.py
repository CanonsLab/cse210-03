from game.scripting.action import Action
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.player1 import Player1

# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor
class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        actors = cast.get_all_actors()
        snake = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        snake.grow_tail(1)
        player2.grow_tail(1)
        for actor in actors:
            actor.move_next()
        