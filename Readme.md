## Libraries and tools used

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [FlaskSQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [PostgreSQL](https://www.postgresql.org/)

## How to run

### Install and configure PostgreSQL


Create Database name tasks_db

The DATABASE_URL variable is your database url. If you are using in localhost, the URL is something like: `"postgresql://postgres:12345678@localhost:5432/tasks_db`.

### Run migrations

1.  ```
    python app.py db init
    ```

2.  ```
    python app.py db migrate
    ```

3.  ```
    python app.py db upgrade
    ```

### Run the server

```
python server.py 
```

The server will be running on `http://127.0.0.1:5000/`


## API Endpoints

- [GET tasks](docs/get_tasks.md)
- [GET tasks/:id](docs/get_task.md)
- [POST tasks/](docs/post_task.md)
- [PUT tasks/:id](docs/put_task.md)
- [DELETE tasks/:id](docs/delete_task.md)
