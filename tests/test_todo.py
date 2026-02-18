from lib.todo import Todo
from lib.todo_list import TodoList

"""
Given a todo task
Instantiates a todo object with task and complete = False
"""

def test_instantiate_todo_task():
    todo_1 = Todo('Do some coding')
    assert vars(todo_1) == {'task': 'Do some coding', 'complete': False}


"""
Given an existing todo
mark_complete updates the 'complete' boolean to True
"""
def test_mark_complete_sets_boolean_to_true():
    todo_1 = Todo('Do some coding')
    todo_1.mark_complete()
    assert todo_1.complete == True
