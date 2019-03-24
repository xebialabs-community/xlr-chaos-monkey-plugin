import random
import sys

randInt = random.randint(0, 1000)
if randInt < failureRate*1000:
    sys.exit("Failing task")

