# Payment microservice 

Paymente is as simple microservice simulating a real payment service

## Instalation 

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install the requirements:

```bash
pip3 install -r requirements.txt
```

## Usage

In order to run the flask api use:

```bash
python3 -m app/app.py
```

or use 
```bash
flask run
```

an then open the browser in:
```bash
http://localhost:5000/
```

## Running with docker 

To run the server on a Docker container, please execute the following from the root directory:

```bash
# Building the image
sudo docker build -t app .
```

```bash
# Starting up the container 
sudo docker run -p app
```

## Running with docker and kubernetes

To run the server on a Docker container using Kubernetes follow the steps:
First we need to build, push and apply the image of the MongoDB database to the kubernetes clusters:
```bash
# Build the database image (download it first in dockerhub) 
# It's worth noticing that MongoDB version 5.0 is not supported by the server. 
# The version used was MongoDB 4.4.0 
sudo docker build -t registry.deti:5000/saudade/mongodb:v2

# Push the image to the server
sudo docker push registry.deti:5000/saudade/mongodb:v2 

# And finally apply in kubernetes registry
kubectl apply -f mongo.yml
```
then build, push and apply the image of the Application to the kubernetes clusters:
```bash
# Build the image 
sudo docker build -t registry.deti:5000/saudade/payment:v1 . 

# Push the image to the server
sudo docker push registry.deti:5000/saudade/payment:v1 

# Create a new secret for use with Docker registries
./create.sh

# Create and update resources in the registry
kubectl apply -f deployment.yaml
```

