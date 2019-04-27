Mini example webapp for [tutelar](https://github.com/TeamWanari/tutelar) auth microservice.

[TODOAPP SWAGGER](https://app.swaggerhub.com/apis/Ksisu/TodoExampleBackend/1)

[TUTELAR SWAGGER](https://app.swaggerhub.com/apis/Ksisu/Tutelar/0.1)

```sh
docker-compose up -d
```

---
### Examples
Register:
```
$ curl --insecure --silent \
>  -XPOST \
>  -H "Content-Type: application/json" \
>  --data '{"username": "ksisu", "password": "Ksisu123"}' \
>  https://lvh.me:9443/basic/register | jq .
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTY0Mjg3MzMsImlkIjoiZTk3NDFiZWYtNGYyYS00YjY0LTgzYTEtYWEzOTkyMjQwOGRhIn0.ywrV2tae81isxFgM_oZDQFJxYZgSutxGUTIgTuU-UDs"
}
```
Create a todo item:
```
$ curl --insecure --silent \
> -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTY0Mjg3MzMsImlkIjoiZTk3NDFiZWYtNGYyYS00YjY0LTgzYTEtYWEzOTkyMjQwOGRhIn0.ywrV2tae81isxFgM_oZDQFJxYZgSutxGUTIgTuU-UDs" \
> -XPOST \
> -H "Content-Type: application/json" \
> --data '{"title": "Example", "done": false}' \
> https://lvh.me:9443/api/todo | jq .
{}
```
List todo items:
```
$ curl --insecure --silent \
> -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTY0Mjg3MzMsImlkIjoiZTk3NDFiZWYtNGYyYS00YjY0LTgzYTEtYWEzOTkyMjQwOGRhIn0.ywrV2tae81isxFgM_oZDQFJxYZgSutxGUTIgTuU-UDs" \
> https://lvh.me:9443/api/todo | jq .
[
  {
    "done": false,
    "title": "Example"
  }
]
```
