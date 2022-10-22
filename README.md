# Mpidegree Assessment Project 
> This is a web application that provides CRUD API endpoints for a business
> to create invoices for purchased products. Admins can also upload a csv
>data of previously purchased invoices. 



## Built With

- Python
- Django
- Mysql 
- Celery


## Getting Started

To get a local copy up and running follow these simple example steps.


### Setup

    git clone https://github.com/smart8099/mpedigree-assessment.git
    cd mpedigree-assessment

### Create and activate Virtual Environment 
    python3 -m venv <your-venv-name>  
    source   your-venv-name/bin/activate

### Install Required dependencies
    pip3 install -r requirements.txt

### Set up Database
    Use Mysql DB
    Create your .env file using the sample example (.env.example).
    Insert your SECRET_KEY, and other database related info in the env file    

### Run DB Migrations
    python3 manage.py migrate    

### Usage
    python3 manage.py runserver
    


## Authors

👤 Abdul Basit Mohammed 

GitHub: @smart8099

- GitHub: [smart8099] (https://github.com/smart8099/)




## 🤝 Contributing
Contributions, issues, and feature requests are welcome!



## Acknowledgments

- Mpidegree Assessment [ Smart8099]
