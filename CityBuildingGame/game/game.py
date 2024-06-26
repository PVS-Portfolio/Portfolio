import pygame as pg
import sys
from networkx import dijkstra_path

from .camera import Camera
from .hud import HUD
from .utils import draw_text
from .workers import Worker
from .world import World
from .buildings import Building

from .settings import WORLD_W, WORLD_H, SHOWFPS, LOAD, SAVE


class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # entities
        self.entities = []
        self.num_characters = 0
        self.camera = Camera(self.width, self.height)
        # hud
        self.hud = HUD(self.width, self.height, self.screen)

        self.days = 0
        self.datestring = ''
        self.get_datestring()
        self.daytimer = pg.time.get_ticks()

        if LOAD:
            savedata = self.load()
        else:
            savedata = None

        if savedata is not None:
            w = int(savedata['world']['x'])
            h = int(savedata['world']['y'])
        else:
            w, h = WORLD_W, WORLD_H
        # world
        self.world = World(self.entities, self.hud, self.camera, w, h, self.width, self.height,
                           savedata=savedata)

        self.spawncooldown = pg.time.get_ticks()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.spawn_worker()
            self.world.mouse_pos = self.hud.mouse_pos = pg.mouse.get_pos()
            self.world.mouse_action = self.hud.mouse_action = pg.mouse.get_pressed()
            self.events()
            self.update()
            self.draw()

    # consider moving this to World class
    def spawn_worker(self):
        if self.world.wrkr_ctr == 1:
            return
        now = pg.time.get_ticks()
        if now - self.spawncooldown > 10000:
            if self.num_characters > sum([i.housing_capacity for i in self.world.towns]) + 3:
                return
            found = False
            while not found:
                x, y = self.world.get_random_position_along_border()
                try:
                    dijkstra_path(self.world.world_network, (x, y), self.world.towns[0].loc)
                except:
                    continue
                Worker(self.world.world[x][y], self.world, f'worker{self.world.wrkr_ctr}')
                self.spawncooldown = now
                found = True
                self.num_characters += 1
                self.world.wrkr_ctr += 1

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.quit()

            # recenter the camera when h is pressed
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_h:
                    self.camera.scroll.x = 0
                    self.camera.scroll.y = 0

            # I have to stop checking everything every update in the World class
            # I need to record button presses here, and then only handle them when necessary in other classes
            # if event.type == pg.MOUSEBUTTONDOWN:
            #     # start drag
            #     print('click')
            # if event.type == pg.MOUSEBUTTONUP:
            #     # end drag
            #     print('unclick')

    def get_datestring(self):
        years = self.days // 336
        num = self.days - years * 336
        months = num // 28
        num -= months * 28
        weeks = num // 7
        num -= weeks * 7
        days = num % 7
        self.datestring = f'Year {years + 1}, Month {months + 1}, Week {weeks + 1}, Day {days + 1}'

    def update(self):
        now = pg.time.get_ticks()
        if now - self.daytimer > 5000:
            self.days += 1
            self.get_datestring()
            self.daytimer = now
        self.camera.update()
        for e in self.entities:
            e.update()
        self.hud.update()
        self.world.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.world.draw()
        self.hud.draw()

        if SHOWFPS:
            draw_text(self.screen,
                      'fps={}'.format(round(self.clock.get_fps())),
                      25,
                      (255, 255, 255),
                      (10, 10))

        pos = self.width * .3
        draw_text(self.screen,
                  f'{self.datestring}',
                  25,
                  (255, 255, 255),
                  (pos, 0))

        pg.display.flip()

    def save(self):
        f = open('savefile.txt', 'w')
        f.write('WORLD\n')
        f.write(self.world.get_state_for_savefile())
        f.write('BUILDINGS\n')
        for b in self.entities:
            if isinstance(b, Building):
                f.write(b.get_state_for_savefile())
        f.write('WORKERS\n')
        for w in self.entities:
            if isinstance(w, Worker):
                f.write(w.get_state_for_savefile())
        f.close()

    def load(self):
        savedata = {'world': {},
                    'workers': [],
                    'buildings': []}
        f = open('savefile.txt', 'r')
        line = f.readline()[:-1]
        if line != 'WORLD':
            raise Exception('BAD SAVE FILE FORMAT')
        line = f.readline()[:-1]
        splitline = line.split('#')
        for pair in splitline:
            pair = pair.split('=')
            if '' not in pair:
                savedata['world'][pair[0]] = pair[1]
        line = f.readline()[:-1]
        if line != 'BUILDINGS':
            raise Exception('BAD SAVE FILE FORMAT')
        line = f.readline()[:-1]
        while line != 'WORKERS':
            savedata['buildings'].append({})
            splitline = line.split('#')
            for pair in splitline:
                pair = pair.split('=')
                if '' not in pair:
                    savedata['buildings'][-1][pair[0]] = pair[1]
            line = f.readline()[:-1]

        line = f.readline()[:-1]
        while line:
            savedata['workers'].append({})
            splitline = line.split('#')
            for pair in splitline:
                pair = pair.split('=')
                savedata['workers'][-1][pair[0]] = pair[1]
            line = f.readline()[:-1]

        f.close()
        return savedata

    def quit(self):
        if SAVE:
            self.world.write_map()
            # self.world.write_world_network()
            # self.world.write_road_network()
            self.save()
        pg.quit()
        sys.exit()
