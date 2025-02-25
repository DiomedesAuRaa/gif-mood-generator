# ECS Python App

This is a Python app that will be dockerized and deployed to Amazon ECS.

## How to Run Locally

1. Build the Docker image:
   ```bash
   docker build -t ecs-app.
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5001:5000 my-python-app
   ```

3. Visit `http://localhost:5000` in your browser.

## How to Deploy to ECS

1. Push the Docker image to ECR.
2. Create an ECS cluster and task definition.
3. Deploy the app as a service in ECS.
# gif-mood-generator
