import sqlite3
import ipdb 

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

class Player:
    def __init__(self, username):
        self.username = username
        self.results_list = []

    def results(self):
        return self.results_list

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if type(username) == str and len(username) >= 3:
            self._username = username
        else: 
            print('Username can only be letters and must be at least 3 charcaters.')
    
class Results:
    def __init__(self, score, player):
        self.score = score
        self.player = player
        self.player.results_list.append(self)

    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if type(player) == Player:
            self._player = player

class Game:
    def __init__(self, title):
        self.title = title
        self.results_list = []
        self.players_list = []
    
    def results(self):
        return self.results_list
    
    def players(self):
        return self.players_list

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        pass 





# p = Player('A')
# ipdb.set_trace()