"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2018.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.


from toah_model import TOAHModel, IllegalMoveError
import sys


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)
    
def init_prompt() -> 'ConsoleController':
    cheeses = input('Enter the number of cheeses you\'d like to play with: ')
    while not cheeses.isnumeric() or int(cheeses) < 1:
        print("Please enter a number higher than zero.")
        cheeses = input('Enter the number of cheeses you\'d like to play with: ')
    return ConsoleController(int(cheeses), 4) 


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        game_model = TOAHModel(self.number_of_stools)
        game_model.fill_first_stool(self.number_of_cheeses)
        quit_message = 'Game Over'
        
        print("Welcome to the Tower of Anne Hoy")
        print('''\nThe objective of this game is to move all cheese rounds from
stool 1, to stool 4 without placing a bigger cheese round on top of
a smaller cheese round.\n''')
        print('''Enter the origin stool (either: stool[1], stool[2], stool[3],
stool[4]) and then similarly enter the desired destination stool which you'd
like to place the cheese round on. To exit the game enter, at any moment,
enter [q].\n''')
        
        while game_model._stool_list[-1]._height() < self.number_of_cheeses:
            print(str(game_model))
            origin = input("Enter origin stool: ")
            if origin.lower() == 'q':
                print(quit_message)
                sys.exit()
            dest = input("Enter destination stool: ")
            if dest.lower == 'q':
                print(quit_message)
                sys.exit()
            self.try_move(game_model, origin, dest)
        return self.win_message(game_model)
    


    def try_move(self, model: TOAHModel, origin: str, dest: str) -> None:
        '''Infinite until proper move is tried.'''
        
        try:
            origin = int(origin) - 1
            dest = int(dest) - 1 
            move(model, origin, dest)
        except IllegalMoveError:
            print("Invalid choice.")
            origin = input("Enter origin stool: ")
            if origin == 'q':
                print("Game Over")
                sys.exit()
            dest = input("Enter destination stool: ")
            if origin == 'q':
                print("Game Over")
                sys.exit()
            self.try_move(model, origin, dest)
        except Exception:
            print('Please enter a valid stool number in the range of 1 to ' + \
                  str(model.number_of_stools) + '.')
            origin = input("Enter origin stool: ")
            if origin == 'q':
                print("Game Over")
                sys.exit()
            dest = input("Enter destination stool: ")
            if origin == 'q':
                print("Game Over")
                sys.exit()
            self.try_move(model, origin, dest)            
    
    def win_message(self, model: TOAHModel) -> str:
        '''Return str representation of model and the win message.'''
        print(str(model))
        print("You finished the game in " + str(model.current_moves_score) + \
               " moves. Congratulations!")
        self.decision()
        
    def decision(self):
        
        decision = input('Do you want to play again? Input yes or no: ')
        if not (decision.lower() == 'yes'or decision.lower() == 'no'):
            self.decision()
        elif decision.lower() == 'yes':
            self.play_loop()
        else:
            print('Game Over')
            sys.exit()
        


if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    x = init_prompt()
    x.play_loop()
    
