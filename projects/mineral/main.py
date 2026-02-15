import shutil
import time
import sys
import tty
import termios
import os

from world.world import World
from world.gen.fastgen import FastGen
from player.player import Player
from block.blocks import AIR

WIDTH = shutil.get_terminal_size().columns
HEIGHT = shutil.get_terminal_size().lines

COORDS = WIDTH * HEIGHT

def get_key():
    fd = sys.stdin.fileno()
    old_set = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_set)
    return key

def move_player_add(world: World, loc_add):
    try:
        loc = int(world.player.loc + loc_add)
        if world.get_block(loc) == AIR: 
            world.set_player_loc(loc)
    except IndexError:
        pass # index out of range если в низ пойти

def move_player_sub(world: World, loc_sub):
    try:
        loc = int(world.player.loc - loc_sub)
        if world.get_block(loc) == AIR: 
            world.set_player_loc(loc)
    except IndexError:
        pass # index out of range если пойти в низ

def show_inv(world: World):
    print("stone:", world.player.items.count('\x1b[90m#'))
    print("gold:", world.player.items.count('\x1b[93mG'))
    print("coal:", world.player.items.count('C'))
    print("cuprum:", world.player.items.count('\033[33mU'))
def main():
    moving = True
    player = Player("\033[34m@", WIDTH*HEIGHT/2)
    
    gen = FastGen(WIDTH, HEIGHT)
    world = World(player, WIDTH, HEIGHT)
    
    world.generate(gen)
    
    while moving:
        os.system("clear")
        world.print()
        ch = get_key()
        
        if ch == "q":
            show_inv(world)
            moving = False

        if ch == "w":
            move_player_sub(world, WIDTH)
        elif ch == "s":
            move_player_add(world, WIDTH)
        elif ch == "a":
            move_player_sub(world, 1)
        elif ch == "d":
            move_player_add(world, 1)
        elif ch == "l":
            world.break_block(int(world.player.loc+1))
        elif ch == "h":
            world.break_block(int(world.player.loc-1))
        elif ch == "k":
            world.break_block(int(world.player.loc-WIDTH))
        elif ch == "j":
            world.break_block(int(world.player.loc+WIDTH))

if __name__ == "__main__":
    main()
