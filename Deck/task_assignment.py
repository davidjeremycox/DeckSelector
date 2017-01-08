import random
import copy


class Task(object):
    def __init__(self, description, difficulty=0, group=None, assignment=Workers.SCUP):
        self.description = description
        self.type = None
        self.difficulty = difficulty
        self.assignment = assignment
        self.group = group

    def flip(self):
        if self.assignment == Workers.SCUP:
            self.assignment = Workers.KIP
        elif self.assignment == Workers.KIP:
            self.assignment = Workers.SCUP

    def __eq__(self, other):
        if not isinstance(other, Task):
            return False
        elif self.assignment != other.assignment:
            return False
        elif self.description != other.description:
            return False
        else:
            return True

    def __str__(self):
        assignee = 'SCUP' if self.assignment == 1 else 'KIP'
        return 'Description: %s Assignee: %s Difficulty: %s' % (self.description, assignee, self.difficulty)


class Workers(object):
    SCUP = 1
    KIP = 2


def get_total_difficulty(task_list):
    total = 0
    for task in task_list:
        total += task.difficulty
    return total


def get_total_assigned_difficult(task_list, assignee):
    total = 0
    for task in task_list:
        if task.assignment == assignee:
            total += task.difficulty
    return total


def difficult_difference(task_list, first_assignee=Workers.SCUP, second_assignee=Workers.KIP):
    first_diff = get_total_assigned_difficult(task_list, first_assignee)
    second_diff = get_total_assigned_difficult(task_list, second_assignee)
    return first_diff - second_diff


def assign_tasks(task_list, first_assignee=Workers.SCUP, second_assignee=Workers.KIP):
    working_list = copy.deepcopy(task_list)
    #working_list.sort(key=lambda x: x.difficulty, reverse=True)
    assigned_list_shuffle = shuffle_assignment(working_list)
    shuffle_difference = difficult_difference(assigned_list_shuffle, first_assignee, second_assignee)
    working_list = copy.deepcopy(task_list)
    assigned_list_equal = equal_assignment(working_list, first_assignee, second_assignee)
    equal_difference = difficult_difference(assigned_list_equal)
    if shuffle_difference < equal_difference:
        return assigned_list_shuffle
    return assigned_list_equal


def shuffle_assignment(task_list, first_assignee=Workers.SCUP, second_assignee=Workers.KIP):
    total_difficulty = get_total_difficulty(task_list)
    target_difficulty = total_difficulty // 2
    random.shuffle(task_list)
    assigned_list = []
    assigned_difficulty = 0
    while (assigned_difficulty < target_difficulty):
        task = task_list.pop()
        assigned_difficulty += task.difficulty
        task.assignment = first_assignee
        assigned_list.append(task)
    for task in task_list:
        task.assignment = second_assignee
    assigned_list.extend(task_list)
    return assigned_list


def equal_assignment(task_list, first_assignee=Workers.SCUP, second_assignee=Workers.KIP):
    assigned_list = []
    target_count = len(task_list) // 2
    assigned_count = 0
    while (assigned_count < target_count):
        task = task_list.pop()
        task.assignment = first_assignee
        assigned_list.append(task)
        assigned_count += 1
    for task in task_list:
        task.assignment = second_assignee
    assigned_list.extend(task_list)
    return assigned_list


def print_task_list(task_list):
    for task in task_list:
        print(str(task))
