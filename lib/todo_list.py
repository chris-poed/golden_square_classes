class TodoList:
    def __init__(self):
        self._my_todo_list = []

    def add(self, todo):
        self._my_todo_list.append(todo)
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos

    def incomplete(self):
        if len(self._my_todo_list) == 0:
            raise Exception('No tasks in the list, well done')
        return [todo for todo in self._my_todo_list if todo.complete == False]
        # Returns:
        #   A list of Todo instances representing the todos that are not complete

    def complete(self):
        return [todo for todo in self._my_todo_list if todo.complete == True]
        # Returns:
        #   A list of Todo instances representing the todos that are complete

    def give_up(self):
        if len(self.incomplete()) == 0:
            raise Exception('All tasks already complete')
        [todo.mark_complete() for todo in self._my_todo_list]
