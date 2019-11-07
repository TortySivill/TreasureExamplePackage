
import random
import copy
import argparse
import os

class Dungeon:

    def __init__(self, name, treasure, adventurer, troll, network):
        self.name = name
        self.treasure = treasure
        self.adventurer = adventurer
        self.troll = troll
        self.network = network


def random_move(network, current_loc):
    targets=network[current_loc]
    return random.choice(targets)

def update_dungeon(dungeon):
    dungeon.adventurer=random_move(dungeon.network, dungeon.adventurer)
    dungeon.troll=random_move(dungeon.network, dungeon.troll)


def outcome(dungeon):
    if dungeon.adventurer==dungeon.troll:
        return -1
    if dungeon.adventurer in dungeon.treasure:
        return 1
    return 0


def run_to_result(dungeon):
    dungeon=copy.deepcopy(dungeon)
    max_steps=1000
    for _ in range(max_steps):
        result= outcome(dungeon)
        if result != 0:
            return result
        update_dungeon(dungeon)
    # don't run forever, return 0 (e.g. if there is no treasure and the troll can't reach the adventurer)
    return result

def success_chance(dungeon, sample):
    trials=sample
    successes=0
    for _ in range(trials):
        outcome = run_to_result(dungeon)
        if outcome == 1:
            successes+=1
    return successes/trials



def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="display a square of a given number",
                    type=str)
    parser.add_argument('--sample', help='sample size', default=10000, type=int)
    args = parser.parse_args()
    
    f = open( args.filename, "r")
    contents =f.read()
    result = [x.strip() for x in contents.split(';')]
    
    name = result[0]
    treasure = [int(result[1])]
    adventurer = int(result[2])
    troll = int(result[3])
    
    network = result[4]
    network2 = [[x.strip()] for x in network.split('\n')]
    network3 = []
    for x in network2:
        temp = []
        for s in str(x):
            if s.isdigit():
                temp.append(int(s))
        network3.append(temp)
    network = network3
    
    dungeon = Dungeon(name, treasure, adventurer, troll, network)
    string = 'The chance of success is ' + str(success_chance(dungeon, args.sample)) + '\n'
    byte_string = string.encode('utf-8')
    os.write(1,byte_string)

if __name__ == "__main__":
    main()


