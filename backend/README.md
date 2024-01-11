# Message API

This project is a Message API created with Python and Django.

## Instructions to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/ppm3/bytes_code_challenge
    ```

2. Navigate to the project directory:

    ```bash
    cd backend
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

5. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver <PORT>
    ```

8. The API will be accessible at `http://localhost:<PORT>/`.

## Instructions to Testing

1. Activate the virtual environment (if not already activated):

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

2. Run the tests:

    ```bash
    python manage.py test
    ```

    This will run all the tests and display the results.

3. API Endpoints

    Below are the available API endpoints in the application:

    - `/health-check`  
    **View**: `messagesAPI.views.health_check`  
    **Name**: `health_check`  
    **Methods**: `GET`

    - `/messages/`  
    **View**: `messagesAPI.views.message_list`  
    **Name**: `message_list`  
    **Methods**: `GET, POST`

    - `/messages/<message_id>/`  
    **View**: `messagesAPI.views.message_detail`  
    **Name**: `message_detail`  
    **Methods**: `GET, PUT, DELETE`

    - `/ping`  
    **View**: `messagesAPI.views.ping`  
    **Name**: `ping`  
    **Methods**: `GET`


4. Documentation for QA

    This line of code is responsible for initializing the [postma_collection](documentation/postman/cc.postman_collection.json) and [environments](documentation/postman/Byte-CC.postman_environment.json) variables.

    - `postma_collection`: This variable represents the Postman collection that will be used for testing and documenting the API endpoints.

    - `environments`: This variable represents the different environments for testing purpuse.

    It is important to ensure that the `postma_collection` and `environments` variables are properly configured before running the API.
