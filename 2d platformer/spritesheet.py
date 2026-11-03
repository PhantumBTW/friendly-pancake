# This imports the Pygame library.
# Pygame gives us tools for drawing images, creating windows, and working with sprite sheets.
import pygame

# This defines a class called SpriteSheet.
# A class is like a blueprint for creating an object that can help us handle sprite images.
# In this case, the object will help us cut out individual frames from a sprite sheet.
class SpriteSheet():
    # This is the constructor method.
    # __init__ is a special method that runs automatically when we create a new SpriteSheet object.
    # The parameter image is the full sprite sheet image that we want to work with.
    def __init__(self, image):
        # self.sheet stores the full sprite sheet image inside the object.
        # This lets us use the image later when we cut frames out of it.
        self.sheet = image

    # This method extracts one frame from the sprite sheet.
    # The method is called get_image because it returns an image frame.
    # Parameters:
    # - frame: which frame number to grab from the sprite sheet
    # - width: width of one frame in pixels
    # - height: height of one frame in pixels
    # - scale: how much bigger or smaller the frame should be
    # - colour: the color that should be treated as transparent
    def get_image(self, frame, width, height, scale, colour):
        # Create a new blank surface (image) to hold the extracted frame.
        # pygame.Surface((width, height)) creates a new drawing area.
        # .convert_alpha() tells Pygame to keep transparency information for this image.
        image = pygame.Surface((width, height)).convert_alpha()

        # Copy a section of the sprite sheet onto our new blank surface.
        # self.sheet is the full sprite sheet.
        # (0, 0) means we place the copied section at the top-left corner of the new image.
        # ((frame * width), 0, width, height) tells Pygame:
        #   - start x position at the current frame number times the frame width
        #   - start y position at 0, since all frames are in one row
        #   - crop a rectangle of width x height
        # This effectively cuts out one sprite frame from the big sprite sheet.
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))

        # Resize the image to make it larger or smaller.
        # Example: if width is 24 and scale is 3, then the new width becomes 72.
        image = pygame.transform.scale(image, (width * scale, height * scale))

        # Set a transparent color key.
        # This means that if a pixel matches the colour parameter, it will become invisible.
        # This is useful when sprites have a solid background color like black that we do not want to show.
        image.set_colorkey(colour)

        # Return the finished sprite image.
        # Now the caller can draw this sprite frame onto the game screen.
        return image

# This class is useful because sprite sheets usually contain many frames in one image.
# Instead of loading each sprite separately, we can extract each frame when we need it.
# This keeps the code organized and makes animation easier to manage.