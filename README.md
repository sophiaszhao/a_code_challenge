# Altagram Starwars Ships Challenge
A service project using Python, retrieving a list of all starships from the Star Wars movies, sorted by the hyperdrive rating.

The project is built with Jupyter Notebook and Python, using the Flask framework. 

Starships data from [SWAPI](https://swapi.dev/) is stored in PostgresSQL database, which is set up via a Jupyter Notebook, using Docker.

### Prerequisites

* Python 3
* Pip 3
* [Jupyter Notebook](https://jupyter.org/)
* [Docker](https://docs.docker.com/get-docker/)

### Installing

```
pip3 install -r requirments.txt
```


## Running the Service

Use the Jupyter Notebook to create and set up the PostgresSQL database inside the Docker container. Run all the cells in notebook except the last clean up step. 

Once the database is running, run the following command to start the flask service.

```
export POSTGRES_USER=altagram 
export POSTGRES_PASSWORD=altagram21
python3 main.py
```

Finally run the last cell in the Jupyter Notebook to clean up.

