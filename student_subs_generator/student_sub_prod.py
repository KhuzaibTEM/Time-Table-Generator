import random
from collections import defaultdict
import os
import csv

subjects = {
    1:"Accounting",
    2:"Art and Design",
    3:"Biology",
    4:"Business",
    5:"Chemistry",
    6:"Computer Science",
    7:"Environmental Management",
    8:"Economics",
    9:"English General Paper",
    10:"Literature in English",
    11:"Further Mathematics",
    12:"Global Perspective",
    13:"History",
    14:"Information Technology",
    15:"Law",
    16:"Math",
    17:"Media Studies",
    18:"Physics",
    19:"Psychology",
    20:"Politics",
    21:"Sociology",
    22:"Thinking Skills",
    23:"Urdu"
}

with open("students (csv files)/student_names.csv", "r") as f:
    with open("students (csv files)/students_sub_list.csv", "w") as af:

        # {student_name : subjects_chosen}
        students_subs = {}
        
        af.write("name")

        for line in f:
            student_name = line.strip()
            amount_sub = random.randint(4, 7)

            if student_name not in students_subs:
                students_subs[student_name] = []

            af.write(f"\n{student_name},")

            for i in range(amount_sub):
                random_sub = random.randint(1, 23)

                while subjects[random_sub] in students_subs[student_name]:
                    random_sub = random.randint(1, 23)

                students_subs[student_name].append(subjects[random_sub])
                
            for o in students_subs[student_name]:
                if o == students_subs[student_name][-1]:
                    af.write(f"{o}") 
                else:
                    af.write(f"{o},")   

class student_subs_class:
    def remove_low_count_subs(self):

        # Common subs to replace the low count subs
        subs = [subjects[19], subjects[5], subjects[17], subjects[6]]

        # {subject: no_of_students}
        subjects_count = defaultdict()

        # list of subjects with low student count
        remove_subs = []

        for i in students_subs.values():
            for j in i:
                if j in subjects_count:
                    subjects_count[j] += 1
                else:
                    subjects_count[j] = 1

        for k in subjects.values():

            # remove subject below 40 students count
            if subjects_count[k] <= 40:

                # Further Math exception which requires at least 15 students
                if k == "Further Mathematics" and subjects_count[k] >= 15:
                    pass
                else:
                    remove_subs.append(k)
                    sub_select = random.choice(subs)
                    subjects_count[sub_select] += subjects_count[k]

                    for i in students_subs.values():
                            if k in i:
                                i.remove(k)
                                if sub_select not in i:
                                    i.append(sub_select)

                                with open("students (csv files)/students_sub_list.csv", "r") as f:
                                    with open("students (csv files)/temp.csv", "w") as af:
                                        checker = csv.DictReader(f)

                                        
                                        af.write("name")
                                        for line in checker:

                                            if line["name"] in students_subs:
                                                af.write("\n"  +line["name"]+ ",")
                                                
                                                for i in line[None]:
                                                    if k == i:
                                                        if sub_select not in students_subs[line["name"]]:
                                                            af.write(f"{sub_select},")
                                                            
                                                        else:
                                                            if len(students_subs[line["name"]]) <= 4:
                                                                subjects_count[sub_select] -= 1

                                                                while sub_select in students_subs[line["name"]]:
                                                                    sub_select = random.choice(subs)

                                                                af.write(f"{sub_select},")
                                                                subjects_count[sub_select] += 1

                                                            else:
                                                                pass

                                                    else:
                                                        af.write(f"{i},")
                                    
                    del subjects_count[k]
        
        os.rename("students (csv files)/students_sub_list.csv", "temp")
        os.rename("students (csv files)/temp.csv", "students (csv files)/students_sub_list.csv")
        os.rename("temp", "students (csv files)/temp.csv")

        return subjects_count



subjects_count = student_subs_class().remove_low_count_subs()
