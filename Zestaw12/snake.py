# Marlena Gryt
# Python 2022/2023
# Zd. 12.3

import pygame
import random
import sys

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# import food images
good_food_img = pygame.image.load("assets/apple.png")
bad_food_img = pygame.image.load("assets/rotten_apple.png")

# display end screen
def end_game(result):
    if result == 0:
        img = pygame.image.load("assets/game_over.png")
    else:
        img = pygame.image.load("assets/you_win.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(black)
        rect = img.get_rect()
        rect.midtop = (window_size[0]*0.5, 0)
        screen.blit(img, rect)
        font = pygame.font.SysFont('times new roman', 20)
        score_surface = font.render('Your score: ' + str(score), False, white)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (window_size[0]*0.5, window_size[1]*0.8)
        screen.blit(score_surface, score_rect)
        pygame.display.update()

pygame.init()
window_size = 500, 500
screen = pygame.display.set_mode(window_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Snake")
frame_rate = pygame.time.Clock()

# set snake starting position
snake_pos = [100, 250]
snake_body = [[100, 250]]

# set food starting position
food_pos = [random.randrange(1, (window_size[0]// 10))*10, random.randrange(1, (window_size[1]//10))*10]
food_spawn = True
food_timer = pygame.time.get_ticks()
food_type = "good"

score = 0
snake_size = 1
game_timer = pygame.time.get_ticks()
direction = 'RIGHT'
new_direction = direction

playing = False
while not playing:
    # check for enter or quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                playing = True
    # display the start screen
    screen.fill(black)
    title_img = pygame.image.load("assets/snake_title.png")
    screen.fill(black)
    title_rect = title_img.get_rect()
    title_rect.midtop = (window_size[0]*0.5, 0)
    screen.blit(title_img, title_rect)
    start_message_font = pygame.font.SysFont('times new roman', 20)
    start_message_surface = start_message_font.render('Hit enter to start', False, white)
    start_message_rect = start_message_surface.get_rect()
    start_message_rect.midtop = (window_size[0]*0.5, window_size[1]*0.65)
    screen.blit(start_message_surface, start_message_rect)
    pygame.display.update()

# game loop
while True:
    # check if the game time has expired
    if pygame.time.get_ticks() - game_timer > 300000: 
        end_game(1)

    for event in pygame.event.get():
        # check for key press or quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_direction = 'UP'
            if event.key == pygame.K_DOWN:
                new_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                new_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                new_direction = 'RIGHT'

    # wrong direction change
    if new_direction == 'UP' and direction == 'DOWN':
        end_game(0)
    if new_direction == 'DOWN' and direction == 'UP':
        end_game(0)
    if new_direction == 'LEFT' and direction == 'RIGHT':
        end_game(0)
    if new_direction == 'RIGHT' and direction == 'LEFT':
        end_game(0)

    # update direction and snake position    
    if new_direction == 'UP':
        direction = 'UP'
        snake_pos[1] -= 10
    if new_direction == 'DOWN':
        direction = 'DOWN'
        snake_pos[1] += 10
    if new_direction == 'LEFT':
        direction = 'LEFT'
        snake_pos[0] -= 10
    if new_direction == 'RIGHT':
        direction = 'RIGHT'
        snake_pos[0] += 10


    # check if the snake's position is outside the bounds of the window
    if snake_pos[0] < 0:
        snake_pos[0] = window_size[0]
    elif snake_pos[0] > window_size[0]:
        snake_pos[0] = 0
    elif snake_pos[1] < 0:
        snake_pos[1] = window_size[1]
    elif snake_pos[1] > window_size[1]:
        snake_pos[1] = 0

    # check if snake crossed its tail
    if snake_pos in snake_body[1:]:
        end_game(0)

    # snake growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        if food_type == "good":     # grow for good food
            score += 1
            snake_size += 1
        else:   # shrink for bad food
            score -= 1  
            snake_size -= 1
            snake_body.pop()
            snake_body.pop()
            if snake_size == 0:
                end_game(0)
        food_spawn = False
    else:
        snake_body.pop()

    # draw the snake
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0]//10))*10, random.randrange(1, (window_size[1]//10))*10]
        food_timer = pygame.time.get_ticks()
        food_type = random.choices(["good", "bad"], weights=[0.7, 0.3])[0]
    food_spawn = True
    
    # draw the food
    if food_spawn:
        food_rect = good_food_img.get_rect()
        food_rect.topleft = food_pos
        if food_type == "good":
            screen.blit(good_food_img, food_rect)
        else:
            screen.blit(bad_food_img, food_rect)

    # make food disappear after 8 seconds
    if pygame.time.get_ticks() - food_timer > 8000:
        food_spawn = False

    # display score
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render('Score: ' + str(score), False, white)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (window_size[0]*0.05, window_size[1]*0.05)
    screen.blit(score_surface, score_rect)

    # display time left
    time_left = (300000 - (pygame.time.get_ticks() - game_timer)) // 1000 
    min, sec = divmod(time_left, 60)
    time_left_surface = font.render('Time left: ' + f"{min:02d}:{sec:02d}", False, white)
    time_left_rect = time_left_surface.get_rect()
    time_left_rect.topleft = (window_size[0]*0.25, window_size[1]*0.05)
    screen.blit(time_left_surface, time_left_rect)

    # update the screen
    pygame.display.update()
    frame_rate.tick(10)


    
