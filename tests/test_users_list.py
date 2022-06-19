from helper_functions.schemas_functions import *
from req_res_client import *

req_res_api = ReqResClient()


# List available users
# GET /api/users?page=1
# Execute one or many JSON Response Assertions
# (Optional) Extract all users, sort them by First Name alphabetically. Print sorted collection.
def test_get_list_users():
    req_res_api.get_users_list(1, 12)
    response_body = req_res_api.get_response_body()

    assert req_res_api.get_response_code() == 200
    assert req_res_api.get_response_headers()["content-type"] == "application/json; charset=utf-8"
    assert req_res_api.get_json_response()["per_page"] == 12
    assert req_res_api.get_json_response()["page"] == 1
    assert_valid_schema(response_body, "../resources/user_list.json")
#
# def test_print_all_users_by_first_name():
#     endpoint = BASE_URL + "/api/users?page=1"
#     total_users = get_total_users_count(endpoint)
#
#     extract_all_users_list(BASE_URL, total_users, "first_name", prnt=True)


# Extract single user details (Id, Email)
# Get extracted user details
# GET /api/users/{USER_ID}
# Execute one or many JSON Response Assertions
def test_extract_single_user_details():
    single_user_details = req_res_api.get_user(1)
    assert_valid_schema(single_user_details, "../resources/user.json")


#     # Try to get details of user that doesn't exist
#     # GET /api/users/{USER_ID}
#     # Execute one or many Assertions
def test_fetch_invalid_user():
    req_res_api.get_user(-1)

    assert req_res_api.response_code == 404
    assert req_res_api.response_body == {}


#     # Create UNIQUE new user
#     # POST /api/users
#     # Execute one or many JSON Response Assertions
def test_create_user():
    req_res_api.create_user(username="aavdzhiev",
                            email="anastas.avdzhiev@gmail.com",
                            password="pass123")

    assert req_res_api.get_response_code() == 201

    assert_valid_schema(req_res_api.get_response_body(), "../resources/created_user.json")


#     # Delete newly created user
#     # DELETE /api/users/{USER_ID}
#     # Execute one or many Assertions
def test_delete_user():
    req_res_api.delete_user(256)

    assert req_res_api.get_response_code() == 204
