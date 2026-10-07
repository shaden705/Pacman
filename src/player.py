import sys
from typing import Tuple

try:
    import pygame
except ModuleNotFoundError as e:
    print(e)
    sys.exit(1)
from src.maze_render import MazeRender


class Player:
    """manage the pacman player and its movement"""
    def __init__(self, start_point: Tuple, maze: MazeRender) -> None:
        """set the players starting position and load its images"""
        self.row, self.col = start_point
        self.dir = ""
        self.maze = maze
        self.img_size = max(1, self.maze.cell_size - 10)
        player_surface_up = pygame.image.load(
            "src/Graphics/player_up.png").convert_alpha()
        player_surface_down = pygame.image.load(
            "src/Graphics/player_down.png").convert_alpha()
        player_surface_right = pygame.image.load(
            "src/Graphics/player_left.png").convert_alpha()
        player_surface_left = pygame.image.load(
            "src/Graphics/player_right.png").convert_alpha()

        self.img_up = pygame.transform.scale(
            player_surface_up, (self.maze.cell_size, self.maze.cell_size)
        )
        self.img_down = pygame.transform.scale(
            player_surface_down, (self.maze.cell_size, self.maze.cell_size)
        )
        self.img_left = pygame.transform.scale(
            player_surface_left, (self.maze.cell_size, self.maze.cell_size)
        )
        self.img_right = pygame.transform.scale(
            player_surface_right, (self.maze.cell_size, self.maze.cell_size)
        )

    def draw(self, screen: pygame.Surface) -> None:
        """draw the player at its current position"""
        if self.dir == "up" or self.dir == "":
            img = self.img_up
        elif self.dir == "down":
            img = self.img_down
        elif self.dir == "right":
            img = self.img_right
        elif self.dir == "left":
            img = self.img_left
        if self.maze.maze[self.row][self.col] == 15:
            while self.col > 0 and self.maze.maze[self.row][self.col] == 15:
                self.col -= 1
        x = (self.col * self.maze.cell_size) + self.maze.margin_maze_col  # row

        y = (self.row * self.maze.cell_size) + self.maze.margin_maze_row  # col

        offset = (self.maze.cell_size - img.get_width()) // 2
        screen.blit(img, (x + offset, y + offset))

    def move(self) -> None:
        """moving players in that dir"""
        cell = self.maze.maze[self.row][self.col]
        if self.dir == "up" and not (cell & 1):
            self.row -= 1
        if self.dir == "right" and not (cell & 2):
            self.col += 1
        if self.dir == "left" and not (cell & 8):
            self.col -= 1
        if self.dir == "down" and not (cell & 4):
            self.row += 1
