## 1) Steps to Download ,  Install and Run project :

### COMMANDS :
>Downloading the project
>1) **git clone https://github.com/piyushnanwani/rest-api-django.git** 
>2) **cd sampleproject**
>Creating a virtual environment
>3) **virtualenv venv**      
>Activate virtual environment
>4) **source venv/bin/activate**     
>Installing all dependencies
>5) **pip3 install -r requirements.txt**       
>Running the project
>6) **django-admin manage.py runserver**


### 2) Simulate GET,POST,PUT,DELETE requests using Postman

https://www.getpostman.com/


### 3) Functionality 

1) GET /api/users : This returns list of users
You can also search user by name as a substring in First Name or Last Name 

---
/api/users - GET​ ​ - To list the users
/api/users?page=1&limit=10&name=James&sort=-age

---

2) POST /api/users/ 

3) PUT /api/users/

4) DELETE /api/users/{id}

Test Cases are also added in test.py
