Mini example webapp for tutelar auth microservice.

[SWAGGER](https://app.swaggerhub.com/apis/Ksisu/TodoExampleBackend/1)

```sh
docker run \
  -d \
  -p 5000:5000 \
  -e TOKEN=secret \
  -e DB_URI=mongodb://localhost/todoapp \
  ksisu/tutelar-example-todoapp-py
```
