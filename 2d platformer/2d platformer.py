
# We are importing the modules we need to build a window, handle events, and use a sprite sheet.
import pygame
import sys
import spritesheet

# This starts Pygame and prepares all the modules it needs.
# Without this, things like the window, keyboard input, and drawing will not work.
pygame.init()

# These variables define the size of the game window in pixels.
# A window that is 500 x 500 means it will be 500 pixels wide and 500 pixels tall.
screen_width = 500
screen_height = 500

# This creates the actual game display window.
# pygame.display.set_mode() opens a new window using the width and height we defined.
# The tuple (screen_width, screen_height) tells Pygame the size.
screen = pygame.display.set_mode((screen_width, screen_height))
sprite_mult = 3
player_x = 0
player_y = 0
player_rect = pygame.Rect(player_x, player_y, 24 * sprite_mult, 24 * sprite_mult)
speedx = 5
gravity = 0.5
y_velocity = 0

step_counter = 0
# This creates a clock object.
# A clock is used to control the speed of the game loop.
# We will use it to limit the game to 60 frames per second.
clock = pygame.time.Clock()

# This loads the sprite sheet image from the file called "2d platformer\doux.png".
# .convert_alpha() makes the image support transparency.
# Transparency is important because sprites usually have transparent backgrounds.
sprite_sheet_image = pygame.image.load(r"2d platformer\doux.png").convert_alpha()

# This creates a SpriteSheet object from our image.
# The SpriteSheet class is likely stored in the file called "spritesheet.py".
# It helps us extract individual frames from a bigger sprite sheet image.
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

# These are color variables.
# In Pygame, colors are often stored as RGB tuples: (Red, Green, Blue)
# Each number is between 0 and 255.
# BG is a dark gray background color for the screen.
BG = (50, 50, 50)

# Black is a color we use as the background key color.
# This is useful because when we pull frames from a sprite sheet, we can make the background color transparent.
Black = (0, 0, 0)

# These lines cut out individual frames from the sprite sheet.
# sprite_sheet.get_image(x, width, height, scale, color_key)
# - x = which frame number to grab from the sheet
# - width = the width of each frame in pixels
# - height = the height of each frame in pixels
# - scale = how much larger or smaller to scale the image
# - color_key = which color should be treated as transparent
# Here, each frame is 24 by 24 pixels and we scale them by 3.
# The Black color is used as the transparent background color.
# create animation list
animation_list = []
animation_steps = [3, 6, 3, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 250
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, sprite_mult, Black))
        step_counter += 1
    animation_list.append(temp_img_list)

# This is the main game loop.
# A game loop keeps running forever while the game is open.
# It handles events, updates objects, draws the screen, and repeats again and again.
while True:
    # This loop checks every event that happened in the game window.
    # Events include mouse clicks, key presses, and the close button.
    for event in pygame.event.get():
        # If the user clicks the X button to close the window, this event type is QUIT.
        if event.type == pygame.QUIT:
            # This closes the Pygame window properly.
            pygame.quit()

            # This ends the Python program safely.
            sys.exit()

    y_velocity += gravity
    player_rect.y += y_velocity
    # gravity engine

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        action = 1
        player_rect.left += speedx
    # checks if the key D is pressed
    # moves the character left at a speed of 5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.right -= speedx
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        y_velocity = -5
    if keys[pygame.K_f]:
        gravity = not gravity

    if player_rect.bottom >= 500:
        player_rect.bottom = 500
        velocity = 0

    # This fills the background of the screen with the BG color (dark gray).
    # It acts like painting the whole window before drawing the sprite on top.
    pygame.draw.rect(screen, Black, player_rect)
    screen.fill(BG)
    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # This draws the first sprite frame onto the screen.
    # screen.blit(image, (x, y)) copies the image onto the screen at the chosen position.
    # Here, the sprite is placed at x = 100 and y = 100.
    screen.blit(animation_list[action][frame], (player_rect.x, player_rect.y))

    # This updates the display so the changes we made become visible.
    # Without this call, the screen would stay blank even though we drew something.
    pygame.display.flip()

    # This limits the game to 60 frames per second.
    # It helps keep the game running smoothly and not too fast.
    clock.tick(60)

# End of the game script.
# The program stays in the while True loop until the user closes the window.
# This is how simple Pygame programs usually run.

# Project notes:
# - Add a floor and level design.
# - Fix the jump logic.
# - Fix the idle animation so it resets after pressing movement keys.
# - Add more tiles, platforms, and background art later.