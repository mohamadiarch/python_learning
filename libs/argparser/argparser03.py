

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('number1',help="first number")
parser.add_argument('number2',help="second number")
args=parser.parse_args()
print("you can this print if you run this program with argument")
print(args)
print(args.number1)
# if you run this program with no argument you get error
# you can run this progrma with -h flag and no argument
# if you send more than 2 arguments you get error too
