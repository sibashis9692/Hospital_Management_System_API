# 1. Project's Title

Hospital_management_system

# 2. Project Description

Hospital Management System is a web-based application built with Django REST framework for managing patient records, doctors, and departments in a hospital.

# 3. How to Install and Run the Project

## Requirements

Make sure you have the following dependencies installed before running the application:

- Python
- Django 4.2.5
- Django REST framework 3.14.0
- djangorestframework-simplejwt 5.3.0
- mysqlclient 2.2.0
- PyJWT 2.8.0

## Installation
1. Create a virtual environment:
```
python -m venv venv
```
2. Activate the virtual environment:
```
venv\Scripts\activate
```
3. Clone the Repository:
```
git clone https://github.com/sibashis9692/Hospital_Management_System_API.git
cd Hospital_Management_System_API
```
4. install dependencies:
```
pip install -r requirements.txt
```
# Database Setup
Before running the application, set up the database as follows:

1. Create a MySQL database for the project.
2. Update the database settings in settings.py:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
3. Run migrate and migrations:
```
python manage.py makemigrations
python manage.py migrate
```
# Running the Application
```
python manage.py runserver
```
The server should now be running at http://localhost:8000

# 5. How to Use the Project

## Authentication

The Medical Records Management Service API utilizes JSON Web Token (JWT) authentication. Follow the steps below to authenticate using JWT:

## 1. User Registration:
To register a new user, make a POST request to the following endpoint:

`POST /register`

Include the following required parameters in the request body:

Role: Role of the user (e.g., "Patient" or "Doctor").

Example Request:
```
POST /register
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "Role": "Doctor",
    "Department_name": "Cardiology",
    "password": "password123"
}
```

Example Response:
```
{
    "Status": "A new Doctor Created Successfully"
}
```

## 2. User Login:

To authenticate a user, make a POST request to the following endpoint:

`POST /login`

Include the following required parameters in the request body:

email: Email address of the user.
password: User's password.

Example Request:
```
POST /login
{
    "email": "john.doe@example.com",
    "password": "password123"
}
```
Example Response:
```
{
    "Status": "Doctor Successfully Logged In",
    "Token": {
        "refresh": "YOUR_REFRESH_TOKEN",
        "access": "YOUR_ACCESS_TOKEN"
    }
}
```


Use the access token received in the response for subsequent requests by including it in the request header as follows:
`Authorization: Bearer YOUR_ACCESS_TOKEN`

## API Endpoints

| Endpoint               | Description                                | Methods                    | Permissions                                    |
|------------------------|--------------------------------------------|----------------------------|------------------------------------------------|
| `/doctors`             | Get all doctors' list (IDs and names)      | GET and POST               | Only doctors                                   |
| `/doctors/<pk>`        | Get particular doctor details              | GET, UPDATE, DELETE         | Only the doctor associated with the profile    |
| `/patients`            | Get all patients' list (ID and name)      | GET and POST               | Any doctor                                     |
| `/patients/<pk>`       | Get particular patient details             | GET, UPDATE, DELETE         | Only the relevant patient and doctors         |
| `/patient_records`     | Get all patient records                    | GET and POST               | Only doctors in the same department            |
| `/patient_records/<pk>`| Get particular patient record               | GET, UPDATE, DELETE         | Only relevant patient and doctors in the same department |
| `/departments`         | Get all departments                        | GET and POST               | Anyone can access                              |
| `/login`               | Get an access token                        | GET and POST               | Anyone can access                              |
| `/register`            | Create a new user                          | POST                       | Anyone can access                              |

