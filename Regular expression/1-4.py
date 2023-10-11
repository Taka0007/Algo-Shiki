import re

S = input()

reg = r'cat|dog'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No") 