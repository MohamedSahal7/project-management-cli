import unittest
from models.task import Task

class TestTask(unittest.TestCase):
    def test_complete_task(self):
        task = Task("Build CLI")
        task.complete()
        self.assertEqual(
            task.status,
            "Completed"
        )

if __name__ == "__main__":
    unittest.main()