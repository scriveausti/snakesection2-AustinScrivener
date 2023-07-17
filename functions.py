import pygame , math
import random as ran


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
    print(screen_width, screen_height)
    middle_of_screen = (screen_width / 2, screen_height / 2)

    return middle_of_screen


def draw_snake(screen,
               colours,
               snake_x: int,
               snake_y: int,
               grid_size: int):
    """
  draws the head of the snake
  """
    pygame.draw.rect(screen, colours['red'], [snake_x, snake_y, grid_size, grid_size])


def snake_tail(score: int):
    """

    """
    snake_length = score

def generate_fruit(screen_height, screen_width, grid_size):
    new_fruit_x = (ran.randint(0, round(screen_width / grid_size))) * grid_size
    new_fruit_y = (ran.randint(0, round(screen_height / grid_size))) * grid_size
    return new_fruit_x, new_fruit_y


def spawn_fruit(screen, colours, fruit_spawned, fruit_x, fruit_y, screen_height, screen_width, grid_size):
    """

    """
    if fruit_spawned == False:
        new_fruit_x, new_fruit_y = generate_fruit(screen_height, screen_width, grid_size)
        print(fruit_x,fruit_y)
        pygame.draw.rect(screen, colours['orange'], [new_fruit_x, new_fruit_y, grid_size, grid_size])
        pygame.draw.rect(screen, colours['orange'], [new_fruit_x, new_fruit_y, grid_size, grid_size])
        spawned = True
        return new_fruit_x, new_fruit_y, spawned
    else:
        return fruit_x, fruit_y, fruit_spawned
