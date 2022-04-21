import pygame
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
fps = 30


# creating game loop
while not exit_game:

    gamewindow.fill(white)
    pygame.draw.rect(gamewindow,black,[snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()  # we need to update
    clock.tick(fps)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x += 5

            if event.key == pygame.K_LEFT:
                snake_x -= 5

            if event.key == pygame.K_UP:
                snake_y -= 5

            if event.key == pygame.K_DOWN:
                snake_y += 5


pygame.quit()
quit()
