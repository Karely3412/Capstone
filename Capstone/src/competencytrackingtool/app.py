from competencytrackingtool.competency_summary import competency_summary
from competencytrackingtool.data import data
from competencytrackingtool.utils import hash_val


class app:
    def __init__(self):
        self.database = data()
        self.user = None
        self.MANAGER = "MANAGER"
        self.EMPLOYEE = "EMPLOYEE"

    def login(self, username, password):
        """
        Handles loggin a user into the application

        """
        if self.is_logged_in():
            self.logout()

        self.user = self.database.get_user(username, hash_val(password))
        if self.user == None or self.user.get_active() == "False":
            self.logout()
            return False
        else:
            return True

    def logout(self):
        """
        Handles the logout functionality

        """
        if self.user:
            self.user = None

    def get_user(self):
        """
        fetches the currently logged in user

        Returns:
        returns the user or None if no user has logged in

        """
        return self.user

    def is_manager(self):
        """
        Returns:
        returns true if the user is a manager and false otherwise

        """
        if self.user:
            return self.user.get_user_type() == self.MANAGER
        return False

    def create_user(self, arr):
        """
        Creates a user

        Parameters:
        args (array) - a list containing the info to help create a user

        """
        if self.is_logged_in() and self.is_manager():
            arr[5] = hash_val(arr[5])
            result = self.database.create_user(arr)
            return result
        else:
            print("Only logged managers can create users")
            return False

    def create_competency(self, arr):
        """
        Creates a competency

        Parameters:
        args (array) - a list containing the info to help create a competency

        """
        if self.is_logged_in() and self.is_manager():
            result = self.database.create_competency(arr)
            return result
        else:
            print("Only logged managers can create competencies")
            return False

    def create_assessment(self, arr):
        """
        Creates an assessment

        Parameters:
        args (array) - a list containing the info to help create an assessment

        """
        if self.is_logged_in() and self.is_manager():
            result = self.database.create_assessment(arr)
            return result
        else:
            print("Only logged managers can create assessments")
            return False

    def create_assessment_result(self, arr):
        """
        Creates an assessment result

        Parameters:
        args (array) - a list containing the info to help create an assessment result

        """
        if self.is_logged_in() and self.is_manager():
            result = self.database.create_assessment_result(arr)
            return result
        else:
            print("Only logged managers can create assessments")
            return False

    def is_logged_in(self):
        """
        Determines if there's a logged in user

        Returns:
        True if there's a logged in user

        """
        return self.user != None

    def get_user(self):
        """
        fetches a user

        Returns:
        the logged in user

        """
        return self.user

    def search_user(self, name):
        """
        fetches a user by their name

        Parameters:
        name (array) - name of the user. Can be either first or last name

        Returns:
        the user with the supplied id

        """
        return self.database.search_user(name)

    def search_user_by_id(self, id):
        """
        fetches a user by their id

        Parameters:
        name (array) - name of the user. Can be either first or last name

        Returns:
        the user with the supplied id

        """
        return self.database.search_user_by_id(id)

    def search_user_with_both_names(self, first_name, last_name):
        """
        Fetches the user by their first nad last name

        Parameters:
        first_name - the user's first name
        last_name - the user's last name

        Returns:
        the user with the supplied name

        """
        return self.database.search_user_with_both_names(first_name, last_name)

    def get_all_users(self):
        """
        fetches all the users form the database

        Returns:
        a list of users

        """
        if not self.is_logged_in or not self.is_manager():
            return []
        result = self.database.get_all_users()
        return result

    def update_user_email(self, email):
        """
        updates the user's email to the supplied email

        Parameters:
        email - the new email

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                self.user.get_user_id(), "email", email
            )
            self.user = self.database.get_user(email, self.user.get_password())
            return result
        else:
            print("Login first")
            return False

    def update_other_user_email(self, other_user, email):
        """
        updates the user's email to the supplied email

        Parameters:
        email - the new email

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                other_user.get_user_id(), "email", email
            )
        else:
            print("Login first")
            return False

    def update_competency(self, old_val, new_val):
        """
        Updates competency's name

        Parameter:
        old_val - the initial name
        new_val - the new name

        """
        return self.database.update_competency(old_val, new_val)

    def update_assessment(self, old_val, new_val):
        """
        Updates assessment's name

        Parameter:
        old_val - the initial name
        new_val - the new name

        """
        return self.database.update_assessment(old_val, new_val)

    def update_assessment_result(self, assessment_name, firstname, lastname, new_val):
        """
        Updates assessment result's score

        Parameter:
        assessment_name - the assessment's name
        firstname - the user's firstname
        lastname - the user's lastname
        new_val - the new score

        """
        return self.database.update_assessment_result(
            assessment_name, firstname, lastname, new_val
        )

    def delete_assessment_result(self, assessment_name, firstname, lastname):
        """
        removes assessment result's score

        Parameter:
        assessment_name - the assessment's name
        firstname - the user's firstname
        lastname - the user's lastname

        """
        return self.database.delete_assessment_result(
            assessment_name, firstname, lastname
        )

    def update_other_user_phone(self, other_user, email):
        """
        updates the user's email to the supplied email

        Parameters:
        email - the new email

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                other_user.get_user_id(), "phone", email
            )
        else:
            print("Login first")
            return False

    def update_user_firstname(self, name):
        """
        updates the user's first name to the supplied name

        Parameters:
        name - the new first name

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                self.user.get_user_id(), "first_name", name
            )
            self.user = self.database.get_user(
                self.user.get_email(), self.user.get_password()
            )
            return result
        else:
            print("Login first")
            return False

    def update_other_user_firstname(self, other_user, name):
        """
        updates the user's first name to the supplied name

        Parameters:
        name - the new first name

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                other_user.get_user_id(), "first_name", name
            )
            return result
        else:
            print("Login first")
            return False

    def update_user_lastname(self, name):
        """
        updates the user's last name to the supplied email

        Parameters:
        name - the new last name

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                self.user.get_user_id(), "last_name", name
            )
            self.user = self.database.get_user(
                self.user.get_email(), self.user.get_password()
            )
            return result
        else:
            print("Login first")
            return False

    def update_other_user_lastname(self, other_user, name):
        """
        updates the user's last name to the supplied name

        Parameters:
        other_user - the user to change their name
        name - the new last name

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                other_user.get_user_id(), "last_name", name
            )
            return result
        else:
            print("Login first")
            return False

    def update_user_password(self, password):
        """
        updates the user's password to the supplied password

        Parameters:
        password - the new password

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                self.user.get_user_id(), "password", hash_val(password)
            )
            self.user = self.database.get_user(
                self.user.get_email(), hash_val(password)
            )
            return result
        else:
            print("Login first")
            return False

    def update_other_user_password(self, other_user, password):
        """
        updates the user's password to the supplied password

        Parameters:
        password - the new password

        Returns
        returns a boolean value to show if the update was successfull

        """
        if self.is_logged_in():
            result = self.database.update_user_info(
                other_user.get_user_id(), "password", hash_val(password)
            )
            return result
        else:
            print("Login first")
            return False

    def get_user_competency_summary_by_name(self, first_name, last_name):
        """
        fetches the user's competency sumary results

        Parameters:
        first_name - the user's name
        last_name - the user's last name

        """
        competency_data = []
        users = self.search_user_with_both_names(first_name, last_name)
        for single_user in users:
            single_data = []
            single_data.append(
                single_user.get_first_name() + " " + single_user.get_last_name()
            )
            single_data.append(single_user.get_email())
            assessments = self.database.get_assessments_by_id(single_user.get_user_id())
            single_data.append(assessments)
            single_data.append(self.database.get_competency_num())
            competency_data.append(competency_summary(single_data))
        return competency_data

    def get_user_competency_summary_by_id(self, id):
        """
        fetches the user's competency sumary results based on a user's id

        Parameters:
        id - the user's id

        """
        competency_data = []
        users = self.search_user_by_id(id)
        for single_user in users:
            single_data = []
            single_data.append(
                single_user.get_first_name() + " " + single_user.get_last_name()
            )
            single_data.append(single_user.get_email())
            assessments = self.database.get_assessments_by_id(single_user.get_user_id())
            single_data.append(assessments)
            single_data.append(self.database.get_competency_num())
            competency_data.append(competency_summary(single_data))
        return competency_data

    def get_competency_summary_for_all_users(self):
        """
        fetches the all the users competency sumary results

        """
        competency_data = []
        users = self.get_all_users()
        for single_user in users:
            single_data = []
            single_data.append(
                single_user.get_first_name() + " " + single_user.get_last_name()
            )
            single_data.append(single_user.get_email())
            assessments = self.database.get_assessments_by_id(single_user.get_user_id())
            single_data.append(assessments)
            single_data.append(self.database.get_competency_num())
            competency_data.append(competency_summary(single_data))
        return competency_data

    def get_all_user_report_for_single_competency(self, name):
        """
        fetches all the users competency sumary results for one competency item

        Parameters:
        name - name of the competency item

        """
        result = []
        users = self.get_all_users()
        for single_user in users:
            total = self.database.get_all_user_report_for_single_competency(
                name, single_user.get_user_id()
            )
            result.append(
                [
                    single_user.get_first_name() + " " + single_user.get_last_name(),
                    total,
                ]
            )
        return result

    def get_single_user_report_for_single_competency(self, username, competencyname):
        """
        fetches a user's competency sumary results for a sinle competency item

        Parameters:
        username - the user's name
        competencyname - the name of the competency item

        """
        result = []
        users = self.search_user(username)
        for single_user in users:
            total = self.database.get_all_user_report_for_single_competency(
                competencyname, single_user.get_user_id()
            )
            result.append(
                [
                    single_user.get_first_name() + " " + single_user.get_last_name(),
                    total,
                ]
            )
        return result

    def get_assessments_for_single_user(self, username):
        """
        fetches the user's assessment

        Parameters:
        username - the user's name

        """
        result = []
        users = self.search_user(username)
        for single_user in users:
            received = self.database.get_assessments_for_single_user(
                single_user.get_user_id()
            )
            for data in received:
                result.append(
                    [
                        data[0],
                        data[1],
                    ]
                )
        return result

    def create_assessment_results(self, arr):
        return self.database.create_assessment_results(arr)

    def close(self):
        self.database.close()
