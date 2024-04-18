# # create a loop that loops through the list over and over

# import pygame as pg

# clock = pg.time.Clock

# frames = ["frame1", "frame2", "frame3", "frame4"]
# x = 0
# then = 0
# FPS = 60
# SPRITESHEET = "idle_frames.png"

# while True:
#     clock.tick(FPS)
#     x = x%len(frames)
#     print(frames[x])
#     x+=1
#     now = pg.time.get_ticks
#     if now - then > 200:
#         print(frames[current_frame])
#         current_frame = (current_frame + 1) % len(frames)
#         print("time for a new frame")
#         print(now)
#         then = now
#     print(pg.time.get_ticks())

#     class Spritesheet:
#     # utility class for loading and parsing spritesheets
#      def __init__(self, filename):
#             self.spritesheet = pg.image.load(filename).convert()
        
#     def get_image(self, x, y, width, height):
#         # grab an image out of a larger spritesheet
#         image = pg.Surface((width, height))
#         image.blit(self.spritesheet, (0, 0), (x, y, width, height))
#         # image = pg.transform.scale(image, (width, height))
#         image = pg.transform.scale(image, (width * 4, height * 4))
#         return image
    
#     def __init__(self):
#         Sprite.__init__(self)
#         self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
#         self.load_images()
#         self.image = self.standing_frames[0]
#         self.rect = self.image.get_rect()
#         self.jumping = False
#         self.walking = False
#         self.current_frame = 0
#         self.last_update = 0


