import random

from org.slf4j import LoggerFactory

logger = LoggerFactory.getLogger("chaosMonkey")

tasks = [task for task in getCurrentPhase().tasks]
pendingStatuses = ['PLANNED', 'PENDING']
pendingTasks = [task for task in tasks if task.status in pendingStatuses]

if len(pendingTasks) > 0:
    randomTaskInd = random.randint(0, len(pendingTasks)-1)
    pendingTasks[randomTaskInd].precondition = "foo = bar"
    taskApi.updateTask(pendingTasks[randomTaskInd])
    logger.warn('Chaos monkey strikes - failed task %s' % pendingTasks[randomTaskInd].id)
else:
    logger.warn('No pending tasks in phase - failing Chaos Monkey task')
    getCurrentTask.precondition = "foo = bar"
    taskApi.updateTask(getCurrentTask)
    taskApi.retryTask(getCurrentTask().id, "Task failed by Chaos Monkey")