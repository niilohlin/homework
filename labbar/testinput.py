
import pexpect
import sys

strings = """

add niil 1234
alias niil nille
lookup niil
lookup nille
lookup dinmamma
antoeu ao
alias kantaroce roc
change niil 4321
alias hurr durr
change dinmamma kalas
add uberman 1337
add berzelius 1828
add e 2.71
save database
quit
""".splitlines()


c = pexpect.spawnu('/usr/bin/env python2 %s' % sys.argv[1])

for cmd in strings:
    c.send(cmd + '\n')
for response in c.readlines():
    print response.strip()

