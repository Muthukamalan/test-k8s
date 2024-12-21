# Classification on K8s

This repository provides an implementation for classifying dog breeds using a DL model exported to the ONNX format, paired with a Gradio interface for easy deployment and interaction. 
The model takes an input image of a dog and predicts the breed.

## Build Docker
```shell
docker login # make sure it's done:: check < /home/username/.docker/config.json >
docker build -t dog_breeds:latest -f Dockerfile .
docker tag dog_breeds:latest muthukamalan/dog-breeds-classifier:latest
docker push muthukamalan/dog-breeds-classifier:latest
```


## Structure
```bash
.
├── app.py
├── Dockerfile
├── examples/
├── flagged/
├── mambaout.onnx
├── README.md
└── requirements.txt
```

## Table of Contents
- Overview
- Prerequisites
- Setup
- Preview
- License
- Contribution

## Overview
This project leverages an ONNX (Open Neural Network Exchange) model that is trained to classify dog breeds. 
The model is hosted through a Gradio app, making it easy for users to upload dog images and view predictions on the breed in real time. 
The Gradio interface is simple and intuitive, allowing anyone with no programming experience to interact with the model.

## Prerequisites
- Python 3
- ONNX
- ONNX Runtime
- Gradio
- NumPy
- Pillow

```bash
pip install -r requirements.txt
```

## Setup
setup a docker file. pull docker image and run it. BANG!! 
```bash 
docker pull ???
docker run --rm -it ??? 
```

## Preview
check `localhost:8080` fr experience to interact with the model.
[PREVIEW-IMAGE]()


##TODO:: K8s


## License
This project is licensed under the MIT License. See the LICENSE file for more details.


## Contributing
Feel free to fork this repository and submit pull requests if you have suggestions for improvement!
