<img align="left" width="145" src="https://upload.wikimedia.org/wikipedia/fr/thumb/e/e9/EPF_logo_2021.png/524px-EPF_logo_2021.png" alt="EPF Logo">



###  <div align="right">  Data Engineering - P2024 <br> <br>  <ins>Date </ins>: <time datetime="2023-01-04"> 2024/0104 </time> <br> <br> <ins>Author </ins>: GAUBIL Clara </div>
<br> 



#   <h1 align="center">  Data Source - API </h1>


```
epf-flower-data-science
│   main.py
│   requirements.txt 
│   tests_endpoint.py
│   tests_functions.py
│
└───src
│   │   app.py
│   
│   └───api
│       │   router.py
│       │
│       └───routes
│           │   authentication.py
│           │   data.py
│           │   hello.py
│           │   parameters.py
│
│   └───config   
│           │   model_parameters.json
│
│   └───data
│           │   Iris.csv
│           │   database.sqlite
│
│   └───model
│           │   KNN_model.pkl
│          
│   └───services
│           │   cleaning.py
│           │   data.py
│           │   parameters.py
│           │   utils.py                
│   
```

- <ins>Question 1: Which Python library/framework is often used to create fast, simple REST APIs?</ins>

Django  
**Flask**  
FastAPI  
All of the above  

The library often used to create fast, simple REST APIs is Flask. Indeed, it is simple and easy to use.

- <ins>Question 2: What's the main difference between Django, Flask and FastAPI in terms of performance and speed?</ins>

Django is generally faster than Flask and FastAPI.  
Flask outperforms Django and FastAPI.  
**FastAPI is renowned for its increased speed and performance compared with Django and Flask.**  
Django, Flask and FastAPI have equivalent performance.  

- <ins>Question 3: What is an endpoint in the context of REST APIs?</ins>

A unique IP address associated with an API.  
A breakpoint in the code where the API can be interrupted.  
**A specific URL to which a request can be sent to interact with the API.**  
A unique identifier assigned to each incoming request.  

- <ins>Question 4: What are the main HTTP verbs used to define REST API methods?</ins>

**GET, POST, PUT, PATCH, DELETE**   
SEND, RECEIVE, UPDATE, REMOVE  
READ, WRITE, MODIFY, DELETE  
FETCH, INSERT, UPDATE, DELETE  

- <ins>Question 5: In the context of REST APIs, what does the term "middleware" mean?</ins>

A component that processes data sent by the user.  
An external library used to speed up API development.  
**Intermediate software that processes the request before it reaches the main application.**  
A method for securing data stored in the database.  

- <ins>Question 6: Which Python library is often used to serialize and deserialize JSON data in the context of REST APIs?</ins>

JSONify  
PyJSON  
**json.dumps() and json.loads()**   
serializeJSON  

- <ins>Question 7: What is the main use of the HTTP "PUT" method in the context of REST APIs?</ins>

Create a new resource.  
**Update an existing resource, or create one if it doesn't exist.**   
Delete a resource.  
Read a specific resource.  

- <ins>Question 8: In FastAPI, how do you define an endpoint to handle a POST request with JSON data?</ins>

**@app.post("/endpoint")**  
@app.get("/endpoint")  
@app.request("/endpoint")  
@app.update("/endpoint")