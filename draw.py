#!/usr/bin/python

from random import *
from math import *
from copy import deepcopy

class draw:
    def __init__(self, members=None, group_size=0):
        self.members = members
        self.group_size = group_size
        self.league_size = self.__get_league_size()
        self.pot_size = ceil(self.league_size/float(self.group_size))

        self.pots = list()
        self.__create_pots()

        self.groups = list()
        self.__draw_groups()

    def __get_league_size(self):
        return len(self.members) - (len(self.members) % self.group_size)

    def __create_pots(self):
        for i in range(self.group_size):
            self.pots.append(self.members[i * self.pot_size:(i+1) * self.pot_size])

    def __draw_groups(self):
        lpots = deepcopy(self.pots)
        for i in range(self.pot_size):
            self.groups.append([pot.pop(randint(0, len(pot)-1)) for pot in lpots if pot])

if __name__ == "__main__":
    members = ['Australia', 'IR Iran', 'Korea Republic', 'Japan', 'Saudi Arabia', 'Syria', 'China PR', \
    'United Arab Emirates', 'Lebanon', 'Oman', 'Iraq', 'Kyrgyz Republic', 'Uzbekistan', 'India', 'Qatar', \
    'Palestine', 'Vietnam', 'Korea DPR', 'Jordan', 'Bahrain', 'Philippines', 'Tajikistan', 'Thailand', \
    'Chinese Taipei', 'Turkmenistan', 'Yemen', 'Myanmar', 'Hong Kong', 'Afghanistan', 'Maldives', 'Kuwait', \
    'Nepal', 'Indonesia', 'Cambodia', 'Singapore', 'Malaysia', 'Laos', 'Bhutan', 'Macau', 'Mongolia', \
    'Timor-Leste', 'Guam', 'Bangladesh', 'Brunei Darussalam', 'Sri Lanka', 'Pakistan']

    draw = draw(members[:40], group_size=5)
    for pot in draw.pots:
        print(pot)
    print(' -  -  -  -  -  -  -  - ')
    for group in draw.groups:
        print(group)
