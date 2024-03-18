# This file was created by: Miles Crooks

# we are importing other game files
'''
hostile enemy
game start/game over 
speed potion
'''
import pygame as pg
from settings import *
from sprites import *
import sys
from random import randint
from os import path

# create a game class 
class Game:
    # behold the methods
    def __init__(self):
        pg.init()
        # 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # 
        pg.display.set_caption("My First Video Game")
        # 
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.running = True
        # later on we'll story game info with this
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'images')
        self.player_img = pg.image.load(path.join(img_folder, 'jake.png')).convert_alpha()
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                print(line)
                self.map_data.append(line)
                print(self.map_data)
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
        self.moneybag = pg.sprite.Group()
        self.potions = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.hitpoints = pg.sprite.Group()
        # self.player = Player(self, 10, 10)
        # self.all_sprites.add(self.player)
        # for x in range(10, 20):
        #     Wall(self, x, 5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'p':
                    self.player = Player(self, col, row)
                if tile == 'z':
                     self.speedpotion = Potions (self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            # this is input
            self.events()
            # this is processing
            self.update()
            # this output
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()
    # methods
    def input(self): 
        pass
    def update(self):
        self.all_sprites.update()
    
    # def draw_grid(self):
        # for x in range(0, WIDTH, TILESIZE):
            # pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        # for y in range(0, HEIGHT, TILESIZE):
            # pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x*TILESIZE,y*TILESIZE)
        surface.blit(text_surface, text_rect)



# coin counter in corner
    def draw(self):
        self.screen.fill(BGCOLOR)
        # self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
        pg.display.flip()

    def events(self):
            # listening for events
            for event in pg.event.get():
                # when you hit the red x the window closes the game ends
                if event.type == pg.QUIT:
                    self.quit()
                    print("the game has ended..")
                # keyboard events
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_LEFT:
                #         self.player.move(dx=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_RIGHT:
                #         self.player.move(dx=1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_UP:
                #         self.player.move(dy=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_DOWN:
                #         self.player.move(dy=1)
                    
    def show_start_screen(self):
        self.screen.fill(ORANGE)
        self.draw_text(self.screen, "Jake Run" , 24, WHITE, WIDTH/2, HEIGHT/2)
        self.draw_text(self.screen, "Press any key to start" , 24, PINK, WIDTH/2, HEIGHT/2)
        pg.display.flip()
        self.wait_for_key()
    # def show_end_screen(self):
    #     if not self.playing:
    #         return
    #     self.screen.fill(ORANGE)
    #     self.draw_text(self.screen, "YOU DIED", 24, WHITE, WIDTH/2, HEIGHT/2)
    #     pg.display.flip()
    #     self.wait_for_key

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

####################### Instantiate game... ###################
g = Game()
g.show_start_screen()
# g.show_end_screen()
while True:
    g.new()
    g.run()
    # g.show_go_screen()
