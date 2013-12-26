class GameGrid:
    """A matrix for storing the full game board."""

    __slots__ = ("width", "height", "_array")

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self._array = array.array(
            "c", (chr(0) for i in xrange(width * height)))

    def get(self, i, j):
        return ord(self._array[j * self.width + i])

    def set(self, i, j, action):
        self._array[j * self.width + i] = chr(action)
