import json
import os

class UserStore:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load(self):
        """Load users from file, return empty list if file doesn't exist."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return []
    
    def save(self, users):
        """Save users list to file as JSON."""
        with open(self.file_path, "w") as f:
            json.dump(users, f, indent=2)
    
    def find_by_id(self, user_id):
        """Find and return user by ID, or None if not found."""
        users = self.load()
        return next((u for u in users if u["id"] == user_id), None)
    
    def update_user(self, user_id, updated_data):
        """Update user by ID. Returns True if successful, False if not found."""
        users = self.load()
        for i, user in enumerate(users):
            if user["id"] == user_id:
                users[i] = {"id": user_id, **updated_data}
                self.save(users)
                return True
        return False
    
    def delete_user(self, user_id):
        """Delete user by ID. Returns True if successful, False if not found."""
        users = self.load()
        filtered = [u for u in users if u["id"] != user_id]
        if len(filtered) == len(users):
            return False
        self.save(filtered)
        return True