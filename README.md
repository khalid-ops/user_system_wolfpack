A django app with user register and login from REST APIs and JWT Authentication
Instructions for app setup:
1. Install required libraries with requirements.txt.
2. Run the migrations with "python manage.py migrate"
3. Start the server with "python manage.py runserver"

available endpoints:

1. 
url : http://127.0.0.1:8000/register
method : POST
data : {
    "email" : "sampleemail@gmail.com",
    "password": "samplepassword"
}
Response : {
    "user": {
        "id": 20,
        "email": "sampleemail@gmail.com"
        "password": "samplepassword"
    },
    "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyMCwiZXhwIjoxNzA3NTk1MjA0fQ.f01qh3M145XqrtObyBLacFwO447JUytzuBqc9VOYOAs"
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

2.    
Use the token recieved from above response for login with authentication 

url : http://127.0.0.1:8000/login
method : POST
data : {
    "email" : "sampleemail@gmail.com",
    "password": "samplepassword"
}
Response : {
    "message": "User logged in!"
}

