#Making a list (dictionary ) of all the info needed for the cvlass squedule : lvl , subject , charges
#added classroom and date for the class squaedule to make it better
class_squedule = [
    {'level': 'B', 'subject': 'Python', 'schedule': 'Monday 1pm 2pm', 'charges': '350 RM', 'Classroom': 'B1-07', 'Date': '22/2'},
    {'level': 'I', 'subject': 'JavaScript', 'schedule': 'Wednesday 1pm 2pm', 'charges': '600 RM', 'Classroom': 'A1-15', 'Date': '22/2'},
    {'level': 'A', 'subject': 'JavaScript', 'schedule': 'Monday 1pm 2pm', 'charges': '1000 RM', 'Classroom': 'S8-02', 'Date': '13/3'},
    {'level': 'I', 'subject': 'Web Dev', 'schedule': 'Friday 9am-10am', 'charges': '600 RM', 'Classroom': 'H5-03', 'Date': '24/3'},
    {'level': 'I', 'subject': 'Python', 'schedule': 'Monday 1pm-3pm', 'charges': '600 RM', 'Classroom': 'A2-22', 'Date': '25/3'},
    {'level': 'A', 'subject': 'Python', 'schedule': 'Tuesday 1pm-4pm', 'charges': '1000 RM', 'Classroom': 'S8-68', 'Date': '02/4'},
    {'level': 'B', 'subject': 'Web Dev', 'schedule': 'Thursday 4pm-5pm', 'charges': '350 RM', 'Classroom': 'P88-01', 'Date': '11/4'},
    {'level': 'B', 'subject': 'C++', 'schedule': 'Friday 1pm-3pm', 'charges': '350 RM', 'Classroom': 'A1-03', 'Date': '26/4'},
    {'level': 'A', 'subject': 'C++', 'schedule': 'Monday 8am-10am', 'charges': '1000 RM', 'Classroom': 'D5-07', 'Date': '01/5'}
]
#def fucntiosn to read from text files
def reading_file_for_trainer(my_file12):
    trainers = []
    with open(my_file12, 'r') as file:
        header = [colonne.strip().lower() for colonne in file.readline().split('|')]

        for line in file:
            data = [colonne.strip() for colonne in line.split('|')]
            trainer = dict(zip(header, data))
            trainers.append(trainer)

    return trainers

def paid_stdudents(trainers, students, email):
    trainer_level = next(
        (trainer.get('level') for trainer in trainers if trainer.get('email', '').lower() == email.lower()), None)

    if trainer_level:

        enrolled_students = [student for student in students if
                             student.get('level') == trainer_level and student.get('paid?') == 'yes']

        print(f"Your lvl : {trainer_level}")



        if enrolled_students:

            print(f"\nEnrolled Students in level :  {trainer_level} --- who have paid thier fees : \n")

            for student in enrolled_students:
                print(f"Name: {student.get('name')}")

                print(f"TP Number: {student.get('tpnumber')}\n")

        else:

            print(f"students in this lvl : {trainer_level} unfortuantely have not paid their fees.")

    else:

        print("Invalid. It seems thst we are unable to find your level. \n Try again later...")


#def funcitio to change password/email of user
def trainer_profile_update(trainers, email):
    for trainer in trainers:
        if trainer.get('email', '').lower() == email.lower():
            print("What do you want to update?")
            print("1. Password")
            print("2. Email")
            choice = input("Enter your choice: ")

            if choice == '1':
                new_password = input("Enter your new password: ")
                trainer['password'] = new_password
                print("Password updated successfully.")
            elif choice == '2':
                new_email = input("Enter your new email: ")
                trainer['email'] = new_email
                print("Email updated successfully.")

            # Write the updated trainer information back to the file
            new_trainers_update(trainers, 'Trainers.txt')
            break
    else:
        print("Trainer not found.")

#saving the data of trainer into txt gile
def new_trainers_update(trainers, my_file12):
    with open(my_file12, 'w') as file:
        header = '|'.join(trainers[0].keys())
        file.write(header + '\n')

        for trainer in trainers:
            values = '|'.join(trainer.values())
            file.write(values + '\n')

    print("Trainers data saved to file.")

#def funciton to read class scheduqle
def class_squedule_r(my_file12):
    with open(my_file12, 'w') as file:
        header = '|'.join(class_squedule[0].keys())
        file.write(header + '\n')

            # Write the data
        for entry in class_squedule:
            values = '|'.join(entry.values())
            file.write(values + '\n')


#lire
    class_schedule = []
    with open(my_file12, 'r') as file:
        header = [colonne.strip().lower() for colonne in file.readline().split('|')]
        for line in file:
            data = [colonne.strip() for colonne in line.split('|')]
            schedule_entry = dict(zip(header, data))
            class_schedule.append(schedule_entry)



    return class_schedule

#std file from lecturer
def std_r_file(my_file12):
    students = []
    with open(my_file12, 'r') as file:
        # Skip the first line (header)
        next(file)

        for line in file:
            # Split the line using '|' as a delimiter
            data = [colonne.strip() for colonne in line.split('|')]

            # Ignore the last column
            student = dict(zip(header[:-1], data))

            students.append(student)

    print("the liste of students  :")
    print(students)

    return students
#student txt file had spelling msitakes so used this method
def spelling_mistakes_correction(student_level):
    # Define the mapping between levels in st22.txt and trainers.txt
    lvl_correction = {'advanced': 'A',
                      'intermediate': 'I',
                      'beginner': 'B',
                      'Advanced': 'A',
                      'Intermediate': 'I',
                      'Beginner': 'B',
                      'begineer': 'B',
                      'intermrdiate': 'I'}

    # Use the mapping to get the corresponding level
    return lvl_correction.get(student_level.lower(), student_level)
def file_std(my_file12):
    students = []
    with open(my_file12, 'r') as file:
        # Skip the first line (header)
        header = [colonne.strip().lower() for colonne in file.readline().split('|')]
        next(file)

        for line in file:
            # Split the line using '|' as a delimiter
            data = [colonne.strip() for colonne in line.split('|')]

            # Ignore the last column
            student = dict(zip(header[:-1], data))

            # Map the student's level using the mapping function
            student['level'] = spelling_mistakes_correction(student.get('level'))

            students.append(student)



    return students



# for trainer
def find_trainer(trainers, email, password):
    for trainer in trainers:
        if trainer.get('email', '').lower() == email.lower() and trainer.get('password', '') == password:
            return True, trainer.get('name'), trainer.get('level')
    return False, None, None

#view schedule for ttainers based on lvls
#view schedule for ttainers based on lvls
def view_schedule(trainers, class_schedule, email):
    level = next((trainer.get('level') for trainer in trainers if trainer.get('email', '').lower() == email.lower()),
                 None)
    if level:
        print(f"\nClass Schedule for Level {level}:\n")
        for entry in class_schedule:
            if entry.get('level') == level:
                print(f"Subject: {entry.get('subject')}")
                print(f"Schedule: {entry.get('schedule')}")
                print(f"Charges: {entry.get('charges')}")
                print(f"Classroom: {entry.get('classroom')}")
                print(f"Date: {entry.get('date')}\n")
    else:
        print("Error: Level not found for the user.")

#def fynction update schedule
def updating_classinfo(class_schedule, trainers, email):
    #finding lvl of trainer
    trainer_level = next(
        (trainer.get('level') for trainer in trainers if trainer.get('email', '').lower() == email.lower()), None)

    if trainer_level:
        # fidning schedule based on the lvl
        level_entries = [entry for entry in class_schedule if entry.get('level') == trainer_level]

        if level_entries:
            print(f"\nCurrent Schedule for Level {trainer_level}:\n")
            for entry in level_entries:
                print(f"Subject: {entry.get('subject')}")
                print(f"Schedule: {entry.get('schedule')}")
                print(f"Charges: {entry.get('charges')}")
                print(f"Classroom: {entry.get('classroom')}")
                print(f"Date: {entry.get('date')}\n")

            #letting the triner update the class info
            subject_to_update = input("Enter the subject to update: ")
            new_schedule = input("Enter the new schedule: ")
            new_charges = input("Enter the new charges: ")
            new_classroom = input("Enter the new classroom: ")
            new_date = input("Enter the new date: ")

            # changing all the info
            for entry in level_entries:
                if entry.get('subject') == subject_to_update:
                    entry['schedule'] = new_schedule
                    entry['charges'] = new_charges
                    entry['classroom'] = new_classroom
                    entry['date'] = new_date


            #sauvegarder l'info into text file
            class_info_register(class_schedule, 'Class_Schedule.txt')
            print(f"Schedule updated successfully for Level {trainer_level}")
        else:
            print(" sorry. therre is no schedule for your level.")
    else:
        print("Seems like the lvl is incorrect.")

#saving the update to txt fle
def class_info_register(class_schedule, my_file12):
    with open(my_file12, 'w') as file:
        # writingi in the header
        header = '|'.join(class_schedule[0].keys())
        file.write(header + '\n')

        # wririjtn in the data
        for entry in class_schedule:
            values = '|'.join(entry.values())
            file.write(values + '\n')

    print("Class schedule saved to file.")

#adding a neew scheudle
def add_new_schedule(class_schedule):
    level = input("Enter the level for the new schedule entry: ")
    subject = input("Enter the subject for the new schedule entry: ")
    new_schedule = input("Enter the schedule for the new entry: ")
    new_charges = input("Enter the charges for the new entry: ")
    new_classroom = input("Enter the new classroom location: ")
    new_date = input("Enter the new date: ")

    # CreatING  a new schedyule entry
    new_entry = {'level': level,
                 'subject': subject,
                 'schedule': new_schedule,
                 'charges': new_charges,
                 'classroom': new_classroom,
                 'date': new_date}

    # i should add entrey to class schedule using append
    class_schedule.append(new_entry)

    #then saving it to my txt file
    class_info_register(class_schedule, 'Class_Schedule.txt')

    print("New schedule added successfully.")

#deletinf a shcedue;l
def deleting_schedule(class_schedule, level):
    # Find the schedule entries for the specified level
    level_entries = [entry for entry in class_schedule if entry.get('level') == level]

    if level_entries:
        print(f"\nCurrent Schedule for Level {level}:\n")
        for entry in level_entries:
            print(f"Subject: {entry.get('subject')}")
            print(f"Schedule: {entry.get('schedule')}")
            print(f"Charges: {entry.get('charges')}")
            print(f"Classroom: {entry.get('classroom')}")
            print(f"Date: {entry.get('date')}\n")

        # Get user input for the entry to delete
        subject_to_delete = input("Enter the subject you want to delete : ")

        # Delete the schedule entry
        class_schedule = [entry for entry in class_schedule if
                          not (entry.get('level') == level and entry.get('subject') == subject_to_delete)]

        # Save the updated schedule to the file
        class_info_register(class_schedule, 'Class_Schedule.txt')

        print(f"Schedule deleted successfully for Lvl {level}")
    else:
        print("Error: No schedule entries found for the specified level.")

#feed back txt file suggestions and complaints
def handle_feedback(my_file12):
    feedback_type = input("Please enter your feedback type \n (1: Suggestions \n 2: Complaints)-- ")
    feedback = input("Please enter your feedback: ")

    new_feedback_entry = f"|{feedback}|\n"

    with open(my_file12, 'r') as file:
        lines = file.readlines()

    found_section = False
    feedback_sections = ['|Suggestions|', '|Complaints|']

    for i, line in enumerate(lines):
        if line.strip() in feedback_sections:
            if line.strip() == '|Suggestions|' and feedback_type == '1':
                found_section = True
            elif line.strip() == '|Complaints|' and feedback_type == '2':
                found_section = True
            continue
        if found_section:
            # Insert the new feedback entry after the appropriate section
            lines.insert(i, new_feedback_entry)
            break
    else:
        # If the section was not found, append the new feedback entry at the end of the file
        lines.append(new_feedback_entry)

    # Write the modified content back to the file
    with open(my_file12, 'w') as file:
        file.writelines(lines)

    print("Thank you for your feedback! It has been successfully sent to the administrator.")
#creating main
def main():
    file_for_trainers_info = 'Trainers.txt'
    file_for_class_squedule = 'Class_Schedule.txt'
    file_for_students_enrolled = 'st1.txt'
    students = file_std(file_for_students_enrolled)


    trainers = reading_file_for_trainer(file_for_trainers_info)
    class_schedule = class_squedule_r(file_for_class_squedule)

    max_num_atmpts = 3
    num_login_attempts = 0


    print("------Welcome to your page. Here you can browse all the information you need------")

    while num_login_attempts < max_num_atmpts:
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        true, name, level = find_trainer(trainers, email, password)

        if true:
            print(f"Login successful! Welcome, {name} here you will find info for your level-- {level})")
            # Choices for lvls
            print('Here are your options :\n')
            print('\nType 1 to view schedule',
                  '\nType 2 for list of students enrolled',
                  '\n Type 3 to update / Delete / Add Class Schedule informations',
                  '\nType 4 to update profile',
                  '\n Type 5 to Send feedback to administror')

            choice = input("Enter your choice: ")

            if choice == '1':
                view_schedule(trainers, class_schedule, email)
            elif choice == '2':
                paid_stdudents(trainers, students, email)

            elif choice == '3':
                print('\nType 1 to update Class Schedule informations',
                      '\nType 2 to delete Class Schedule informations',
                      '\n Type 3 to insert Class Schedule informations')
                choice1 = input("Enter your choice: ")
                if choice1 == '1':
                    level = next((trainer.get('level') for trainer in trainers if
                                  trainer.get('email', '').lower() == email.lower()), None)
                    if level:
                        updating_classinfo(class_schedule, trainers, email)
                    else:
                        print("sorry. you entered a non existent level. try again later")
                elif choice1 == '2':
                    level = next((trainer.get('level') for trainer in trainers if
                                  trainer.get('email', '').lower() == email.lower()), None)
                    if level:
                        deleting_schedule(class_schedule, level)
                    else:
                        print("level not found, try again.")
                elif choice1 == '3':
                    add_new_schedule(class_schedule)
            elif choice == '4':
                trainer_profile_update(trainers, email)
            elif choice == '5':
                handle_feedback(my_file12='tst2.txt')




            break
        else:
            num_login_attempts += 1
            remaining_attempts = max_num_atmpts - num_login_attempts
            print(f"Invalid email or password. \n only {remaining_attempts} attempts remaining.")

    if num_login_attempts == max_num_atmpts:
        print("sorry, you have exeeced the amount of possible atempts.")
#calling main functuioen

if __name__ == "__main__":
    main()
