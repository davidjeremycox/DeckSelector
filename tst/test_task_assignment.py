import Deck.task_assignment as task_assignment
from Deck.task_assignment import Task, Workers
import random
import UnitTestHelper.helper_functions as helper

def build_task_list():
    descriptions = ['a', 'b', 'c']
    tasks = [Task(x) for x in descriptions]
    tasks[0].assignment = Workers.SCUP
    tasks[0].difficulty = 1
    tasks[1].assignment = Workers.KIP
    tasks[1].difficulty = 2
    tasks[2].assignment = Workers.SCUP
    tasks[2].difficulty = 3
    return tasks

def build_even_task_list():
    descriptions = ['a', 'b', 'c', 'd']
    tasks = [Task(x) for x in descriptions]
    tasks[0].assignment = Workers.SCUP
    tasks[0].difficulty = 1
    tasks[1].assignment = Workers.KIP
    tasks[1].difficulty = 1
    tasks[2].assignment = Workers.SCUP
    tasks[2].difficulty = 1
    tasks[3].assignment = Workers.SCUP
    tasks[3].difficulty = 1
    return tasks

def test_shuffle_assignment():
    random.seed(10)
    sample_tasks = build_task_list()
    assigned_tasks = task_assignment.shuffle_assignment(sample_tasks, Workers.KIP, Workers.SCUP)
    ref_assignees = [Workers.KIP, Workers.KIP, Workers.SCUP]
    for ind, pair in enumerate(zip(assigned_tasks, ref_assignees)):
        task, ref_assignee = pair
        helper.print_if_assert('Task assignment mismatch index: %s' % ind, task.assignment, ref_assignee)

def test_equal_assignment():
    random.seed(10)
    sample_tasks = build_task_list()
    assigned_tasks = task_assignment.equal_assignment(sample_tasks, Workers.KIP, Workers.SCUP)
    ref_assignees = [Workers.KIP, Workers.SCUP, Workers.SCUP]
    for ind, pair in enumerate(zip(assigned_tasks, ref_assignees)):
        task, ref_assignee = pair
        helper.print_if_assert('Task assignment mismatch index: %s' % ind, task.assignment, ref_assignee)

def test_equal_assignment_even():
    random.seed(10)
    sample_tasks = build_even_task_list()
    assigned_tasks = task_assignment.equal_assignment(sample_tasks, Workers.KIP, Workers.SCUP)
    ref_assignees = [Workers.KIP, Workers.KIP, Workers.SCUP, Workers.SCUP]
    for ind, pair in enumerate(zip(assigned_tasks, ref_assignees)):
        task, ref_assignee = pair
        helper.print_if_assert('Task assignment mismatch index: %s' % ind, task.assignment, ref_assignee)

def test_task_assign():
    random.seed(10)
    sample_tasks = build_task_list()
    assigned_tasks = task_assignment.assign_tasks(sample_tasks)
    ref_assignees = [Workers.SCUP, Workers.KIP, Workers.KIP]
    scup_diff = task_assignment.get_total_assigned_difficult(assigned_tasks, Workers.SCUP)
    kip_diff = task_assignment.get_total_assigned_difficult(assigned_tasks, Workers.SCUP)
    ref_scup_diff, ref_kip_diff = 3, 3
    helper.print_if_assert('Scup difficulty mismatch', scup_diff, ref_scup_diff)
    helper.print_if_assert('Scup difficulty mismatch', kip_diff, ref_kip_diff)
    for ind, pair in enumerate(zip(assigned_tasks, ref_assignees)):
        task, ref_assignee = pair
        helper.print_if_assert('Task assignment mismatch index: %s' % ind, task.assignment, ref_assignee)

def test_task_assign_equal():
    random.seed(10)
    sample_tasks = build_even_task_list()
    assigned_tasks = task_assignment.assign_tasks(sample_tasks)
    ref_assignees = [Workers.SCUP, Workers.SCUP, Workers.KIP, Workers.KIP]
    scup_diff = task_assignment.get_total_assigned_difficult(assigned_tasks, Workers.SCUP)
    kip_diff = task_assignment.get_total_assigned_difficult(assigned_tasks, Workers.SCUP)
    ref_scup_diff, ref_kip_diff = 2, 2
    helper.print_if_assert('Scup difficulty mismatch', scup_diff, ref_scup_diff)
    helper.print_if_assert('Kip difficulty mismatch', kip_diff, ref_kip_diff)
    for ind, pair in enumerate(zip(assigned_tasks, ref_assignees)):
        task, ref_assignee = pair
        helper.print_if_assert('Task assignment mismatch index: %s' % ind, task.assignment, ref_assignee)
