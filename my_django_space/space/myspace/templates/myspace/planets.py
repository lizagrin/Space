import random
from vpython import sphere
sphere()
#
# import pygame
# import sys
#
# # We will work with Vector2 because it has some useful functions.
# from pygame.math import Vector2
#
# from random import randrange
#
# import ctypes
#
# # Enable High Dots Per Inch so the image displayed on the window is sharper.
# ctypes.windll.shcore.SetProcessDpiAwareness(1)
#
# # Configuration
# pygame.init()
# fps = 60
# fpsClock = pygame.time.Clock()
#
# # Window Size
# windowdim = Vector2(800, 800)
# screen = pygame.display.set_mode((int(windowdim.x), int(windowdim.y)))
# planets = []
#
#
# class Planet():
#     def __init__(self, position, delta=Vector2(0, 0), radius=10, imovable=False):
#
#         # Where the planet is at the moment
#         self.position = position
#
#         # The Radius determines how much this planet affects others
#         self.radius = radius
#
#         # The Velocity
#         self.delta = delta
#
#         # If this planet is moving
#         self.imovable = imovable
#
#         # If this planet can be eaten by others.
#         self.eatable = False
#
#         # Appending itself to the list so its process
#         # function will later be called in a loop.
#         planets.append(self)
#
#     def process(self):
#         # This function will be called once every frame
#         # and it is responsible for calculating where the planet will go.
#
#         # No Movement Calculations will happen if the planet doesnt move at all.
#         # it also wont be eaten.
#         if not self.imovable:
#             for i in planets:
#                 if not i is self:
#                     try:
#                         if self.eatable:
#                             if self.position.distance_to(i.position) < self.radius + i.radius:
#                                 print('Eaten')
#                                 i.radius += self.radius
#                                 planets.remove(self)
#                         dir_from_obj = (i.position - self.position).normalize() * 0.01 * (i.radius / 10)
#                         self.delta += dir_from_obj
#                     except:
#                         print('In the same spot')
#
#             self.position += self.delta
#
#         # Drawing the planet at the current position.
#         pygame.draw.circle(
#             screen,
#             [255, 255, 255],
#             self.position,
#             self.radius,
#         )
#
#
# # Game loop.
# while True:
#     screen.fill((0, 0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     for p in planets:
#         p.process()
#
#     pygame.display.flip()
#     fpsClock.tick(fps)
#
#     # Sun and two opposing Planets
#     Planet(Vector2(400, 400), radius=50, imovable=True)
#
#     Planet(Vector2(400, 200), delta=Vector2(3, 0), radius=10)
#     Planet(Vector2(400, 600), delta=Vector2(-3, 0), radius=10)
