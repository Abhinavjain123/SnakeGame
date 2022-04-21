import pygame
import random
import os

pygame.init()  # initialise
pygame.mixer.init()

screen_width = 900
screen_height = 500

# colours    0 to 255  rgb
game_bc = (156, 217, 255)
over_c = (170,190,220)
wel_c = (45,0,255)
head_c = (127, 127, 127)

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
pink = (255, 0,255)
yellow = (255, 255, 0)

barrier = [[300,200],[310,200],[320,200]]

# making game window
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()
pygame.display.update()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text, [x, y])

def welcome():
    exit_game = False
    while not exit_game:

        gamewindow.fill(over_c)
        text_screen("WELCOME! to Snakes Game", wel_c, 220, 170)
        text_screen("Press space to continue", black, 250, 240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                    exit_game = True

        pygame.display.update()
        clock.tick(40)

def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        if [x, y] == snk_list[-1]:
            pygame.draw.circle(gamewindow,(0,255,0),[x+10,y+10],12)
            pygame.draw.circle(gamewindow,black,[x+6,y+6],3)
            pygame.draw.circle(gamewindow,black,[x+14,y+6],3)
            pygame.draw.arc(gamewindow,red,[x+4,y+6,12,12],3.4,6.3)
            # pygame.draw.ellipse(gamewindow,red,[x+6,y+12,8,4])
        else:
            pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


# creating game loop
def gameloop():
    pygame.mixer.music.load("bc.mp3")
    pygame.mixer.music.play()

    exit_game = False
    game_over = False

    # specific variables

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(200, int(screen_width / 1.5))
    food_y = random.randint(100, int(screen_height / 1.5))

    score = 0
    init_velocity = 5

    direction = ""

    fps = 40
    snake_size = 20

    snk_list = []
    snk_length = 1

    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:

        if game_over:
            gamewindow.fill(over_c)
            text_screen("Game Over! Press Enter to Continue", (104,34,139), 140, 170)
            text_screen("Your score = " + str(score), (255,20,147), 310, 230)
            text_screen("Highscore = " + str(hiscore), red, 305, 280)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
                        exit_game = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if direction != "left":
                            velocity_x = init_velocity
                            velocity_y = 0
                            direction = "right"

                    if event.key == pygame.K_LEFT:
                        if direction != "right":
                            velocity_x = -init_velocity
                            velocity_y = 0
                            direction = "left"

                    if event.key == pygame.K_UP:
                        if direction != "down":
                            velocity_y = -init_velocity
                            velocity_x = 0
                            direction = "up"

                    if event.key == pygame.K_DOWN:
                        if direction != "up":
                            velocity_y = init_velocity
                            velocity_x = 0
                            direction = "down"

                    if event.key == pygame.K_END:
                        score += 10
            
                                      

            snake_x += velocity_x
            snake_y += velocity_y
            
            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                pygame.mixer.music.load("food.mp3")
                pygame.mixer.music.play()
                score += 10

                food_x = random.randint(200, int(screen_width / 1.5))
                food_y = random.randint(100, int(screen_height / 1.5))
                snk_length += 4
                
                if score > int(hiscore):
                    hiscore = score
                    with open("hiscore.txt", "w") as f:
                        f.write(str(score))

            gamewindow.fill(game_bc)
            text_screen("Score: " + str(score), (104,34,139), 5, 5)
            text_screen("High Score: " + str(hiscore), (255,0,255), 230, 5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            while [food_x,food_y] in barrier:
                pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            pygame.draw.rect(gamewindow,yellow,[300,200,snake_size,snake_size])
            pygame.draw.rect(gamewindow,yellow,[310,200,snake_size,snake_size])
            pygame.draw.rect(gamewindow,yellow,[320,200,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_over = True

            if (abs(snake_x-300)<15 and abs(snake_y-200)<15) or (abs(snake_x-310)<15 and abs(snake_y-200)<15) or (abs(snake_x-320)<15 and abs(snake_y-200)<15):
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_over = True

            # pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gamewindow, black, snk_list, snake_size)

        pygame.display.update()  # we need to update
        clock.tick(fps)
        

welcome()

pygame.quit()

quit()
