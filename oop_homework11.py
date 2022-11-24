import json


class User:

    def __init__(self, username, password, email=None, age=None, phone=None, *args, **kwargs):
        self.uname = username
        self.pw = password
        self.email = email
        self.age = age
        self.phone = phone
        self.data = {"username": self.uname,
                     "password": self.pw,
                     "email": self.email,
                     "age": self.age,
                     "phone": self.phone}

        with open("user_information.json", "a") as data_json_file:
            json.dump(self.data, data_json_file)


class PyRequest(User):

    def __init__(self, authorization=None, body=None, user=None, *args, **kwargs):
        self.headers = []
        self.authorization = authorization
        self.body = body
        self.user = user
        super().__init__(*args, **kwargs)

    def local_login(self):
        with open("user_information.json", "r") as file:
            file = json.load(file)

            for user_info in file:
                if user_info["username"] == self.uname and user_info["password"] == self.pw:

                    return True

    def login_required(self, func):
        def decor():
            if self.local_login() is True:
                func()
            else:
                raise "401 unauthorised request error"

        return decor

    @login_required
    def get_user_info(self):
        with open("user_information.json", "r") as file:
            file = json.load(file)

            for user_info in file:
                if user_info["username"] == self.uname and user_info["password"] == self.pw:
                    print(user_info)


user_1 = User(username="qwerty", password="12345678", email="qwerty123@gmailcom", age="29", phone="09603828294")
user_2 = User(username="asdfg", password="56781234", email="asdfg123@gmailcom", age="27", phone="09654654294")
user_3 = PyRequest(username="johndon", password="1234")
user_4 = PyRequest(username="qwerty", password="12345678")
user_3.get_user_info()
user_4.get_user_info()








