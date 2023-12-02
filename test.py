import re

string = "99lbqpxzzlbtvkmfrvrnmcxttone"

pattern = r"one"

matches = re.findall(pattern,string)

print(matches)