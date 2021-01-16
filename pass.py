import string
import random
import sys


print(
    ''.join([str(s) for s in [random.choice(
        string.ascii_letters + string.digits + "{}[]()/\'\"`~,;:.<>"
    ) for p in range(int(sys.argv[1]))
    ]])
)
