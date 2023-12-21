class Point:
    """Stores the x and y coordinates of point"""

    x_coordinate = 0
    y_coordinate = 0

    def __init__(self, x_coordinate, y_coordinate):
        """ Calls set_point(), so the x_coordinate and y_coordinate can be set

            :parameter x_coordinate: float; the value of the point's x coordinate
            :parameter y_coordinate: float; the value of the point's y coordinate

            :returns: None
        """

        self.set_coordinates(x_coordinate, y_coordinate)

    def set_coordinates(self, x_coordinate, y_coordinate):
        """ Sets the x_coordinate and y_coordinate can be set

            :parameter x_coordinate: float; the value of the point's x coordinate
            :parameter y_coordinate: float; the value of the point's y coordinate

            :returns: None
        """

        self.x_coordinate, self.y_coordinate = x_coordinate, y_coordinate

    def get_copy(self):
        """:returns: Point; a copy of this point"""

        return Point(self.x_coordinate, self.y_coordinate)