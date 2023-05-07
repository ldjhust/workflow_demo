class MyModel(models.Model):
    # 状态机字段和待办事项字段...

    def complete_todo_item(self, todo_item):
        # 根据待办事项设置相应的外键字段为 None
        if self.todo_item_1 == todo_item:
            self.todo_item_1 = None
        elif self.todo_item_2 == todo_item:
            self.todo_item_2 = None
        elif self.todo_item_3 == todo_item:
            self.todo_item_3 = None

        # 如果所有待办事项都已经完成，则将对象转移到下一个状态
        if not self.todo_item_1 and not self.todo_item_2 and not self.todo_item_3:
            self._next_status()

        self.save()

    def _next_status(self):
        # 自动转移到下一个状态
        if self.status == Status.CREATED.value:
            self.to_state_1()
        elif self.status == Status.STATE_1.value:
            self.to_state_2()
        elif self.status == Status.STATE_2.value:
            self.to_state_3()
        elif self.status == Status.STATE_3.value:
            self.to_state_4()
        elif self.status == Status.STATE_4.value:
            self.to_state_5()
        elif self.status == Status.STATE_5.value:
            self.to_completed()



class MyModel(models.Model):
    # 状态机字段和待办事项字段...

    def get_todo_items(self):
        if self.status == Status.CREATED.value:
            return [
                {'name': 'task_1', 'assignee': 'user_1'},
                {'name': 'task_2', 'assignee': 'user_2'},
                {'name': 'task_3', 'assignee': 'user_3'}
            ]
        elif self.status == Status.STATE_1.value:
            return [
                {'name': 'task_4', 'assignee': 'user_4'},
                {'name': 'task_5', 'assignee': 'user_5'},
                {'name': 'task_6', 'assignee': 'user_6'}
            ]
        # ... 其他状态的待办事项

    def complete_todo_item(self, task_name, assignee_username):
        todo_item = TodoItem.objects.get(name=task_name, assignee__username=assignee_username)
        # 完成待办事项并转移到下一个状态，与步骤 4 相同
        # ...


class MyModel(models.Model):
    # 状态机字段和待办事项字段...

    def _next_status(self):
        if self.status == Status.CREATED.value:
            self.todo_item_1 = TodoItem.objects.get(name="task_1", assignee__username="user_1")
            self.todo_item_2 = TodoItem.objects.get(name="task_2", assignee__username="user_2")
            self.todo_item_3 = TodoItem.objects.get(name="task_3", assignee__username="user_3")
            self.to_state_1()
        elif self.status == Status.STATE_1.value:
            self.todo_item_1 = TodoItem.objects.get(name="task_4", assignee__username="user_4")
            self.todo_item_2 = TodoItem.objects.get(name="task_5", assignee__username="user_5")
            self.todo_item_3 = TodoItem.objects.get(name="task_6", assignee__username="user_6")
            self.to_state_2()
        elif self.status == Status.STATE_2.value:
            # ... 其他状态的待办事项


