import numpy as np
from tabulate import tabulate # got the documentation from https://medium.com/@qemhal.h/different-ways-to-display-a-table-in-python-d867aefb624a

def add_class_to_schedule(schedule, course):
    """
    Attempts to add a course to the schedule.
    If a time conflict is found, it will print a warning and skip that block.

    param schedule: 8x5 numpy array representing the weekly schedule
    param course: Class object to be added
    """
    success = True  # Track if the course fits fully
    for day, period in course.get_time_blocks():
        if schedule[period][day] == "":
            # No conflict, safe to place
            schedule[period][day] = course.to_display_string()
        else:
            # Conflict detected
            print(f"⚠️ Conflict detected: {course.name} conflicts with another class on day {day}, period {period}.")
            success = False
    return success

def passes_preferences(course, preferences, schedule=None):
    """
    Checks if a course passes all the student's preferences.

    param course: Class object
    param preferences: Dictionary of preferences
    param schedule: (Optional) Current schedule, to check for max_classes rule
    return True if course is acceptable, False otherwise
    """

    if preferences is None:
        #All checks are automatically passed because there are no restrictions.
        return True

    # 1. Check no_early_periods
    if 'no_early_periods' in preferences:
        earliest = preferences['no_early_periods']
        for _, period in course.get_time_blocks():
            if period < earliest:
                return False

    # 2. Check no_late_periods
    if 'no_late_periods' in preferences:
        latest = preferences['no_late_periods']
        for _, period in course.get_time_blocks():
            if period > latest:
                return False

    # 3. Check avoid_days
    if 'avoid_days' in preferences:
        avoid_days = preferences['avoid_days']
        for day, _ in course.get_time_blocks():
            if day in avoid_days:
                return False

    # 4. Check preferred_instructors
    if 'preferred_instructors' in preferences:
        preferred = preferences['preferred_instructors']
        if course.instructor not in preferred:
            return False

    # 5. Check max_classes per day (ONLY if a schedule is provided)
    if schedule is not None and 'max_classes' in preferences:
        max_per_day = preferences['max_classes']
        # Count how many classes are already on each day
        for day, _ in course.get_time_blocks():
            classes_on_day = sum(1 for cell in schedule[day] if cell != "")
            if classes_on_day >= max_per_day:
                return False

    return True
def build_schedule(class_list, preferences, schedule=None):
    """
    Builds an optimized schedule based on classes and student preferences,
    and prints the final schedule.

    param class_list: List of Class objects
    param preferences: Dictionary of preferences
    param schedule: Optional existing schedule array (5x8), if None, creates new
    return Final numpy array representing the schedule
    """
    if schedule is None:
        schedule = np.full((8,5), "", dtype=object)

    for course in class_list:
        if not passes_preferences(course, preferences, schedule):
            print(f"⏩ Skipping {course.name} due to preferences.")
            continue

        added = add_class_to_schedule(schedule, course)
        if added:
            print(f"✅ {course.name} added successfully.")
        else:
            print(f"🚫 {course.name} could not be fully added due to conflicts.")

    # Now, print the final schedule
    print("\n📅 Final Weekly Schedule:")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print(tabulate(schedule, headers=days, tablefmt="fancy_grid")) # prints schedule out in a nice grid

    return schedule