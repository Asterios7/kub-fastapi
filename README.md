https://github.com/Asterios7/kub-fastapi/actions/workflows/Tests/badge.svg

# Fastapi - Kubernetes


[**Overview**](#overview)
| [**Requirements**](#requirements)
| [**How to use**](#how-to-use)
| [**Testing**](#testing)

## Overview<a id="overview"></a>

A fastapi app with a simple streamlit frontend with docker and kubernetes.

## Requirements<a id="requirements"></a>

Things to install

- Docker
- minikube (Optional, only for Kubernetes)
- kubectl  (Optional, only for Kubernetes)

## How to use<a id="how-to-use"></a>

For starting the app:
1. Open a terminal
2. Go to /path/to/kub-fastapi
3. Execute `docker compose up --build`
4. Open browser at http://localhost:8501/ 

For stopping the app from the same terminal path execute:

`docker compose down`


## Testing<a id="testing"></a>

For testing the code execute the run_tests.sh script with:

`bash run_test.sh`
