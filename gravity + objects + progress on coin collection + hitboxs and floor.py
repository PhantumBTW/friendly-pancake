import pygame
import sys
pygame.init()
screen_width = pygame.width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
speedx = 10
jump = 15
y_velocity = 0
gravity = 0.5
y = 400
x = 200


player_rect = pygame.Rect(100, 200, 50, 50)
#defines the rect argument with the parameters: (left, top, width, height)
enemy_rect = pygame.Rect(400, 500, 100, 500)
#creates a static block at the floor 
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
        # Check if the player's bottom edge has hit or gone through the floor (600)
    if player_rect.bottom >= 600:
        player_rect.bottom = 600  # Snap them exactly onto the floor
        y_velocity = 0            # Reset speed to 0 so they stop falling

            
    screen.fill((0,0,0))

    y_velocity += gravity
    player_rect.y += y_velocity
    #gravity engine

    pygame.draw.rect(screen, (0,255,0),enemy_rect)

    pygame.draw.rect(screen, (255, 0, 0), player_rect)
#draws a rect (the screen u want to draw on, (R,G,B), the rect u wanna draw)
    pygame.draw.circle(screen, (0,0,255),(x,y),25,)
    #COINS 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
    #checks if the key D is pressed
        player_rect.left += speedx
        # moves the character left at a speed of 5
    if keys[pygame.K_a]:
        player_rect.left -= speedx
    if keys[pygame.K_w]:
        player_rect.top -= jump


    if player_rect.colliderect(enemy_rect):
        y_velocity = -0.5
        player_rect.bottom = 500
    #check if player collide with green squre, if so gets tpd to top of it and gravity is canncled out 

    if player_rect.right == 400:
        player_rect.right = 400
    # check if player is touching side by position if so tpd back, cant use collision unoless you used two sep vairable for wall and top 
    
   
        

    pygame.display.flip()
    clock.tick(100)
#updates the screen the clock tick is refresh rate



# the if statement on the coin collider needs fixing perhaps assign it a hitbox???????