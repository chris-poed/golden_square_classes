from lib.todo_list import TodoList
from lib.todo import Todo

"""
Given one task
Returns a list of one incomplete task
"""

def test_todo_list_integration():
    todo_list = TodoList()
    todo_1 = Todo('Make breakfast')
    todo_list.add(todo_1)
    assert todo_list.incomplete() == [todo_1]
