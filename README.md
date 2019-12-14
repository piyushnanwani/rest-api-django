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

### 3) Desciption of Project
>A REST-API is made which stores the user data.
  3.1 User have the following attributes:-
  ● ID
  ● First Name
  ● Last Name
  ● Company Name
  ● Age
  ● City
  ● State
  ● Zip
  ● Email
  ● Web
3.2 Application hast the following endpoints : 
  3.2.1 /api/users - GET​ ​ - To list the users
   3.2.1.1 Response with HTTP status code ​ 200 ​ on success
   3.2.1.2 Also, support for some query parameters:-
        3.2.1.2.1 page - a number for pagination
        3.2.1.2.2 limit - no. of items to be returned, default limit is 5
        3.2.1.2.3 name - search user by name as a substring in First Name or Last Name (Note, use substring
                  matching algorithm/pattern to match the name)
        3.2.1.2.4 Sort - name of attribute, the items to be sorted. By default it returns items in ascending order
                  if this parameter exist, and if the value of parameter is prefixed with ​ ‘-’ ​ character, then it
                  should return items in descending order
  3.2.2 /api/users - POST​ ​ - To create a new user
  3.2.3 /api/users/{id} - GET​ ​ - To get the details of a user
    3.2.3.1 Here {id} will be the id of the user in path parameter
    3.2.3.2 Response with HTTP status code ​ 200 ​ on success
  3.2.4 /api/users/{id} - PUT​ ​ - To update the details of a user  
    3.2.4.1 Here {id} will be the id of the user in path parameter
  3.2.5 /api/users/{id} - DELETE​ ​ - To delete the user
    3.2.5.1 Here {id} will be the id of the user in path parameter
    3.2.5.2Response with HTTP status code ​ 200 ​ on success

### 3) Functionality 

1) GET /api/users : This returns list of users
You can also search user by name as a substring in First Name or Last Name 

2) POST /api/users/ 

3) PUT /api/users/

4) DELETE /api/users/{id}

Test Cases are also added in test.py
