import enum 
import random
from typing import List, Tuple

class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        return Position(
            self.x + direction.x,
            self.y + direction.y
        )
    
    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False
    
    def __hash__(self):
        return hash(
            (self.x, self.y)
        )
    
    def __str__(self):
        return "{0}(x={1}, y={2})".format(
            self.__class__.__name__,
            self.x,
            self.y,
        )
    
class Direction(Position, enum.Enum):
    UP = 0, -1
    DOWN = 0, 1
    LEFT = -1, 0
    RIGHT = 1, 0
        
    def reverse(self):
        return _REVERSE_MAP[self]
    
    _REVERSE_MAP = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT,
    }

class Cell(object):
    def __init__(self):
        self.cell_type = " "
        self.walls = {
            Direction.UP: True,
            Direction.DOWN: True,
            Direction.LEFT: True,
            Direction.RIGHT: True,
        }
    
    def open(self, direction):
        self.walls[direction] = False
    
    def is_open(self, direction):
        return not self.walls[direction]

def rand_position(width, height):
    return Position(
        x=random.randint(0, width - 1),
        y=random.randint(0, height - 1)
    )

def is_out_of_bounds(pos, width, height):
    return pos.x < 0 or pos.x >= width or pos.y < 0 or pos.y >= height

def open_walls(grid, pos, direction):
    neighbor = pos.move(direction)
    grid[pos.y][pos.x].open(direction)
    grid[neighbor.y][neighbor.x].open(direction.reverse())

def gen_neighbors(pos, width, height):
    neighbors = []
    for direction in Direction:
        neighbor = pos.move(direction)
        if not is_out_of_bounds(neighbor, width, height):
            neighbors.append((neighbor, direction))
    return neighbors

def dfsmap(width, height):
    grid = [[Cell() for _ in range(width)] for _ in range(height)]

    # Init search
    pos = rand_position(width, height)
    neighbors = gen_neighbors(pos, width, height)
    random.shuffle(neighbors)

    fringe = [(pos, neighbors)]
    visited = {pos}

    # Explore
    while fringe:
        pos, neighbors = fringe[-1]
        neighbor, direction = neighbors.pop()

        if not neighbors:
            fringe.pop()
        
        if neighbor not in visited:
            visited.add(neighbor)
            open_wall(grid, pos, direction)
            new_neighbors = gen_neighbors(neighbor, width, height)
            fringe.append((neighbor, gen_neighbors(neighbor, width, height)))
    
    return grid

def to_layout(grid):
    height = len(grid)
    width = len(grid[0])

    layout = [["%" for _ in range(2 * width + 1)] for _ in range(2 * height + 1)]

    for y_pos, row in enumerate(grid):
        layout_y = 2 * y_pos + 1
        for x_pos, cell in enumerate(row):
            layout_x = 2 * x_pos + 1
            layout_p = Position(layout_x, layout_y)

            layout[layout_p.y]
            for direction in Direction:
                if cell.is_open(direction):
                    pos = layout_p.move(direction)
                    layout[pos.y][pos.x]


if __name__ == "__main__":
    width = 20
    height = 20
    grid = dfsmap(width, height)

    pacman_pos = rand_position(width, height)
    food_pos = rand_position(width, height)
    while pacman_pos == food_pos:
        food:pos = rand_position(width, height)
    
    grid[pacman_pos.y[pacman_pos.x].cell_type] = "P"
    grid[food_pos.y][food_pos.x].cell_type = "."

    layout = to_layout()