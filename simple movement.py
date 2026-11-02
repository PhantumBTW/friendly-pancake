import pygame
import sys
pygame.init()
screen_width = pygame.width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
speed = 10


player_rect = pygame.Rect(100, 200, 50, 50)
#defines the rect argument with the parameters: (left, top, width, height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
#Loops the game until you click "x"


    if player_rect.left > screen_width:
        player_rect.left = -50
    if player_rect.right < 0:
        player_rect.right = 800
    if player_rect.top < 0:
        player_rect.top = 600
    if player_rect.top > 600:
        player_rect.top = 0
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), player_rect)
#draws a rect (the screen u want to draw on, (R,G,B), the rect u wanna draw)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
    #checks if the key D is pressed
        player_rect.left += speed
        # moves the character left at a speed of 5
    if keys[pygame.K_a]:
        player_rect.left -= speed
    if keys[pygame.K_w]:
        player_rect.top -= speed

    if keys[pygame.K_s]:
        player_rect.top += speed

    pygame.display.flip()
    clock.tick(100)
#updates the screen the clock tick is refresh rate
