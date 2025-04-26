from classClass import Class
Class1 = Class(name="MAD2502", instructor="Ross Ptacek", section="17336", day= "024", period=5)
print(Class1.to_display_string())
print(Class1.get_time_blocks())
print(str(Class1))