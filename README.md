![Tests](https://github.com/Asterios7/kub-fastapi/actions/workflows/tests.yaml/badge.svg)

# kub-fastapi

[**Overview**](#overview)
| [**Prerequisites**](#Prerequisites)
| [**How to use**](#how-to-use)
| [**Testing**](#testing)

## Overview<a id="overview"></a>

This repository contains a Face Detection API built with FastAPI, deployable via Docker Compose and Kubernetes. The application processes images, highlighting detected faces by drawing bounding boxes around them.

#### Features

- FastAPI Face Detection: Utilizes FastAPI to provide face detection functionality.
- Deployment Options:
  - Docker Compose: Easily deploy using Docker Compose.
  - Kubernetes: Enables deployment on Kubernetes clusters.
- Streamlit Interface: Docker Compose deployment includes a Streamlit interface for user interaction.

#### Functionality

Upon providing an image, the API returns the same image with bounding boxes indicating the detected faces.

## Prerequisites<a id="Prerequisites"></a>

Before getting started, ensure you have the following installed:

- [Docker](https://docs.docker.com/engine/install/)
- [minikube](https://minikube.sigs.k8s.io/docs/start/) (Required for Kubernetes deployment)
- [kubectl](https://minikube.sigs.k8s.io/docs/handbook/kubectl/) (Required for Kubernetes deployment)

## How to use<a id="how-to-use"></a>

**Local Deployment Using Docker**

1. Start the App:

```bash
cd /path/to/kub-fastapi
docker compose up --build
```

2. Access the app:

   - Streamlit: http://localhost:8501/
   - FastAPI: http://localhost:8000/

3. Stop the App:

```bash
docker compose down
```

**Local Deployment Using Kubernetes**

1. Start Minikube:

```bash
minikube start
```

Verify status:

```bash
minikube status
```

2. Deploy to Kubernetes:

```bash
kubectl apply -f kubernetes/backend-deployment.yaml
kubectl apply -f kubernetes/backend-service.yaml
minikube service backend-service
```

Access the API using the provided port of minikube service.

3. Cleanup:

```bash
kubectl delete -f kubernetes/backend-deployment.yaml
kubectl delete -f kubernetes/backend-service.yaml
```

## Testing<a id="testing"></a>

For testing the code execute the run_tests.sh script with:

`bash run_test.sh`

locust -f load_test/locustfile.py
