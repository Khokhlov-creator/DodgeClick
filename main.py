"""
This is main file of DodgeClick game
Hey there!
"""
# NOTE: it is good to have a docstring for each file and function. Docstrings are defined by triple """
import sys
import pygame
import random
import array as arr
from queue import Queue
from enum import Enum

walls_locations = [300]


class Walls:
    def __init__(self):
        self.walls_color = (86, 135, 95)
        self.walls_x = walls_locations
        self.random.randint(120, 400)
        self.wall


class Collision:
    def __init__(self):
        pass


class MouseDirection(Enum):
    """
	Enumerate class that defines UP and DOWN mouse directions
	U just specify, that 0 is for UP and 1 is for DOWN,
	but in code it is more readable
	"""
    UP = 0
    DOWN = 1


class DodgeClick:
    """
	This is main class for the game
	The benefit of having a class, that u can have class attributes (self.something),
	that can be called from any class method, so u don't need to pass function input again and again
	"""

    def __init__(self):
        """
		This is initialization function, when u run DodgeClick() -> this part is called
		So run everything u want to initialize here
		"""
        # Init PyGame:
        pygame.init()
        height_wall = random.randint(120, 400)
        # height_wall_bot =
        screenheight, screenwidth = 480, 640
        my_walls = Walls
        # Define screen size:
        self.screen = pygame.display.set_mode((screenwidth, screenheight))
        # Define rectangular size:
        self.rect = pygame.Rect(180, 200, 20, 20)
        # Set the main rectangular color
        self.rect_color = (255, 45, 45)
        self.rect_2 = pygame.Rect(175, 200, 10, 18)
        self.rect_3 = pygame.Rect(170, 205, 5, 9)

        self.wall_upper_1_front = pygame.Rect(620, 0, 20, height_wall - 90)
        self.wall_bottom_1_front = pygame.Rect(620, height_wall + 90, 20, 480)
        self.wall_upper_2_front = pygame.Rect(780, 0, 20, height_wall - 90)
        self.wall_bottom_2_front = pygame.Rect(780, height_wall + 90, 20, 480)
        self.wall_upper_3_front = pygame.Rect(940, 0, 20, height_wall - 90)
        self.wall_bottom_3_front = pygame.Rect(940, height_wall + 90, 20, 480)
        self.q = Queue(maxsize=6)

    # TODO: u may add new figures here

    def _move_mouse(self, mouse_direction):
        """
		This is private function -> it has underscore _ before the name
		This means the function should be called only from the inside of the class
		You should not call it from the main function for example
		"""
        offset_x, offset_y = 0, 4
        pygame.time.wait(10)
        self.screen.fill((0, 0, 0))
        if self.rect.bottom == 480 or self.rect.top == 0:
            offset_y = 0  # TODO: make it as GAME OVER
        pygame.draw.rect(self.screen, (69, 45, 45), self.rect_2, 0)
        pygame.draw.rect(self.screen, (69, 45, 45), self.rect_3, 0)
        self.walls = list
        #for x in range(Queue.maxsize):
        pygame.draw.rect(self.screen, (86, 135, 95), self.wall_upper_1_front)
        pygame.draw.rect(self.screen, (86, 135, 95), self.wall_bottom_1_front)

        pygame.draw.rect(self.screen, (86, 135, 95), self.wall_upper_2_front)
        pygame.draw.rect(self.screen, (86, 135, 95), self.wall_bottom_2_front)

        pygame.draw.rect(self.screen, (86, 135, 95), self.wall_upper_3_front)
        pygame.draw.rect(self.screen, (86, 135, 95), self.wall_bottom_3_front)

        self.queued_wall_upper=self.wall_upper_1_front
        self.queued_wall_bottom=self.wall_bottom_1_front

        if pygame.Rect.colliderect(self.rect, self.queued_wall_upper) or pygame.Rect.colliderect(self.rect,
                                                                                                  self.queued_wall_bottom):
            offset_y = 0
            self.wall_upper_1_front.move_ip(+2, 0)
            self.wall_bottom_1_front.move_ip(+2, 0)
            self.wall_upper_2_front.move_ip(+2, 0)
            self.wall_bottom_2_front.move_ip(+2, 0)
            self.wall_upper_3_front.move_ip(+2, 0)
            self.wall_bottom_3_front.move_ip(+2, 0)
        elif self.queued_wall_upper.x < self.rect.x:
            self.queued_wall_bottom = self.wall_bottom_2_front
            self.queued_wall_upper = self.wall_upper_2_front
            self.wall_upper_2_front = self.wall_upper_3_front
            self.wall_bottom_2_front = self.wall_bottom_3_front


        if mouse_direction == MouseDirection.UP:  # You may see how good it is to have enums. U just look at code and understands what it means
            self.rect.move_ip(offset_x,
                              offset_y)  # This magic 4 can be a class attribute -> self.horizontal/vertical_offset
            self.rect_2.move_ip(offset_x, offset_y)
            self.rect_3.move_ip(offset_x, offset_y)
            self.wall_upper_1_front.move_ip(-2, 0)
            self.wall_bottom_1_front.move_ip(-2, 0)
            self.wall_upper_2_front.move_ip(-2, 0)
            self.wall_bottom_2_front.move_ip(-2, 0)
            self.wall_upper_3_front.move_ip(-2, 0)
            self.wall_bottom_3_front.move_ip(-2, 0)

        elif mouse_direction == MouseDirection.DOWN:
            self.rect.move_ip(offset_x, -offset_y)
            self.rect_2.move_ip(offset_x, -offset_y)
            self.rect_3.move_ip(offset_x, -offset_y)
            self.wall_upper_1_front.move_ip(-2, 0)
            self.wall_bottom_1_front.move_ip(-2, 0)
            self.wall_upper_2_front.move_ip(-2, 0)
            self.wall_bottom_2_front.move_ip(-2, 0)
            self.wall_upper_3_front.move_ip(-2, 0)
            self.wall_bottom_3_front.move_ip(-2, 0)

        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 0)

    def mouse_down(self):  # NOTE: use CamelCase in Python only for class names, functions_should_be_names_like_this
        """
		Moves mouse down
		"""
        self._move_mouse(MouseDirection.DOWN)

    def mouse_up(self):  # NOTE: use CamelCase in Python only for class names, functions_should_be_names_like_this
        """
		Moves mouse up
		"""
        self._move_mouse(MouseDirection.UP)

    def quit_game(self):
        """
		Quites the game
		"""
        pygame.quit()
        sys.exit()

    def run_main_loop(self):
        """
		This can be the main loop which runs everything for the game
		"""
        while True:
            for event in pygame.event.get():
                pygame.draw.rect(self.screen, self.rect_color, self.rect, 0)

            if event.type == pygame.QUIT:
                self.quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down()

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_up()

            if event.type == pygame.MOUSEMOTION:
                pass
            pygame.display.flip()


def main():
    # Init game class:
    game = DodgeClick()
    # Run main loop:
    game.run_main_loop()


# This is the entry point - python runs program from here
if __name__ == "__main__":
    # It is better to call main function from here
    # Otherwise the variables assigned here will be global -> possible naming errors
    # (you may accidentally call global var from local function)
    main()
