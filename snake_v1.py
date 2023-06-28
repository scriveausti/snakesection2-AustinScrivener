import pygame,time

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


'format colour : rgb value (tulip)'

colours = {
  'black':  (0,0,0),
  'white':  (255,255,255),
  'green':  (0,255,0),
  'red':    (255,0,0),
  'blue' :  (0,0,255)
}

def get_middle_screen():
  '''
  This it the middle of the output screen 
  outputs a tulip (middle x, middle y)
  '''
  screen_width,screen_hight = pygame.display.get_window_size()
  print(screen_width,screen_hight)
  middle_of_screen = (screen_width/2,screen_hight/2)
  
  return middle_of_screen

pygame.init()

font = pygame.font.SysFont("arialblack", 50)

def message(msg, text_colour, bkgd_colour):
  '''
  displays a text box in the middle of the screen 
  '''
  txt = font.render(msg, True, text_colour, bkgd_colour,)
  center_of_screen = get_middle_screen()
  text_box = txt.get_rect(center = center_of_screen)
  screen.blit(txt, text_box)

screen = pygame.display.set_mode((screen_width,screen_hight),pygame.RESIZABLE)
print(pygame.display.get_window_size(),screen_width,screen_hight)

while not quit_game == True:
  for event in pygame.event.get():
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
  
  screen.fill('dark green')
  
  pygame.draw.rect(screen, 'dark red', [snake_x, snake_y, grid_size, grid_size])
  
  pygame.display.update()
  clock.tick(frame_rate)

message ("You died!", 'dark green', "dark red")
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()