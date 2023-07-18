import random
import pygame, time
import functions as fun
from colours import colours



snake_colour = 'red'
fruit_colour = 'orange'

frame_rate = 6
screen_width = 700
screen_height = 500

grid_size = 20

middle_of_screen = ((screen_width / 2), (screen_height / 2))
score = 0
highscore = 0

clock = pygame.time.Clock()
playing = True
snake_x = (screen_width - grid_size) / 2
snake_y = (screen_height - grid_size) / 2
snake_x_change = 0
snake_y_change = 0

snake_pos_been = []

fruit_spawned = False
fruit_x = 0 
fruit_y = 0
fruit_size = 20
fruit_collection_size = (fruit_size/2)

tail_pos_x = {}
tail_pos_y = {}

background_colour = colours['green']

score_and_highscore_space_from_border = 10



def message(msg, text_colour, bkgd_colour):
    '''
    displays a text box in the middle of the screen
    '''
    txt = font.render(msg, True, text_colour, bkgd_colour)
    center_of_screen = fun.get_middle_screen()
    text_box = txt.get_rect(center=center_of_screen)
    screen.blit(txt, text_box)

def ui(score,highscore,space_from_border):
  """
  displays score and highscore
  
  """
  
  text_colour = colours['black']
  bkgd_colour = None
  #draw score 
  txt = font.render(('score: {}'.format(score)), True, text_colour, bkgd_colour)
  text_box = txt.get_rect(topleft= (space_from_border,space_from_border))
  screen.blit(txt, text_box)

  #draw highscore
  txt = font.render(('highscore: {}'.format(highscore)), True, text_colour, bkgd_colour)
  screen_width, screen_height = fun.get_screen_size()
  text_box = txt.get_rect(topright=((screen_width - space_from_border),space_from_border))
  screen.blit(txt, text_box)

# game start
pygame.init()

font = pygame.font.SysFont("comicsans", 50)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
print(pygame.display.get_window_size(), screen_width, screen_height)

# main game loop

while playing:
    for event in pygame.event.get():
        # when the window is resized the screen width and height are updated
        if event.type == pygame.WINDOWRESIZED:
            screen_width, screen_height = fun.get_screen_size()

        if event.type == pygame.QUIT:
            playing = False

        # snake movement
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


  
    if snake_x >= screen_width - grid_size or snake_x < 0 or snake_y >= screen_height - grid_size or snake_y < 0:
        playing = False


    #update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change
  
    #clears the past frame 
    screen.fill(background_colour)
    #draws head of snake
    fun.draw_snake(screen,snake_colour,snake_x,snake_y,grid_size)
    


    #spawn fruit 
    fruit_x,fruit_y,fruit_spawned = fun.spawn_fruit(screen,fruit_colour,fruit_spawned,fruit_x,fruit_y,screen_height,screen_width,grid_size,fruit_size)
  


    #fruit collection 
    if (snake_x <= (fruit_x + fruit_collection_size) and snake_y <= (fruit_y + fruit_collection_size)) and (snake_x >= (fruit_x - fruit_collection_size) and snake_y >= (fruit_y - fruit_collection_size)) :
        score += 1
        print(score)
        fruit_spawned = False

    #snakes history 
    snake_pos_been.insert(0,snake_y)
    snake_pos_been.insert(0,snake_x)
    #clears unused things to make list shorter 
    if len(snake_pos_been) > (score * 2)+6:
      snake_pos_been.pop((score * 2)+5)
      snake_pos_been.pop((score * 2)+6)



  #draws snakes tail
    i =2
    while i < ((score*2)+2):
      tail_x = snake_pos_been[i]
      tail_y = snake_pos_been[i+1]
      tail_pos_x[int((i-2)/2)] = (tail_x)
      tail_pos_y[int((i-2)/2)] = (tail_y)
      pygame.draw.rect(screen, colours['dark red'], [tail_x, tail_y, grid_size, grid_size])
      i += 2

      if snake_y == tail_y and snake_x == tail_x:
        playing = False
  

    ui(score, highscore ,score_and_highscore_space_from_border)
      
    pygame.display.update()
    clock.tick(frame_rate)

message("You died!", colours['red'], None)
pygame.display.update()
time.sleep(3)

pygame.quit()