# Steps Follow Making Docker Image

1) Create DockerFile

```
FROM python:3.9-slim                                   #Set up the Base Environment

WORKDIR /app                                           #Set up the Folder in the container

COPY . .                                               #Copy all the file into create folder in the container

RUN pip install --no-cache-dir -r requirements.txt     # Install Required Dependencies

EXPOSE 5000                                            # Expose port 5000 for Flask         

CMD ["python", "app.py"]                               # Define the command to run the app

```

2) Create .dockerigonre File
```
__pycache__/
*.pyc
*.pyo
*.pyd
env/
venv/
instance/
.git/
*.db

``` 
4)  Build the Docker Image
```
docker build -t <Docker Image Name> .
```
5) Run the Docker Container
```
docker run -p <port>:<port> <Docker Image Name>
```

## Push Docker Image to the Docker Hub

1) Login to Docker Hub
```
docker login
```
2) check your existing Docker images
```
docker images
```
3) Tag Your Docker Image
```
docker tag <Docker Image> <your_dockerhub_username>/<Docker Image>:<Tag>
```
4) Push the Docker Image to Docker Hub
```
docker push <your_dockerhub_username>/
```
5) Pull and Run the Image on Any System
```
docker pull <your_dockerhub_username>/<Docker Image>:<Tag>
docker run -p <Port>:<port> <your_dockerhub_username>/<Docker Image>
```
   
