import sys
args = sys.argv[1:]
if len(args) < 2:
 print("none")
else:
 for para in args[::-1]:
  print(para)
