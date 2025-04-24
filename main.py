from classClass import Class
import numpy as np

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
comp_math = Class(name="MAD2502", instructor="Ross Ptacek", section="17336", day="024", period=5)
prog_1 = Class(name="COP3502C", instructor="Ashish Aggarwal", section="10565", day="123", period=7, duration=2)
prog_2 = Class(name="COP3503C", instructor="Fatemah Tavassoli", section="11444", day="024", period=2)
prog_with_r = Class(name="STA3100", instructor="Thomas Ippolito", section="20154", day="024", period=7)

# math classes
calc_1 = Class(name="MAC2311", instructor="STAFF", section="13464", day="024", period=4)
calc_2 = Class(name="MAC2312", instructor="STAFF", section="13532", day="024", period=7)
calc_3 = Class(name="MAC2313", instructor="STAFF", section="13613", day="024", period=8)
lin_alg_1 = Class(name="MAS4105", instructor="STAFF", section="13330", day="0124", period=5)

# science classes
physics_1 = Class(name="PHY2053", instructor="STAFF", section="14666", day="13", period=5)
physics_2 = Class(name="PHY2054", instructor="STAFF", section="14616", day="13", period=2)
gen_chem_1 = Class(name="CHM2045", instructor="STAFF", section="10561", day="024", period=1)
bio_1 = Class(name="BSC2010", instructor="David Oppenheimer", section="11154", day="024", period=2)

# english classes
english_1 = Class(name = "ENC1101", instructor = "Angela Brown", section = "27585", day = "13", period = 3)
english_2 = Class(name = "ENC1102", instructor = "STAFF", section = "11916", day = "24",period = 4)
english_3 = Class(name = "ENC1136", instructor = "STAFF", section = "16175", day = "024", period = 4)

schedule = np.empty((8, 5)) # making an empty numpy array with 8 rows (for the 8 periods) and 5 columns (for the days of the week)
