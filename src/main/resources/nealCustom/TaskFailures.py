import random
import sys

randInt = random.randint(0, 1000)
if float(randInt) < float(failureRate)*1000:
    sys.exit("Deliberately failing task")

