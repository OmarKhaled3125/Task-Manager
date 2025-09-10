import requests

class ApiClient:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url
        self.token = None

    def _headers(self):
        """Helper function to include Authorization if logged in."""
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def signup(self, username, password, email=None):
        payload = {"username": username, "password": password}
        if email:  # optional email support
            payload["email"] = email

        response = requests.post(
            f"{self.base_url}/auth/register",
            json=payload,
            headers=self._headers()
        )

        if response.status_code == 201:
            return True

        # Print for debugging
        print("Signup failed:", response.status_code, response.text)
        return False

    def login(self, username, password):
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            self.token = response.json().get("access_token")
            return True
        return False

    def get_tasks(self):
        response = requests.get(f"{self.base_url}/tasks", headers=self._headers())
        if response.status_code == 200:
            return response.json()
        return []

    def add_task(self, title, description=""):
        response = requests.post(
            f"{self.base_url}/tasks",
            json={"title": title, "description": description},
            headers=self._headers(),
        )
        return response.status_code == 201

    def delete_task(self, task_id):
        response = requests.delete(
            f"{self.base_url}/tasks/{task_id}", headers=self._headers()
        )
        return response.status_code == 200

    def update_task(self, task_id, data):
        response = requests.put(
            f"{self.base_url}/tasks/{task_id}",
            json=data,
            headers=self._headers(),
        )
        return response.status_code == 200

    def delete_account(self):
        response = requests.delete(
            f"{self.base_url}/auth/delete", headers=self._headers()
        )
        if response.status_code == 200:
            # clear token so user is logged out after deletion
            self.token = None
            return True

        print("Account deletion response:", response.status_code, response.text)  # <-- Add debug
        return response.status_code == 200
