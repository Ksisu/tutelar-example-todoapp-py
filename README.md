Mini example webapp for tutelar auth microservice.

```sh
docker run \
  -d \
  -p 5000:5000 \
  -e TOKEN=secret \
  -e DB_URI=mongodb://localhost/todoapp \
  ksisu/tutelar-example-todoapp-py
```
