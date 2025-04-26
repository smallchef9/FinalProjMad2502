import numpy as np
from classClass import Class
import scheduler

sample_preferences = {
    "no_early_periods": 1,          # No classes before 3rd period
    "no_late_periods": 6,            # No classes after 7th period
    "avoid_days": [4],               # Avoid Friday classes
    "preferred_instructors": ["Ross Ptacek", "Dr. Newton"],  # Only allow these instructors
    "max_classes": 3                 # No more than 3 classes per day
}


sample_class_list = [
    Class(name="MAD2502", instructor="Ross Ptacek", section="17336", day="0123", period=5),
    Class(name="PHY2053", instructor="Dr. Newton", section="29110", day="13", period=2),
    Class(name="ENC1102", instructor="Ms. Austen", section="31145", day="4", period=1)
]

scheduler.build_schedule(sample_class_list, sample_preferences)
