import requests  # Used to make HTTP requests, allowing interaction with web APIs or fetching web content.
import pytest  # Testing framework for writing and running unit tests


# Define the API endpoint URL
API_URL = 'https://o3u6mzl4yg.execute-api.us-east-1.amazonaws.com/visitorCounter'

def test_visitor_counter_system():
    """
    System test for the Visitor Counter API.

    This test performs the following actions:
    1. Makes a GET request to the visitor counter API to retrieve the initial visitor count.
    2. Validates that the response status code is 200 (OK).
    3. Ensures that the response body contains a valid integer representing the visitor count.
    4. Verifies that the response includes the correct CORS header (`Access-Control-Allow-Origin` set to '*').
    5. Makes a second GET request to increment the visitor count.
    6. Validates that the status code of the second response is also 200.
    7. Ensures that the visitor count has incremented by 1 compared to the initial value.
    8. Prints the initial and updated visitor count for debugging purposes.

    Assertions:
    - The API responds with a status code of 200 on both requests.
    - The visitor count is a valid integer.
    - The CORS header is correctly set to allow cross-origin requests.
    - The visitor count increments by exactly 1 after the second request.

    Raises:
    - ValueError: If the visitor count in the response cannot be converted to an integer.
    - AssertionError: If the status code is not 200, the CORS header is missing/incorrect, or the visitor count does not increment by 1 as expected.

    To run this test, use pytest:
    - pytest -vs
    - pytest -vs test_visitor_counter_system.py
    """
    
    # Make the first request to get the initial visitor count
    print("\nMaking the first request to get the initial visitor count")
    response = requests.get(API_URL)
    
    # Check the response status code
    print(f"Checking if the response status code is 200. Status code received: {response.status_code}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Check if the response contains a valid integer for visitor count
    initial_count_text = response.text.strip()
    print(f"Checking if the response contains a valid visitor count. Retrieved: {initial_count_text}")
    assert initial_count_text.isdigit(), f"Visitor count is missing or not a valid integer. Response body: '{response.text}'"
    
    initial_count = int(initial_count_text)
    print(f"Initial visitor count retrieved: {initial_count}")

    # Verify the CORS header (Access-Control-Allow-Origin)
    cors_header = response.headers.get('Access-Control-Allow-Origin')
    print(f"Verifying the CORS header. CORS header value: {cors_header}")
    assert cors_header == '*', "CORS header is missing or incorrect"
    
    # Make the second request to increment the visitor count
    print("Making the second request to increment the visitor count")
    response = requests.get(API_URL)
    
    # Check the status code again
    print(f"Checking if the response status code is 200 again. Status code received: {response.status_code}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Ensure the visitor count has incremented by 1
    updated_count = int(response.text.strip())
    print(f"Updated visitor count retrieved: {updated_count}")
    assert updated_count == initial_count + 1, f"Expected visitor count {initial_count + 1}, but got {updated_count}"
    
    # Print success message for debugging purposes
    print(f"Test passed: Visitor count incremented from {initial_count} to {updated_count}")