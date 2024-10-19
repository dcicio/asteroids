# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()			# Group of objects that will need to be updated in the game loop
	drawable = pygame.sprite.Group()			# Group of objects that will need to be drawn in the game loop
	Player.containers = (updatable, drawable)
	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#	print("Starting asteroids!")
#	print(f"Screen width: {SCREEN_WIDTH}")
#	print(f"Screen height: {SCREEN_HEIGHT}")


	# GAME LOOP
	while True:
		for event in pygame.event.get():		# Closing the window will exit the game loop
			if event.type == pygame.QUIT:
				return

		screen.fill("black")

		for obj in updatable:
			obj.update(dt)
		
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000				# Limit framerate to 60 FPS

if __name__ == "__main__":
	main()
