import pytest
import allure
from base_api import BaseAPI
from data.user_data import CREATE_USER, UPDATE_USER
from utils.logger import get_logger

logger = get_logger()


@pytest.fixture
def api():
    return BaseAPI()


@allure.title("Verify GET all users API")
@allure.description("Validate that all users are fetched successfully")
def test_get_all_users_success(api):
    logger.info("Starting test: GET all users")

    response = api.get("/users")
    data = response.json()

    logger.info(f"Users count: {len(data)}")

    assert response.status_code == 200, "get users failed"
    assert len(data) >= 2
    assert isinstance(data, list)


@allure.title("Verify CREATE user API")
@allure.description("Validate that a new user is created successfully")
def test_create_user(api):
    logger.info("Starting test: CREATE user")

    response = api.post("/users", CREATE_USER)
    data = response.json()

    logger.info(f"Created user: {data}")

    assert response.status_code == 200, "Create new user failed"
    assert data["name"] == CREATE_USER["name"]
    assert data["job"] == CREATE_USER["job"]
    assert "id" in data


@allure.title("Verify UPDATE user API")
@allure.description("Validate that an existing user is updated successfully")
def test_update_user(api):
    logger.info("Starting test: UPDATE user")

    create_user_response = api.post("/users", CREATE_USER)
    new_user = create_user_response.json()
    user_id = new_user["id"]

    logger.info(f"User created with ID: {user_id}")

    assert create_user_response.status_code == 200, "create new user failed"
    assert "id" in new_user

    response = api.put(f"/users/{user_id}", UPDATE_USER)
    updated_user = response.json()

    logger.info(f"Updated user: {updated_user}")

    assert response.status_code == 200, "update user failed"
    assert updated_user["name"] == UPDATE_USER["name"]
    assert updated_user["job"] == UPDATE_USER["job"]


@allure.title("Verify DELETE user API")
@allure.description("Validate that a user is deleted successfully")
def test_delete_user(api):
    logger.info("Starting test: DELETE user")

    create_user_response = api.post("/users", CREATE_USER)
    new_user = create_user_response.json()
    user_id = new_user["id"]

    logger.info(f"User created with ID: {user_id}")

    assert create_user_response.status_code == 200
    assert "id" in new_user

    response = api.delete(f"/users/{user_id}")
    data = response.json()

    logger.info(f"Delete response: {data}")

    assert response.status_code == 200, "Delete user failed"
    assert data["message"] == "User deleted"