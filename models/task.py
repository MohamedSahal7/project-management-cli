class Task:
    id_counter = 1
    def __init__(self, title, assigned_to=""):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.title = title
        self.status = "Pending"
        self.assigned_to = assigned_to

    def complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.title} - {self.status}"