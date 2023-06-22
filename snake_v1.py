import pygame,time

screen_width = 700
screen_hight = 500
grid_size = 5

clock = pygame.time.Clock()
quit_game = False
snake_x = screen_width / 2
snake_y = screen_hight / 2
snake_x_change = 0
snake_y_change = 0

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_hight),pygame.RESIZABLE)
print(pygame.display.get_window_size())

while not quit_game == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit_game = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        snake_x_change = -1 * grid_size
        snake_y_change = 0
      elif event.key == pygame.K_RIGHT:
        snake_x_change = grid_size
        snake_y_change = 0
      elif event.key == pygame.K_UP:
        snake_y_change = -1 * grid_size
        snake_x_change = 0
      elif event.key == pygame.K_DOWN:
        snake_y_change = grid_size
        snake_x_change = 0

  if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_hight or snake_y < 0:
    quit_game = True
  
  snake_x += snake_x_change
  snake_y += snake_y_change
  
  screen.fill('dark green')
  
  pygame.draw.rect(screen, 'dark red', [snake_x, snake_y, grid_size, grid_size])
  
  pygame.display.update()
  clock.tick(30)

pygame.quit()