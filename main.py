from classClass import Class
import sys
import numpy as np
from tabulate import tabulate # got the documentation from https://medium.com/@qemhal.h/different-ways-to-display-a-table-in-python-d867aefb624a
from scheduler import *
import readerr as read

sample_preferences = {
    "no_early_periods": 1,          # Do not allow classes before 3rd period (periods 0 or 1 are not allowed)
    "no_late_periods": 6,            # Do not allow classes after 7th period (periods 7 or higher are not allowed)
    "avoid_days": [4],               # Avoid classes on Friday (day 4)
    "max_classes": 3                 # No more than 3 classes scheduled on any single day
}
def find_classname(name_wanted,all_classes: list):
  """
  Returns a list of class objects filtered by the desired class (only 1 at this time)
  """
  return [each_class for each_class in all_classes if each_class.get_name() == name_wanted.upper()]

def find_instructor(ins_wanted, all_ins: list):
  """
  Returns a list of class objects filtered by the desired instructor (only 1 at this time)
  """
  return [each_ins for each_ins in all_ins if each_ins.get_instructor().upper() == ins_wanted.upper()]

# programming classes
comp_math = Class(name="MAD2502", instructor="Ross Ptacek", section="17336", day="024", period=5, credits = 3)
prog_1 = Class(name="COP3502C", instructor="Ashish Aggarwal", section="10565", day="123", period=6, duration=2, credits = 4)
prog_2 = Class(name="COP3503C", instructor="Fatemah Tavassoli", section="11444", day="024", period=2, credits = 4)
prog_with_r = Class(name="STA3100", instructor="Thomas Ippolito", section="20154", day="024", period=7, credits = 3)

# math classes
calc_1 = Class(name="MAC2311", instructor="STAFF", section="13464", day="024", period=4, credits = 4)
calc_2 = Class(name="MAC2312", instructor="STAFF", section="13532", day="024", period=6, credits = 4)
calc_3 = Class(name="MAC2313", instructor="STAFF", section="13613", day="024", period=7, credits = 4)
lin_alg_1 = Class(name="MAS4105", instructor="STAFF", section="13330", day="0124", period=5, credits = 3)

# science classes
physics_1 = Class(name="PHY2053", instructor="STAFF", section="14666", day="13", period=5, credits = 3)
physics_2 = Class(name="PHY2054", instructor="STAFF", section="14616", day="13", period=2, credits = 3)
gen_chem_1 = Class(name="CHM2045", instructor="STAFF", section="10561", day="024", period=1, credits = 3)
bio_1 = Class(name="BSC2010", instructor="David Oppenheimer", section="11154", day="024", period=2, credits = 3)

# english classes
english_1 = Class(name = "ENC1101", instructor = "Angela Brown", section = "27585", day = "13", period = 3, credits = 3)
english_2 = Class(name = "ENC1102", instructor = "STAFF", section = "11916", day = "24",period = 4, credits = 3)
english_3 = Class(name = "ENC1136", instructor = "STAFF", section = "16175", day = "024", period = 4, credits = 3)


classes_list = [comp_math, prog_1, prog_2, prog_with_r, calc_1, calc_2, calc_3, lin_alg_1, physics_1, physics_2, gen_chem_1, bio_1, english_1, english_2, english_3]



tester = read.loadClasses("randomClasses.txt")
test_list = [comp_math, physics_1, english_1, calc_3, prog_1, prog_with_r] # the most desired class should be first, the least desired last
test_preferences = {'no_early_periods': 3, 'avoid_days': [4],'preferred_instructors': ['Ross Ptacek', 'Ashish Aggarwal'],
                    'max_classes':2}


def main():
  global classes_list
  my_courses = []
  my_preferences = {}
  menu = """
1. Add courses to cart
2. View your courses
3. Add preferences
4. Build schedule
5. Read classes from file
6. Exit
  """
  print("Welcome to the schedule builder :)")


  running = True
  while running:
    print(menu)
    menu_select = input("What would you like to do?: ")

    if menu_select.isdigit():
      if menu_select == "1":
        print("All available courses: ")
        for ind,course in enumerate(classes_list):
          print(f"{ind+1}. {course.name}")
        print()

        selecting = True
        while selecting:
          course_to_add = input("Enter a course code (to stop, enter 'done'): ")

          course_found = None
          for course in classes_list:
            if course_to_add.upper() == course.get_name().upper():  # Ignore case sensitivity
              course_found = course
              break

          if course_found:
            # Add the class object to my_courses
            my_courses.append(course_found)
            print(f"✅ Course {course_found.name} has been added to your cart!\n")
          elif course_to_add.lower() == "done":
            selecting = False
          else:
            print(f"❌ We do not offer this course: '{course_to_add}'.\n")


      elif menu_select == "2":
          if my_courses:
            print("Your selected courses: ")
            for ind,course in enumerate(my_courses):
              print(f"{ind+1}. {course.name}")
          else:
            print("You haven't selected any courses!")


      elif menu_select == "3":

        pref_menu = """

Choose a preference to add:

1. No early periods

2. No late periods

3. Avoid specific days

4. Preferred instructors

5. Max classes per day

6. Go back to main menu

"""

        adding_prefs = True

        while adding_prefs:

          print(pref_menu)

          pref_select = input("Select an option: ")

          if pref_select == "1":

            earliest = int(input("Enter the earliest allowed period (0-7): "))

            my_preferences["no_early_periods"] = earliest

            print(f"✅ Set no classes before period {earliest}.\n")


          elif pref_select == "2":

            latest = int(input("Enter the latest allowed period (0-7): "))

            my_preferences["no_late_periods"] = latest

            print(f"✅ Set no classes after period {latest}.\n")


          elif pref_select == "3":

            days = input(
              "Enter the days to avoid (example: 4 for Friday, multiple days separated by commas like 2,4): ")

            days_list = [int(day.strip()) for day in days.split(",")]

            my_preferences["avoid_days"] = days_list

            print(f"✅ Will avoid days: {days_list}.\n")


          elif pref_select == "4":
            instructors = input("Enter preferred instructors (separate names by commas): ")
            instructor_list = [inst.strip() for inst in instructors.split(",")]
            my_preferences["preferred_instructors"] = instructor_list
            print(f"✅ Set preferred instructors: {instructor_list}.\n")


          elif pref_select == "5":
            max_classes = int(input("Enter the maximum number of classes per day: "))
            my_preferences["max_classes"] = max_classes
            print(f"✅ Set max {max_classes} classes per day.\n")

          elif pref_select == "6":
            adding_prefs = False

          else:
            print("❌ Invalid selection. Please try again.")

      elif menu_select == "4":
        build_schedule(my_courses, my_preferences)

      elif menu_select == "5":
        filename = input("Enter the filename to load classes from: ")
        try:
          new_classes = read.loadClasses(filename)
          classes_list.extend(new_classes)
          print(f"✅ {len(new_classes)} classes successfully loaded and added to available courses!\n")
        except FileNotFoundError:
          print(f"❌ Could not find file '{filename}'. Please make sure it exists.")

      elif menu_select == "6":
        running = False
        print("\nThank you for using the schedule builder :) Goodbye!")
        sys.exit()
      elif int(menu_select) > 5:
        print("Invalid selection, please try again.")
    else:
      print("Invalid selection, please try again.")



while __name__ == "__main__":
  main()
test_schedule = build_schedule(tester,sample_preferences ) # insert preferences dictionary here