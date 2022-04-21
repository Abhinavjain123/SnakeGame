import pygame
import random
pygame.init()                                          # initialise

screen_width = 900
screen_height = 500

# colours    0 to 255  rgb
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# making game window
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")
pygame.display.update()

# specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
clock = pygame.time.Clock()

fps = 40
velocity_x = 0
velocity_y = 0
init_velocity = 5

food_x = random.randint(300,screen_width/2)
food_y = random.randint(200,screen_height/2)

score = 0
font = pygame.font.SysFont(None,55)
def text_screen(text, color, x , y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])



# creating game loop
while not exit_game:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

            if event.key == pygame.K_F1:
                velocity_y = 0
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)< 6:
        score += 1
        print("score \n",score*10)

        food_x = random.randint(300, screen_width / 2)
        food_y = random.randint(200, screen_height / 2)

    gamewindow.fill(white)
    text_screen("Score: " + str(score * 10), red, 5, 5)
    pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()  # we need to update
    clock.tick(fps)



pygame.quit()
quit()
