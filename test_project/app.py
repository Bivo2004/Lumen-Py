# test_project/app.py

from database import MySQLDatabase

class WebServer:
    def __init__(self):
        # TIGHT COUPLING: The server builds its own specific database dependency.
        # It is now impossible to test this without a real MySQL database.
        self.db = MySQLDatabase()

    def start_server(self):
        print("Starting the web server...")
        self.db.connect()

    def load_user_profile(self, user_id):
        user_data = self.db.get_user(user_id)
        print(f"Displaying profile for: {user_data}")

if __name__ == "__main__":
    app = WebServer()
    app.start_server()
    app.load_user_profile(42)