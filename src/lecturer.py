import sys,time
import datetime
from datetime import date

# Printslow is a function that would print our header in a way that transitional
def print_slow(word):
    #run the word
    for l in word:
        #make it appear within 0
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)

# Takes in a textfile that hold the format of a table and returns a matrix
def listing (file_name):
    liste = []
    with open(file_name , 'r') as file :
        #skips the first two lines since they are the header
        file.readline()
        file.readline()
        for line in file :
            #slices raw data and used '|' as a divider
            r = line.strip().split("|")
            #remove exccess empty spaces and addes it to liste
            r = [item.strip() for item in r if item]
            liste.append(r)
    return liste

# Clear function capitalized the first letter of a letter
def clear(word):
    liste = word.strip().split()
    #in case the word is a tp number is doesnt touch it and return as it is
    if word[2:].isdigit() == False:
        for i in range(len(liste)):
            #capitalizes the word
            liste[i] = liste[i].capitalize()
    #in case is a name is join them as one
    if len(liste) > 1 :
        clean = ' '.join(liste)
    else :
        clean = str(liste[0])
    return clean

#registers a student within the st1.txt file
def register_student(file_name):
    print_slow("|--------------♡---------------|\n")
    enter = ["\tName :", "\tTPnumber :", "\tEmail :", "\tContact :", "\tAddress :", "\tLevel :", "\tModules :",
             "\tDate :", "Paid?", "Invoice:"]
    register = []
    liste = listing(file_name)  # liste file_name into a matrix
    max_attempts = 3  # Maximum number of attempts to correct errors

    for _ in range(max_attempts + 1):
        register = []  # Reset register list for each attempt
        for i in range(0 , 8):
            user_input = input(enter[i])
            cleaned_input = user_input.strip()  # Remove leading/trailing whitespace
            if not cleaned_input:  # If input is empty
                print("\n\033[1mEmpty prompts are not accepted!\033[0m")
                break  # Break out of inner loop
            register.append(clear(cleaned_input))

        else:  # This block is executed if the inner loop completes without encountering a 'break'
            # Check if TP number already exists
            if any(entry[1] == register[1] for entry in liste):
                print("\n\033[1mTP number is already taken!\033[0m")
            else:
                # insert with paid no until student pays and calculate invoice amount
                paid = 'no'
                register.insert(8 , paid)
                if register[5] == 'Advanced':
                    register.insert(9 , '1000')
                elif register[5] == 'Intermediate':
                    register.insert(9 , '600')
                elif register[5] == 'Beginner':
                    register.insert(9 , '350')

                with open(file_name, 'a') as file:
                    file.write(
                        "| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} |\n".format(
                            *register))
                print("\n\033[1mRegistration successful\033[0m")
                return  # Exit the function after successful registration

        if _ == max_attempts:
            print("\n\033[1mMaximum attempts reached. Registration unsuccessful.\033[0m")
            return




# Registers lecturer
def register_lecturer(file_name):
    print_slow("|--------------♡---------------|\n")
    enter = ["\tUsername :", "\tPassword :"]
    register = []
    liste = listing(file_name) # Turns the file_name into a matrix
    max_attempts = 3  # Maximum number of attempts to correct errors

    for _ in range(max_attempts + 1):
        register = []  # Reset register list for each attempt
        for i in enter:
            user_input = input(i)
            cleaned_input = user_input.strip()  # Remove leading/trailing whitespace
            if not cleaned_input:  # If input is empty
                print("\n\033[1mEmpty prompts are not accepted!\033[0m")
                break  # Break out of inner loop
            register.append(clear(cleaned_input))
        else:  # This block is executed if the inner loop completes without encountering a 'break'
            # Check if username already exists
            if any(entry[0] == register[0] for entry in liste):
                print("\n\033[1mUsername is already taken!\033[0m")
            else:
                with open(file_name, 'a') as file:
                    file.write("| {:<24} | {:<25} |\n".format(*register))
                print("\n\033[1mRegistration successful\033[0m")
                return  # Exit the function after successful registration
        if _ == max_attempts:
            print("\n\033[1mMaximum attempts reached. Registration unsuccessful.\033[0m")





def replacestudent(file_name, matrix, new_value, row_index, col_index):
    sect = ['name', 'tpnumber', 'email', 'contact', 'residence', 'level', 'module', 'Date' , "Paid?" , "Invoice"]
    # Update the matrix with the new value at the specified row and column indices
    matrix[row_index][col_index] = new_value

    # Now, update the file with the modified matrix
    with open(file_name, 'w') as file:
        file.write("| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} |\n".format(*sect))
        file.write("|" + "-" * 27 + "|" + "-" * 27 + "|" + "-" * 32 + "|" + "-" * 27 + "|" + "-" * 27 + "|" + "-" * 27 +"|" + "-" * 32 +"|" + "-" * 27+"|" + "-" * 27+"|" + "-" * 27 +"|\n")

        for row in matrix:
            formatted_row = "| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} |".format(*row)
            file.write(formatted_row + '\n')


def replacelecturer(file_name, matrix, new_value, row_index, col_index):
    sect = ['Username' , 'Password']
    # Update the matrix with the new value at the specified row and column indices
    matrix[row_index][col_index] = new_value

    # Now, update the file with the modified matrix
    with open(file_name, 'w') as file:
        file.write("| {:<24} | {:<25} |\n".format(*sect))
        file.write("|" + "-" * 26 + "|" + "-" * 27 + "|\n")
        for row in matrix:
            formatted_row = "| {:<24} | {:<25} |".format(*row)
            file.write(formatted_row + '\n')



def updatestudent(file_name):
    print_slow("|--------------♡---------------|\n")
    sect = ['name', 'tpnumber', 'email', 'contact', 'residence', 'level', 'module', 'date', 'paid?', 'invoice']
    name = input('\tname :')
    tpnumber = input("\ttpnunmber :")
    TPnumber = clear(tpnumber)
    liste = listing(file_name) # Turns the file_name into a matrix
    for x, row in enumerate(liste):
        for j, val in enumerate(row):
            #to make sure we don't update another student but the one wanted
            if liste[x][j] == TPnumber:
                    while True:
                        elm = input('\nWhat would you like to update? \n\tMenu: \n\t1. name \n\t2. tpnumber \n\t3. email \n\t4. contact \n\t5. address \n\t6. level \n\t7. modules \n\t8. Date \n\t9. Paid? \n\t10. Invoice\n\nWhat is your selected choice?')
                        elm = elm.strip()
                        if elm.isdigit():
                            r = int(elm) - 1
                            if 0 <= r <= 9:
                                new = input(f'What would you like to change the {sect[r]} to?')
                                new = clear(new)
                                for ind in range(len(sect)):
                                    if sect[ind] == sect[r]:
                                        replacestudent(file_name, liste, new, x, ind)
                                        update_succesful = True
                                        break
                                break  # Break the loop if the input is valid
                            else:
                                print('n\033[1mError please choose from the menu given!\033[0m')
                        else:
                            print('\n\033[1mError please enter a valid number!\033[0m')
    if update_succesful == True:
        return '♡Update successful♡'
    else :
        return 'No update were made'

def updateprofile(file_name, name, password):
    print_slow("|--------------♡---------------|\n")
    liste = listing(file_name)
    update_successful = False
    for x in range(len(liste)):
        if liste[x][0] == name:
            while True:
                elm = input("\nWhat would you like to update?\n\tMenu: \n\t1. Username \n\t2. Password \n\nWhat is your selected choice?")
                elm = elm.strip()
                #to make sure the prompt is a number
                if elm.isdigit():
                    r = int(elm)
                    # verify that we have the number between the number available on the menu
                    if 1 <= r <= 2:
                        new = input("\nWhat would you like to change it to?")
                        new = clear(new)
                        if r == 1:
                            replacelecturer(file_name, liste, new, x, 0)
                            update_successful = True
                            break
                        elif r == 2:
                            replacelecturer(file_name, liste, new, x, 1)
                            update_successful = True
                            break
                    else:
                        print("\n\033[1mError please choose from the menu given!\033[0m")
                else:
                    print('\n\033[1mError please enter a valid number!\033[0m')
    if update_successful:
        return '♡ Update successful ♡'
    else:
        return 'No updates were made.'



def matrixdate(matrix):
    #takes a matrix of student text file and returns a matrix with just dates
    date = []
    for i , row in enumerate(matrix):
            data = matrix[i][7].split("-")
            data = [int(elem) for elem in data if elem]
            date.append(data)


    return date
def get_diff(today, enddate):
    #calculate the difference between today and the day they should end their training
    diff = enddate - today
    return diff.days

def deletestudent(file_name):
    print_slow("|--------------♡---------------|\n")
    sect = ['name', 'tpnumber', 'email', 'contact', 'residence', 'level', 'module', 'Date', "Paid?", "Invoice"]

    #transform the text file into a matrix
    liste = listing(file_name)
    #A matrix that only contains the dates in each the student started
    matrix = matrixdate(liste)


    #The in which we're today
    today = str(date.today())
    today = today.split("-")
    datetoday = datetime.date(int(today[0]), int(today[1]), int(today[2]))


    #the modiffied matrix
    lastform = []
    #the student deleted
    deleted = []


    #Would delete from the liste the student in which finished their training
    for i, row in enumerate(matrix):
            #To know when they will end we must get the day they started and add 3 months
            datestart = datetime.date(int(matrix[i][0]) , int(matrix[i][1]) , int(matrix[i][2]))
            if int(matrix[i][1]) > 9: #for the months are all modulo 12
                dateend = datetime.date(int(matrix[i][0]), (int(matrix[i][1])+3) % 12, int(matrix[i][2]))
            else :
                dateend = datetime.date(int(matrix[i][0]), int(matrix[i][1]) +3, int(matrix[i][2]))

            #the closer they get to their end day the smaller the difference is
            if get_diff(datetoday, dateend) > 0:
                    lastform.append(liste[i])
            elif get_diff(datetoday , dateend) < 0 :
                    deleted.append(liste[i])

    #The modified matrix would be transformed back to the wanted form into the text file
    with open(file_name, 'w') as file:
        file.write(
            "| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} |\n".format(
                *sect))
        file.write("|" + "-" * 27 + "|" + "-" * 27 + "|" + "-" * 32 + "|" + "-" * 27 + "|" + "-" * 27 + "|" + "-" * 27 +"|" + "-" * 32 +"|" + "-" * 27+"|" + "-" * 27+"|" + "-" * 27 +"|\n")

        for line in lastform:
            formatted_row = "| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} |".format(
                *line)
            file.write(formatted_row + '\n')
    #published to the lecturer the student that we're deleted from the text file
    for v in range(len(deleted)) :
        print(f'\n{deleted[v][0]} has been deleted since their training ended.')
    print("♡Thanks for using our service♡")

def approval (file_name ):
    print_slow("|--------------♡---------------|\n")
    sect = ['name' , 'tpnumber' , 'email' , 'contact' , 'residence' , 'level' , 'module' , 'date' , 'paid?' , 'invoice' , 'state']
    liste = listing(file_name)
    for i in range(len(liste)):
        if liste[i][10] == 'pending':
            while True :
                ask = input(f'{liste[i][0]} is requesting. \nDo you approve of their admission to {liste[i][6]} module?\n\tMenu : \n\t1.Yes \n\t2.No \n\nWhat is your selected choice?')
                ask.strip()
                if ask.isdigit():
                    r = int(ask)
                    if 1 <= r <= 2 :
                        if r==1 :
                            #modify the list in accordance of the lecturer wish
                            liste[i][10] = "Approved"
                            break
                        elif r==2 :
                            liste[i][10] = 'Rejected'
                            break
                    else :
                        print("Please enter a number between 1 and 2.")
                else :
                    print("Please enter a valid number.")

    for i in range(len(liste)):
        #index = 10
        if liste[i][10] == 'Rejected':
            liste.pop(i)
    #the request text file get modified with the new liste
    with open(file_name, 'w') as file:
        file.write("| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<45} | {:<25} | {:<25} | {:<25} | {:<25} |\n".format(*sect))
        file.write("|" + "-" * 27 + "|" + "-" * 27 + "|" + "-" * 32 + "|" + "-" * 27 + "|" + "-" * 27 + "|" + "-" * 27 +"|" + "-" * 47 +"|" + "-" * 27 +"|" + "-" * 27 +"|" + "-" * 27 +"|" + "-" * 27 +"|\n")
        for row in liste:
            formatted_row = "| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<45} | {:<25} | {:<25} | {:<25} | {:<25} |".format(*row)
            file.write(formatted_row + '\n')

    for i in range(len(liste)):
        liste[i].pop(10)
        register = liste[i]

        #once approved they also get added on the student text file
        with open('st1.txt', 'a') as file:
            file.write(
                "| {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} | {:<30} | {:<25} | {:<25} | {:<25} |\n".format(
                    *register))

        register.pop(0)
    print("♡Thanks for using our service♡")
def choice(name, password):
    print_slow("|--------------♡---------------|\n")
    while True:
        choice = input(f'Hello, {name}, what would you like to do? \n\tMenu: \n\t1. Register student \n\t2. Update \n\t3. Delete \n\t4. Request \n\nWhat is your selected choice?')
        choice = choice.strip()
        if choice.isdigit():
            r = int(choice)
            if 1<= r <= 4 :
                # Calls to register student
                if r == 1:
                    return register_student('st1.txt')
                elif r == 2:
                    # Calls to update either profile or student
                    print_slow("|--------------♡---------------|\n")
                    detail = input("\nWould you like to update your profile or a student's? \n\tMenu: \n\t1. Profile \n\t2. Student \n\nWhat is your selected choice?")
                    detail = detail.strip()
                    if detail == '1':
                        return updateprofile('test1.txt', name, password)
                    elif detail == '2':
                        return updatestudent('st1.txt')
                elif r == 3:
                    # Calls to deleted the student that ended their training
                    return deletestudent('st1.txt')
                elif r == 4:
                    # Calls to approve those waiting within the request text file
                    return approval('request.txt')
            else :
                print('\n\033[1mError please choose from the menu given!\033[0m"')
        else:
            print('\n\033[1mError please enter a valid number!\033[0m')

#login function for lecturer
def login(file_name):
    print_slow("|--------------♡---------------|\n")
    name = input("\tusername :")
    password = input("\tpassword :")
    name = clear(name)
    liste = listing (file_name)
    for i , row in enumerate(liste):
        if liste[i][0] == name :
            if liste[i][1] == password:
                return choice(name , password)
            elif  liste[i][1] != password :
                # gives the user a second chance to get it right
                print('\n\033[1mincorrect password please try again\033[0m')
                password = input("\tpassword :")
                if password == liste[i][1] :
                    return choice(name , password)
                else :
                    # This being the 3rd one is their last chance as mentioned
                    print("\n\033[1mThis is your last chance!\033[0m")
                    password = input("\tpassword :")
                    if password == liste[i][1] :
                        return choice(name , password)


    return 'Failed login'




