Data to API mobile app

this app allows users to submit their personal info(data) to an API endpoint 

TABLE OF CONTENTS:

-Usage
-Dependencies
-File Structure
-API Integration



USAGE

Run the application
python main.py

USAGE INSTRUCTIONS

Enter the required details (Date, Hour, Minute, Name, Surname, Sex) in the respective input fields.
Click on the "Submit" button to send data to the API.
Dialog boxes will appear indicating success or failure of the data submission.

DEPENDENCIES

List of dependencies required to run the application:

Python 3.x
Kivy 2.x
KivyMD 1.x
requests

FILE STRUCTURE

MainApp/
│
├── main.py           # Main application script
├── api.py            # Module for API interaction
└── README.md         # This file

API IINTEGRATION

The application interacts with the following API:

Endpoint: http://bazihero.com/api/algo/firststep
Payload: Data sent includes date, hour, minute, name, surname, and sex.
Error Handling: Handles HTTP errors and validates JSON responses.



