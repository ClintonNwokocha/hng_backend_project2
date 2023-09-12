# Django CRUD API fot Person Management 
This is a simple Django project that demonstrates CRUD (Create, Read, Update, Delete) operations through a RESTful API. It manages 'Person' objects that have a 'name' attribute.
## Table of Contents

* Installation
    * Prerequisites
* Usage
    * API Endpoints
* Testing
* UML and ER Diagrams

## Installation
First, clone the github repository to your local machine:
https://github.com/ClintonNwokocha/hng_backend_project2.git

### Prerequisites
* Python 3.x
* Django
* Virtualenv (recommended)

## Usage
### API Endpoints
POST /api/: Creates a new person.
GET /api/<int:user_id>/: Retrieves the person with the given ID.
PUT /api/<int:user_id>/update/: Updates the person with the given ID.
DELETE /api/<int:user_id>/delete/: Deletes the person with the given ID.

## Testing
To run the API tests, execute the following command;
python test_api.py

## UML and ER Diagrams
see ![UML Diagram](CRUD_UML.png) and ![ER Diagram](ER_CRUD.PNG)

  
