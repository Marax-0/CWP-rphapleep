import sys
args = sys.argv[1:]
if len(args) != 1:
 print("none")
else:
 count = args[0].count('z')
 if count == 0:
  print("none")
 else:
  print('z' * count)
