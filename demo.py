from req_res_client import *


def demo():
    """
    Demo for the ReqResClient class methods
    """
    example_dict = {'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George',
                    'last_name': 'Bluth', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'}

    # Instantiate a new ReqResClient object
    req_res_api = ReqResClient()

    # Returns a dictionary with the data of a single user
    print("\n\nget_user: ", req_res_api.get_user(1))

    # Returns a list with user dictionaries(JSON), based on how many pages and user per pages is provided
    print("\n\nget_users_list: ", req_res_api.get_users_list(1, 2))

    # Prompts the API and gets the total user count, based on server response
    print("\n\nget_total_users_count: ", req_res_api.get_total_users_count())

    # Extracts all users and sorts them by the key provided (ex.by first_name).
    # Prints the result if prnt argument is True
    print("\n\nextract_all_users_list:\n")
    req_res_api.extract_all_users_list("first_name", True)

    # Prints all or partial single user details
    print("\nprint_user_details: \n")
    req_res_api.print_user_details(example_dict, "first_name", "email")

    req_res_api.get_users_list(1, 12)
    print(req_res_api.get_json_response())

    print(req_res_api.extract_all_users_list("first_name"))

    print("\n\ncreate_user:\n")
    req_res_api.create_user(username="aavdzhiev", email="anastas.avdzhiev@gmail.com", password="pass123")
    print(req_res_api.get_response())
    print(req_res_api.get_json_response())
    print(req_res_api.get_response_headers())


    print("\n\ndelete_user:\n")
    req_res_api.delete_user(256)
    print(req_res_api.get_response_code())


if __name__ == "__main__":
    demo()
