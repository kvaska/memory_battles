from dataclasses import dataclass
from typing import Any
from collections import namedtuple as nt
import random
import math


class Position(nt('position', ['x', 'y'])):
    pass


@dataclass
class Cell:
    '''class Cell describes abilities of player`s cell'''
    hp: int = 10
    energy: int = 1
    speed_level: int = 1
    fight_level: int = 1
    deviding_level: int = 1
    num_to_upgrade: int = 0
    upgr_order: str = '' #'sssff'
    position: Position = Position(0, 0)
    player_clan: int = 0
    # cost_of_upgr: Any = [10, 20, 40] = 10*(2**(cur_apgr_count - 1))

    def upgrade(self):
        upgr = self.upgr_order[self.num_to_upgrade:min(
            self.num_to_upgrade+1, len(self.num_to_upgrade))]
        cur_upgr_count = min(self.upgr_order[:min(
            self.num_to_upgrade+1, len(self.num_to_upgrade))].count(upgr), 3)
        cost_of_upgr = 10*(2**(cur_upgr_count - 1))
        if self.energy > self.cost_of_upgr.inde:
            if (upgr == '' or cur_upgr_count > 3):
                return
            if upgr == 's':
                self.speed_level += 1
            elif upgr == 'f':
                self.fight_level += 1
            elif upgr == 'd':
                self.deviding_level += 1
            else:
                return
            self.num_to_upgrade = min(
                self.num_to_upgrade + 1, len(self.upgr_order))
            self.energy -= self.cost_of_upgr

    def move(self, direction: str):
        cur_pos = self.position
        new_pos = cur_pos
        if direction == 'u':
            new_pos = (cur_pos[0] + (2**(self.speed_level-1)), cur_pos[1])
        elif direction == 'd':
            new_pos = (cur_pos[0] - (2**(self.speed_level-1)), cur_pos[1])
        elif direction == 'r':
            new_pos = (cur_pos[0], cur_pos[1] + (2**(self.speed_level-1)))
        elif direction == 'l':
            new_pos = (cur_pos[0], cur_pos[1] - (2**(self.speed_level-1)))
        if(-50 < new_pos[0] < 50 and -50 < new_pos[1] < 50):
            self.position = new_pos
        else:
            self.hp -= 5


def fight(first: Cell, second: Cell):
    while first.hp > 0 and second.hp > 0:
        first.hp -= second.fight_level * random.randint(0, 1)
        second.hp -= first.fight_level * random.randint(0, 1)