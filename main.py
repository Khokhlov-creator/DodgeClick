"""
This is main file of DodgeClick game
Hey there!
"""
# NOTE: it is good to have a docstring for each file and function. Docstrings are defined by triple """
import sys
import pygame
from enum import Enum


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
		# Define screen size:
		self.screen = pygame.display.set_mode((640, 480))
		# Define rectangular size:
		self.rect = pygame.Rect(40, 200, 20, 20)
		# Set the main rectangular color
		self.rect_color = (255, 45, 45)

		# TODO: u may add new figures here

	def _move_mouse(self, mouse_direction):
		"""
		This is private function -> it has underscore _ before the name
		This means the function should be called only from the inside of the class
		You should not call it from the main function for example
		"""
		pygame.time.wait(10)
		self.screen.fill((0, 0, 0))

		pygame.draw.rect(self.screen, (69, 45, 45), self.rect, 0)

		if mouse_direction == MouseDirection.UP:  # You may see how good it is to have enums. U just look at code and understands what it means
			self.rect.move_ip(4, 4)  # This magic 4 can be a class attribute -> self.horizontal/vertical_offset
		elif mouse_direction == MouseDirection.DOWN:
			self.rect.move_ip(4, -4)

		pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 0)

	def mouse_down(self):  # NOTE: use CamelCase in Python only for class names, functions_should_be_names_like_this
		"""
		Moves mouse down
		"""
		self._move_mouse(MouseDirection.DOWN)

	def mouse_up(self):  # NOTE: use CamelCase in Python only for class names, functions_should_be_names_like_this
		"""
		Moves mouse down
		"""
		self._move_mouse(MouseDirection.UP)

	def quite_game(self):
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
					self.quite_game()

				if event.type == pygame.MOUSEBUTTONDOWN:
					print('Hey DOWN')
					self.mouse_down()

				if event.type == pygame.MOUSEBUTTONUP:
					print('Hey UP')
					self.mouse_up()

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
