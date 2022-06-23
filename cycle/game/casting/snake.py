import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color, initialY):
        super().__init__()
        self._segments = []
        self._color = color
        self._prepare_body(initialY)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            #segment.set_color(constants.GREEN)
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        currentVelocity = self._segments[0].get_velocity()
        # if chaging direction tail grows
        if currentVelocity.get_x() != velocity.get_x() and currentVelocity.get_y() != velocity.get_y():
            self.grow_tail(1)
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, initialY):
        x = int(constants.MAX_X / 2)
        y = initialY #int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            #color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            #segment.set_color(color)
            segment.set_color(self._color)
            self._segments.append(segment)