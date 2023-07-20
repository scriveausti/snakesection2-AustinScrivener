import pygame
import random as ran
from colours import colours




def get_screen_size():
    """
  this gives the screen width and height
  outputs a tulip (screen_width,screen_height)
  """
    return pygame.display.get_window_size()


def get_middle_screen():
    """
  This returns the x and y positions of the middle of the output screen
  outputs a tulip (middle_x, middle_y)
  """
    screen_width, screen_height = get_screen_size()
    print('screen width: {}, screen height: {}'.format(screen_width, screen_height))
    middle_of_screen = (screen_width / 2, screen_height / 2)

    return middle_of_screen


def draw_snake(screen,
               colour,
               snake_x,
               snake_y,
               grid_size: int):
    """
  draws the head of the snake
  """
    pygame.draw.rect(screen, colours[colour], [snake_x, snake_y, grid_size, grid_size])


def generate_fruit(screen_height, screen_width, grid_size,fruit_size):
  """
  generates a random poin on screen that on the same grid as the snake 
  """
  
  new_fruit_x = (ran.randint(fruit_size, round(((screen_width-(grid_size*2)) / grid_size))) * grid_size)+grid_size
  new_fruit_y = (ran.randint(fruit_size, round(((screen_height-(grid_size*2)) / grid_size))) * grid_size)+grid_size
  return new_fruit_x, new_fruit_y


def spawn_fruit(screen, colour: str, fruit_spawned, fruit_x, fruit_y, screen_height, screen_width, grid_size,fruit_size):
    """
    draws the fruit and if there is no fruit on screen it will generate a new one 
    """
    if fruit_spawned == False:
        new_fruit_x, new_fruit_y = generate_fruit(screen_height, screen_width, grid_size,fruit_size)
        print("fruit x: {}, fruit y: {}".format(fruit_x,fruit_y))
        spawned = True
        pygame.draw.rect(screen, colours[colour], [new_fruit_x, new_fruit_y, fruit_size, fruit_size])
        return new_fruit_x, new_fruit_y, spawned
    else:
        pygame.draw.rect(screen, colours[colour], [fruit_x, fruit_y, fruit_size, fruit_size])
        return fruit_x, fruit_y, fruit_spawned
