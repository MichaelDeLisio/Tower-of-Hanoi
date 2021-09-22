"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
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
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "__main__":'

import time, math
from toah_model import TOAHModel, MoveSequence


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    height = model.get_number_of_cheeses()
    move_seq = MoveSequence([])
    four_solver(height, move_seq, 0, 1, 2, 3)
    model._move_seq = move_seq
    if animate:
        print(str(model))
    for move in move_seq._moves:
        model.move(move[0], move[1])
        if animate:
            time.sleep(delay_btw_moves)
            print(str(model))        
    
def four_solver(height, move_seq, org, intm, intm2, dest) -> None:
    if height > 1:
        j = 1
        i = 1 
        moves_acc = float('inf')
        i = find_i(height, j, i, moves_acc)       
        four_solver(height - i, move_seq, org, intm, dest, intm2)
        three_solver(i, move_seq, org, intm, dest)
        four_solver(height - i, move_seq, intm2, intm, org, dest)
    else:
        move_seq.add_move(org, dest)

def three_solver(height: int, move_seq: MoveSequence, org, intm, dest) -> None:
    '''Modifies model to complete the Tour of Anne Hoy Game with three stools.
    For a model with n cheeses, the model is completed in 2^n - 1 moves.
    '''
    if height == 1:
        move_seq.add_move(org, dest)
    else:
        three_solver(height-1, move_seq, org, dest, intm)
        three_solver(1, move_seq, org, intm, dest)
        three_solver(height-1, move_seq, intm, org, dest)

        
def find_i(n, j, i, moves_acc):
    if j == n:
        return i
    else:
        new_moves = (2 * find_optimal_moves(n-j)) + 2**j - 1
        if new_moves < moves_acc :
            i = j
            moves_acc = new_moves
        j += 1
    return find_i(n, j, i, moves_acc)

def find_optimal_moves(n):
    if (n <= 1):
        return 1
    else:
        i = find_i(n, 1, 1, float("inf"))
    return 2 * find_optimal_moves(n-i) + 2**i - 1
    

if __name__ == '__main__':
    num_cheeses = 25
    delay_between_moves = 1
    console_animate = True

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    

