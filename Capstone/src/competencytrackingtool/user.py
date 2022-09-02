class user:
    def __init__(self, arr):
        self.user_id = arr[0]
        self.first_name = arr[1]
        self.last_name = arr[2]
        self.phone = arr[3]
        self.email = arr[4]
        self.password = arr[5]
        self.acive_status = arr[6]
        self.date_created = arr[7]
        self.hire_date = arr[8]
        self.user_type = arr[9]

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_active(self):
        return self.acive_status

    def get_date_created(self):
        return self.date_created

    def get_hire_date(self):
        return self.hire_date

    def get_user_type(self):
        return self.user_type

    def get_user_id(self):
        return self.user_id
