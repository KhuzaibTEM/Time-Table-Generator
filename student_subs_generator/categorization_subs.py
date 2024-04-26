from student_sub_prod import students_subs
from student_sub_prod import subjects_count
import csv
import os

class Categorize:
    def categorize_subs(self):
        for subject, count in subjects_count.copy().items():
            if count > 50:

                # Calculate the number of classes needed (max 50 students per class)
                num_classes = (count // 50) + (1 if count % 50 > 0 else 0)
                
                # Create classes with initial counts as zeros
                categorized_subjects = {f"{subject} {chr(65 + i)}": 0 for i in range(num_classes)}
                
                # Distribute students evenly across classes yes exactly
                students_per_class = count // num_classes
                remaining_students = count % num_classes
                assigned_students = 0

                # Assign students to each class
                for class_name in categorized_subjects:

                    # Determine the number of students for this class
                    class_students = students_per_class
                    if remaining_students > 0:
                        class_students += 1
                        remaining_students -= 1
                    
                    # Assign students to this class
                    for sub_list in students_subs.values():
                        if subject in sub_list and class_name not in sub_list:
                            sub_list.remove(subject)
                            sub_list.append(class_name)
                            categorized_subjects[class_name] += 1
                            assigned_students += 1
                            
                            if categorized_subjects[class_name] >= 50:
                                break

                        

                        if assigned_students == class_students * (list(categorized_subjects.keys()).index(class_name) + 1):
                            break

                
                with open("students (csv files)/students_sub_list.csv", "r") as f:
                    with open("students (csv files)/temp.csv", "w") as af:
                        checker = csv.DictReader(f)


                        af.write(f"name:,Subjects chosen:")
                        for line in checker:

                            if line["name"] in students_subs:
                                af.write("\n"  +line["name"]+ ",")
                                
                                
                                
                                if students_subs[line["name"]] != line[None]:
                                    for j in students_subs[line["name"]]:
                                        if j == students_subs[line["name"]][-1]:
                                            af.write(f"{j}")
                                        else:
                                            af.write(f"{j},")
                                else:
                                    for j in line[None]:
                                        if j == students_subs[line["name"]][-1]:
                                            af.write(f"{j}")
                                        else:
                                            af.write(f"{j},")
                                               
                    
                    
                # Update subjects_count with categorized subjects
                subjects_count.copy().update(categorized_subjects)

                

        os.rename("students (csv files)/students_sub_list.csv", "temp")
        os.rename("students (csv files)/temp.csv", "students (csv files)/students_sub_list.csv")
        os.rename("temp", "students (csv files)/temp.csv")


        return subjects_count.copy(), students_subs

sort = Categorize()    
    
print(sort.categorize_subs())
