class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Trainer:
    id_counter = 1

    def __init__(self, trainer_name, level):
        self.id = Trainer.id_counter
        Trainer.id_counter += 1
        self.trainer_name = trainer_name
        self.level = level

class Administrator(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.trainers = {}
        self.modules = []  # List of modules as dictionaries
        self.monthly_income_report = {}
        self.feedback = {'Suggestions': [], 'Complaints': []}

    def register_trainer(self, trainer_name, level):
        trainer = Trainer(trainer_name, level)
        self.trainers[trainer.id] = {"trainer_object": trainer, "assigned_modules": []}
        return f"Trainer {trainer_name} registered successfully with ID: {trainer.id} and Level: {level}."

    def delete_trainer(self, trainer_id):
        if trainer_id in self.trainers:
            del self.trainers[trainer_id]
            return f"Trainer with ID {trainer_id} deleted successfully."
        else:
            return f"Trainer with ID {trainer_id} not found."

    def assign_trainer(self, trainer_id, module):
        if trainer_id in self.trainers:
            trainer = self.trainers[trainer_id]["trainer_object"]
            self.trainers[trainer_id]["assigned_modules"].append({"module": module})
            return f"Trainer {trainer.trainer_name} (ID: {trainer.id}, Level: {trainer.level}) assigned to {module} module."
        else:
            return f"Trainer with ID {trainer_id} not found."

    def update_module(self, old_module, new_module):
        for module_dict in self.modules:
            if old_module in module_dict["module"]:
                module_dict["module"] = new_module
                return f"Module '{old_module}' updated to '{new_module}'."
        return f"Module '{old_module}' not found."

    def view_monthly_income_report(self, trainer_id=None, module=None):
        if trainer_id and module:
            return f"Monthly Income Report for Trainer ID: {trainer_id}, Module: {module}, Income: {self.calculate_income(trainer_id)}"
        elif trainer_id:
            return f"Monthly Income Report for Trainer ID: {trainer_id}, Total Income: {self.calculate_income(trainer_id)}"
        elif module:
            return f"Monthly Income Report for Module: {module}, Total Income: {self.calculate_income(module)}"
        else:
            return "Monthly Income Report for All Trainers and Modules."

    def view_feedback(self):
        feedback_text = "||Feedback||\n\n|Suggestions|\n\n"
        feedback_text += "\n".join(self.feedback['Suggestions'])
        feedback_text += "\n\n|Complaints|\n\n"
        feedback_text += "\n".join(self.feedback['Complaints'])
        return feedback_text

    def update_profile(self):
        print("1. Change Trainer Level")
        print("2. Change Assigned Module")
        print("3. Update Module")
        print("4. Back to Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            trainer_id = int(input("Enter trainer ID to change level: "))
            new_level = input("Enter new level (Beginner/Intermediate/Advanced): ")
            while new_level not in ["Beginner", "Intermediate", "Advanced"]:
                print("Invalid level. Please choose from Beginner, Intermediate, or Advanced.")
                new_level = input("Enter new level (Beginner/Intermediate/Advanced): ")

            if trainer_id in self.trainers:
                trainer = self.trainers[trainer_id]["trainer_object"]
                trainer.level = new_level
                return f"Trainer {trainer.trainer_name} (ID: {trainer.id}) level changed to {new_level}."
            else:
                return f"Trainer with ID {trainer_id} not found."

        elif choice == "2":
            trainer_id = int(input("Enter trainer ID to change assigned module: "))
            new_module = input("Enter new module: ")

            if trainer_id in self.trainers:
                self.trainers[trainer_id]["assigned_modules"] = [{"module": new_module}]
                return f"Assigned module for Trainer ID {trainer_id} changed to {new_module}."
            else:
                return f"Trainer with ID {trainer_id} not found."

        elif choice == "3":
            old_module = input("Enter module to update: ")
            new_module = input("Enter new module name: ")
            return self.update_module(old_module, new_module)

        elif choice == "4":
            return "Back to Menu."

        else:
            return "Invalid choice. Please enter a number between 1 and 4."

    def calculate_income(self, trainer_id):
        if trainer_id in self.trainers:
            level = self.trainers[trainer_id]["trainer_object"].level
            if level == "Beginner":
                return 300
            elif level == "Intermediate":
                return 600
            elif level == "Advanced":
                return 1000
        return 0

    def save_data(self, filename):
        with open(filename, 'w') as file:
            # Save trainers
            file.write("Trainers:\n")
            for trainer_id, trainer_data in self.trainers.items():
                trainer_obj = trainer_data["trainer_object"]
                assigned_modules = trainer_data["assigned_modules"]
                file.write(f"{trainer_obj.id}\t{trainer_obj.trainer_name}\t{trainer_obj.level}\t{assigned_modules}\n")

            # Save modules
            file.write("\nModules:\n")
            for module_dict in self.modules:
                file.write(f"{module_dict['module']}\n")

            # Save monthly income report
            file.write("\nMonthly Income Report:\n")
            for module, income in self.monthly_income_report.items():
                file.write(f"{module}\t{income}\n")

            # Save feedback
            file.write("\nFeedback:\n")
            file.write("|Suggestions|\n")
            for suggestion in self.feedback['Suggestions']:
                file.write(f"{suggestion}\n")

            file.write("|Complaints|\n")
            for complaint in self.feedback['Complaints']:
                file.write(f"{complaint}\n")

        print("Data saved successfully.")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

            trainers_start = lines.index("Trainers:\n") + 1
            trainers_end = lines.index("\nModules:\n")
            modules_start = trainers_end + 1
            modules_end = lines.index("\nMonthly Income Report:\n")
            monthly_income_start = modules_end + 1
            monthly_income_end = lines.index("\nFeedback:\n")
            feedback_start = monthly_income_end + 1

            # Load trainers
            for line in lines[trainers_start:trainers_end]:
                parts = line.strip().split('\t')
                trainer_id, trainer_name, level, assigned_modules = parts
                self.trainers[int(trainer_id)] = {"trainer_object": Trainer(trainer_name, level), "assigned_modules": eval(assigned_modules)}

            # Load modules
            self.modules = [{"module": line.strip()} for line in lines[modules_start:modules_end]]

            # Load monthly income report
            for line in lines[monthly_income_start:feedback_start]:
                module, income = line.strip().split('\t')
                self.monthly_income_report[module] = float(income)

            # Load feedback
            feedback_lines = lines[feedback_start:]
            current_feedback_type = None
            current_feedback = []
            for line in feedback_lines:
                line = line.strip()
                if line.startswith('|Suggestions|'):
                    current_feedback_type = 'Suggestions'
                elif line.startswith('|Complaints|'):
                    current_feedback_type = 'Complaints'
                elif line.startswith('|'):
                    current_feedback_type = None
                elif current_feedback_type:
                    current_feedback.append(line)

            for feedback in current_feedback:
                feedback_type, feedback_text = feedback.split('|')
                feedback_type = feedback_type.strip()
                feedback_text = feedback_text.strip()
                if feedback_type in self.feedback:
                    self.feedback[feedback_type].append(feedback_text)
                else:
                    self.feedback[feedback_type] = [feedback_text]

            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found. No data loaded.")
        except Exception as e:
            print(f"Error loading data: {e}")

def main():
    # Admin login
    admin_username = "admin"
    admin_password = "adminpass"

    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    if entered_username == admin_username and entered_password == admin_password:
        print("Login successful. You are now logged in as an administrator.")
        admin = Administrator(admin_username, admin_password)

        # Load data (optional)
        admin.load_data("data.txt")

        while True:
            print("\nMenu:")
            print("1. Register Trainer")
            print("2. Assign Trainer to Module")
            print("3. Delete Trainer")
            print("4. View Monthly Income Report")
            print("5. View Trainer Feedback")
            print("6. Update Profile")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                trainer_name = input("Enter trainer name to register: ")
                level = input("Enter level (Beginner/Intermediate/Advanced): ")
                while level not in ["Beginner", "Intermediate", "Advanced"]:
                    print("Invalid level. Please choose from Beginner, Intermediate, or Advanced.")
                    level = input("Enter level (Beginner/Intermediate/Advanced): ")
                print(admin.register_trainer(trainer_name, level))

            elif choice == "2":
                trainer_id = int(input("Enter trainer ID to assign: "))
                module = input("Enter module name: ")
                print(admin.assign_trainer(trainer_id, module))

            elif choice == "3":
                trainer_id_to_delete = int(input("Enter trainer ID to delete (press Enter to skip): "))
                if trainer_id_to_delete:
                    result = admin.delete_trainer(trainer_id_to_delete)
                    print(result)

            elif choice == "4":
                trainer_id = int(input("Enter trainer ID to view monthly income report (press Enter for all trainers): "))
                module = input("Enter module to filter (press Enter for all modules): ")
                print(admin.view_monthly_income_report(trainer_id=trainer_id, module=module))

            elif choice == "5":
                print(admin.view_feedback())

            elif choice == "6":
                print(admin.update_profile())

            elif choice == "7":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

            # Save data after each operation
            admin.save_data("data.txt")

    else:
        print("Invalid credentials. Access denied.")

if __name__ == "__main__":
    main()
