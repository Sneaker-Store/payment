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
http://localhost:8080/
```

## Running with docker 

To run the server on a Docker container, please execute the following from the root directory:

```bash
# sbuilding the image
sudo docker build -t app .
```

```bash
# starting up the container 
sudo docker run -p 8080:8080 app
```

## Running with docker and kubernetes

To run the server on a Docker container using Kubernetes follow the steps:

```bash
# build the image 
sudo docker build -t registry.deti:5000/saudade/payment:v1 . 

# push the image to the server
sudo docker push registry.deti:5000/saudade/payment:v1 

# create a new secret for use with Docker registries
./create.sh

# create and update resources in the registry
kubectl apply -f deployment.yaml
```

