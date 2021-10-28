class Department:
    # Department - SEM, Tourism, Logistics etc.
    def __init__(self, name, courses):
        # Name of department
        self.name = name
        # Courses (by specialty)
        self.courses = courses

    def get_name(self): return self.name

    def get_courses(self): return self.courses