from .dungeon import *
from pytest import raises
import roughly

def test_random_move():
  assert random_move([[1], [0,2], [1, 3], [2,4], [3]], 0 ) == 1

  assert random_move([[1], [0,2], [1, 3], [2,4], [3]], 1 ) == 0 or 2


def test_success_chance():
	assert success_chance( 
{'name': 'dungeon3', 'treasure': [2], 'adventurer': 0, 'troll': 4, 'network': [[1], [0, 2], [1, 3], [2, 4], [3]]}, 10000) == 0