## Flask products 
A simple containerized RESTful API with CRUD operations. The app folder contains the main structure of the application. The configuration files can be found in the instance folder. There are unit and integrations tests in the tests folder. The Kubernetes manifests can ve found in the
manifests file accordingly. 

### Technologies
The main technologies used in this project are:
* Flask
* Postgresql
* MongoDB
* Docker & Docker-compose
* Kubernetes
* Argo Gitops (Argo CD & Argo Workflows)

### Setup
Assuming Docker is installed, the first step is to build the image and run it locally. In order to isolate the app from the 
database, the connection string in instance/config.py can be changed to

```
SQLALCHEMY_DATABASE_URI = "sqlite:///" + file_path
```

In the terminal we need to make sure we are in the right directory where the Dockerfile is, or that we specify the right directory,
 so the image can be built.
```
docker build -t products-image .
```
```
docker run -dp 5000:5000 products-image
```
To see if the application started, inspect the logs of the container with
```
docker logs [container_id]
```
The container's id is returned after the run command is executed and the output should look similar to this

```
[7] [INFO] Starting gunicorn 20.1.0
[7] [INFO] Listening at: http://0.0.0.0:5000 (7)
[7] [INFO] Using worker: sync
[9] [INFO] Booting worker with pid: 9
```

Next step is to setup the databases. We go back to instance/config.py and change (comment/uncomment) to the uri's which use the environment variables. Make sure postgres is installed (https://www.postgresql.org/download/) and mongodb compass (https://www.mongodb.com/products/compass)
for running the databases locally. However, there is also a (preffered) option to run mongodb as a cloud database with MongoDb Atlas (https://www.mongodb.com/atlas/database).

To check whether postgresql is running 
```
service postgresql status
```
To check whether mongodb is running 
```
service mongodb status
```

In order to run the databases with docker-compose, we need to set an .env file which contains the database credentials as seen as
in the app/read_env.py file and then we can start the services with
```
docker-compose up
```

### Kubernetes 

Minikube is a utility we can use to run Kubernetes (k8s) on our local machines. It creates a single node cluster contained in a virtual machine. This cluster lets us try out Kubernetes operations without requiring the time and resource-consuming installation of full-blown K8s. Kubectl is a command line tool for Kubernetes, then enables the interaction with the cluster: to create pods, services and other components.

There are different ways to install both, depending on the OS (https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/)

If its running on Linux and Docker environment then minikube can be started with

```
minikube start --driver=docker
```

Next we enable the ingress controller with
```
minikube addons enable ingress
```

Now we can deploy the manifests to the locally run kubernetes cluster 
```
kubectl apply -f manifests-folder/
```

Every time there's some kind of change, we need to rebuild and upload the new image, then stop the container that's running currently and redeploy it using the new image. This process is lengthy and repetitive so it can be automatized by using a CD tool, we'll be using Argo CD.


### Argo CD 
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. It is implemented as a kubernetes controller which continuously monitors running applications and compares the current, live state against the desired target state (as specified in the Git repo).

To setup Argo Workflows and Argo CD, follow the steps under 
1. Install Argo Workflows and Argo Events
2. Install Argo CD

at https://github.com/ekrajchevska/argo-gitops
