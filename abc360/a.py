import re

S = input().strip()

if re.fullmatch(r".*R.*M.*", S) != None:
    print("Yes")
else:
    print("No")
