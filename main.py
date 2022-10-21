# import pygame module in this program
import pygame
from pygame import mixer
# activate the pygame library
pygame.init()

# define the screen width and height
WIDTH = 1400
HEIGHT = 800

# define color variables
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# create the display surface object
screen = pygame.display.set_mode([WIDTH, HEIGHT])
# set the pygame window name
pygame.display.set_caption('Beat Maker')
# create a font object
label_font = pygame.font.Font('Roboto-Bold.ttf', 32)

# set up framerate
fps = 60
# set up clock
timer = pygame.time.Clock()

# create main game loop
run = True
while run:
  # while true, execute loop 60 times per second
  timer.tick(fps)
  # set background color
  screen.fill(black)

  # check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  # update display
  pygame.display.flip()
  # quit pygame
pygame.quit()