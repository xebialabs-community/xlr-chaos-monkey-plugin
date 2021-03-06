import random

from org.slf4j import LoggerFactory

logger = LoggerFactory.getLogger("chaosMonkey")

tasks = [task for phase in getCurrentRelease().phases for task in phase.tasks]
pendingStatuses = ['PLANNED', 'PENDING']
pendingTasks = [task for task in tasks if task.status in pendingStatuses]

if len(pendingTasks) > 0:
    randomTaskInd = random.randint(0, len(pendingTasks)-1)
    pendingTasks[randomTaskInd].precondition = "foo = bar"
    taskApi.updateTask(pendingTasks[randomTaskInd])
    logger.warn('Chaos monkey strikes - failed task %s' % pendingTasks[randomTaskInd].id)
else:
    logger.warn('No pending or planned tasks in release - failing Chaos Monkey task')
    sys.exit("Task failed by Chaos Monkey")