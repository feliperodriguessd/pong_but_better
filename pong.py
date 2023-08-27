import pygame   

pygame.init()

#INITIALS
WIDTH, HEIGTH=1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGTH))

run = True #variable created to use False as a way to exit the game

#colors
BLUE = (0, 0, 225)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGTH/2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7

#paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle = right_paddle = HEIGTH/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)

#main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    #balls movement controls
    if ball_y <= 0 + radius or ball_vel_y >= HEIGTH - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGTH/2 - radius
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGTH/2 - radius
        ball_vel_x, ball_vel_y = 0.7, 0.7



    #movements
    ball_x = ball_vel_x
    ball_y = ball_vel_y
    #OBJECTS

    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    #pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height) )
    #pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height) )
    pygame.display.update()