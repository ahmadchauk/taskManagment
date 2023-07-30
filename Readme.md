## Libraries and tools used

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [PostgreSQL](https://www.postgresql.org/)

## How to run

### Install and configure PostgreSQL

Create Database name tasks_db

### configure environment

rename .env.example to .env

fill the DATABASE_URL with the link `postgresql://postgres:12345678@localhost:5432/tasks_db`

### Run migrations

1.  ```
    flask db init
    ```

2.  ```
    flask db migrate
    ```

3.  ```
    flask db upgrade
    ```

### Run the server

```
python server.py 
```

The server will be running on `http://127.0.0.1:5000/`



