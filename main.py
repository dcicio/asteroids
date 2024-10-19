# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()			# Group of objects that will need to be updated in the game loop
	drawable = pygame.sprite.Group()			# Group of objects that will need to be drawn in the game loop
	asteroids = pygame.sprite.Group()			# Group of objects that are asteroids
	shots = pygame.sprite.Group()				# Group of objects that are shots
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable,)
	Shot.containers = (updatable, drawable, shots)
	
	asteroidfield = AsteroidField()
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


	# GAME LOOP
	while True:
		for event in pygame.event.get():		# Closing the window will exit the game loop
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)
		
		for obj in asteroids:
			if player.check_collision(obj):
				print("Game over!")
				sys.exit()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000				# Limit framerate to 60 FPS

if __name__ == "__main__":
	main()
