# How to use
1. Clone the repository to your local machine

2. Make sure you have [Docker](https://docs.docker.com/install/) installed on your local machine

3. Install [Docker Compose](https://docs.docker.com/compose/install/)

4. Open a terminal, cd to this Docker-Task folder

5. Run 
```
sudo docker-compose up --build
```

6. If everything goes fine, your console will finally output -
```
docker-node-mongo | MongoDB Connected
```

7. Test the application by making a GET request to
```
localhost/products/test 
```
(by using [Postman](https://www.getpostman.com/) or just simply visiting the link on your browser). You should be see the following text -  
Greetings from the Test controller!

8. You can now make GET, POST, PUT, DELETE requests to this
running server using **Postman** and the procedure followed in [this article](https://codeburst.io/writing-a-crud-app-with-node-js-and-mongodb-e0827cbbdafb)
(Ensure that you do not type a port number while making the requests, for example you would just
use localhost/products/test, not localhost:(port)/products/test)
