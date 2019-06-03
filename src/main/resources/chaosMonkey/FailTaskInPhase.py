import random

from org.slf4j import LoggerFactory

logger = LoggerFactory.getLogger("chaosMonkey")

tasks = [task for task in getCurrentPhase().tasks]
pendingStatuses = ['PLANNED', 'PENDING', 'IN_PROGRESS', 'WAITING_FOR_INPUT']
pendingTasks = [task for task in tasks if task.status in pendingStatuses]

if len(pendingTasks) > 0:
    randomTaskInd = random.randint(0, len(pendingTasks)-1)
    taskApi.failTask(pendingTasks[randomTaskInd].id, "Task failed by Chaos Monkey")
    logger.warning('Chaos monkey strikes - failed task %s' % pendingTasks[randomTaskInd].id)
else:
    logger.warning('No pending tasks in phase - failing Chaos Monkey task')
    taskApi.failTask(getCurrentTask().id, "Task faild by Chaos Monkey")