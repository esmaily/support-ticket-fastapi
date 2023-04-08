 
# Online Support Ticketing with fastapi

A Online Support Ticketing of using Fast API in Python.

## Preconditions:

- Python 3

 

## Run locally

1. Clone this Repo

   `git clone (https://github.com/esmaily/support-ticket-fastapi)`
2. Cd into the Fast-Api folder

   `cd support-ticket-fastapi`
3. Create a virtual environment

   `python3 -m venv venv`
4. Activate virtualenv

   `source venv/bin/activate`

5. Cd into the src folder

   `cd src`
6. Install the required packages

   `python -m pip install -r requirements.txt`
7. Start the app

   ```shell
   python main.py
   ```

   7b. Start the app using Uvicorn

   ```shell
   uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002
   ```

8. Ensure you have a Postgres Database running locally.
   Additionally create a `support-tikect_dev` database with user `**fast_api**` having required privileges.
   OR
   Change the DATABASE_URL variable in the **.env** file inside then `app` folder to reflect database settings (user:password/db)
```

 

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=support_ticket
```
