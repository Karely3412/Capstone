import datetime
from competencytrackingtool.app import app
import csv

from competencytrackingtool.utils import hash_val


class main:
    def __init__(self):
        self.application = app()
        self.MAX_EMPLOYEE_MENU_OPTIONS = 7
        self.MAX_MANAGER_MENU_OPTIONS = 22

    def run(self):
        """
        Start of the main class. Controls how the application will run

        """
        if not self.application.is_logged_in():
            while True:
                print("Please login")
                username = input("\tusername: ")
                password = input("\tpassword: ")
                result = self.application.login(username, password)
                if result:
                    break
                print("Invalid login credentials!\n")
        self.display_menu()

    def display_menu(self):
        """
        Determines the kind of menu the user will be shown

        """
        print(
            "\nWelcome "
            + self.application.get_user().get_first_name()
            + " "
            + self.application.get_user().get_last_name()
            + ","
        )
        print("Type the menu number to choose an option:")
        if not self.application.is_manager():
            self.display_employee_menu()
        else:
            self.display_manager_menu()
        result = input("Your option: ")
        if self.is_input_valid(result):
            self.handle_selected_menu_option(int(result))
        else:
            print("Invalid input!")
            self.display_menu()

    def is_input_valid(self, val):
        """
        Ensures the input is an integer and it is within the range of the menu options provided.

        Parameters:
        val (str): The string input from the user

        Returns:
        bool: True if the input is valid and False otherwise

        """
        try:
            result = int(val)
            if self.application.is_manager():
                return result >= 1 and result <= self.MAX_MANAGER_MENU_OPTIONS
            return result >= 1 and result <= self.MAX_EMPLOYEE_MENU_OPTIONS
        except:
            print("Invalid input!")
            return False

    def handle_selected_menu_option(self, val):
        """
        Calls the relevant function for each menu option

        Parameters:
        val (int): The chosen menu option

        """
        if val == 1:
            self.handle_change_first_name()
        elif val == 2:
            self.handle_change_last_name()
        elif val == 3:
            self.handle_change_email()
        elif val == 4:
            self.handle_change_password()
        elif val == 5:
            self.application.logout()
        elif self.application.is_manager():
            self.handle_selected_manager_menu_option(val)
        elif not self.application.is_manager():
            self.handle_selected_employee_menu_option(val)
        else:
            print("You chose option: " + str(val))
        self.run()

    def handle_selected_manager_menu_option(self, val):
        """
        Shows the additional menu options that a manager should see

        """
        if val == 6:
            self.display_all_users()
        elif val == 7:
            self.handle_search_user()
        elif val == 8:
            self.get_all_user_report_for_single_competency()
        elif val == 9:
            self.get_single_user_report_for_single_competency()
        elif val == 10:
            self.get_assessments_for_single_user()
        elif val == 11:
            self.add_new_user()
        elif val == 12:
            self.add_new_competency()
        elif val == 13:
            self.add_new_assessment()
        elif val == 14:
            self.handle_adding_assessment_result()
        elif val == 15:
            self.handle_edit_user_info()
        elif val == 16:
            self.handle_edit_competency()
        elif val == 17:
            self.handle_edit_assessment()
        elif val == 18:
            self.handle_edit_assessment_result()
        elif val == 19:
            self.handle_delete_assessment_result()
        elif val == 20:
            self.export_competency_report_by_competency_and_users()
        elif val == 21:
            firstname = input("Enter user's firstname: ")
            lastname = input("Enter user's lastname: ")
            users = self.application.search_user_with_both_names(firstname, lastname)
            if not users:
                print("User doesn't exist")
            else:
                self.export_user_competency_summary_by_id(users[0].get_user_id())
        elif val == 22:
            self.process_assessment_results_from_csv()
        else:
            print("You selected option: " + str(val))

    def handle_edit_assessment(self):
        """
        Modifies the assessment
        """
        response = input("Enter assessment name: ")
        new_value = input("Enter new assessment name: ")
        if not self.application.update_assessment(response, new_value):
            print("Assessment requested doesn't exist")

    def handle_delete_assessment_result(self):
        """
        Delets a specific assessment result

        """
        response = input("Enter assessment name: ")
        firstname = input("Enter user first name: ")
        lastname = input("Enter user last name: ")
        if not self.application.delete_assessment_result(response, firstname, lastname):
            print("Assessment requested doesn't exist")

    def handle_edit_assessment_result(self):
        """
        Modifies the assessment results

        """
        response = input("Enter assessment name: ")
        firstname = input("Enter user first name: ")
        lastname = input("Enter user last name: ")
        new_val = input("Enter new score: ")
        if not self.application.update_assessment_result(
            response, firstname, lastname, new_val
        ):
            print("Assessment requested doesn't exist")

    def handle_edit_competency(self):
        """
        Modifies the competency information

        """
        response = input("Enter competency name: ")
        new_value = input("Enter new competency name: ")
        if not self.application.update_competency(response, new_value):
            print("Competency requested doesn't exist")

    def handle_edit_user_info(self):
        """
        Changes a user's info

        """
        first_name = input("Enter the user's firstname: ")
        last_name = input("Enter the user's lastname: ")
        edit_user = self.application.search_user_with_both_names(first_name, last_name)
        if not edit_user:
            print("User doesn't exist!")
            return

        self.display_user_options(edit_user[0])

    def display_user_options(self, param):
        """
        Displays the sub menu options

        Parameters:
        param - the user whose account will be modified

        """
        print("1 Change user's firstname")
        print("2 Change user's lastname")
        print("3 Change user's email")
        print("4 Change user's password")
        print("5 Change user's phone number")
        result = input("Your option: ")
        if self.is_input_valid(result):
            self.handle_selected_user_detail_to_change_menu_option(int(result), param)
        else:
            print("Invalid input!")

    def handle_selected_user_detail_to_change_menu_option(self, val, other_user):
        """
        Performs the necessary action when a user makes a selection on the sub menu

        Properties:
        val - the user's option
        other_user - the user whose account will be modified

        """
        if val == 1:
            result = input("Enter new first name: ")
            self.application.update_other_user_firstname(other_user, result)
        elif val == 2:
            result = input("Enter new last name: ")
            self.application.update_other_user_lastname(other_user, result)
        elif val == 3:
            result = input("Enter new email: ")
            self.application.update_other_user_email(other_user, result)
        elif val == 4:
            result = input("Enter new password: ")
            self.application.update_other_user_password(other_user, result)
        elif val == 5:
            result = input("Enter new phone number: ")
            self.application.update_other_user_phone(other_user, result)
        else:
            print("Invalid input!")

    def handle_adding_assessment_result(self):
        """
        Adds the assessment results to the database

        """
        if not self.application.is_manager():
            return
        arr = []
        user_name = input("Please enter the name of the user: ")
        assessment_name = input("Please enter the assessment name: ")
        score_id = input("Please enter the score (It should only be from 0 to 4): ")
        date_taken = datetime.datetime.now()
        manager_id = self.application.get_user().get_user_id()
        id = hash_val(
            user_name + assessment_name + score_id + str(date_taken) + str(manager_id)
        )
        arr.append(id)
        arr.append(user_name)
        arr.append(assessment_name)
        arr.append(score_id)
        arr.append(date_taken)
        arr.append(manager_id)
        self.application.create_assessment_result(arr)

    def add_new_competency(self):
        """
        Adds a competency object to the database

        """
        if not self.application.is_manager():
            return
        arr = []
        name = input("Enter the name of the competency: ")
        date_created = datetime.datetime.now()
        id = hash_val(name + str(date_created))
        arr.append(id)
        arr.append(name)
        arr.append(date_created)
        self.application.create_competency(arr)

    def add_new_assessment(self):
        """
        Adds a new assessment to the database

        """
        if not self.application.is_manager():
            return
        arr = []
        name = input("Please enter name of the assessment: ")
        date_created = datetime.datetime.now()
        competency = input("Please enter name of competency: ")
        id = hash_val(name + str(date_created) + competency)
        arr.append(id)
        arr.append(name)
        arr.append(date_created)
        arr.append(competency)
        self.application.create_assessment(arr)

    def add_new_user(self):
        """
        Adds a new user to the database

        """
        if not self.application.is_manager():
            return
        arr = []
        firstname = input("Please enter first name: ")
        lastname = input("Please enter last name: ")
        phone = input("Please enter phone number: ")
        email = input("Please enter email: ")
        password = input("Please enter password: ")
        active = input("Please enter T if user is active and F if not: ")
        date_created = datetime.datetime.now()
        hire_date = datetime.datetime.now()
        user_type = input(
            "Please enter E if user is ordinary user and M if user is a manager: "
        )
        if active == "F":
            active = "FALSE"
        else:
            active = "TRUE"

        if user_type == "M":
            user_type = "MANAGER"
        else:
            user_type = "EMPLOYEE"

        arr.append(
            hash_val(
                firstname
                + lastname
                + phone
                + email
                + password
                + str(date_created)
                + str(hire_date)
            )
        )
        arr.append(firstname)
        arr.append(lastname)
        arr.append(phone)
        arr.append(email)
        arr.append(password)
        arr.append(active)
        arr.append(date_created)
        arr.append(hire_date)
        arr.append(user_type)
        self.application.create_user(arr)

    def handle_selected_employee_menu_option(self, val):
        """
        Perfroms the appropriate action depending on the menu option selected

        """
        if val == 6:
            self.get_user_competency_summary_by_id(
                self.application.get_user().get_user_id()
            )
        elif val == 7:
            self.export_user_competency_summary_by_id(
                self.application.get_user().get_user_id()
            )
        else:
            print("You selected option: " + str(val))

    def handle_search_user(self):
        """
        Searches for a user from the databse using their name

        """
        name = input("Enter name to search: ")
        users = self.application.search_user(name)
        for val in users:
            print(
                val.get_first_name()
                + " "
                + val.get_last_name()
                + " | "
                + val.get_user_type().capitalize()
            )

    def display_all_users(self):
        """
        Fetches and displays all users stored in the database

        """
        if not self.application.is_manager():
            return
        users = self.application.get_all_users()
        for val in users:
            print(
                val.get_first_name()
                + " "
                + val.get_last_name()
                + " | "
                + val.get_user_type().capitalize()
            )

    def handle_change_first_name(self):
        """
        Changes the firstname of the user

        """
        result = input("Enter your new first name: ")
        self.application.update_user_firstname(result)

    def handle_change_last_name(self):
        """
        Changes the lastname of the user

        """
        result = input("Enter your new last name: ")
        self.application.update_user_lastname(result)

    def handle_change_email(self):
        """
        Changes the user's email

        """
        result = input("Enter your new email: ")
        self.application.update_user_email(result)

    def handle_change_password(self):
        """
        Changes the user's password

        """
        result = input("Enter your new password: ")
        self.application.update_user_password(result)

    def display_employee_menu(self):
        """
        Shows the employee user's menu

        """
        print("1 Change first name")
        print("2 Change last name")
        print("3 Change email")
        print("4 Change password")
        print("5 Logout")
        print("6 View competency and assessment data")
        print("7 Export competency report")

    def display_manager_menu(self):
        """
        Shows the manager's menu

        """
        print("1 Change first name")
        print("2 Change last name")
        print("3 Change email")
        print("4 Change password")
        print("5 Logout")
        print("6 View all users")
        print("7 Search for user")
        print(
            "8 View a report of all users and their competency levels for a given competency"
        )
        print("9 View a competency level report for an individual user")
        print("10 View a list of assessments for a given user")
        print("11 Add a user")
        print("12 Add a new competency")
        print("13 Add a new assessment to a competency")
        print("14 Add an assessment result for a user for an assessment")
        print("15 Edit a user's information")
        print("16 Edit a competency")
        print("17 Edit an assessment")
        print("18 Edit an assessment result")
        print("19 Delete an assessment result")
        print("20 Export competency report by competency and users")
        print("21 Export competency report for a single user")
        print("22 Import assessment results from a CSV file")

    def get_assessments_for_single_user(self):
        """
        fetches a single user's assessment

        """
        user_name = input("Please enter user's name (first or last name): ")
        result = self.application.get_assessments_for_single_user(user_name)
        for data in result:
            print("Assessment name: " + data[0])
            print("Competency level: " + str(data[1]) + "\n")

    def get_all_user_report_for_single_competency(self):
        """
        Gets all of the users' report for a specific competency

        """
        name = input("Please enter the name of the competency: ")
        result = self.application.get_all_user_report_for_single_competency(name)
        for data in result:
            print("User name: " + data[0])
            print("Competency level: " + str(data[1]) + "\n")

    def get_single_user_report_for_single_competency(self):
        """
        Fetches a user's report for a specific competency

        """
        user_name = input("Please enter user's name (first or last name): ")
        name = input("Please enter the name of the competency: ")
        result = self.application.get_single_user_report_for_single_competency(
            user_name, name
        )
        for data in result:
            print("User name: " + data[0])
            print("Competency level: " + str(data[1]) + "\n")

    def get_user_competency_summary_by_name(self, first_name, last_name):
        """
        fetches a user's competency using their name

        """
        results = self.application.get_user_competency_summary_by_name(
            first_name, last_name
        )
        for val in results:
            print_assessments = ""
            for elem in val.get_assessments():
                print_assessments = (
                    print_assessments
                    + "\n\t\tCompetency name: "
                    + elem.get_competency_name()
                )
                print_assessments = (
                    print_assessments
                    + "\n\t\tAssessment name: "
                    + elem.get_assessment_name()
                )
                print_assessments = (
                    print_assessments + "\n\t\tScore: " + str(elem.get_score())
                )
            print(
                "Name: "
                + val.get_name()
                + "\n\tEmail: "
                + val.get_email()
                + "\n\tAssessments: "
                + print_assessments
                + "\n\tAverage competency score: "
                + val.get_average_competency_score()
            )

    def get_user_competency_summary_by_id(self, id):
        """
        Fetches a user's competency summary using their id

        """
        results = self.application.get_user_competency_summary_by_id(id)
        for val in results:
            print_assessments = ""
            for elem in val.get_assessments():
                print_assessments = (
                    print_assessments
                    + "\n\t\tCompetency name: "
                    + elem.get_competency_name()
                )
                print_assessments = (
                    print_assessments
                    + "\n\t\tAssessment name: "
                    + elem.get_assessment_name()
                )
                print_assessments = (
                    print_assessments + "\n\t\tScore: " + str(elem.get_score())
                )
            print(type(val.get_name()))
            print(
                "Name: "
                + val.get_name()
                + "\n\tEmail: "
                + val.get_email()
                + "\n\tAssessments: "
                + print_assessments
                + "\n\tAverage competency score: "
                + str(val.get_average_competency_score())
            )

    def get_competency_summary_for_all_users(self):
        """
        fetches the competency summary for all users

        """
        result = self.application.get_competency_summary_for_all_users()
        for val in result:
            print_assessments = ""
            for elem in val.get_assessments():
                print_assessments = (
                    print_assessments
                    + "\n\t\tCompetency name: "
                    + elem.get_competency_name()
                )
                print_assessments = (
                    print_assessments
                    + "\n\t\tAssessment name: "
                    + elem.get_assessment_name()
                )
                print_assessments = (
                    print_assessments + "\n\t\tScore: " + str(elem.get_score())
                )
            print(
                "Name: "
                + val.get_name()
                + "\n\tEmail: "
                + val.get_email()
                + "\n\tAssessments: "
                + print_assessments
                + "\n\tAverage competency score: "
                + val.get_average_competency_score()
            )

    def export_competency_report_by_competency_and_users(self):
        """
        Exports all user's competency summary

        """
        try:
            header = ["name", "email", "assessments", "average competency score"]
            data = []
            result = self.application.get_competency_summary_for_all_users()
            for val in result:
                print_assessments = ""
                for elem in val.get_assessments():
                    print_assessments = (
                        print_assessments
                        + "\n\t\tCompetency name: "
                        + elem.get_competency_name()
                    )
                    print_assessments = (
                        print_assessments
                        + "\n\t\tAssessment name: "
                        + elem.get_assessment_name()
                    )
                    print_assessments = (
                        print_assessments + "\n\t\tScore: " + str(elem.get_score())
                    )
                row = [
                    val.get_name(),
                    val.get_email(),
                    print_assessments,
                    val.get_average_competency_score(),
                ]
                data.append(row)

            with open(
                "competency_summary_for_al_users.csv", "w", encoding="UTF8", newline=""
            ) as f:
                writer = csv.writer(f)

                # write the header
                writer.writerow(header)

                # write multiple rows
                writer.writerows(data)
        except:
            print("Please make sure the file name is correct")

    def export_user_competency_summary_by_id(self, id):
        """
        Exports a user's competency summary using their id

        """
        try:
            header = ["name", "email", "assessments", "average competency score"]
            data = []
            results = self.application.get_user_competency_summary_by_id(id)
            for val in results:
                print_assessments = ""
                for elem in val.get_assessments():
                    print_assessments = (
                        print_assessments
                        + elem.get_competency_name()
                        + " - "
                        + elem.get_assessment_name()
                        + ": "
                        + str(elem.get_score())
                    )

                row = [
                    val.get_name(),
                    val.get_email(),
                    print_assessments,
                    val.get_average_competency_score(),
                ]
                data.append(row)

            with open("competency_summary.csv", "w", encoding="UTF8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(data)
        except:
            print("Please make sure the file name is correct")

    def process_assessment_results_from_csv(self):
        """
        Creates assessment result entries using the data from a csv file

        """
        try:
            filepath = input("Enter assessment results csv file path: ")
            data = []
            with open(filepath, encoding="utf8") as f:
                csv_reader = csv.reader(f)
                next(csv_reader)

                for line in csv_reader:
                    arr = []
                    id = hash_val(str(line))
                    manager_id = self.application.get_user().get_user_id()
                    arr.append(id)
                    arr.extend(line)
                    arr.append(manager_id)
                    data.append(arr)

            for d in data:
                self.application.create_assessment_results(d)
        except:
            print("Please make sure the file path is correct")


application = main()
application.run()
