from competencytrackingtool.app import app
import hashlib


def test_db_connection():
    print("\nTESTING DB CONNECTION")
    info = app()
    if info.is_logged_in():
        print("Already logged")
    else:
        info.login("employee", "test")
    info.close()


def test_login_with_invalid_credentials():
    print("\nTESTING LOGIN WITH INVALID CREDENTIALS")
    info = app()
    if info.is_logged_in():
        print("Already logged")
    else:
        info.login("employee", "testy")
    info.close()


def test_login():
    print("\nTESTING LOGIN")
    info = app()
    if info.is_logged_in():
        print("Already logged in")
    else:
        info.login("employee", "test")
    print(info.is_logged_in())
    info.logout()
    print(info.is_logged_in())
    info.close()


def test_employee_creating_new_user():
    print("\nTESTING EMPLOYEE CREATING NEW USER")
    info = app()
    if info.is_logged_in():
        print("Already logged in")
    else:
        info.login("employee", "test")
    print(
        info.create_user(
            [
                789,
                "Userfirst",
                "Userlast",
                "+254712345678",
                "employee",
                "test",
                "True",
                "123456789",
                "123456789",
                "EMPLOYEE",
            ]
        )
    )
    info.close()


def test_manager_creating_new_user():
    print("\nTESTING MANAGER CREATING NEW USER")
    info = app()
    if info.is_logged_in():
        print("Already logged in")
    else:
        info.login("manager", "test")
    print(
        info.create_user(
            [
                789,
                "Userfirst",
                "Userlast",
                "+254712345678",
                "employee2",
                "test",
                "True",
                "123456789",
                "123456789",
                "EMPLOYEE",
            ]
        )
    )
    info.close()


def test_create_user_with_existing_username():
    print("\nTESTING CREATING NEW USER WITH EXISTING USERNAME")
    info = app()
    if info.is_logged_in():
        print("Already logged in")
    else:
        info.login("manager", "test")
    print(
        info.create_user(
            [
                654,
                "Userfirst",
                "Userlast",
                "+254712345678",
                "employee",
                "test",
                "True",
                "123456789",
                "123456789",
                "EMPLOYEE",
            ]
        )
    )
    info.close()


def test_loggedout_user_creating_new_user():
    print("\nTESTING LOGGEDOUT USER CREATING NEW USER")
    info = app()
    if info.is_logged_in():
        info.logout()
    print(
        info.create_user(
            [
                789,
                "Userfirst",
                "Userlast",
                "+254712345678",
                "employee",
                "test",
                "True",
                "123456789",
                "123456789",
                "EMPLOYEE",
            ]
        )
    )
    info.close()


def test_change_email():
    print("\nTESTING CHANGING EMAIL")
    info = app()
    info.login("employee", "test")
    print("Email before: " + info.get_user().get_email())
    info.update_user_email("employee_updated")
    print("Email after: " + info.get_user().get_email())
    info.close()


def test_change_firstname():
    print("\nTESTING CHANGING FIRSTNAME")
    info = app()
    info.login("employee", "test")
    print("Firstname before: " + info.get_user().get_first_name())
    info.update_user_firstname("firstname_changed")
    print("Firstname after: " + info.get_user().get_first_name())
    info.close()


def test_change_lastname():
    print("\nTESTING CHANGING LASTNAME")
    info = app()
    info.login("employee", "test")
    print("Lastname before: " + info.get_user().get_last_name())
    info.update_user_lastname("lastname_changed")
    print("Lastname after: " + info.get_user().get_last_name())
    info.close()


def test_change_password():
    print("\nTESTING CHANGING PASSWORD")
    info = app()
    info.login("employee", "test")
    print("Password before: " + info.get_user().get_password())
    info.update_user_password("password_changed")
    print("Password after: " + info.get_user().get_password())
    info.close()


def __main__():
    test_db_connection()
    test_login_with_invalid_credentials()
    test_login()
    test_employee_creating_new_user()
    test_loggedout_user_creating_new_user()
    test_manager_creating_new_user()
    test_create_user_with_existing_username()
    test_change_email()
    test_change_firstname()
    test_change_lastname()
    test_change_password()


__main__()
