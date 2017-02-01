'''https://docs.google.com/spreadsheets/d/11Ter3a38OXjwzwkWccF96ng3CFvFEx-bPBR__1IPh1Q/edit?usp=sharing'''

import sys
import random
def loadFromFile(fn):
    with open(fn) as textFile:
        list = [line.strip(' \t\n\r').split(",") for line in textFile]
    return list

tech=loadFromFile("tech.txt")
verb=loadFromFile("verbs.txt")
issues=loadFromFile("issues.txt")

i_tech=random.randint(0, len(tech))
i_verb=random.randint(0, len(verb))
i_issues=random.randint(0, len(issues))

print
print
print random.choice(tech[i_tech]),random.choice(verb[i_verb]),random.choice(issues[i_issues])
print
print
