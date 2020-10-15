'''
usage: python quickflash.py [-h] -f FILEPATH [-d DELIMITER] [--no_shuffle] [--no_header]

Use the `help` flag for more information about the parameters.
'''

import sys, random, os
import argparse

# ...
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True, dest="filepath", help="Path of file")
parser.add_argument(
    "-d",
    "--delim",
    default="\t",
    dest="delimiter",
    help=r"Delimiter of source file (default \t)",
)
parser.add_argument(
    "--no_shuffle",
    dest="shuffle",
    action="store_false",
    help="Prevent shuffling of data",
)
parser.add_argument(
    "--no_header",
    dest="header",
    action="store_false",
    help="Prevent considering first line as header",
)

args = parser.parse_args()


def quickflash(args):
    with open(args.filepath, 'r') as df:
        data = df.readlines()
        data = [x.strip() for x in data]
        if args.header:
            data = data[1:]
        cards = [
            (x.split(args.delimiter)[0], ' '.join(x.split(args.delimiter)[1:]))
            for x in data
        ]
        if args.shuffle:
            random.shuffle(cards)

    ans = ''
    print('Type exit to quit')

    i = 0
    while ans.lower() != 'exit' and len(cards) > 0:
        os.system('clear')
        print(cards[0][0])
        tmp = input()
        print(cards[0][1])
        ans = input()
        if len(ans) == 0:
            cards.pop(0)
        else:
            cards.append(cards.pop(0))
        i += 1
        print('\n' * 2 + '=' * 5 + '\n' * 2)

    print(f'Done! Reviewed {i} times.')


if __name__ == '__main__':
    quickflash(args)
