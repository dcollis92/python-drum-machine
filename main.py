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

# set up variables
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6

# create the drum machine grid


def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT], 5)
    bottom_box = pygame.draw.rect(
        screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Kick Drum', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 330))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 430))
    floor_tom_text = label_font.render('Floor Tom', True, white)
    screen.blit(floor_tom_text, (30, 530))
    # draw lines between instruments
    for i in range(instruments):
        pygame.draw.line(
            screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)
    # draw lines between beats
    # will scale with number of beats
    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen, gray, [
                                    i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)], 5, 5)


# create main game loop
run = True
while run:
    # while true, execute loop 60 times per second
    timer.tick(fps)
    # set background color
    screen.fill(black)
    # invoke draw_grid function
    draw_grid()

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.flip()
    # quit pygame
pygame.quit()
