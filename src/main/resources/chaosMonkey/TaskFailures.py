import random
import sys

from org.slf4j import LoggerFactory

logger = LoggerFactory.getLogger("chaosMonkey")

randInt = random.randint(0, 1000)

if float(randInt) < float(failureRate)*1000:
    logger.error('Chaos monkey strikes - task failure')
    sys.exit(1)
else:
    sys.exit(0)