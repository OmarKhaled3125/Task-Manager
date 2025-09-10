from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget,
    QLineEdit, QMessageBox, QListWidgetItem
)


class TaskWindow(QWidget):
    def __init__(self, api_client):
        super().__init__()
        self.api_client = api_client
        self.setWindowTitle("Tasks")

        layout = QVBoxLayout()

        # Task list
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        # New task input
        self.new_task_input = QLineEdit()
        self.new_task_input.setPlaceholderText("New task title")
        layout.addWidget(self.new_task_input)

        # Add task button
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        # Refresh button
        refresh_button = QPushButton("Refresh")
        refresh_button.clicked.connect(self.load_tasks)
        layout.addWidget(refresh_button)

        # Delete button
        delete_button = QPushButton("Delete Selected Task")
        delete_button.clicked.connect(self.handle_delete)
        layout.addWidget(delete_button)

        # Complete button
        complete_button = QPushButton("Mark Selected as Complete")
        complete_button.clicked.connect(self.handle_complete)
        layout.addWidget(complete_button)

        # Delete Account button
        delete_account_button = QPushButton("Delete Account")
        delete_account_button.setStyleSheet("background-color: red; color: white;")
        delete_account_button.clicked.connect(self.handle_delete_account)
        layout.addWidget(delete_account_button)

        self.setLayout(layout)

        # Load tasks on startup
        self.load_tasks()

    def load_tasks(self):
        """Fetch tasks from API and display in the list."""
        self.task_list.clear()
        tasks = self.api_client.get_tasks()
        for task in tasks:
            item = QListWidgetItem(f"{task['title']} ({task['status']})")
            item.setData(1000, task["id"])  # store task_id in custom role
            self.task_list.addItem(item)

    def add_task(self):
        """Add a new task using API."""
        title = self.new_task_input.text()
        if not title:
            QMessageBox.warning(self, "Error", "Task title cannot be empty")
            return

        if self.api_client.add_task(title):
            self.new_task_input.clear()
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Failed to add task")

    def get_selected_task_id(self):
        """Get task ID from selected list item."""
        selected = self.task_list.currentItem()
        if not selected:
            return None
        return selected.data(1000)  # retrieve task_id safely

    def handle_delete(self):
        """Delete selected task."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            QMessageBox.warning(self, "Error", "No task selected")
            return
        self.delete_task(task_id)

    def handle_complete(self):
        """Mark selected task as completed."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            QMessageBox.warning(self, "Error", "No task selected")
            return
        self.update_task_status(task_id)

    def delete_task(self, task_id):
        if self.api_client.delete_task(task_id):
            QMessageBox.information(self, "Success", "Task deleted!")
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Failed to delete task.")

    def update_task_status(self, task_id):
        if self.api_client.update_task(task_id, {"status": "completed"}):
            QMessageBox.information(self, "Success", "Task marked as completed!")
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Error", "Failed to update task.")

    def handle_delete_account(self):
        """Delete the currently logged-in account."""
        confirm = QMessageBox.question(
            self,
            "Confirm Deletion",
            "Are you sure you want to delete your account? This action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if confirm == QMessageBox.Yes:
            if self.api_client.delete_account():
                QMessageBox.information(self, "Success", "Account deleted. Exiting app.")
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Failed to delete account.")
