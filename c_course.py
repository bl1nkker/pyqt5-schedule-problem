class Course:
    def __init__(self, number, name, instructor, max_num_of_student) -> None:
        self.number = number
        self.name = name
        self.instructors = instructor
        self.max_num_of_student = max_num_of_student

    def get_number(self): return self.number

    def get_name(self): return self.name

    def get_instructors(self): return self.instructors

    def get_max_num_of_students(self): return self.max_num_of_student

    def __str__(self) -> str: return self.name