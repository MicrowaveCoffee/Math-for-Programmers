from math import pi,sqrt

# CHALLENGE: Museum Security System
# 
# You're building a security system for a museum with multiple rooms and security zones.
# Each room has security cameras with different detection areas, and some areas overlap.

class SecurityCamera:
    def __init__(self, name, center_x, center_y, detection_range):
        """
        A security camera with circular detection area.
        
        Args:
            name: Camera identifier
            center_x, center_y: Camera position
            detection_range: Radius of circular detection area
        """
        self.name = name
        self.center_x = center_x
        self.center_y = center_y
        self.detection_range = detection_range
    
    def can_detect(self, person):
        """
        TODO: Implement this method!
        
        Check if a person is within this camera's circular detection area.
        Use the distance formula: sqrt((x2-x1)² + (y2-y1)²)
        
        Returns True if person is within detection_range, False otherwise.
        
            Hint: You can avoid using sqrt by comparing squared distances:
            If distance² ≤ range², then distance ≤ range
        """
        # YOUR CODE HERE
        distance = sqrt((person.x - self.center_x)**2 + (person.y - self.center_y)**2)
        return distance <= self.detection_range


class LaserGrid:
    def __init__(self, name, x1, y1, x2, y2):
        """
        A rectangular laser grid security system.
        
        Args:
            name: Grid identifier  
            x1, y1: Bottom-left corner
            x2, y2: Top-right corner
        """
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def is_breached(self, person):
        """
        TODO: Implement this method!
        
        Check if a person has breached the laser grid.
        This is similar to the in_area method you just completed.
        
        Returns True if person is inside the grid area, False otherwise.
        """
        # YOUR CODE HERE
        return (self.x1 <= person.x <= self.x2) and (self.y1 <= person.y <= self.y2)

class Person:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def move_to(self, new_x, new_y):
        """Move person to new coordinates."""
        self.x = new_x
        self.y = new_y
        print(f"{self.name} moved to ({self.x}, {self.y})")

class SecuritySystem:
    def __init__(self):
        self.cameras = []
        self.laser_grids = []
        self.people = []
        self.alerts = []
    
    def add_camera(self, camera):
        self.cameras.append(camera)
    
    def add_laser_grid(self, grid):
        self.laser_grids.append(grid)
    
    def add_person(self, person):
        self.people.append(person)
    
    def check_all_security(self):
        """
        TODO: Implement this method!
        
        Check all people against all security systems.
        
        For each person:
        1. Check if they're detected by any camera
        2. Check if they've breached any laser grid
        3. Add appropriate alert messages to self.alerts list
        
        Clear self.alerts at the start of each check.
        
        Alert message format:
        - Camera detection: "CAMERA ALERT: {person.name} detected by {camera.name}"
        - Laser breach: "LASER ALERT: {person.name} breached {grid.name}"
        """
        # YOUR CODE HERE
        self.alerts = []
        for person in self.people:
            for camera in self.cameras:
                if camera.can_detect(person):
                  self.alerts.append(f"CAMERA ALERT: {person.name} detected by {camera.name}")              
            for grid in self.laser_grids:
                if grid.is_breached(person):
                  self.alerts.append(f"LASER ALERT: {person.name} breached {grid.name}") 
                
            
                



    
    def get_people_in_zone(self, zone_x1, zone_y1, zone_x2, zone_y2):
        """
        TODO: Implement this method!
        
        Find all people within a specific rectangular zone.
        This could be used for evacuation procedures.
        
        Returns a list of people within the specified area.
        """
        # YOUR CODE HERE
        people_in_area = []
        for person in self.people:
            if (zone_x1 <= person.x <= zone_x2) and (zone_y1 <= person.y <= zone_y2):
                people_in_area.append(person)
        return people_in_area



# TEST YOUR IMPLEMENTATION
def test_security_system():
    # Create security system
    security = SecuritySystem()
    
    # Add cameras (circular detection)
    camera1 = SecurityCamera("Camera-A", 5, 5, 3)  # Center at (5,5), range 3
    camera2 = SecurityCamera("Camera-B", 15, 10, 4) # Center at (15,10), range 4
    security.add_camera(camera1)
    security.add_camera(camera2)
    
    # Add laser grids (rectangular areas)
    grid1 = LaserGrid("Grid-1", 0, 0, 10, 8)     # Bottom-left (0,0) to top-right (10,8)
    grid2 = LaserGrid("Grid-2", 12, 6, 20, 15)   # Bottom-left (12,6) to top-right (20,15)
    security.add_laser_grid(grid1)
    security.add_laser_grid(grid2)
    
    # Add people
    person1 = Person("Alice", 3, 4)    # Should be detected by Camera-A and in Grid-1
    person2 = Person("Bob", 16, 9)     # Should be detected by Camera-B and in Grid-2  
    person3 = Person("Charlie", 25, 25) # Should be safe from all detection
    
    security.add_person(person1)
    security.add_person(person2)
    security.add_person(person3)
    
    # Test security check
    print("=== Initial Security Check ===")
    security.check_all_security()
    for alert in security.alerts:
        print(alert)
    
    # Move people and check again
    print("\n=== After Alice moves to (8, 8) ===")
    person1.move_to(8, 8)
    security.check_all_security()
    for alert in security.alerts:
        print(alert)
    
    # Test zone evacuation
    print(f"\n=== People in evacuation zone (0,0) to (12,12) ===")
    people_in_zone = security.get_people_in_zone(0, 0, 12, 12)
    for person in people_in_zone:
        print(f"{person.name} at ({person.x}, {person.y})")

# Uncomment to test when you're ready:
test_security_system()

# BONUS CHALLENGES (try these after completing the main methods):
# 1. Add a method to find the "blind spots" - areas not covered by any camera
# 2. Add overlapping detection zones - areas covered by multiple cameras
# 3. Add triangular security zones (hint: you'll need point-in-triangle algorithms)
# 4. Add motion detection - track if someone moves between security checks