Step to reproduce issues of stats not printing from api calls.

- Start the server by calling this command : 
    python grpc/hello_server.py

- The above command will start a hello_server on localhost:50051

- Run the locust driver class which uses locust as library: python grpc/locust_driver.py

- The Csv files generated and logs created will have zero stats output
  ```
     locust test have completed running
     Test run completed.
     requests after run : 0
     Failures after run : 0
  ```
  

Steps to build the project

- Create virtualenv python project. I used pycharm for the same

- pip install -r requirements.txt to download depndecies
