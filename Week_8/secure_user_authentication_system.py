import hashlib
from datetime import datetime
import hmac

class User:
    def __init__(self, username, password, privilege_level):
        # Validate inputs
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        valid_levels = ['guest', 'standard', 'admin']
        if privilege_level not in valid_levels:
            raise ValueError(f"Invalid privilege level. Must be one of: {valid_levels}")
        
        self.username = username
        self._password_hash = self._hash_password(password)
        self.privilege_level = privilege_level
        self.login_attempts = 0
        self.account_status = 'active'
        self.activity_log = []
        self.log_activity(f'Account created with privilege level: {privilege_level}')

    def log_activity(self, text):
        """Log all user activities with timestamps."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.activity_log.append(f'[{timestamp}] {text}')

    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def authenticate(self, password: str) -> bool:
        """Authenticate user with password."""
        if self.account_status == 'locked':
            self.log_activity('Login attempt on locked account')
            return False

        attempt_hash = self._hash_password(password)

        if hmac.compare_digest(attempt_hash, self._password_hash):
            self.login_attempts = 0
            self.log_activity('Login successful')
            return True
        else:
            self.login_attempts += 1
            self.log_activity(f'Failed login attempt #{self.login_attempts}')

            if self.login_attempts >= 3:
                self.lock_account()

            return False

    def check_privileges(self, required_level):
        """Check if user has sufficient privileges."""
        privilege_tiers = {'guest': 1, 'standard': 2, 'admin': 3}
        user_tier = privilege_tiers.get(self.privilege_level, 0)
        required_tier = privilege_tiers.get(required_level, 0)
        
        has_access = user_tier >= required_tier
        self.log_activity(f'Privilege check for {required_level}: {"granted" if has_access else "denied"}')
        return has_access

    def lock_account(self):
        """Lock account after too many failed attempts."""
        self.account_status = 'locked'
        self.log_activity('Account locked due to 3 failed login attempts')
        return 'Account has been locked due to too many failed login attempts.'

    def reset_login_attempts(self, admin_user, admin_password: str) -> bool:
        """Unlock account - can only be done by an admin user."""
        # Check if the requesting user is an admin
        if admin_user.privilege_level != 'admin':
            self.log_activity(f'Unauthorized unlock attempt by {admin_user.username}')
            return False
        
        # Verify admin's password (using their own authenticate method)
        if not admin_user.authenticate(admin_password):
            self.log_activity(f'Failed unlock attempt by {admin_user.username} - invalid password')
            return False
        
        # Unlock this account
        self.account_status = 'active'
        self.login_attempts = 0
        self.log_activity(f'Account unlocked by admin: {admin_user.username}')
        return True

    def set_privilege_level(self, new_level: str, admin_user, admin_password: str) -> bool:
        """Change privilege level - requires admin authorization."""
        valid_levels = ['guest', 'standard', 'admin']
        
        if new_level not in valid_levels:
            self.log_activity(f'Invalid privilege level attempted: {new_level}')
            return False
        
        # Only admins can change privileges
        if admin_user.privilege_level != 'admin':
            self.log_activity(f'Unauthorized privilege change attempt by {admin_user.username}')
            return False
        
        if not admin_user.authenticate(admin_password):
            return False
        
        old_level = self.privilege_level
        self.privilege_level = new_level
        self.log_activity(f'Privilege changed from {old_level} to {new_level} by {admin_user.username}')
        return True

    def change_password(self, old_password: str, new_password: str) -> bool:
        """Change user password after verifying old password."""
        if self.account_status == 'locked':
            self.log_activity('Password change attempted on locked account')
            return False
        
        # Verify old password
        if not hmac.compare_digest(self._hash_password(old_password), self._password_hash):
            self.log_activity('Failed password change - incorrect old password')
            return False
        
        # Validate new password
        if len(new_password) < 8:
            self.log_activity('Failed password change - new password too short')
            return False
        
        self._password_hash = self._hash_password(new_password)
        self.log_activity('Password changed successfully')
        return True

    def safe_user_display(self):
        """Display user information without exposing sensitive data."""
        self.log_activity('User information requested')
        return {
            'username': self.username,
            'privilege_level': self.privilege_level,
            'account_status': self.account_status,
            'login_attempts': self.login_attempts
        }

    def get_activity_log(self):
        """Return the activity log."""
        return self.activity_log.copy()

    def __repr__(self):
        """String representation that doesn't expose sensitive data."""
        return f"User(username='{self.username}', privilege='{self.privilege_level}', status='{self.account_status}')"


# Test the implementation
if __name__ == "__main__":
    print("=== Creating Users ===")
    admin = User('admin_user', 'AdminPass123', 'admin')
    user1 = User('john_doe', 'SecurePass456', 'standard')
    guest = User('guest_user', 'GuestPass789', 'guest')