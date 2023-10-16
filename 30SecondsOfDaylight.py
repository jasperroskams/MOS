
from random import randint

import pyxel

import world
from player import Player

def send_msg(world, msg, col):
    world.journal.push_new_line(msg, col)

def kill_enemy(world, enemy):
    world.current_map.entities.remove(enemy)

def player_attacked_enemy(world, player, enemy):
    enemy.hp = max(0, enemy.hp - (player.attack + Player.WEAPONS[player.weapon][0]))
    if enemy.hp == 0:
        send_msg(world, "You killed the " + enemy.name + \
            ". Got " + str(enemy.xp) + " XP!", 3)
        player.add_xp(world, enemy.xp)
        kill_enemy(world, enemy)
    else:
        send_msg(world, "You hit the " + enemy.name + ".", 11)

def enemy_attacked_player(world, enemy, player):
    shield_val = Player.SHIELDS[player.shield][0]
    #print(shield_val)
    if randint(1, 100) <= shield_val:
        send_msg(world, "You blocked the " + enemy.name + ".", 12)
    else:
        player.hp = max(0, player.hp - enemy.attack)
        if player.hp == 0:
            pyxel.stop()
            pyxel.playm(2, loop=False)
            send_msg(world, "You died.", 8)
            world.set_game_over()
        else:
            send_msg(world, "Got hit by " + enemy.name + ".", 8)
import pyxel

class DaylightControl:
    DAYLIGHT_SECS = 30
    MAX_SECS = DAYLIGHT_SECS * 2

    def __init__(self):
        self.frame_cnt = 0
        self.sec_cnt = 0

    def update(self, world):
        # 0-27 = day = all normal tile colours
        # 28 = early dusk = all orange except nearest
        # 29 = late dusk = all dark red except nearest
        # 30-57 = night = all dark blue except nearest
        # 58 = early dawn = all dark red except nearest
        # 59 = late dawn = all orange except nearest

        self.frame_cnt += 1
        if self.frame_cnt == 10:
            self.frame_cnt = 0
            self.sec_cnt += 1
            if self.sec_cnt == self.MAX_SECS:
                self.sec_cnt = 0

        if self.frame_cnt == 0:
            if self.sec_cnt == 29: # night time spooky music
                pyxel.playm(2, loop=False)
            elif self.sec_cnt == 58: # happy end of night
                pyxel.playm(3, loop=False)
            elif self.sec_cnt == 0:
                pyxel.playm(1, loop=False)

        if self.sec_cnt > 29 and self.sec_cnt < 58:
            for i in range(2, 16):
                pyxel.pal(i, 1)
        elif self.sec_cnt == 28 or self.sec_cnt == 59:
            for i in range(2, 16):
                pyxel.pal(i, 9)
        elif self.sec_cnt == 29 or self.sec_cnt == 58:
            for i in range(2, 16):
                pyxel.pal(i, 2)

    def is_night(self):
        if self.sec_cnt >= 0 and self.sec_cnt <= 27:
            return False
        else:
            return True

from random import randint, choice

from entity import Entity
import combat

class Enemy(Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)

        self.type = self.TYPE_ENEMY

        self.hp = 5
        self.max_hp = 5
        self.attack = 1
        self.defence = 1
        self.xp = 1

        self.max_move_delay = 10 # frames
        self.move_delay = 0 # frames

    def update(self, map):
        self.move_delay += 1
        if self.move_delay == self.max_move_delay:
            self.move_delay = 0

            if not self.try_attack(map):
                if choice([0,1]) == 0:
                    self.move(choice([-1, 1]), 0, map)
                else:
                    self.move(0, choice([-1, 1]), map)

    def try_attack(self, map):
        p_tile_x = map.player.tile_x
        p_tile_y = map.player.tile_y
        if (self.tile_x == p_tile_x and (abs(self.tile_y - p_tile_y) == 1)) or\
            (self.tile_y == p_tile_y and (abs(self.tile_x - p_tile_x) == 1)):
            combat.enemy_attacked_player(map.world, self, map.player)

    def move(self, move_x, move_y, map):
        if map.is_tile_free_for_enemy(self.tile_x + move_x, self.tile_y + move_y):
            if move_x != 0:
                self.tile_x = max(0, min(map.tm_w-1, self.tile_x + move_x))
            elif move_y != 0:
                self.tile_y = max(0, min(map.tm_h-1, self.tile_y + move_y))

    def draw(self, cam):
        super().draw(cam)

def create(name, tile_x, tile_y):
    e = None
    if name is "Rat":
        e = Rat(tile_x, tile_y)
    elif name is "Scorpion":
        e = Scorpion(tile_x, tile_y)
    elif name is "Guard":
        e = Guard(tile_x, tile_y)
    elif name is "Strongman":
        e = Strongman(tile_x, tile_y)
    elif name is "Ghost":
        e = Ghost(tile_x, tile_y)
    elif name is "Skeleton":
        e = Skeleton(tile_x, tile_y)
    elif name is "Zombie":
        e = Zombie(tile_x, tile_y)
    elif name is "Serpent":
        e = Serpent(tile_x, tile_y)
    elif name is "Witch":
        e = Witch(tile_x, tile_y)

    return e

class Rat(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Rat", 0, 48, 8, tile_x, tile_y)

        self.hp = 1
        self.max_hp = 1
        self.attack = 1
        self.defence = 1
        self.xp = 1

        self.max_move_delay = 20 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Scorpion(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Scorpion", 0, 56, 8, tile_x, tile_y)

        self.hp = 3
        self.max_hp = 3
        self.attack = 3
        self.defence = 3
        self.xp = 2

        self.max_move_delay = 15 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Guard(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Guard", 0, 40, 0, tile_x, tile_y)

        self.hp = 8
        self.max_hp = 8
        self.attack = 8
        self.defence = 8
        self.xp = 3

        self.max_move_delay = 15 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Strongman(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Strongman", 0, 48, 0, tile_x, tile_y)

        self.hp = 14
        self.max_hp = 14
        self.attack = 14
        self.defence = 14
        self.xp = 3

        self.max_move_delay = 12 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Ghost(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Ghost", 0, 72, 8, tile_x, tile_y)

        self.hp = 2
        self.max_hp = 2
        self.attack = 2
        self.defence = 2
        self.xp = 4

        self.max_move_delay = 5 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Skeleton(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Skeleton", 0, 64, 0, tile_x, tile_y)

        self.hp = 6
        self.max_hp = 6
        self.attack = 6
        self.defence = 6
        self.xp = 5

        self.max_move_delay = 15 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Zombie(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Zombie", 0, 72, 0, tile_x, tile_y)

        self.hp = 16
        self.max_hp = 16
        self.attack = 16
        self.defence = 16
        self.xp = 6

        self.max_move_delay = 20 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Serpent(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Serpent", 0, 32, 8, tile_x, tile_y)

        self.hp = 20
        self.max_hp = 20
        self.attack = 20
        self.defence = 20
        self.xp = 8

        self.max_move_delay = 20 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

class Witch(Enemy):
    def __init__(self, tile_x, tile_y):
        super().__init__("Witch", 0, 56, 0, tile_x, tile_y)

        self.hp = 25
        self.max_hp = 25
        self.attack = 25
        self.defence = 25
        self.xp = 40

        self.max_move_delay = 18 # frames
        self.move_delay = randint(1, self.max_move_delay-1) # frames

import pyxel

class Entity:
    TYPE_NONE = -1
    TYPE_PLAYER = 0
    TYPE_ENEMY = 1
    TYPE_WEAPON = 2
    TYPE_SHIELD = 3
    TYPE_POTION = 4
    TYPE_TELEPORTER = 5
    TYPE_TRIGGER = 6

    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        self.name = name
        self.img = img
        self.img_x = img_x
        self.img_y = img_y
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.type = -1

    def update(self, map):
        raise NotImplementedError

    def draw(self, cam):
        if self.tile_x*8 + 8 < cam.x or self.tile_x >= cam.x + cam.w or\
            self.tile_y*8 <= cam.y - 8 or self.tile_y*8 >= cam.y + cam.h:
            return
        # blt(x, y, img, u, v, w, h, [colkey])
        pyxel.blt(40 + self.tile_x*8 - cam.x, \
            8 + self.tile_y*8 - cam.y, \
            self.img, \
            self.img_x, \
            self.img_y, \
            8, 8)

import pyxel

from world import World
from hud import Hud
from journal import Journal
from main_menu import MainMenu

class Game:
    STATE_MAIN_MENU = 0
    STATE_MAP = 1

    def __init__(self):
        self.state = self.STATE_MAIN_MENU
        self.main_menu = MainMenu(self)
        self.world = None
        self.hud = None

        #self.new_game()

    def new_game(self):
        pyxel.stop()
        pyxel.playm(1, loop=False)
        self.main_menu = None
        self.state = self.STATE_MAP
        self.world = World(self)
        self.hud = Hud(self.world)

    def game_over(self):
        self.state = self.STATE_MAIN_MENU
        self.main_menu = MainMenu(self)

    def update(self, inputs):
        if self.state is self.STATE_MAP:
            self.world.update(inputs)
            self.hud.update()
        elif self.state is self.STATE_MAIN_MENU:
            self.main_menu.update(inputs)

    def draw(self):
        if self.state is self.STATE_MAP:
            self.world.draw()
            self.hud.draw()
        elif self.state is self.STATE_MAIN_MENU:
            self.main_menu.draw()
import pyxel

from player import Player

class Hud:
    def __init__(self, world):
        self.world = world

    def update(self):
        pass

    def draw(self):
        pyxel.pal()

        # bltm(x, y, tm, u, v, w, h, [colkey])
        pyxel.bltm(0, 0, 7, 0, 0, 160, 120, 15)

        map_title_w = len(self.world.current_map.name) * 4
        pyxel.rect(80 - ((map_title_w + 4) / 2), 0, map_title_w + 4, 8, 0)
        pyxel.text(80 - map_title_w / 2, 1, self.world.current_map.name, 7)

        # blt(x, y, img, u, v, w, h, [colkey])
        pyxel.text(9, 10, "You", 7)
        pyxel.blt(23, 8, 0, 32, 0, 8, 8) # man

        x = 8
        y = 20

        # health
        pyxel.blt(x, y, 0, 48, 48, 8, 8) # heart
        pyxel.text(x+2, y+8, str(self.world.current_map.player.hp) + "/" + str(self.world.current_map.player.max_hp), 7) # hp text

        y += 20

        p = self.world.current_map.player

        # attack
        attack = p.attack + Player.WEAPONS[p.weapon][0]
        ax = x
        if attack > 9:
            ax -= 6
        att_img = [Player.WEAPONS[p.weapon][1],Player.WEAPONS[p.weapon][2]]
        pyxel.blt(x, y, 0, att_img[0], att_img[1], 8, 8) # sword
        pyxel.text(ax+20, y, str(attack), 7)

        y += 8

        # defence
        defence = Player.SHIELDS[p.shield][0]
        dx = x
        if defence > 9:
            dx -= 6
        def_img = [Player.SHIELDS[p.shield][1],Player.SHIELDS[p.shield][2]]
        pyxel.blt(x, y, 0, def_img[0], def_img[1], 8, 8) # shield
        pyxel.text(dx+20, y, str(defence), 7)

        y += 14

        # xp needed for next level
        level = self.world.current_map.player.level
        next = 0
        xp = 0
        if level < Player.MAX_LEVEL-1:
            next = Player.XP_LEVELS[level+1]
            xp = next - self.world.current_map.player.xp
        xpx = x
        if xp > 9:
            xpx -= 6
        pyxel.blt(x, y, 0, 24, 48, 8, 8)
        pyxel.text(xpx+20, y, str(xp), 7)

        y += 8

        # level
        lx = x
        if level+1 > 9:
            lx -= 6
        pyxel.text(x, y, "Lvl", 7)
        pyxel.text(lx+20, y, str(level+1), 7)

        y += 8
import pyxel

class Input:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    CONFIRM = 4
    CANCEL = 5

    def __init__(self):
        self.inputs = []

    def update(self):
        self.inputs.clear()

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_W) or \
            pyxel.btn(pyxel.GAMEPAD_1_UP):
            self.inputs.append(self.UP)
        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.KEY_S) or \
            pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            self.inputs.append(self.DOWN)
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A) or \
            pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.inputs.append(self.LEFT)
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D) or \
            pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.inputs.append(self.RIGHT)

        if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_N) or \
            pyxel.btn(pyxel.GAMEPAD_1_A):
            self.inputs.append(self.CONFIRM)
        elif pyxel.btn(pyxel.KEY_X) or pyxel.btn(pyxel.KEY_M) or \
            pyxel.btn(pyxel.GAMEPAD_1_B):
            self.inputs.append(self.CANCEL)

        return self.inputs
import pyxel

class Journal:
    MAX_LINES = 3

    def __init__(self, world):
        self.x = 8
        self.y = 88
        self.lines = []
        self.world = world

    def push_new_line(self, line, col):
        if len(self.lines) == self.MAX_LINES:
            self.lines.pop(0)
        self.lines.append([line, col])

    def draw(self):
        # text(x, y, s, col)
        for i in range(len(self.lines)):
            pyxel.text(self.x, self.y + i * 8, self.lines[i][0], self.lines[i][1])
from random import randint, choice, sample
import math

import pyxel

from game import Game
from input import Input

class App:
    FPS = 10
    TITLE = "30 Seconds of Daylight"

    def __init__(self):
        pyxel.init(160, 120, caption=self.TITLE, scale=4, fps=self.FPS)

        pyxel.load("../res/rpg01.pyxres")

        self.input = Input()
        self.game = Game()

        pyxel.mouse(visible=True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.game.update(self.input.update())

    def draw(self):
        pyxel.cls(0)

        self.game.draw()

App()
import pyxel

import game

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.select_y = 50
        pyxel.stop()
        pyxel.playm(0, loop=True)

    def update(self, input):
        if pyxel.btn(pyxel.KEY_ENTER):
            self.game.new_game()

    def draw(self):
        pyxel.text(40, 20, "30 Seconds of Daylight", 10)
        pyxel.text(55, 50, "Enter to Start", 12)
        pyxel.text(55, 90, "Escape to Exit", 9)
from random import sample, choice



class Map:
    LADDER_TILE = 48/8 + (16/8 * 32)

    WALKABLE_TILES = [
        8/8 + (8/8 * 32),
        32/8 + (32/8 * 32),
        40/8 + (32/8 * 32),
        32/8 + (64/8 * 32),
        LADDER_TILE
    ]

    def __init__(self, name, tm, tm_x, tm_y, tm_w, tm_h, world):
        self.name = name
        self.tm = tm
        self.tm_x = tm_x
        self.tm_y = tm_y
        self.tm_w = tm_w
        self.tm_h = tm_h
        self.cam = Rect(0, 0, 80, 72)
        self.update_cam = True
        self.world = world

        self.player = None
        self.entities = []

    def enter(self, p_tile_x, p_tile_y, player):
        self.update_cam = True
        self.player = player
        self.player.tile_x = p_tile_x
        self.player.tile_y = p_tile_y

        self.entities.clear()
        self.spawn_enemies()
        self.spawn_items()

    def spawn_enemies(self):
        open_tiles = []
        for y in range(self.tm_h):
            for x in range(self.tm_w):
                tile = pyxel.tilemap(self.tm).get(self.tm_x + x, self.tm_y + y)
                if (x != self.player.tile_x or \
                    y != self.player.tile_y) and \
                    tile in self.WALKABLE_TILES and \
                    distance((x, y), (self.player.tile_x, self.player.tile_y)) >= 4:
                    open_tiles.append([self.tm_x + x, self.tm_y + y])

        # enemy chances
        lvl = self.player.level+1
        chances = {
            "Rat": 0,
            "Scorpion": 0,
            "Guard": 0,
            "Strongman": 0,

            "Ghost": 0,
            "Skeleton": 0,
            "Zombie": 0,
            "Serpent": 0
        }

        if lvl >= 15:
            chances["Rat"] = 10
            chances["Scorpion"] = 10
            chances["Guard"] = 10
            chances["Strongman"] = 20

            chances["Ghost"] = 10
            chances["Skeleton"] = 10
            chances["Zombie"] = 10
            chances["Serpent"] = 20
        elif lvl >= 10:
            chances["Rat"] = 20
            chances["Scorpion"] = 20
            chances["Guard"] = 10

            chances["Ghost"] = 20
            chances["Skeleton"] = 20
            chances["Zombie"] = 10
        elif lvl >= 5:
            chances["Rat"] = 50
            chances["Scorpion"] = 20

            chances["Ghost"] = 15
            chances["Skeleton"] = 15

        else:
            chances["Rat"] = 80

            chances["Ghost"] = 20

        en_list = []
        for key in chances:
            num = chances.get(key)
            for i in range(num):
                en_list.append(key)

        #print(en_list)

        num_to_gen = math.floor(len(open_tiles) * 0.15)

        #print(num_to_gen)

        random_open_tiles = sample(open_tiles, num_to_gen)
        for i in range(num_to_gen):
            self.add_entity(enemy.create(choice(en_list), \
                random_open_tiles[i][0], random_open_tiles[i][1]))
            #self.add_entity(Rat(random_open_tiles[i][0], random_open_tiles[i][1]))

    def spawn_items(self):
        open_tiles = []
        for y in range(self.tm_h):
            for x in range(self.tm_w):
                tile = pyxel.tilemap(self.tm).get(self.tm_x + x, self.tm_y + y)
                if (x != self.player.tile_x or \
                    y != self.player.tile_y) and \
                    tile in self.WALKABLE_TILES and \
                    distance((x, y), (self.player.tile_x, self.player.tile_y)) >= 4:
                    open_tiles.append([self.tm_x + x, self.tm_y + y])

        if self.player.hp < math.floor(self.player.max_hp * 0.75):
            tile = choice(open_tiles)
            self.add_entity(potion.Red(tile[0], tile[1]))
            open_tiles.remove(tile)

        if choice([0,1]) == 0:
            if self.player.weapon == "None":
                tile = choice(open_tiles)
                self.add_entity(weapon.Club(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.weapon == "Club":
                tile = choice(open_tiles)
                self.add_entity(weapon.Sword(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.weapon == "Sword":
                tile = choice(open_tiles)
                self.add_entity(weapon.Axe(tile[0], tile[1]))
                open_tiles.remove(tile)
        else:
            if self.player.shield == "None":
                tile = choice(open_tiles)
                self.add_entity(shield.Wood(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.shield == "Wood":
                tile = choice(open_tiles)
                self.add_entity(shield.Bronze(tile[0], tile[1]))
                open_tiles.remove(tile)
            elif self.player.shield == "Bronze":
                tile = choice(open_tiles)
                self.add_entity(shield.Steel(tile[0], tile[1]))
                open_tiles.remove(tile)

    def update(self, inputs):
        self.player.update(inputs, self)

        if self.update_cam:
            self.cam.x = max(0, min(self.tm_w*8 - \
                self.cam.w, self.player.tile_x*8 - 40))
            self.cam.y = max(0, min(self.tm_h*8 - \
                self.cam.h, self.player.tile_y*8 - 32))

        for e in self.entities:
            e.update(self)

        self.entities.sort( key=lambda  x: x.type, reverse=True)

        self.update_cam = False

    def _is_tile_solid(self, tile_x, tile_y):
        tile = pyxel.tilemap(self.tm).get(self.tm_x + tile_x, self.tm_y + tile_y)
        if tile in self.WALKABLE_TILES:
            return False
        else:
            return True

    def _is_tile_occupied(self, tile_x, tile_y):
        for e in self.entities:
            if e.tile_x == tile_x and e.tile_y == tile_y:
                if e.type == e.TYPE_PLAYER or e.type == e.TYPE_ENEMY:
                    return True
        if tile_x == self.player.tile_x and tile_y == self.player.tile_y:
            return True
        return False

    def is_tile_free_for_enemy(self, tile_x, tile_y):
        if self.is_tile_free(tile_x, tile_y):
            tile = pyxel.tilemap(self.tm).get(self.tm_x + tile_x, self.tm_y + tile_y)
            if tile == self.LADDER_TILE:
                return False
            else:
                return True
        else:
            return False

    def is_tile_free(self, tile_x, tile_y):
        if tile_x < 0 or tile_x >= self.tm_w or\
            tile_y < 0 or tile_y >= self.tm_h:
            return False

        if self._is_tile_solid(tile_x, tile_y) or\
            self._is_tile_occupied(tile_x, tile_y):
            return False
        else:
            return True

    def tile_get_any_enemy(self, tile_x, tile_y):
        for e in self.entities:
            if self.tm_x + e.tile_x == self.tm_x + tile_x and self.tm_y + e.tile_y ==   self.tm_y + tile_y and\
                e.type == Entity.TYPE_ENEMY:
                return e
        return None

    def tile_get_any_item(self, tile_x, tile_y):
        for e in self.entities:
            if (self.tm_x + e.tile_x == self.tm_x + tile_x and\
                self.tm_y + e.tile_y == self.tm_y + tile_y) and\
                (e.type == Entity.TYPE_WEAPON or \
                e.type == Entity.TYPE_SHIELD or \
                e.type == Entity.TYPE_POTION or \
                e.type == Entity.TYPE_TELEPORTER or \
                e.type == Entity.TYPE_TRIGGER):
                return e
        return None

    # note: e tile values are from the texture, so need to be resized.
    def add_entity(self, e):
        e.tile_x -= self.tm_x
        e.tile_y -= self.tm_y
        if e.type == e.TYPE_TELEPORTER:
            to_map = self.world.map_dict[e.to_map_name]
            e.to_tile_x -= to_map.tm_x
            e.to_tile_y -= to_map.tm_y
        self.entities.append(e)

    def draw(self, draw_tilemap, draw_entities, night):
        if draw_tilemap:
            # bltm(x, y, tm, u, v, w, h, [colkey])
            if night: # clip close around player

            # pyxel.blt(40 + self.tile_x*8 - cam.x, \
                # 8 + self.tile_y*8 - cam.y, \
                # self.img, \
                # self.img_x, \
                # self.img_y, \
                # 8, 8)

                clip_x = 40 + self.player.tile_x*8 - self.cam.x - 8
                clip_y = 8 + self.player.tile_y*8 - self.cam.y - 8

                pyxel.clip(clip_x, clip_y, 24, 24)
            else: # clip normally to camera window
                pyxel.clip(40, 8, 80, 72)

            pyxel.bltm(40-self.cam.x, 8-self.cam.y, self.tm, self.tm_x, self.tm_y, self.tm_w, self.tm_h)

            #pyxel.rect(self.tm_x, self.tm_y, self.tm_w*8, self.tm_h*8, 7)

        if draw_entities:
            if night:
                for e in self.entities:
                    x_dist = e.tile_x - self.player.tile_x
                    y_dist = e.tile_y - self.player.tile_y
                    if x_dist >= -1 and x_dist <= 2 and \
                        y_dist >= -1 and y_dist <= 2:
                        e.draw(self.cam)
            else:
                for e in self.entities:
                    e.draw(self.cam)

        self.player.draw(self.cam)

        pyxel.clip()

import map
import weapon
import shield
import potion
import teleporter
import trigger

def load_all(world):
    _load(world, "Courtyard")
    _load(world, "Outer Gate")
    _load(world, "East Wall")
    _load(world, "West Wall")
    _load(world, "Rear Ward")
    _load(world, "Secret Gardens")

def _load(world, map_name):
    new_map = None

    if map_name == "Courtyard":
        new_map = map.Map(map_name, 0, 0, 0, 16, 16, world)
    elif map_name == "Outer Gate":
        new_map = map.Map(map_name, 0, 48, 16, 16, 16, world)
    elif map_name == "East Wall":
        new_map = map.Map(map_name, 0, 0, 16, 24, 16, world)
    elif map_name == "West Wall":
        new_map = map.Map(map_name, 0, 24, 16, 24, 16, world)
    elif map_name == "Rear Ward":
        new_map = map.Map(map_name, 0, 16, 0, 48, 16, world)
    elif map_name == "Secret Gardens":
        new_map = map.Map(map_name, 0, 64, 0, 24, 16, world)

    if new_map != None:
        world.map_dict[map_name] = new_map

def enter_map(world, map_name, player, enter_tile_x, enter_tile_y):
    new_map = None
    new_map = world.map_dict[map_name]
    if new_map != None:
        world.current_map = world.map_dict[map_name]
        new_map.enter(enter_tile_x, enter_tile_y, player)
    if map_name == "Courtyard":
        new_map.add_entity(teleporter.Teleporter(7, 15, 55, 17, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(8, 15, 56, 17, "Outer Gate"))
        new_map.add_entity(trigger.Trigger(7, 1, trigger.Trigger.TYPE_CASTLE_DOOR))
        new_map.add_entity(trigger.Trigger(8, 1, trigger.Trigger.TYPE_CASTLE_DOOR))

    elif map_name == "Outer Gate":
        new_map.add_entity(teleporter.Teleporter(55, 16, 7, 14, "Courtyard"))
        new_map.add_entity(teleporter.Teleporter(56, 16, 8, 14, "Courtyard"))
        new_map.add_entity(teleporter.Teleporter(48, 27, 22, 27, "East Wall"))
        new_map.add_entity(teleporter.Teleporter(48, 28, 22, 28, "East Wall"))
        new_map.add_entity(teleporter.Teleporter(63, 27, 25, 27, "West Wall"))
        new_map.add_entity(teleporter.Teleporter(63, 28, 25, 28, "West Wall"))

    elif map_name == "East Wall":
        new_map.add_entity(teleporter.Teleporter(23, 27, 49, 27, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(23, 28, 49, 28, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(8, 16, 24, 14, "Rear Ward"))

    elif map_name == "West Wall":
        new_map.add_entity(teleporter.Teleporter(24, 27, 62, 27, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(24, 28, 62, 28, "Outer Gate"))
        new_map.add_entity(teleporter.Teleporter(45, 16, 61, 14, "Rear Ward"))

    elif map_name == "Rear Ward":
        new_map.add_entity(teleporter.Teleporter(24, 15, 8, 17, "East Wall"))
        new_map.add_entity(teleporter.Teleporter(61, 15, 45, 17, "West Wall"))
        new_map.add_entity(teleporter.Teleporter(39, 0, 76, 14, "Secret Gardens"))
        new_map.add_entity(teleporter.Teleporter(40, 0, 77, 14, "Secret Gardens"))

    elif map_name == "Secret Gardens":
        new_map.add_entity(teleporter.Teleporter(76, 15, 39, 1, "Rear Ward"))
        new_map.add_entity(teleporter.Teleporter(77, 15, 40, 1, "Rear Ward"))
        new_map.add_entity(trigger.Trigger(74, 1, trigger.Trigger.TYPE_CASTLE_KEY))

from entity import Entity
from input import *
import combat
import map_loader
import trigger

class Player(Entity):
    # name/key, attack, img_x, img_y
    WEAPONS = {
        "None": [1, 32, 56, 2],
        "Club": [3, 64, 32, 3],
        "Sword": [6, 48, 32, 5],
        "Axe": [9, 56, 32, 10]
    }

    # name/key, defence, img_x, img_y
    SHIELDS = {
        "None": [2, 32, 56],
        "Wood": [6, 72, 72],
        "Bronze": [12, 72, 56],
        "Steel": [18, 72, 48]
    }

    MAX_XP = 99
    MAX_LEVEL = 20

    XP_LEVELS = []
    for i in range(1, MAX_LEVEL+1):
        XP_LEVELS.append(round(0.04 * (i ^ 3) + 0.8 * (i ^ 2) + 2 * i))

    #for i in range(len(XP_LEVELS)):
    #    print("XP for level " + str(i+1) + " : " + str(XP_LEVELS[i]))

# XP for level 1 : 0
# XP for level 2 : 4
# XP for level 3 : 7
# XP for level 4 : 13
# XP for level 5 : 16
# XP for level 6 : 15
# XP for level 7 : 18
# XP for level 8 : 24
# XP for level 9 : 27
# XP for level 10 : 27
# XP for level 11 : 30
# XP for level 12 : 36
# XP for level 13 : 39
# XP for level 14 : 38
# XP for level 15 : 41
# XP for level 16 : 47
# XP for level 17 : 50
# XP for level 18 : 49
# XP for level 19 : 52
# XP for level 20 : 59

    def __init__(self):
        super().__init__("Player", 0, 32, 0, 0, 0)

        self.type = self.TYPE_PLAYER
        self.hp = 10
        self.max_hp = 10
        self.attack = 1
        self.defence = 1
        self.level = 0
        self.xp = 0

        self.weapon = "None"
        self.shield = "None"
        self.attack_delay = 0

        self.has_castle_key = False

    def add_xp(self, world, n):
        if self.level < self.MAX_LEVEL-1:
            next_level_xp = self.XP_LEVELS[self.level+1]
            self.xp = min(self.MAX_XP, self.xp + n)
            if self.xp >= next_level_xp:
                self.level += 1
                world.journal.push_new_line("Level up! (" + str(self.level+1) + ")", 9)
                self.xp = 0
                self.max_hp += 1
                self.attack += 1
                self.defence += 1
                #self.hp = self.max_hp

                # for i in range(self.MAX_LEVEL-1, -1, -1):
                    # #print(str(self.XP_LEVELS[i]))
                    # if self.xp >= self.XP_LEVELS[i]:
                        # self.level = i
                        # self.xp = 0
                        # break

    def update(self, inputs, map):
        if self.attack_delay > 0:
            self.attack_delay -= 1;

        if Input.CONFIRM in inputs:
            if Input.UP in inputs:
                self.do_attack(0, -1, map)
            elif Input.DOWN in inputs:
                self.do_attack(0, 1, map)
            elif Input.LEFT in inputs:
                self.do_attack(-1, 0, map)
            elif Input.RIGHT in inputs:
                self.do_attack(1, 0, map)
        else:
            if Input.UP in inputs:
                self.move(0, -1, map)
            elif Input.DOWN in inputs:
                self.move(0, 1, map)
            elif Input.LEFT in inputs:
                self.move(-1, 0, map)
            elif Input.RIGHT in inputs:
                self.move(1, 0, map)

        if Input.CANCEL in inputs:
            self.do_pickup(map)

    def do_attack(self, dir_x, dir_y, map):
        if self.attack_delay == 0:
            enemy = map.tile_get_any_enemy(self.tile_x + dir_x, self.tile_y + dir_y)
            if enemy is not None:
                #map.entities.remove(enemy)
                self.attack_delay = self.WEAPONS[self.weapon][3];
                combat.player_attacked_enemy(map.world, self, enemy)

    def do_pickup(self, map):
        item = map.tile_get_any_item(self.tile_x, self.tile_y)
        if item != None:
            if item.type == item.TYPE_WEAPON:
                self.weapon = item.name
                map.world.journal.push_new_line(\
                    "You got the " + self.weapon + "!", 12)
                map.entities.remove(item)
            elif item.type == item.TYPE_SHIELD:
                self.shield = item.name
                map.world.journal.push_new_line(\
                    "You got the " + self.shield + " shield!", 12)
                map.entities.remove(item)
            elif item.type == item.TYPE_POTION:
                item.drink(self)
                map.world.journal.push_new_line(\
                    "You drank the " + item.name + " potion!", 14)
                map.entities.remove(item)

    def move(self, move_x, move_y, map):
        item = map.tile_get_any_item(self.tile_x + move_x, self.tile_y + move_y)
        if item != None:
            if item.type == item.TYPE_TELEPORTER:
                map_loader.enter_map(map.world, item.to_map_name, self,\
                    item.to_tile_x, item.to_tile_y)
                return
            elif item.type == item.TYPE_TRIGGER:
                if item.trigger_type == item.TYPE_CASTLE_DOOR:
                    if self.has_castle_key:
                        map.world.journal.push_new_line(\
                        "You open the doors! Well done!", 7)
                        map.world.set_game_over()
                    else:
                        map.world.journal.push_new_line(\
                        "Find the key to open the doors!", 7)
                elif item.trigger_type == item.TYPE_CASTLE_KEY:
                    self.has_castle_key = True
                    map.world.journal.push_new_line(\
                        "You found the CASTLE KEY!", 7)
                    map.entities.remove(item)

        if map.is_tile_free(self.tile_x + move_x, self.tile_y + move_y):
            if move_x != 0:
                self.tile_x = max(0, min(map.tm_w-1, self.tile_x + move_x))
                map.update_cam = True
            elif move_y != 0:
                self.tile_y = max(0, min(map.tm_h-1, self.tile_y + move_y))
                map.update_cam = True
        #else:
        #    pass
            #play(ch, snd, loop=False)
            #if pyxel.play_pos(3) == -1:
            #    pyxel.play(3, 0)

    def draw(self, cam):
        if self.hp == 0:
            return
        super().draw(cam)

import entity
import player

class Potion(entity.Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)

        self.type = self.TYPE_POTION

    def update(self, map):
        pass

    def drink(self, player):
        raise NotImplementedError

class Red(Potion):
    def __init__(self, tile_x, tile_y):
        super().__init__("Red", 0, 56, 64, tile_x, tile_y)

    def drink(self, player):
        player.hp = player.max_hp

from entity import Entity

class Shield(Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)

        self.type = self.TYPE_SHIELD

    def update(self, map):
        pass

class Wood(Shield):
    def __init__(self, tile_x, tile_y):
        super().__init__("Wood", 0, 72, 72, tile_x, tile_y)

class Bronze(Shield):
    def __init__(self, tile_x, tile_y):
        super().__init__("Bronze", 0, 72, 56, tile_x, tile_y)

class Steel(Shield):
    def __init__(self, tile_x, tile_y):
        super().__init__("Steel", 0, 72, 48, tile_x, tile_y)
from entity import Entity

class Teleporter(Entity):
    def __init__(self, tile_x, tile_y, to_tile_x, to_tile_y, to_map_name):
        super().__init__("Teleporter", 0, 32, 0, tile_x, tile_y)

        self.type = self.TYPE_TELEPORTER
        self.to_tile_x = to_tile_x
        self.to_tile_y = to_tile_y
        self.to_map_name = to_map_name

    def update(self, map):
        pass

    def draw(self, cam):
        pass


from entity import Entity

class Trigger(Entity):
    TYPE_CASTLE_DOOR = 0
    TYPE_CASTLE_KEY = 1

    def __init__(self, tile_x, tile_y, type):
        super().__init__("Trigger", 0, 32, 0, tile_x, tile_y)

        self.type = self.TYPE_TRIGGER
        self.trigger_type = type

    def update(self, map):
        pass

    def draw(self, cam):
        pass

import math

class Rect:
    def __init__ (self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def collides_rect(self, other):
        pass

    def contains_point(self, x, y):
        pass

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

from entity import Entity

class Weapon(Entity):
    def __init__(self, name, img, img_x, img_y, tile_x, tile_y):
        super().__init__(name, img, img_x, img_y, tile_x, tile_y)

        self.type = self.TYPE_WEAPON

    def update(self, map):
        pass

class Club(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Club", 0, 64, 32, tile_x, tile_y)

class Sword(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Sword", 0, 48, 32, tile_x, tile_y)

class Axe(Weapon):
    def __init__(self, tile_x, tile_y):
        super().__init__("Axe", 0, 56, 32, tile_x, tile_y)

import pyxel

from map import Map
from daylight_control import DaylightControl
from player import Player
from journal import Journal
import map_loader

class World:
    MAX_GAME_OVER_WAIT_TICKS = 30 #3 secs

    def __init__(self, game):
        self.game = game
        self.map_dict = {}
        self.current_map = None
        map_loader.load_all(self)

        self.daylight_control = DaylightControl()

        self.player = Player()

        map_loader.enter_map(self, "Courtyard", self.player, 7, 1)

        self.journal = Journal(self)

        self.game_over = False
        self.game_over_ticks = 0

    def set_game_over(self):
        self.game_over = True

    def update(self, inputs):
        if self.game_over:
            self.game_over_ticks += 1
            if self.game_over_ticks == self.MAX_GAME_OVER_WAIT_TICKS:
                self.game.game_over()
        else:
            self.daylight_control.update(self)
            self.current_map.update(inputs)

    def draw(self):
        self.current_map.draw(True, False, False)
        if self.daylight_control.is_night():
            pyxel.pal()
            self.current_map.draw(True, True, True)
        else:
            self.current_map.draw(False, True, False)

        self.journal.draw()
