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
clock = pygame.time.Clock()
pygame.display.update()

font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])


# creating game loop
def gameloop():

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

    fps = 50
    snake_size = 15

    snk_list = []
    snk_length = 1

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            gamewindow.fill(white)
            text_screen("Game Over! Press Enter to continue", red, 140, 170)
            text_screen("Your score = " + str(score), red, 310, 230)
            text_screen("Highscore = " + str(hiscore), red, 300, 280)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
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

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x) < 10 and abs(snake_y-food_y) < 10:
                score += 10

                food_x = random.randint(200, int(screen_width/1.5))
                food_y = random.randint(100, int(screen_height/1.5))
                snk_length += 4
                if score > int(hiscore):
                    hiscore = score
                    with open("hiscore.txt", "w") as f:
                        f.write(str(score))

            gamewindow.fill(white)
            text_screen("Score: " + str(score), red, 5, 5)
            text_screen("Hiscore: " + str(hiscore), red, 230, 5)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            # pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gamewindow, black, snk_list, snake_size)

        pygame.display.update()  # we need to update
        clock.tick(fps)


gameloop()

pygame.quit()

quit()
