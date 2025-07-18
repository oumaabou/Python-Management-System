class StudentDisplay:
    def login(self):
        max_login_attempts = 3
        login_attempts = 0

        while login_attempts < max_login_attempts:
            username = input("Enter student ID: ")
            password = input("Enter password: ")

            with open('profile.txt', 'r') as f:
                # reading the profile.txt file to obtain the username and password
                for line in f:
                    # Split the line into columns
                    columns = line.strip().split('|')
                    if len(columns) >= 1:  # Ensure theres at least 1 column
                        name = columns[1].strip()
                        username_in_file = columns[2].strip()
                        password_in_file = columns[3].strip()

                        if username == username_in_file and password == password_in_file:
                            print("Login successful")
                            self.dashboard(username_in_file, password_in_file)
                            return  # Exit the function and the loop after successful login
                    else:
                        print("Insufficient information, please contact lecturer")

                # If no match found in the file
                login_attempts += 1
                print(f"Login failed, Please try again {max_login_attempts - login_attempts} attempts left.")

        # after the 3rd attempt code will end due to max attempts made
        print("Max login attempts reached. Please try again later")

    def dashboard(self, username_in_file,password_in_file):
        while True:
            print(f"\nStudent Dashboard: ")
            print("1. View Schedule")
            print("2. Send Request to Enroll in Additional Class")
            print("3. View Pending Requests")
            print("4. Delete Pending Requests")
            print("5. View Invoices")
            print("6. Make Payment")
            print("7. Update Profile")
            print("8. Logout")

            choice = input("Please enter your choice (number): ")

            if choice == '1':
                self.schedule()

            elif choice == '2':
                self.enrollment(username_in_file)

            elif choice == '3':
                self.view_pending_requests(username_in_file)

            elif choice == '4':
                self.delete_pending_requests(username_in_file)

            elif choice == '5':
                self.invoice(username_in_file)

            elif choice == '6':
                self.make_payment(username_in_file)

            elif choice == '7':
                self.update_profile(username_in_file,password_in_file)

            elif choice == '8':
                print("Successfully logged out.Thank you")
                break

            else:
                print("Invalid choice. Please try again.")

    def schedule(self):  # option 1 which opens the class schedule txt file
        with open("Class_Schedule.txt", 'r') as f:
            schedule = f.read()
            print(schedule)

    def enrollment(self,username_in_file):
        enroll = input(f"Which subject would you like to enroll in?[A- Advanced,I - Intermediate, B-Beginner]\nPython\nJavaScript\nWeb Development\nC++\n(exp:A,Python)\n")

        with open("st1.txt", "r+") as p:
            lines = p.readlines()
            # Find and display the row where the name matches
            for line in lines:
                columns = line.strip().split('|')
                tpno = columns[2].strip()
                if username_in_file == tpno:
                    profile = '|'.join(columns).strip()
                    profile_list = profile.strip().split('|')

                    with open("request.txt","a") as request_file:
                        if profile_list[11].strip() == '':
                            profile_list[11] = "pending                   |"
                            profile_list[7] = enroll + '            '
                            updated_profile = '|'.join(profile_list) + '\n'
                            request_file.writelines([updated_profile + '\n'])

                        else:
                            print("Request has already been made.Only one request can be made per semester")

    def view_pending_requests(self,username_in_file):
        with open("st1.txt", "r") as p:
            lines = p.readlines()
            # Find and display the row where the name matches
            for line in lines:
                columns = line.strip().split('|')
                tpno = columns[2].strip()
                if username_in_file == tpno:
                    profile = '|'.join(columns).strip()
                    profile_list = profile.strip().split('|')

                    with open("request.txt", "r") as f:
                        list = f.readlines()
                        for row in list:
                            column = row.strip().split('|')
                            tpno = column[2].strip()
                            if tpno == username_in_file:
                                state = column[11].strip()
                                print(f"pending status : {state}")
                                if state == '':
                                    print("No requests made")


    def delete_pending_requests(self,username_in_file):
        with open("request.txt", 'r+') as f:
            lines = f.readlines()
        with open("request.txt", 'w') as f:
            for line in lines:
                columns = line.strip().split('|')
                tpno = columns[2].strip()
                if username_in_file != tpno:
                    f.write(line)
        print("Pending requests deleted.")


    def invoice(self, username_in_file):
        with open("st1.txt", 'r+') as t:
            lines = t.readlines()
            # Find and display the row where the name matches
            for line in lines:
                columns = line.strip().split('|')
                tpno = columns[2].strip()
                if username_in_file == tpno:
                    profile = '|'.join(columns).strip()
                    list = profile.strip().split('|')
                    invoice = list[10]
                    print(f"RM{invoice}")

    def make_payment(self, username_in_file):
        with open("st1.txt", 'r+') as p:
            lines = p.readlines()
        for i, line in enumerate(lines):
            # Find and display the row where the name matches
            columns = line.strip().split('|')
            tpno = columns[2].strip()
            if username_in_file == tpno:
                profile = '|'.join(columns).strip()
                list = profile.strip().split('|')
                invoice = list[10]
                print("Total needed to be payed: RM", invoice)
                H = input("How would you like to make payment:\n1. Online Transfer\n2. JomPay\n")

                if H == '1':
                    input("Please enter your bank details")
                    print("Payment success, thank you")
                    columns[9] = 'yes                         '
                    columns[10] = 'N0                   '

                elif H == '2':
                    input("Please enter JomPay account details: ")
                    print("Payment success, thank you")
                    columns[9] = 'yes                         '
                    columns[10] = 'N0                   '

                else:
                    print("Please enter a valid number")

                updated_line = '|'.join(columns) + '\n'
                lines[i] = updated_line

            with open("st1.txt","w") as file:
                file.writelines(lines)


    def update_profile(self, username_in_file,password_in_file):
        with open("st1.txt", 'r+') as p:
            lines = p.readlines()
            # Display the first two lines
            for i in range(min(2, len(lines))):
                print(lines[i].strip())

            # Find and display the row where the name matches
            for line in lines:
                columns = line.strip().split('|')
                tpno = columns[2].strip()
                if username_in_file == tpno:
                    profile = '|'.join(columns).strip()
                    print(profile)
                    profile.strip().split('|')

            options = input("What would you like to update: \n1.Password \n2.Email\n3.Contact number\n4.Residence\n")
            if options in ['1', '2', '3', '4']:
                with open("profile.txt", 'r+') as p:
                    lines = p.readlines()
                    for i, line in enumerate(lines):
                        columns = line.strip().split('|')
                        tpno = columns[2].strip()

                        if username_in_file == tpno:
                            if len(columns) >= 1:
                                if options == '1':
                                    check = input("Please enter old password:")
                                    if check == password_in_file:
                                        new_password = input("Enter the new password: ")
                                        columns[3] = new_password + '                   '
                                elif options == '2':
                                    new_email = input("Enter the new email: ")
                                    columns[4] = new_email + '                  '
                                elif options == '3':
                                    new_contact_number = input("Enter the new contact number: ")
                                    columns[5] = new_contact_number + '                 '
                                elif options == '4':
                                    new_residence = input("Enter the new residence: ")
                                    columns[6] = new_residence + '                  '
                                else:
                                    print("Invalid option")

                                updated_line = '|'.join(columns) + '\n'
                                lines[i] = updated_line
        with open("profile.txt","w") as file:
            # p.write(line[0])
            file.writelines(lines)
            file.truncate()  # Remove any remaining content if the new content is shorter than the original
            print("Profile successfully updated")


# Create an instance of the StudentDisplay class and call the login method
"""student_system = StudentDisplay()
student_system.login()"""
