
class Class:
    def __init__(self, name, instructor, section, day, period, duration=1, credits=3):
        self.name = name
        self.instructor = instructor
        self.section = section
        self.day = [int(d) for d in str(day)]
        self.period = period
        self.duration = duration
        self.credits = credits
    """Most parameters self explanatory, 
    day parameter will be a string including ints 0-4 representing Monday-Friday,
    periods will run from 0-7 inclusive,
    duration defaults to 1, denotes how many periods a class runs,
    Ex: Class1 = Class(name="MAD2502", instructor="Ross Ptacek", section="17336", day="024",period=5)
    """
    def __repr__(self):
        return f"{self.name} (Sec {self.section}) with {self.instructor}"

    def get_time_blocks(self):
        """
        Returns list of (day, period) tuples this class occupies.
        """
        blocks = []
        for d in self.day:
            for p in range(self.period, self.period + self.duration):
                blocks.append((d, p))
        return blocks

    def get_name(self):
        """
        A getter for the class name for the Class object
        """
        return self.name

    def get_instructor(self):
        """
        returns the name of the instructor for the Class object
        """
        return self.instructor

    def to_display_string(self):
        """
        Display string for the schedule grid.
        """
        return f"{self.name}\n{self.instructor}\nSec {self.section}\nPeriod {self.period}"
