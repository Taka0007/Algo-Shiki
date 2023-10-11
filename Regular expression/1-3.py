import re

S = input()

reg = r'^a{1,5}b{10}c*$'

search = re.search(reg, S)
if search:
    print("Yes")
else:
    print("No") 