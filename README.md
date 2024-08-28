The application has four routes:

/: A simple route that returns "Hello World!".
/sheela: A route that returns a string with a stored age value.
/sheela/<age> (GET): A route that returns a string with a stored age value.
/sheela/<age> (POST): A route that allows you to update the stored age value via a POST request.
Getting Started
Prerequisites
To run this application, you need to have Python installed on your system. You can download Python from python.org.

You also need to install Flask, which is a Python web framework. You can install Flask using pip:

bash
Copy code
pip install flask
Running the Application
Clone the repository or copy the code into a new file named app.py.

Open a terminal (or command prompt) and navigate to the directory where app.py is located.

Run the Flask application by executing:

bash
Copy code
python app.py
The application will start running on http://127.0.0.1:5000/.

Usage
Access the default route: Open a web browser and navigate to http://127.0.0.1:5000/ to see "Hello World!".
Check Sheela's age: Go to http://127.0.0.1:5000/sheela to see a message with the stored age.
Update Sheela's age: Use a tool like curl, Postman, or any HTTP client to send a POST request to http://127.0.0.1:5000/sheela/<age> with the new age value.
Example POST request using curl:
bash
Copy code
curl -X POST http://127.0.0.1:5000/sheela/30
After sending this request, the stored age will be updated to 30.

Notes
This application is intended for educational purposes to demonstrate basic Flask routing and handling HTTP methods.
The application uses a global variable to store the age, which is not suitable for production use. For a real-world application, consider using a database to persist data.
