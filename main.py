import random
import prettytable

POPULATION_SIZE = 9


class Course:
    def __init__(self, number, name, instructor, max_num_of_student) -> None:
        self.number = number
        self.name = name
        self.instructor = instructor
        self.max_num_of_student = max_num_of_student

    def get_number(self): return self.number

    def get_name(self): return self.name

    def get_instructor(self): return self.instructor

    def get_max_num_of_students(self): return self.max_num_of_student

    def __str__(self) -> str: return self.name


class Instructor:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self): return self.id

    def get_name(self): return self.name

    def __str__(self): return self.name


class Room:
    # Class Room
    def __init__(self, number, seating_capacity):
        self.number = number
        self.seating_capacity = seating_capacity

    def get_number(self): return self.number

    def get_seating_capacity(self): return self.seating_capacity


class MeetingTime:
    # Meeting Time
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def get_id(self): return self.id

    def get_time(self): return self.time


class Class:
    # Row in the Schedule (Ex: Math, 10.00 - 11.00, Some Instructor, Cabinet)
    def __init__(self, id, dept, course):
        self.id = id
        self.dept: Department = dept
        self.course: Course = course
        self.instructor: Instructor or None = None
        self.meeting_time: MeetingTime or None = None
        self.room: Room or None = None

    def get_id(self): return self.id

    def get_dept(self): return self.dept

    def get_course(self): return self.course

    def get_instructor(self): return self.instructor

    def get_meeting_time(self): return self.meeting_time

    def get_room(self) -> Room: return self.room

    def set_instructor(self, instructor): self.instructor = instructor

    def set_meeting_time(self, meeting_time): self.meeting_time = meeting_time

    def set_room(self, room): self.room = room

    def __str__(self): return f'{self.dept.get_name()},{self.course.get_name()},' \
                              f'{self.room.get_number()},{self.instructor.get_id()}, ' \
                              f'{self.meeting_time.get_id()}'


class Data:
    # This needs to retrieve from form (PyQT5)
    ROOMS = [['R1', 25], ['R2', 45], ['R3', 35]]
    MEETING_TIMES = [['MT1', 'MWF 09:00 - 10:00'],
                     ['MT2', 'MWF 10:00 - 11:00'],
                     ['MT3', 'TTH 09:00 - 10:30'],
                     ['MT4', 'TTH 10:30 - 12:00']]
    INSTRUCTORS = [['I1', 'Dr James Web'],
                   ['I2', 'Mr Mike Brown'],
                   ['I3', 'Dr Steve Day'],
                   ['I4', 'Mrs Jane Doe']]

    def __init__(self):
        self.rooms = []
        self.meeting_times = []
        self.instructors = []
        for i in range(len(self.ROOMS)):
            # Create new room (id, number)
            new_room = Room(self.ROOMS[i][0], self.ROOMS[i][1])
            self.rooms.append(new_room)
        for i in range(len(self.INSTRUCTORS)):
            # Create new instructor (id, name)
            new_instructor = Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1])
            self.instructors.append(new_instructor)
        for i in range(len(self.MEETING_TIMES)):
            # Create new room (id, time)
            new_meeting_times = MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1])
            self.meeting_times.append(new_meeting_times)

        # Create courses (number, name, instructors, max_num_of_student)
        course1 = Course('C1', '325K', [self.instructors[0], self.instructors[1]], 25)
        course2 = Course('C2', '319K', [self.instructors[0], self.instructors[1], self.instructors[2]], 35)
        course3 = Course('C3', '462k', [self.instructors[0], self.instructors[1]], 25)
        course4 = Course('C4', '464K', [self.instructors[2], self.instructors[3]], 35)
        course5 = Course('C5', '360C', [self.instructors[3]], 35)
        course6 = Course('C6', '303K', [self.instructors[0], self.instructors[2]], 45)
        course7 = Course('C7', '303L', [self.instructors[1], self.instructors[3]], 45)

        self.courses = [course1, course2, course3, course4, course5, course6, course7]

        # Create Departments (name, courses)
        dept1 = Department('MATH', [course1, course3])
        dept2 = Department('MATH', [course2, course4, course5])
        dept3 = Department('MATH', [course6, course7])

        self.depts = [dept1, dept2, dept3]
        # Sum of courses, ex: [2,3,2] = 7
        self.number_of_classes = sum([len(self.depts[i].get_courses()) for i in range(len(self.depts))])

    def get_rooms(self):
        return self.rooms

    def get_instructors(self) -> list[Instructor]:
        return self.instructors

    def get_courses(self) -> list[Course]:
        return self.courses

    def get_depts(self):
        return self.depts

    def get_meeting_times(self):
        return self.meeting_times

    def get_number_of_classes(self):
        return self.number_of_classes


class Schedule:
    def __init__(self):
        self.data = data
        # List of classes
        self.classes = []
        self.number_of_conflicts = 0
        self.fitness = -1
        # Total number of classes
        self.class_numb = 0
        self.is_fitness_changed = True

    def get_classes(self) -> list[Class]:
        self.is_fitness_changed = True
        return self.classes

    def get_number_of_conflicts(self):
        return self.number_of_conflicts

    def get_fitness(self):
        if self.is_fitness_changed:
            self.fitness = self.calculate_fitness()
            self.is_fitness_changed = False
        return self.fitness

    def calculate_fitness(self):
        self.number_of_conflicts = 0
        # Retrieve current classes in the schedule
        classes: [Class] = self.get_classes()
        # For each class:
        for class_index_1 in range(len(classes)):
            current_class_1: Class = classes[class_index_1]
            # Check, if max_num_of_students in the course, fits the room
            if current_class_1.get_room().get_seating_capacity() < current_class_1.get_course().get_max_num_of_students():
                # if not, conflicts +1
                self.number_of_conflicts += 1
            for class_index_2 in range(len(classes)):
                current_class_2: Class = classes[class_index_2]
                # Non-repeatable classes
                if class_index_2 >= class_index_1:
                    # Check, if meeting time of different(by id) classes is match (it's still non-conflictable)
                    if (current_class_1.get_meeting_time() == current_class_2.get_meeting_time() and
                            current_class_1.get_id() != current_class_2.get_id()):
                        # Check if two classes with the same meeting time are processed in the same room
                        if current_class_1.get_room() == current_class_2.get_room():
                            # if so, conflict + 1
                            self.number_of_conflicts += 1
                        # Check if two classes with the same meeting time are processed with the same instructor
                        if current_class_1.get_instructor() == current_class_2.get_instructor():
                            # if so, conflict + 1
                            self.number_of_conflicts += 1
        return 1 / (1 * self.number_of_conflicts + 1)

    def __str__(self):
        result = ''
        for i in range(len(self.classes) - 1):
            result += str(self.classes[i]) + ', '
        result += str(self.classes[len(self.classes) - 1])
        return result

    # This method is for dummy, random data. Just to set all up for algorithm
    def initialize(self):
        depts = self.data.get_depts()
        for i in range(len(depts)):
            # Courses of current department
            courses = depts[i].get_courses()
            for j in range(len(courses)):
                # Create new Class (id, department, course)
                new_class = Class(self.class_numb, depts[i], courses[j])
                self.class_numb += 1
                # Set initialize data, Random of the list
                new_class.set_meeting_time(data.get_meeting_times()[random.randrange(0, len(data.get_meeting_times()))])
                new_class.set_room(data.get_rooms()[random.randrange(0, len(data.get_rooms()))])
                new_class.set_instructor(data.get_instructors()[random.randrange(0, len(data.get_instructors()))])
                self.classes.append(new_class)
        return self


class Population:
    # Here we define how many schedules will be in our population
    def __init__(self, size):
        self.size = size
        self.data = data
        self.schedules = []
        for i in range(0, size):
            self.schedules.append(Schedule().initialize())

    def get_schedules(self) -> list[Schedule]: return self.schedules


class Algorithm:
    pass


class Department:
    # Department - SEM, Tourism, Logistics etc.
    def __init__(self, name, courses):
        # Name of department
        self.name = name
        # Courses (by specialty)
        self.courses = courses

    def get_name(self): return self.name

    def get_courses(self): return self.courses


# Result


class DisplayManager(object):
    def print_available_data(self):
        print('> All Available Data')
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructors()
        self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        available_depts_table = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(len(depts)):
            courses = depts.__getitem__(i).get_courses()
            temp_str = '['
            for j in range(len(courses) - 1):
                temp_str += courses[j].__str__() + ','
            temp_str += courses[len(courses) - 1].__str__() + ']'
            available_depts_table.add_row([depts.__getitem__(i).get_name(), temp_str])
        print(available_depts_table)

    def print_course(self):
        available_courses_table = prettytable.PrettyTable(
            ['id', 'course #', 'max # of students', 'instructors'])
        courses = data.get_courses()
        for i in range(len(courses)):
            instructors: list[Instructor] = courses[i].get_instructor()
            temp_str = ''
            for j in range(len(instructors) - 1):
                temp_str += instructors[j].__str__() + ', '
            temp_str += instructors[len(instructors) - 1].__str__()
            available_courses_table.add_row(
                [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_max_num_of_students()), temp_str])
        print(available_courses_table)

    def print_instructors(self):
        available_instructors_table = prettytable.PrettyTable(['id', 'instructors'])
        instructors = data.get_instructors()
        for i in range(len(instructors)):
            available_instructors_table.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(available_instructors_table)

    def print_room(self):
        available_rooms_table = prettytable.PrettyTable(['room #', 'max seating capacity'])
        rooms = data.get_rooms()
        for i in range(len(rooms)):
            available_rooms_table.add_row([rooms[i].get_number(), rooms[i].get_seating_capacity()])
        print(available_rooms_table)

    def print_meeting_times(self):
        available_meeting_time_table = prettytable.PrettyTable(['id', 'Meeting Time'])
        meeting_times = data.get_meeting_times()
        for i in range(len(meeting_times)):
            available_meeting_time_table.add_row([meeting_times[i].get_id(), meeting_times[i].get_time()])
        print(available_meeting_time_table)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(['schedule #', 'fitness', '# of conflicts', 'classes'])
        schedules = population.get_schedules()
        for i in range(len(schedules)):
            current_schedule: Schedule = schedules[i]
            table1.add_row([str(i),
                            round(current_schedule.get_fitness(), 3),
                            current_schedule.get_number_of_conflicts(),
                            str(list(map(lambda x: x.__str__(), current_schedule.get_classes())))
                            ])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(['Class #', 'Dept', 'Course', 'Room', 'Instructor', 'Meeting Time'])
        for i in range(len(classes)):
            current_class: Class = classes[i]
            table.add_row([str(i),
                           current_class.get_dept().get_name(),
                           f'{current_class.get_course().get_name()} ({current_class.get_course().get_number()}, {str(current_class.get_course().get_max_num_of_students())})',
                           f'{current_class.get_room().get_number()}, ({str(current_class.get_room().get_seating_capacity())})',
                           f'{current_class.get_instructor().get_name()} ({str(current_class.get_instructor().get_id())})',
                           f'{current_class.get_meeting_time().get_time()} ({str(current_class.get_meeting_time().get_id())})'
                           ])
        print(table)


data = Data()
display_manager = DisplayManager()
display_manager.print_available_data()
generation_number = 0
print(f'\n> Generation # {generation_number}')
pp = Population(POPULATION_SIZE)
pp.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
display_manager.print_generation(pp)
display_manager.print_schedule_as_table(pp.get_schedules()[0])
