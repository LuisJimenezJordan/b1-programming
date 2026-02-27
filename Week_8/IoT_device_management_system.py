from datetime import datetime

class Device:
    def __init__(self, device_id, device_type, owner, firmware_version='1.0.0'):
        # Validate inputs
        if not device_id or not isinstance(device_id, str):
            raise ValueError("device_id must be a non-empty string")
        
        valid_types = ['camera', 'sensor', 'thermostat', 'lock', 'router', 'other']
        if device_type not in valid_types:
            raise ValueError(f"device_type must be one of: {valid_types}")
        
        if not owner or not isinstance(owner, str):
            raise ValueError("owner must be a non-empty string")
        
        self.device_id = device_id
        self.device_type = device_type
        self.firmware_version = firmware_version
        self.compliance_status = 'unknown'
        self.owner = owner
        self.last_security_scan = None
        self.is_active = True
        self.activity_log = []
        self.log_activity('SYSTEM', f'Device registered - Type: {device_type}, Owner: {owner}')

    def log_activity(self, username: str, message: str):
        """Log device activity with timestamp."""
        entry = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "user": username,
            "event": message
        }
        self.activity_log.append(entry)

    def authorise_access(self, user, admin_override=False):
        """Authorize user access to device."""
        is_admin = user.check_privileges('admin')

        # Device must be active
        if not self.is_active:
            self.log_activity(user.get_username(), 'Access denied - Device inactive')
            return False

        # Check compliance (unless admin override)
        if self.compliance_status != 'compliant':
            if is_admin and admin_override:
                self.log_activity(user.get_username(), 'Access granted - Admin compliance override')
                return True
            elif not is_admin:
                self.log_activity(user.get_username(), 'Access denied - Non-compliant device')
                return False

        # Check ownership (admins can access any device)
        if self.owner != user.get_username() and not is_admin:
            self.log_activity(user.get_username(), 'Access denied - Not device owner')
            return False

        self.log_activity(user.get_username(), 'Access granted')
        return True

    def update_firmware(self, version, user):
        """Update device firmware - admin only."""
        if not user.check_privileges('admin'):
            self.log_activity(user.get_username(), 'Firmware update denied - insufficient privileges')
            return False
        
        old_version = self.firmware_version
        self.firmware_version = version
        self.log_activity(user.get_username(), f'Firmware updated from {old_version} to {version}')
        return True

    def run_security_scan(self, user=None):
        """Run security scan on device."""
        self.last_security_scan = datetime.now()
        self.compliance_status = 'compliant'
        username = user.get_username() if user else 'SYSTEM'
        self.log_activity(username, 'Security scan completed - Device now compliant')
        return True

    def check_compliance(self):
        """Check if device is compliant (scanned within 30 days)."""
        if self.last_security_scan is None:
            self.compliance_status = 'unknown'
            return False

        days_since_scan = (datetime.now() - self.last_security_scan).days
        if days_since_scan > 30:
            self.compliance_status = 'non-compliant'
            self.log_activity('SYSTEM', f'Device non-compliant - {days_since_scan} days since last scan')
            return False

        return self.compliance_status == 'compliant'

    def quarantine_device(self, user, reason: str):
        """Quarantine a compromised device - admin only."""
        if not user.check_privileges('admin'):
            self.log_activity(user.get_username(), 'Quarantine attempt denied - insufficient privileges')
            return False
        
        self.is_active = False
        self.compliance_status = 'quarantined'
        self.log_activity(user.get_username(), f'Device quarantined: {reason}')
        return True

    def reactivate_device(self, user):
        """Reactivate a quarantined device - admin only."""
        if not user.check_privileges('admin'):
            self.log_activity(user.get_username(), 'Reactivation denied - insufficient privileges')
            return False
        
        self.is_active = True
        self.log_activity(user.get_username(), 'Device reactivated')
        return True

    def get_device_info(self):
        """Get device information."""
        return {
            'device_id': self.device_id,
            'device_type': self.device_type,
            'firmware_version': self.firmware_version,
            'compliance_status': self.compliance_status,
            'owner': self.owner,
            'is_active': self.is_active,
            'last_scan': self.last_security_scan.strftime('%Y-%m-%d') if self.last_security_scan else 'Never'
        }

    def get_activity_log(self):
        """Get device activity log."""
        return self.activity_log.copy()


class DeviceManager:
    def __init__(self):
        self.devices = {}  # Changed from list to dictionary

    def add_device(self, device):
        """Add a device to the system."""
        if device.device_id in self.devices:
            return False  # Device already exists
        
        self.devices[device.device_id] = device
        return True

    def remove_device(self, device_id, user):
        """Remove a device from the system - admin only."""
        if not user.check_privileges('admin'):
            return False
        
        if device_id in self.devices:
            del self.devices[device_id]
            return True
        
        return False

    def get_device(self, device_id):
        """Retrieve a device by ID."""
        return self.devices.get(device_id)

    def get_devices_by_owner(self, owner):
        """Get all devices owned by a specific user."""
        return [d for d in self.devices.values() if d.owner == owner]

    def get_non_compliant_devices(self):
        """Get list of non-compliant devices."""
        non_compliant = []
        for device in self.devices.values():
            device.check_compliance()
            if device.compliance_status != 'compliant':
                non_compliant.append(device)
        return non_compliant

    def generate_security_report(self, user):
        """Generate comprehensive security report - admin only."""
        if not user.check_privileges('admin'):
            return None

        report = {
            'generated_by': user.get_username(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'total_devices': len(self.devices),
            'compliant_count': 0,
            'non_compliant_count': 0,
            'inactive_count': 0,
            'quarantined_count': 0,
            'devices': []
        }
        
        for device in self.devices.values():
            device.check_compliance()  # Update compliance status
            info = device.get_device_info()
            
            if device.compliance_status == 'compliant':
                report['compliant_count'] += 1
            elif device.compliance_status == 'quarantined':
                report['quarantined_count'] += 1
            else:
                report['non_compliant_count'] += 1
            
            if not device.is_active:
                report['inactive_count'] += 1
            
            report['devices'].append(info)
        
        return report

    def list_all_devices(self):
        """List all device IDs."""
        return list(self.devices.keys())


# Test implementation
if __name__ == "__main__":
    # Note: You'll need to import or define the User class from Exercise 1
    # For testing purposes, here's a simplified User class
    
    class User:
        def __init__(self, username, privilege_level):
            self.username = username
            self.privilege_level = privilege_level
        
        def get_username(self):
            return self.username
        
        def check_privileges(self, required_level):
            levels = {'guest': 1, 'standard': 2, 'admin': 3}
            return levels.get(self.privilege_level, 0) >= levels.get(required_level, 0)
    
    print("=== IoT Device Management System Test ===\n")
    
    # Create users
    admin = User('admin_user', 'admin')
    alice = User('alice', 'standard')
    bob = User('bob', 'standard')
    
    # Create device manager
    manager = DeviceManager()
    
    # Add devices
    print("=== Adding Devices ===")
    device1 = Device('CAM001', 'camera', 'alice', '2.1.0')
    device2 = Device('SENSOR042', 'sensor', 'bob', '1.5.3')
    device3 = Device('LOCK099', 'lock', 'alice', '3.0.1')
    
    manager.add_device(device1)
    manager.add_device(device2)
    manager.add_device(device3)
    
    print(f"Total devices: {len(manager.list_all_devices())}\n")
    
    # Test access control
    print("=== Testing Access Control ===")
    print(f"Alice accessing her camera: {device1.authorise_access(alice)}")
    print(f"Bob accessing Alice's camera: {device1.authorise_access(bob)}")
    print(f"Admin accessing Alice's camera: {device1.authorise_access(admin)}\n")
    
    # Run security scans
    print("=== Running Security Scans ===")
    device1.run_security_scan(admin)
    device2.run_security_scan(admin)
    print(f"Device1 compliant: {device1.check_compliance()}")
    print(f"Device3 compliant: {device3.check_compliance()}\n")
    
    # Test quarantine
    print("=== Testing Quarantine ===")
    device2.quarantine_device(admin, "Suspicious activity detected")
    print(f"Device2 can be accessed: {device2.authorise_access(bob)}\n")
    
    # Generate security report
    print("=== Security Report ===")
    report = manager.generate_security_report(admin)
    print(f"Report generated by: {report['generated_by']}")
    print(f"Total devices: {report['total_devices']}")
    print(f"Compliant: {report['compliant_count']}")
    print(f"Non-compliant: {report['non_compliant_count']}")
    print(f"Quarantined: {report['quarantined_count']}")