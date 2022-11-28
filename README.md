# learning-platform-be

### Installing application :  
 1  git clone https://github.com/Ciant-Andy/learning-platform-be.git  
 2  pip install -r requirements.txt  
 3  create .env file with this variables :

    POSTGRES_SERVER=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB= 
    PROJECT_NAME=learning-platform
    SECRET_KEY=
    FIRST_SUPERUSER=
    FIRST_SUPERUSER_PASSWORD=
    BACKEND_CORS_ORIGINS=["http://localhost", "http://localhost:3000", "http://localhost:8080", "https://localhost"]
    USERS_OPEN_REGISTRATION=False

 4 python main.py  
 5 use http://localhost:8000/redoc to see API documentation
 
![Alt Text](https://media.tenor.com/Yc99UMbsvmgAAAAd/chainsaw-man-chainsaw-man-anime.gif)