import sys
import re

args = sys.argv[1:]

if len(args) != 2:
 print("none")
else:
 keyword = args[0]
 target_keyword = args[1]
 matches = re.findall(keyword, target_keyword)
 if not matches:
  print("none")
 else:
  print(len(matches))
