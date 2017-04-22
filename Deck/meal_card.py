import copy

from Deck.nested_card import NestedCard
import Deck.task_assignment as task_assignment


class Meal(NestedCard):
    def __init__(self, name, json_values, card_definitions=None):
        super(Meal, self).__init__(name, json_values, card_definitions)
        self.name = name
        self.cooking_tasks = [task_assignment.Task(**values) for values in json_values['cooking_tasks']]
        self.cleaning_tasks = [task_assignment.Task(**values) for values in json_values['cleaning_tasks']]
        if json_values.get('auto_assign', False):
            self.assign()

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
        if not self.is_nested():
            base_str = "Meal: %s" % self.name
            base_str += '\nCooking Tasks:'
            for task in self.cooking_tasks:
                base_str += '\n\t%s' % str(task)
            base_str += '\nCleaning Tasks:'
            for task in self.cleaning_tasks:
                base_str += '\n\t%s' % str(task)
            return base_str
        else:
            return super(Meal, self).__str__()

    def assign(self):
        self.cooking_tasks = self.assign_tasks(self.cooking_tasks)
        self.cleaning_tasks = self.assign_tasks(self.cleaning_tasks)

    @staticmethod
    def assign_tasks(task_list):
        return task_assignment.assign_tasks(task_list)

    def flip(self):
        for task in self.cooking_tasks:
            task.flip()
        for task in self.cleaning_tasks:
            task.flip()


def FlippedMealFactory(name, json_values, card_definitions):
    meal = Meal(name, json_values, card_definitions)
    flipped_meal = copy.deepcopy(meal)
    flipped_meal.flip()
    meal.factory = 'FlippedMealFactory'
    flipped_meal.factory = 'FlippedMealFactory'
    return [meal, flipped_meal]
