# FastAPI Model Serving
A repo for training a basic linear regression model and serving the saved model utilizing Docker and FastAPI.

## Project Overview:
The goal of this project is to build a basic linear regression model to be served using Docker and FastAPI.

## Getting Started:
1. In a bash terminal run 'source ./setup.sh' to install all dependencies
2. Train and save model by running 'python code/train_model.py'
3. Test application by running 'uvicorn main:app'
4. Run 'curl -X GET http://localhost:8000/info' in a bash terminal to get application information
5. Run 'docker build . -t fast_api_model_serving' with Docker Desktop up and running
6. Run 'docker run -p 8000:8000 fast_api_model_serving' in bash terminal to get application up
7. Use Docker terminal to make API calls (see tests/example_calls.txt)

# Sample API Call
curl -H "Content-Type: application/json" -d '{
  "list_price": 18500.00
}' -XPOST http://0.0.0.0:8000/predict