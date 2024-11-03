# App for presentaion

## Local run

```bash
# run DB
docker run -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -p 5432:5432 -d postgres

# run app
poetry run fastapi run app/main.py


```
