# test_project/database.py

class MySQLDatabase:
    def __init__(self):
        # Hardcoding credentials is a classic Junior move
        self.host = "127.0.0.1"
        self.user = "admin"
        self.connected = False

    def connect(self):
        print(f"Connecting to MySQL database at {self.host} as {self.user}...")
        self.connected = True

    def get_user(self, user_id):
        if not self.connected:
            return "Error: DB not connected."
        return {"id": user_id, "name": "Alice", "status": "active"}