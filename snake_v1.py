import random

import pygame, time
import functions as fun
from colours import colours

screen_width = 700
screen_height = 500
grid_size = 20
frame_rate = 5
middle_of_screen = ((screen_width / 2), (screen_height / 2))
score = 0

collection_size = 10

clock = pygame.time.Clock()
quit_game = False
snake_x = (screen_width - grid_size) / 2
snake_y = (screen_height - grid_size) / 2
snake_x_change = 0
snake_y_change = 0
fruit_spawned = False
fruit_x = 0 
fruit_y = 0

def message(msg, text_colour, bkgd_colour):
    '''
    displays a text box in the middle of the screen
    '''
    txt = font.render(msg, True, text_colour, bkgd_colour, )
    center_of_screen = fun.get_middle_screen()
    text_box = txt.get_rect(center=center_of_screen)
    screen.blit(txt, text_box)

def menu():
  """"""









# game start
pygame.init()

font = pygame.font.SysFont("arialblack", 50)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
print(pygame.display.get_window_size(), screen_width, screen_height)

# main game loop

while not quit_game == True:
    for event in pygame.event.get():
        # when the window is resized the screen width and height are updated
        if event.type == pygame.WINDOWRESIZED:
            screen_width, screen_height = fun.get_screen_size()

        if event.type == pygame.QUIT:
            quit_game = True

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

    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        quit_game = True

    snake_x += snake_x_change
    snake_y += snake_y_change


    screen.fill(colours['green'])
    fun.draw_snake(screen,colours,snake_x,snake_y,grid_size)



  #spawn fruit 
    fruit_x,fruit_y,fruit_spawned = fun.spawn_fruit(screen,"orange",fruit_spawned,fruit_x,fruit_y,screen_height,screen_width,grid_size)
  

    #fruit collection 
    if (snake_x <= (fruit_x + collection_size) and snake_y <= (fruit_y + collection_size)) and (snake_x >= (fruit_x - collection_size) and snake_y >= (fruit_y - collection_size)) :
        score += 1
        print(score)
        fruit_spawned = False


    pygame.display.update()
    clock.tick(frame_rate)

message("You died!", colours['green'], colours['red'])
pygame.display.update()
time.sleep(3)

pygame.quit()