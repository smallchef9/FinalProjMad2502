from classClass import Class
def loadClasses(filename):
    """
    Reads class data from a plain text file and returns a list of Class objects.

    param filename: Path to the text file
    return List of Class objects
    """
    class_list = []

    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            # Clean and split the line
            parts = line.strip().split(',')

            if len(parts) >= 5:  # Minimum 5 parts: name, instructor, section, day, period
                name = parts[0]
                instructor = parts[1]
                section = parts[2]
                day = parts[3]
                period = int(parts[4])
                if len(parts) > 5:
                    duration = int(parts[5])
                else:
                    duration = 1
                new_class = Class(name, instructor, section, day, period, duration)
                class_list.append(new_class)
            else:
                print(f" This line sucks {line.strip()}")

    return class_list
