import requests
from config import BASE_URL
from utils.logger import get_logger

logger = get_logger()


class BaseAPI:

    def get(self, endpoint):
        logger.info(f"GET request to {endpoint}")

        response = requests.get(BASE_URL + endpoint)

        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Body: {response.text}")

        return response

    def post(self, endpoint, payload):
        logger.info(f"POST request to {endpoint}")
        logger.info(f"Payload: {payload}")

        response = requests.post(BASE_URL + endpoint, json=payload)

        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Body: {response.text}")

        return response

    def put(self, endpoint, payload):
        logger.info(f"PUT request to {endpoint}")
        logger.info(f"Payload: {payload}")

        response = requests.put(BASE_URL + endpoint, json=payload)

        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Body: {response.text}")

        return response

    def delete(self, endpoint):
        logger.info(f"DELETE request to {endpoint}")

        response = requests.delete(BASE_URL + endpoint)

        logger.info(f"Response Status: {response.status_code}")
        logger.info(f"Response Body: {response.text}")

        return response