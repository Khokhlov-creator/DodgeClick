"""
This is main file of DodgeClick game
Hey there!
"""
# NOTE: it is good to have a docstring for each file and function. Docstrings are defined by triple """
import sys
import pygame
import random
import typing

from enum import Enum

walls_locations = [300]

WINDOW_SIZE = 480, 640


class Wall:
	def __init__(self, x=100, y=100, w=20, h=20, color=(86, 135, 95)):
		self.w = w
		self.h = h
		self.x = x
		self.y = y
		self.body = pygame.Rect(x, y, w, h)
		self.color = color

	def set_position(self, new_x, new_y):
		self.body.update(new_x, new_y, self.w, self.h)

	def move(self, new_x, new_y):
		self.body.move_ip(new_x, new_y)

	def set_size(self, new_w, new_h):
		self.body.update(self.x, self.y, new_w, new_h)

	def get_current_x_position(self):
		return self.x

	def is_up_wall(self):
		return self.y < WINDOW_SIZE[0] / 2


neq_wall = Wall(200, 200)


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
		screenheight, screenwidth = WINDOW_SIZE
		# Define screen size:
		self.screen = pygame.display.set_mode((screenwidth, screenheight))
		# Define rectangular size:
		self.player = pygame.Rect(180, 200, 20, 20)
		# Set the main rectangular color
		self.player_color = (255, 45, 45)
		self.wall_color = (86, 135, 95)
		# self.rect_2 = pygame.Rect(175, 200, 10, 18)
		# self.rect_3 = pygame.Rect(170, 205, 5, 9)
		# self.wall_upper = pygame.Rect(620, 0, 20, height_wall - 90)
		# self.wall_bottom = pygame.Rect(620, height_wall + 90, 20, 480)

		self.walls: typing.List[Wall] = []
		self.init_walls()
	def init_walls(self):

		random_height = random.randint(120, 400)
		random_wall_offset = random.randint(100, 400)

		xs = [620, 620, 620 + random_wall_offset, 620 + 2 * random_wall_offset]
		ys = [random_height - 90, random_height + 90, random_height - 90, random_height + 90]

		for x, y in zip(xs, ys):
			new_wall = Wall(x, y, 20, 300)
			self.walls.append(new_wall)

	# TODO: u may add new figures here
	def draw_rect(self, rectangle: Wall):
		pygame.draw.rect(self.screen, rectangle.color, rectangle.body)

	def _move_mouse(self, mouse_direction):
		"""
		This is private function -> it has underscore _ before the name
		This means the function should be called only from the inside of the class
		You should not call it from the main function for example
		"""
		offset_x, offset_y = 0, 4
		pygame.time.wait(10)
		self.screen.fill((0, 0, 0))
		if self.player.bottom == 480 or self.player.top == 0:
			offset_y = 0  # TODO: make it as GAME OVER

		for wall in self.walls:
			self.draw_rect(wall)

			if pygame.Rect.colliderect(self.player, wall) or pygame.Rect.colliderect(self.player, wall):
				offset_y = 0
				wall.move(2, 0)

			wall.move(-2, 0)

		if mouse_direction == MouseDirection.UP:  # You may see how good it is to have enums. U just look at code and understands what it means
			self.player.move_ip(offset_x, offset_y)  # This magic 4 can be a class attribute -> self.horizontal/vertical_offset

		elif mouse_direction == MouseDirection.DOWN:
			self.player.move_ip(offset_x, -offset_y)

		pygame.draw.rect(self.screen, (255, 0, 0), self.player, 0)

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
				pygame.draw.rect(self.screen, self.player_color, self.player, 0)

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
