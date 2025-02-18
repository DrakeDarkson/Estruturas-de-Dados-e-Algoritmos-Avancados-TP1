import heapq

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, priority, task_name):
        heapq.heappush(self.tasks, (priority, task_name))

    def pop_task(self):
        if not self.tasks:
            raise IndexError("Nenhuma tarefa na fila")
        return heapq.heappop(self.tasks)

    def peek_task(self):
        return self.tasks[0] if self.tasks else None

    def __str__(self):
        return str(self.tasks)

# Exemplo:
scheduler = TaskScheduler()
scheduler.add_task(3, "Revisar código")
scheduler.add_task(1, "Responder e-mails")
scheduler.add_task(2, "Corrigir bug")

print("Fila de prioridade:", scheduler)

print("Tarefa com maior prioridade:", scheduler.pop_task())
print("Fila após remoção:", scheduler)
