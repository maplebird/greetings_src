# greetings_src


### Source code: 

Grabbed source code from this tutorial:
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

curl localhost:8080

Example:

```vlad@Macbook greetings_ci (master) $ curl localhost:8080
{"content":"Hello, World!"}
```