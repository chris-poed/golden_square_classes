import pytest
from lib.todo import Todo
from lib.todo_list import TodoList

"""
Given one todo
Adds the todo to the list
"""
def test_todo_list_adds_one_todo():
    todo_list = TodoList()
    todo_1 = Todo('Make breakfast')
    todo_list.add(todo_1)
    assert todo_list.incomplete() == [todo_1]



"""
Given multiple todos
Returns one incomplete todo
"""
def test_todo_list_returns_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo('Make breakfast')
    todo_2 = Todo('Make lunch')
    todo_3 = Todo('Make dinner')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todo_list.incomplete() == [todo_3]



"""
Given multiple todos
Returns two complete todos
"""
def test_todo_list_returns_complete_todos():
    todo_list = TodoList()
    todo_1 = Todo('Make breakfast')
    todo_2 = Todo('Make lunch')
    todo_3 = Todo('Make dinner')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_1.mark_complete()
    todo_2.mark_complete()
    assert todo_list.complete() == [todo_1, todo_2]



"""
Given multiple todos
Give_up marks all todos as complete
"""
def test_give_up_marks_all_todos_as_complete():
    todo_list = TodoList()
    todo_1 = Todo('Make breakfast')
    todo_2 = Todo('Make lunch')
    todo_3 = Todo('Make dinner')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    todo_list.give_up()
    assert todo_list.complete() == [todo_1, todo_2, todo_3]

"""
If no todos in the list
Return an error message to the user 'No tasks in the list, well done'
"""
def test_todo_list_incomplete_returns_message_when_no_tasks():
    todo_list = TodoList()
    with pytest.raises(Exception) as error:
        todo_list.incomplete()
    assert str(error.value) == 'No tasks in the list, well done'


"""
If all todos already complete
Return an error message to the user 'All tasks already complete'
"""

def test_give_up_marks_all_todos_as_complete():
    todo_list = TodoList()
    todo_1 = Todo('Make breakfast')
    todo_2 = Todo('Make lunch')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    todo_2.mark_complete()
    with pytest.raises(Exception) as error:
        todo_list.give_up()
    assert str(error.value) == 'All tasks already complete'