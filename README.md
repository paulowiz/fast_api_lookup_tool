
  
<!-- PROJECT -->  
<p align="center">  
  <h3 align="center">   
   Data Engineer Assignment Matrixiangroup
  </h3>   
</p>  
  
<!-- ABOUT THE PROJECT -->  
## 🤔 Introduction  

Develop an ETL pipeline for extracting, transforming, and loading data from Spain's address zip file on S3 into a database, coupled with the creation of a RESTful API to enable address search based on textual input.
<br />   
  
  
<!-- INSTALLATION -->  

# 🔨 Installation and Running

Install the required dependencies by running:

  
1. Clone this repository  
  
2. Setup inside the `docker-compose.yml` the variable `LOCAL_RUN=1` if you are running in your computer. I recommend `LOCAL_RUN=0` just on server with more resources (CPU and Memory RAM)
  
3. Run docker compose `docker-compose up -d --build` (be sure if your ports 8000 and 5433 are available)

4. The ETL is going to run first, and it is taking about `3-4 minutes`

5. After the ETL done you can check the API here http://localhost:8000/docs and try it out the endpoint.

<br />  
  
## 📚 Project Files Overview
- app
  - routes
    - `address.py`: address route with the endpoint to search by text. 
  - `main.py`: main file to run the API service and swagger.
  - `models.py`: ORM Table Mapping.
- etl
  - `main.py`: Main file to run the ETL pipeline.
  - `utils.py`: class with generic functions to the etl process.
- `requirements.txt`: A file containing project dependencies.
- `database.py`: Database setup.
- `.gitignore`: Defines files that should be ignored by Git.
- `lab.ipynb`: Initial analysis that I did before building the ETL and service.
- `docker-compose.yml`: A Docker file to run Postgres Database,ETL Process and REST API(Fast API)

## 🔓 Author and Acknowledgements

- **Author**: [Paulo Mota](https://www.linkedin.com/in/paulo-mota-955218a2/)<br>
