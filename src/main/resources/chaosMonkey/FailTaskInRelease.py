import random

from org.slf4j import LoggerFactory

logger = LoggerFactory.getLogger("chaosMonkey")

tasks = [task for phase in getCurrentRelease().phases for task in phase.tasks]
pendingStatuses = ['PLANNED', 'PENDING']
pendingTasks = [task for task in tasks if task.status in pendingStatuses]

if len(pendingTasks) > 0:
    randomTaskInd = random.randint(0, len(pendingTasks)-1)
    pendingTasks[randomTaskInd].precondition = "foo = bar"
    logger.warning('Chaos monkey strikes - failed task %s' % pendingTasks[randomTaskInd].id)
else:
    logger.warning('No pending tasks in phase - failing Chaos Monkey task')
    getCurrentTask.precondition = "foo = bar"
    taskApi.retryTask(getCurrentTask().id, "Task failed by Chaos Monkey")