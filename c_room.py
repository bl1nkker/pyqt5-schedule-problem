class Room:
    # Class Room
    def __init__(self, number, seating_capacity):
        self.number = number
        self.seating_capacity = seating_capacity

    def get_number(self): return self.number

    def get_seating_capacity(self): return self.seating_capacity