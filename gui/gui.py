from PyQt5.QtWidgets import QApplication
from gui.api_client import ApiClient
from gui.windows.signup import SignupWindow
from gui.windows.tasks import TaskWindow

class MainApp:
    def __init__(self):
        self.api_client = ApiClient()

        # Start with signup/login window
        self.signup_window = SignupWindow(self.api_client, self.open_tasks)
        self.signup_window.show()

        self.task_window = None

    def open_tasks(self):
        self.task_window = TaskWindow(self.api_client)
        self.task_window.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
