# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	pygame.init()
	timer = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	# GAME LOOP
	while True:
		for event in pygame.event.get():		# Closing the window will exit the game loop
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		player.draw(screen)
		player.update(dt)
		pygame.display.flip()
		dt = timer.tick(60) / 1000

if __name__ == "__main__":
	main()
