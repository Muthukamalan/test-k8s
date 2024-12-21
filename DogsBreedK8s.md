Once we tested with Dockerfile+ONNX+gradio, will do

```bash

# to see all docker container inside minikube as welll
eval $(minikube docker-env) 
docker ps
docker image ls
```
```log
REPOSITORY                                           TAG                          IMAGE ID       CREATED         SIZE
classifier-k8s                                       latest                       ebc3fd59ae30   3 minutes ago   992MB
```

and build dockerfile inside the minikube
```
docker build -t classifier-k8s -f Dockerfile .
docker ps
```
