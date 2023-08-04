# Matrixian Data Engineering assignment

Please describe your project here.

## Set-up Python environment
Run from the project root (on Linux):
```shell
python3.10 -m venv --upgrade-deps venv
source venv/bin/activate
pip install -r requirements.txt
```

## Database
You can choose between MongoDB and PostgreSQL.

Below is the command to create and run a Docker container that will host the MongoDB database:
```shell
docker run -d --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=admin mongo:5
```
Below is the command to create and run a Docker container that will host the PostgreSQL database:
```shell
docker run -d --name postgres -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust postgres:14
```

## Usage
Run one of the commands below to serve the application on `localhost:8000`:
```shell
python3.10 main.py
```
```shell
uvicorn main:app
```

## Documentation
When running, documentation for the application can be found at
[http://localhost:8000/docs](http://localhost:8000/docs).
