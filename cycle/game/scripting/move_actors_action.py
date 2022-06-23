from game.scripting.action import Action


""" MoveActorsAction class helps update the position of the actors """
class MoveActorsAction:
    def __init__(Action) -> None:
        pass

    # Override the execute(cast, script) method as follows:
    def execute(self,cast, script):
    # get all the actors from the cast
        actors  = cast.get_all_actors()
        # loop through the actors
        for actor in actors:
            #call the move_next() method on each actor
            actor.move_next()