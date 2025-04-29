from classClass import Class
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

# def schedule_maker(classes: list):
#     """
#     Parameters:
#          classes: the list of classes the user wants to add to their schedule
#          # planning on adding more parameters later (time of day, preferred professor, etc.)
#
#     Returns:
#         schedule: a 8x5 list that represents the 5 days of the week and 8 class periods
#     """
#
#     schedule = [[None for col in range(5)] for row in range(8)] # making a list with 8 rows and 5 columns
#     total_credits = 0
#
#     for clss in classes:
#         if clss in classes_list:
#             ind = classes_list.index(clss)
#             time_blocks = classes_list[ind].get_time_blocks()
#
#             added_class = False
#             for day, period in time_blocks:
#                 if schedule[int(period)][int(day)] is None:
#                     schedule[int(period)][int(day)] = classes_list[ind].to_display_string()
#                     added_class = True
#                 else:
#                     print(f"{clss} conflicts with another class, could not add to schedule.")
#
#             if added_class:
#                 total_credits += classes_list[ind].credits
#         if total_credits > 18:
#             print("Maximum credit hours reached.")
#             break
#
#     return schedule, total_credits

tester = read.loadClasses("randomClasses.txt")
test_list = [comp_math, physics_1, english_1, calc_3, prog_1, prog_with_r] # the most desired class should be first, the least desired last
test_schedule = build_schedule(tester,sample_preferences ) # insert preferences dictionary here