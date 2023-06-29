import pygame


def get_screen_size():
  '''
  this gives the screen width and hight
  outputs a tulip (screen_width,screen_hight)
  '''
  return pygame.display.get_window_size()

def get_middle_screen():
  '''
  This returns the x and y positionss of the middle of the output screen 
  outputs a tulip (middle_x, middle_y)
  '''
  screen_width,screen_hight = get_screen_size()
  print(screen_width,screen_hight)
  middle_of_screen = (screen_width/2,screen_hight/2)
  
  return middle_of_screen