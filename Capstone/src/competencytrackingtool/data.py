import sqlite3 as db
import datetime
from competencytrackingtool.assessment import assessment

from competencytrackingtool.user import user
from competencytrackingtool.utils import hash_val


class data:
    def __init__(self):
        """
        Establishes a connection to the database

        """
        try:
            self.connection = db.connect(
                "competency_tracking_tool_db",
                detect_types=db.PARSE_DECLTYPES | db.PARSE_COLNAMES,
            )
            self.create_tables()
            self.create_test_users()
            self.create_test_competencies()
            self.create_test_competency_scale()
            self.competency_num = self.evaluate_competency_num()
        except db.Error as error:
            print("Error (data.__init__): ", error)

    def close(self):
        """
        closes the database connection

        """
        if self.connection:
            self.connection.close()

    def evaluate_competency_num(self):
        """
        fetches the number of rows in the competency table

        """
        try:
            result = self.execute("SELECT COUNT(id) FROM competencies")
            if result:
                return result[0]
            else:
                return 0
        except db.Error as error:
            print("Error (data.get_user): ", error)
        return 0

    def execute(self, query):
        """
        Executes queries that need a value returned

        Parameters:
        query - the sql query to run

        Returns:
        returns the results from the query

        """
        try:
            cursor = self.connection.execute(query)
            result = cursor.fetchall()
            cursor.connection.commit()
            return result
        except db.Error as error:
            print("Error (data.execute): ", error)

        return None

    def create_tables(self):
        """
        Creates the tables required to run the application

        """
        # User table
        try:
            self.connection.execute("DROP TABLE IF EXISTS `user`")
            self.connection.execute("DROP TABLE IF EXISTS `competencies`")
            self.connection.execute("DROP TABLE IF EXISTS `competency_scale`")
            self.connection.execute("DROP TABLE IF EXISTS `assessment_data`")
            self.connection.execute("DROP TABLE IF EXISTS `assessment_result`")
            self.connection.execute(
                """CREATE TABLE `user`(
                `id` TEXT NOT NULL,
                `first_name` VARCHAR(25) NOT NULL,
                `last_name` VARCHAR(25) NOT NULL,
                `phone` VARCHAR(13) NOT NULL,
                `email` VARCHAR(255) NOT NULL,
                `password` VARCHAR(500) NOT NULL,
                `active` VARCHAR(5) NOT NULL,
                `date_created` TIMESTAMP NOT NULL,
                `hire_date` TIMESTAMP NOT NULL,
                `user_type` VARCHAR(8) NOT NULL,
                PRIMARY KEY(`id`)
            )"""
            )
            self.connection.execute(
                """CREATE TABLE `competencies`(
                    `id` TEXT NOT NULL,
                    `name` TEXT NOT NULL,
                    `date_created` TIMESTAMP NOT NULL,
                    PRIMARY KEY(`id`)
                )"""
            )
            self.connection.execute(
                """CREATE TABLE `competency_scale`(
                    `id` TEXT NOT NULL,
                    `scale` VARCHAR(255) NOT NULL,
                    PRIMARY KEY(`id`)
                )"""
            )
            self.connection.execute(
                """CREATE TABLE `assessment_data`(
                    `id` TEXT NOT NULL,
                    `name` TEXT NOT NULL,
                    `date_created` TIMESTAMP NOT NULL,
                    `competency_id` INT NOT NULL,
                    FOREIGN KEY(`competency_id`) REFERENCES competencies(`id`),
                    PRIMARY KEY(id)
                )"""
            )
            self.connection.execute(
                """CREATE TABLE `assessment_result` (
                    `id` TEXT NOT NULL PRIMARY KEY,
                    `user_id` INT NOT NULL,
                    `assessment_id` INT NOT NULL,
                    `score_id` INT NOT NULL,
                    `date_taken` TIMESTAMP NOT NULL,
                    `manager_id` INT NOT NULL,
                    FOREIGN KEY(`user_id`) REFERENCES user(`id`),
                    FOREIGN KEY(`assessment_id`) REFERENCES assessment_data(`id`),
                    FOREIGN KEY(`score_id`) REFERENCES competency_scale(`id`),
                    FOREIGN KEY(`manager_id`) REFERENCES user(`id`)
                )"""
            )
            self.connection.commit()
        except db.Error as error:
            print("Error (data.create_tables): ", error)

    def create_test_users(self):
        """
        Creates test users to help access the application

        """
        try:
            self.create_user(
                [
                    "123",
                    "John",
                    "Doe",
                    "4444444444",
                    "employee",
                    hash_val("test"),
                    "True",
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                    "EMPLOYEE",
                ]
            )
            self.create_user(
                [
                    "789",
                    "Brian",
                    "Lee",
                    "5555555555",
                    "employee_2",
                    hash_val("test"),
                    "True",
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                    "EMPLOYEE",
                ]
            )
            self.create_user(
                [
                    "456",
                    "Jane",
                    "Doe",
                    "6666666666",
                    "manager",
                    hash_val("test"),
                    "True",
                    datetime.datetime.now(),
                    datetime.datetime.now(),
                    "MANAGER",
                ]
            )
        except db.Error as error:
            print("Error (data.create_test_users): ", error)

    def create_test_competencies(self):
        """
        Creates test competencies to help users interact with the application

        """
        try:
            hashed_id = hash_val(
                "Computer Anatomy - Data Types" + str(datetime.datetime.now())
            )
            self.create_competency(
                [
                    hashed_id,
                    "Computer Anatomy - Data Types",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Variables" + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Variables",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Functions" + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Functions",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Boolean Logic"
                        + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Boolean Logic",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Conditionals" + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Conditionals",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val("Computer Anatomy - Loops" + str(datetime.datetime.now())),
                    "Computer Anatomy - Loops",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Data Structures"
                        + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Data Structures",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val("Computer Anatomy - Lists" + str(datetime.datetime.now())),
                    "Computer Anatomy - Lists",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Dictionaries" + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Dictionaries",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Working with Files"
                        + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Working with Files",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Exception Handling"
                        + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Exception Handling",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Quality Assurance (QA)"
                        + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Quality Assurance (QA)",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Object-Oriented Programming"
                        + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Object-Oriented Programming",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Recursion" + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Recursion",
                    datetime.datetime.now(),
                ]
            )
            self.create_competency(
                [
                    hash_val(
                        "Computer Anatomy - Databases" + str(datetime.datetime.now())
                    ),
                    "Computer Anatomy - Databases",
                    datetime.datetime.now(),
                ]
            )
        except db.Error as error:
            print("Error (data.create_test_competencies): ", error)

    def create_competency(self, arr):
        """
        Creates a new competency entry into the database

        Parameters:
        arr - a list of parameters required to make the competency

        """
        try:
            query = "INSERT INTO `competencies` (`id`, `name`, `date_created`) VALUES (?,?,?);"
            self.connection.execute(
                query,
                (arr[0], arr[1], arr[2]),
            )
            self.connection.commit()
            return True
        except db.Error as error:
            print("Error (data.create_competency): ", error)
            return False

    def create_assessment(self, arr):
        """
        Creates a new assessment entry in to the database

        """
        try:
            result = self.execute(
                'SELECT id FROM `competencies` WHERE `name` = "' + arr[-1] + '";'
            )
            if not result:
                print("Competency doesn't exist")
                return False

            competency_id = result[0]
            arr[-1] = competency_id[0]
            self.add_assessment_data(arr)
            return True
        except db.Error as error:
            print("Error (data.create_assessment): ", error)
            return False

    def create_assessment_result(self, arr):
        """
        Creats a new assessment result entry into the database

        """
        try:
            result = self.search_user(arr[1])
            if not result:
                print("User doesn't exist")
                return False

            user_id = result[0].get_user_id()

            result = self.execute(
                'SELECT id FROM `assessment_data` WHERE `name` = "' + arr[2] + '";'
            )
            if not result:
                print("Assessment doesn't exist")
                return False

            assessment_id = result[0]
            arr[1] = user_id
            arr[2] = assessment_id[0]
            self.add_assessment_result(arr)
            return True
        except db.Error as error:
            print("Error (data.create_competency): ", error)
            return False

    def create_test_competency_scale(self):
        """
        Creates sample competency scale entries into the database

        """
        try:
            self.create_competency_scale([0, "0 - No competency"])
            self.create_competency_scale([1, "1 - Basic Competency"])
            self.create_competency_scale([2, "2 - Intermediate Competency"])
            self.create_competency_scale([3, "3 - Advanced Competency"])
            self.create_competency_scale([4, "4 - Expert Competency"])
        except db.Error as error:
            print("Error (data.create_test_competencies): ", error)

    def create_competency_scale(self, arr):
        """
        Helper function to make it easy to create competency scale entries into the database

        Parameters:
        arr - list of parameters needed to create new competency scale entries

        """
        try:
            query = "INSERT INTO `competency_scale` (`id`, `scale`) VALUES (?,?);"
            self.connection.execute(
                query,
                (arr[0], arr[1]),
            )
            self.connection.commit()
            return True
        except db.Error as error:
            print("Error (data.create_competency): ", error)
            return False

    def add_assessment_data(self, arr):
        """
        Adds assessment data into the database

        """
        try:
            query = "INSERT INTO `assessment_data` (`id`,`name`,`date_created`,`competency_id`) VALUES (?,?,?,?);"
            self.connection.execute(
                query,
                (arr[0], arr[1], arr[2], arr[3]),
            )
            self.connection.commit()
            return True
        except db.Error as error:
            print("Error (data.create_competency): ", error)
            return False

    def add_assessment_result(self, arr):
        """
        Adds assessment results into the database

        Parameters:
        arr - list of parameters required to create assessment result entries

        """
        try:
            query = "INSERT INTO `assessment_result` (`id`,`user_id`,`assessment_id`,`score_id`,`date_taken`,`manager_id`) VALUES (?,?,?,?,?,?);"
            self.connection.execute(
                query,
                (arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]),
            )
            self.connection.commit()
            return True
        except db.Error as error:
            print("Error (data.create_competency): ", error)
            return False

    def get_user(self, email, password):
        """
        Fetches a user based on their email and password from the databse

        Parameters:
        email - user's email
        password - user's password

        """
        try:
            result = self.execute(
                'SELECT * FROM user WHERE email = "'
                + email
                + '" AND password = "'
                + password
                + '";'
            )
            if result:
                return user(result[0])
            else:
                return None
        except db.Error as error:
            print("Error (data.get_user): ", error)
        return None

    def get_all_users(self):
        """
        Returns a collection of all users in the database

        """
        users = []
        try:
            result = self.execute("SELECT * FROM `user`")
            if result:
                for val in result:
                    users.append(user(val))
        except db.Error as error:
            print("Error (data.get_all_users): ", error)
        return users

    def search_user(self, name):
        """
        Fetches a user fomr the database with the supplied parameter

        Parameter:
        name - the name of the user to retrieve

        Returns:
        a user object

        """
        users = []
        try:
            result = self.execute(
                'SELECT * FROM `user` WHERE first_name LIKE "%'
                + name
                + '%" OR last_name LIKE "%'
                + name
                + '%"'
            )
            if result:
                for val in result:
                    users.append(user(val))
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return users

    def search_user_by_id(self, id):
        """
        Fetches a user from the database that had the supplied id

        Parameter:
        id - the user's id

        """
        users = []
        try:
            result = self.execute('SELECT * FROM `user` WHERE `id` = "' + id + '"')
            if result:
                for val in result:
                    users.append(user(val))
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return users

    def search_user_with_both_names(self, first_name, last_name):
        """
        Fetches a user with the supplied first_name and last_name

        Paramaters:
        first_name - user's first name
        last_name - user's last name

        """
        users = []
        try:
            result = self.execute(
                'SELECT * FROM `user` WHERE first_name = "'
                + first_name
                + '" AND last_name = "'
                + last_name
                + '"'
            )
            if result:
                for val in result:
                    users.append(user(val))
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return users

    def get_assessments_by_id(self, id):
        """
        fetches an assessment from the databse with the supplied id paramater

        Parameters:
        id - the assessment's id

        Returns:
        the retrieved assessment

        """
        assessments = []
        try:
            result = self.execute(
                'SELECT `assessment_result`.`score_id`, `assessment_data`.`name`, `competencies`.`name`  from `assessment_result` INNER JOIN `assessment_data` ON `assessment_result`.`assessment_id` = `assessment_data`.`id` INNER JOIN `competencies` ON `assessment_data`.`competency_id` = `competencies`.`id` WHERE `assessment_result`.`user_id` = "'
                + str(id)
                + '"'
            )
            if result:
                for val in result:
                    assessments.append(assessment(val))
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return assessments

    def create_user(self, arr):
        """
        Creates a new user entry in the database

        """
        try:
            result = self.execute('SELECT id FROM user WHERE email = "' + arr[4] + '";')
            if result:
                print("Username already exists")
                return False

            query = "INSERT INTO `user` (`id`,`first_name`,`last_name`,`phone`,`email`,`password`,`active`,`date_created`,`hire_date`,`user_type`) VALUES (?,?,?,?,?,?,?,?,?,?);"
            self.connection.execute(
                query,
                (
                    arr[0],
                    arr[1],
                    arr[2],
                    arr[3],
                    arr[4],
                    arr[5],
                    arr[6],
                    arr[7],
                    arr[8],
                    arr[9],
                ),
            )
            self.connection.commit()
            return True
        except db.Error as error:
            print("Error (data.create_user): ", error)
            return False

    def update_user_info(self, id, column, value):
        """
        Updates the user's information

        Parameters:
        id - the user's id
        column - the table column to update
        value - the new value

        """
        try:
            self.connection.execute(
                "UPDATE `user` SET `"
                + column
                + '` = "'
                + value
                + '" WHERE id = "'
                + str(id)
                + '"'
            )
            self.connection.commit()
            return True
        except db.Error as error:
            print("Error (data.update_user_info): ", error)
        return False

    def get_all_user_report_for_single_competency(self, name, user_id):
        """
        Fetches all the user reports for a single competency

        Parameters:
        name - the competency's name
        user_id - the user's id

        """
        result = 0
        try:
            info = self.execute(
                'SELECT `assessment_result`.`score_id` FROM `assessment_result` INNER JOIN `assessment_data` ON `assessment_data`.`id` = `assessment_result`.`assessment_id` INNER JOIN `competencies` ON `competencies`.`id` = `assessment_data`.`competency_id` WHERE `assessment_result`.`user_id` = "'
                + str(user_id)
                + '" AND `competencies`.`name` = "'
                + name
                + '"'
            )
            if info:
                for val in info:
                    result = result + val
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return result

    def get_assessments_for_single_user(self, user_id):
        """
        Fetches the assessment results for a single user

        Paramets:
        user_id - the user's id

        Returns the assessment object

        """
        try:
            info = self.execute(
                'SELECT `assessment_data`.`name`, `assessment_result`.`score_id` FROM `assessment_result` INNER JOIN `assessment_data` ON `assessment_data`.`id` = `assessment_result`.`assessment_id` WHERE `assessment_result`.`user_id` = "'
                + str(user_id)
                + '"'
            )
            if info:
                return info
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return []

    def get_competency_num(self):
        """
        fetches the number of competency entries in the table

        Returns:
        the number of competency entries

        """
        return self.competency_num[0]

    def update_competency(self, old_val, new_val):
        """
        Updates competency's name

        Parameter:
        old_val - the initial name
        new_val - the new name

        """
        try:
            id = self.execute(
                'SELECT `id` FROM `competencies` WHERE `name` = "' + old_val + '"'
            )
            if not id:
                return False

            info = self.execute(
                'UPDATE `competencies` SET `name` = "'
                + new_val
                + '" WHERE id = "'
                + str(id)
                + '"'
            )
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return True

    def update_assessment(self, old_val, new_val):
        """
        Updates assessment's name

        Parameter:
        old_val - the initial name
        new_val - the new name

        """
        try:
            id = self.execute(
                'SELECT `id` FROM `assessment_data` WHERE `name` = "' + old_val + '"'
            )
            if not id:
                return False

            info = self.execute(
                'UPDATE `assessment_data` SET `name` = "'
                + new_val
                + '" WHERE id = "'
                + str(id)
                + '"'
            )
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return True

    def update_assessment_result(self, assessment_name, firstname, lastname, new_val):
        """
        Updates assessment's name

        Parameter:
        old_val - the initial name
        new_val - the new name

        """
        try:
            searched_user = self.search_user_with_both_names(firstname, lastname)
            if not searched_user:
                return False

            user_id = searched_user[0].get_user_id()
            id = self.execute(
                'SELECT `assessment_result`.`id` FROM `assessment_result` INNER JOIN `assessment_data` ON `assessment_data`.`id` = `assessment_result`.`assessment_id` WHERE `assessment_result`.`user_id` = "'
                + str(user_id)
                + '" AND `assessment_data`.`name` = "'
                + assessment_name
                + '"'
            )
            if not id:
                return False

            info = self.execute(
                "UPDATE `assessment_result` SET `score_id` = "
                + new_val
                + ' WHERE id = "'
                + str(id)
                + '"'
            )
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return True

    def delete_assessment_result(self, assessment_name, firstname, lastname):
        """
        Updates assessment's name

        Parameter:
        old_val - the initial name
        new_val - the new name

        """
        try:
            searched_user = self.search_user_with_both_names(firstname, lastname)
            if not searched_user:
                return False

            user_id = searched_user[0].get_user_id()
            id = self.execute(
                'SELECT `assessment_result`.`id` FROM `assessment_result` INNER JOIN `assessment_data` ON `assessment_data`.`id` = `assessment_result`.`assessment_id` WHERE `assessment_result`.`user_id` = "'
                + str(user_id)
                + '" AND `assessment_data`.`name` = "'
                + assessment_name
                + '"'
            )
            if not id:
                return False

            info = self.execute(
                'DELETE FROM `assessment_result` WHERE id = "' + str(id) + '"'
            )
        except db.Error as error:
            print("Error (data.search_user): ", error)
        return True

    def create_assessment_results(self, arr):
        """
        Creates a new assessment results entry in the database

        """
        try:
            query = "INSERT INTO `assessment_result` (`id`, `user_id`, `assessment_id`, `score_id`, `date_taken`, `manager_id`) VALUES (?,?,?,?,?,?);"
            self.connection.execute(
                query,
                (
                    arr[0],
                    arr[1],
                    arr[2],
                    arr[3],
                    arr[4],
                    arr[5],
                ),
            )
            self.connection.commit()
            return True
        except db.Error as error:
            print("Error (data.create_user): ", error)
            return False
