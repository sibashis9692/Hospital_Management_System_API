# Hospital Management System

Hospital Management System is a web-based application built with Django REST framework for managing patient records, doctors, and departments in a hospital or healthcare facility.

## Features

- User registration and authentication with JWT tokens.
- Differentiate between Doctors and Patients.
- Manage patient records, including diagnostics, observations, and treatments.
- Department management with details like diagnostics, location, and specialization.
- Comprehensive API endpoints for data management.
- Role-based access control for Doctors and Patients.

## Requirements

Make sure you have the following dependencies installed before running the application:

- Python 3.x
- Django 4.2.5
- Django REST framework 3.14.0
- djangorestframework-simplejwt 5.3.0
- mysqlclient 2.2.0
- PyJWT 2.8.0

You can install these dependencies by running:

```
pip install -r requirements.txt
```

## Installation

1. Clone the Repository:
```
git clone https://github.com/sibashis9692/Hospital_Management_System_API.git
cd Hospital_Management_System_API
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:
```
venv\Scripts\activate
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
python manage.py migrations
python manage.py migrate
```
# Running the Application
```
python main.py
```
The server should now be running at http://localhost:5000

# API Endpoints

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

