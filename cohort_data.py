def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """


    houses = set()

    # Code goes here
    with open(filename) as input_file:
        for line in input_file:
            line = line.rstrip()
            tokenized_line = line.split("|")
            house = tokenized_line[2]
            if len(house) >0:
                houses.add(house)


    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    # Code goes here
    with open(filename) as input_file:
        for line in input_file:
            line = line.rstrip()
            tokenized_line = line.split("|")
            first_name, last_name, house, advisor, cohort = tokenized_line
            full_name = first_name + " " + last_name
            if house != "":
                all_students.append(full_name)
            
            if cohort == "Winter 2015":
                winter_15.append(full_name)
            elif cohort == "Summer 2015":
                summer_15.append(full_name)
            elif cohort == "Spring 2015":
                spring_15.append(full_name)
            elif cohort == "TA":
                tas.append(full_name)

    # print all_students
    # print tas
    # print "WINTER"
    # print winter_15
    # print "SUMMER"
    # print summer_15
    # print "SPRING"
    # print spring_15
    
    all_students.sort()
    tas.sort()
    winter_15.sort()
    summer_15.sort()
    spring_15.sort()
    
    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    # Code goes here
    with open(filename) as input_file:
        for line in input_file:
            line = line.rstrip()
            tokenized_line = line.split("|")
            first_name, last_name, house, advisor, cohort = tokenized_line
            #full_name = first_name + " " + last_name

            if house == "Gryffindor":
                gryffindor.append(last_name)
            elif house == "Dumbledore's Army":
                dumbledores_army.append(last_name)
            elif house == "Ravenclaw":
                ravenclaw.append(last_name)
            elif house == "Order of the Phoenix":
                order_of_the_phoenix.append(last_name)
            elif house == "Slytherin":
                slytherin.append(last_name)
            elif house == "Hufflepuff":
                hufflepuff.append(last_name)
            elif cohort == "TA":
                tas.append(last_name)
            elif cohort == "I":
                instructors.append(last_name)

    hufflepuff.sort(),
    gryffindor.sort(),
    ravenclaw.sort(),
    slytherin.sort(),
    dumbledores_army.sort(),
    order_of_the_phoenix.sort(),
    tas.sort(),
    instructors.sort()
    
    all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
            
    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here
    with open(filename) as input_file:
        for line in input_file:
            line = line.rstrip()
            tokenized_line = line.split("|")
            first_name, last_name, house, advisor, cohort = tokenized_line
            full_name = first_name + " " + last_name

            if len(house) > 1:
                student_info = (full_name, house, advisor, cohort)
                student_list.append(student_info) 
    
    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here
    print "Who would you like to find?"
    search_student = raw_input("Please enter a first and last name: ")
    
    for student in student_list:
        if search_student == student[0]:
            return search_student +"'s" + " cohort is " + student[3]
    
    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()
    winter_15 = set()
    summer_15 = set()
    spring_15 = set()

    # Code goes here
    with open(filename) as input_file:
        for line in input_file:
            line = line.rstrip()
            tokenized_line = line.split("|")
            first_name, last_name, house, advisor, cohort = tokenized_line
        
            if cohort == "Winter 2015":
                winter_15.add(first_name)
            elif cohort == "Spring 2015":
                spring_15.add(first_name)
            elif cohort == "Summer 2015":
                summer_15.add(first_name)
        
        win_sp = winter_15 & spring_15
        win_sum = winter_15 & summer_15
        sum_sp = summer_15 & spring_15

        duplicate_names = win_sp | win_sum | sum_sp

        # duplicate_names.add(win_sp)
        # duplicate_names.add(win_sum)
        # duplicate_names.add(sum_sp)

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here
    search_student = "Liz Acosta" #raw_input("search for a student and I'll return their house members")
    cohort_set = set()
    house_set = set()

    for student in student_list:
        full_name, house, advisor, cohort = student
        if search_student == full_name:
            student_cohort = cohort 
            student_house = house
                    

    for student in student_list:
        full_name, house, advisor, cohort = student
        if student_cohort == cohort:
            cohort_set.add(full_name)
        if student_house == house:
            house_set.add(full_name)


    student_house_members = cohort_set & house_set       

    print student_house_members
    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
#print students_by_house("cohort_data.txt")
all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
#result = find_cohort_by_student_name(all_students_data)
#print result
#print find_name_duplicates("cohort_data.txt")
find_house_members_by_student_name(all_students_data)
