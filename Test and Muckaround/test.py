import hashlib

class User:
    def __init__(self, username, password, privilege_level):
        self.username = username
        self.password = password
        self.privilege_level = privilege_level

    def hashed_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def check_privileges(self, required_level):
        privilege_hierarchy = {'guest': 0, 'standard': 1, 'admin': 2}
        return privilege_hierarchy.get(self.privilege_level, 0) >= privilege_hierarchy.get(required_level, 0)

    def safe_user_display(self):
        return {
            'privilege_level': self.privilege_level,
        }

user1 = User('john123', 'safepassword', 'admin')

user1.hashed_password('safepassword')
print (user1.hashed_password(user1.password))

user1.safe_user_display()