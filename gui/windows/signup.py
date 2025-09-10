from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox

class SignupWindow(QWidget):
    def __init__(self, api_client, on_success):
        super().__init__()
        self.api_client = api_client
        self.on_success = on_success  # callback to open tasks after signup/login

        self.setWindowTitle("Sign Up / Login")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Username"))
        self.username_input = QLineEdit()
        layout.addWidget(self.username_input)

        layout.addWidget(QLabel("Password"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.handle_signup)
        layout.addWidget(signup_button)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_signup(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if not username or not password:
            QMessageBox.warning(self, "Error", "Username and password required")
            return

        if self.api_client.signup(username, password):
            QMessageBox.information(self, "Success", "Account created! Please login.")
        else:
            QMessageBox.warning(self, "Error", "Sign up failed (maybe username exists)")

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.api_client.login(username, password):
            QMessageBox.information(self, "Success", "Login successful!")
            self.on_success()  # open Task window
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Login failed. Check credentials.")
