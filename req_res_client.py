import requests
from operator import itemgetter


class ReqResClient:
    BASE_URL = "https://reqres.in/"

    def __init__(self, endpoint="", response="", response_code="",
                 response_body="", total_users="", response_headers=""):
        self.endpoint = endpoint
        self.response = response
        self.response_code = response_code
        self.response_headers = response_headers
        # response_body
        self.response_body = response_body
        self.total_users = total_users

    # Getters
    def get_endpoint(self):
        return self.endpoint

    def get_response(self):
        return self.response

    def get_response_code(self):
        return self.response_code

    def get_json_response(self):
        return self.response_body

    def get_response_headers(self):
        return self.response_headers

    def get_response_body(self):
        return self.response_body

    # Setters
    def set_response(self, response):
        self.response = response

    def set_response_code(self, response_code):
        self.response_code = response_code

    def set_json_response(self, json_response):
        self.response_body = json_response

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    # Class Methods
    def get_user(self, user_id):
        """
        :param user_id: int
        :return: Dictionary with single user data
        """
        self.set_endpoint("api/users/{}".format(user_id))
        self.response = requests.get(self.BASE_URL
                                     + self.endpoint)
        self.response_body = self.response.json()
        self.response_code = self.response.status_code

        return self.response_body

    def get_users_list(self, page, per_page):
        """
        :param page: int
        :param per_page: int
        :return: Returns a list with user dictionaries.
        """
        self.set_endpoint("api/users?page={}&per_page={}".format(page, per_page))
        self.response = requests.get(self.BASE_URL + self.endpoint)
        self.response_body = self.response.json()
        self.set_response_code(self.response.status_code)
        self.response_headers = self.response.headers
        self.response_body = self.response.json()

        return self.response_body

    def get_total_users_count(self):
        """
        :return: Return the total users count as int based on server response.
        """
        self.set_endpoint("api/users?page=1&per_page=1")
        self.response = requests.get(self.BASE_URL + self.endpoint)
        self.response_body = self.response.json()

        return self.response_body.get("total")

    def extract_all_users_list(self, key, prnt=""):
        """
        :param key: str
        :param prnt: bool
        :return: Return a list with all users sorted by key. If additional argument prnt is passed, print the list
        """
        self.total_users = self.get_total_users_count()
        self.response = requests.get(self.BASE_URL + self.endpoint)
        self.response_body = self.response.json()
        self.set_response_code(self.response.status_code)
        self.response_headers = self.response.headers

        user_list = (self.get_users_list(1, self.total_users))["data"]

        sorted_user_list = sorted(user_list, key=itemgetter(key))

        if prnt:
            for user in sorted_user_list:
                self.print_user_details(user)
                print()

        return sorted_user_list

    @staticmethod
    def print_user_details(user_dict, *args):
        """
        :param user_dict: dict
        :param args: str
        :return: Prints partial user details based on arguments. Prints all user details if not arguments are given.
        """
        user_details = []

        for key in args:
            if key in user_dict.keys():
                print(key, ":", user_dict[key])

        if len(args) == 0:
            user_details = [print(key, ':', value) for key, value in user_dict.items()]

        return user_details

    def create_user(self, username="", email="", password=""):
        """
        :param username: str
        :param email: str
        :param password: str
        :return: Create a new user.
        """
        self.set_endpoint("api/users")

        payload = {"username": username, "email": email, "password": password}
        self.response = requests.post(self.BASE_URL + self.endpoint,
                                      json=payload)
        self.set_response_code(self.response.status_code)
        self.set_response_code(self.response.status_code)
        self.response_headers = self.response.headers
        self.response_body = self.response.json()

    def delete_user(self, user_id):
        """
        :param user_id: int
        :return: Deletes a user with the given id.
        """
        self.set_endpoint("api/users/{}".format(user_id))
        self.response = requests.delete(self.BASE_URL + self.endpoint)
        self.set_response_code(self.response.status_code)


