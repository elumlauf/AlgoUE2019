import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help="Number of disks")
text="elumlauf-TowersOfHanoi.py fragt nach der Anzahl der Scheiben und gibt die Liste der Transfers "\
    "der Scheiben zwischen zwei Türmen in der Datei Towers_STDOUT.txt aus"

move_number = 0
args = parser.parse_args()

def tower(disks, left,middle,right):
    global move_number
    if disks == 1:
        move_number += 1
        print('Move disk from {} to {}.'.format(left, right))
        return

    tower(disks - 1, left, right, middle)
    move_number+=1
    print('Move disk from {} to {}.'.format(left, right))
    tower(disks - 1, middle, left, right)

disks = args.n
tower(disks, 'A', 'B', 'C')
print(move_number, file=sys.stderr)
