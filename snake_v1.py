import pygame,time
import colours


screen_width = 700
screen_hight = 500
grid_size = 20
frame_rate = 10


clock = pygame.time.Clock()
quit_game = False
middle_of_screen = ((screen_width/2),(screen_hight / 2))
snake_x = (screen_width - grid_size) / 2 
snake_y = (screen_hight - grid_size) / 2
snake_x_change = 0
snake_y_change = 0


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
  
def message(msg, text_colour, bkgd_colour):
  '''
  displays a text box in the middle of the screen 
  '''
  txt = font.render(msg, True, text_colour, bkgd_colour,)
  center_of_screen = get_middle_screen()
  text_box = txt.get_rect(center = center_of_screen)
  screen.blit(txt, text_box)



#game start
pygame.init()

font = pygame.font.SysFont("arialblack", 50)

screen = pygame.display.set_mode((screen_width,screen_hight),pygame.RESIZABLE)
print(pygame.display.get_window_size(),screen_width,screen_hight)

#main game loop
while not quit_game == True:
  for event in pygame.event.get():
    #if pygame.WINDOWRESIZED:
      #screen_width, screen_hight = get_screen_size()
    if event.type == pygame.QUIT:
      quit_game = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        snake_x_change = -1 * grid_size
        snake_y_change = 0
      elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        snake_x_change = grid_size
        snake_y_change = 0
      elif event.key == pygame.K_UP or event.key == pygame.K_w:
        snake_y_change = -1 * grid_size
        snake_x_change = 0
      elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        snake_y_change = grid_size
        snake_x_change = 0

  if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_hight or snake_y < 0:
    quit_game = True
  
  snake_x += snake_x_change
  snake_y += snake_y_change
  
  screen.fill(colours.get('green'))
  
  pygame.draw.rect(screen, colours.get('red'), [snake_x, snake_y, grid_size, grid_size])
  
  pygame.display.update()
  clock.tick(frame_rate)

message ("You died!", colours.get('green'), colours.get('red'))
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()