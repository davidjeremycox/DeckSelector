import copy

from Deck.card import Card
import Deck.task_assignment as task_assignment

class Meal(Card):
    def __init__(self, name, json_dict, type_definition):
        self.name = name
        self.cooking_tasks = []
        self.cleaning_tasks = []

    def __eq__(self, other):
        if not isinstance(other, Meal):
            return False
        if self.name != other.name:
            return False
        if len(self.cooking_tasks) != len(other.cleaning_tasks):
            return False
        if len(self.cleaning_tasks) != len(other.cleaning_tasks):
            return False
        for task, other_task in zip(self.cooking_tasks, other.cooking_tasks):
            if task != other_task:
                return False
        for task, other_task in zip(self.cleaning_tasks, other.cleaning_tasks):
            if task != other_task:
                return False
        return True

    def __str__(self):
        if self.deck == None:
            pass

    def assign(self):
        self.cooking_tasks = self.assign_tasks(self.cooking_tasks)
        self.cleaning_tasks = self.assign_tasks(self.cleaning_tasks)

    def assign_tasks(self, task_list):
        return task_assignment.assign_tasks(task_list)
