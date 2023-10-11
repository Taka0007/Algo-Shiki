import re

S = input()

reg = r'^metho+d$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No") 