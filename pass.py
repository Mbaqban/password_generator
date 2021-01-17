import string
import random
import sys


print(
    ''.join([random.choice(
        string.ascii_letters + string.digits + "{}[]()/\'\"`~,;:.<>"
    ) for p in range(int(sys.argv[1]))
    ])
)
