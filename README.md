# greetings_src

Source code for Greetings microservice

This is a proof of concept/exercise to see how much of a deployment pipeline I could create in about 4-6 hours.

### Source code: 

Grabbed node source code from this tutorial:
https://scotch.io/tutorials/build-a-restful-api-using-node-and-express-4

Slightly modified to fit my needs

Simple Rest API that listens on port 8080 and returns "Hello, World!" as a json in the content field.
 
### Installation instructions

```
git clone https://github.com/maplebird/greetings_src.git
cd greetings_src
npm install
```

### Startup instructions

```
npm start
```

### To access the server:

```
curl localhost:8080
```

Example:

```
vlad@Macbook greetings_ci (master) $ curl localhost:8080
{"content":"Hello, World!"}
```

### Unit tests

Need Python 2.7 with argparse module installed

To run unit tests, build project as normal and start the server

Then run unittest/tests.py with localhost and against port 8080.

Example:

```
cd unittest
python tests.py -u localhost -p 8080
```

Sample output:

```
vlad@Macbook unittest (master) $ python tests.py -u localhost -p 8080
Test 1 successful, server is up
Test 2 successful, GET returns Hello, World!
2 out of 2 tests were successful.
```

### Init.d script

If you're running an init.d compatible system (i.e. Linux), you can run it as a service.

Copy sys/greetings to /etc/init.d to /etc/rc.d/init.d/ and start/stop via service:

```
sudo cp sys/greetings /etc/rc.d/init.d/
service greetings start
```

This service is deployed automatically on node bootstrap/installation via greetings_ci project.
