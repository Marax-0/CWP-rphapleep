import sys

args = sys.argv[1:]

if len(args) != 1:
 print("none")
else:
 text = input("What was the parameter? ")
 if text == args[0]:
  print("Good job!")
 else:
  print("Nope, sorry...")

