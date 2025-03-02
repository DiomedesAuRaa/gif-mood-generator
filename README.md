# [Mood GIF Generator](http://ecs-alb-245690102.us-east-1.elb.amazonaws.com:5000/)
[Available Here:](http://ecs-alb-245690102.us-east-1.elb.amazonaws.com:5000/)

A Python web application that generates a GIF based on your mood. The app asks for your mood, fetches a relevant GIF from Giphy, and displays it in your browser.

---

## Features

- **Mood Input**: Enter your mood (e.g., happy, sad, excited).
- **GIF Fetching**: Fetches a GIF from Giphy based on your mood.
- **Web Interface**: Simple and easy-to-use web interface built with Flask.

---

## Prerequisites

Before running the app, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Giphy API Key**: Sign up at [Giphy Developers](https://developers.giphy.com/) to get a free API key.

---

## How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mood-gif-app.git
cd mood-gif-app
```

### 2. Add Your Giphy API Key

Open the `app.py` file and replace `YOUR_GIPHY_API_KEY` with your actual Giphy API key:

```python
API_KEY = "YOUR_GIPHY_API_KEY"
```

### 3. Build the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t mood-gif-app .
```

### 4. Run the Docker Container

Start the container with:

```bash
docker run -it --rm -p 5000:5000 --env-file .env mood-gif-app
```

### 5. Open the App in Your Browser

Visit the following URL in your browser:

[http://localhost:5000](http://localhost:5000)

---

## Project Structure

```
mood-gif-app/
│
├── Dockerfile
├── requirements.txt
├── .env (required for local use)
├── app.py
└── templates/
    └── index.html
```

---

## Technologies Used

- **Python**: The core programming language.
- **Flask**: Web framework for creating the web interface.
- **Giphy API**: Fetches GIFs based on the user's mood.
- **Docker**: Containerization for easy deployment and running.

---

## CI/CD Workflow for Deployment

This project is integrated with a CI/CD pipeline using GitHub Actions. Upon any changes pushed to the main branch, a workflow is triggered, which initiates the deployment of the app to AWS ECS Fargate.

### Workflow Details

- **GitHub Actions Workflow**:
  - The workflow is triggered when there are changes to the main branch of the repository.
  - The workflow pushes a workflow initiator to the following GitHub Actions workflow: **ECS App Deploy Workflow**.

- **ECS Fargate Deployment**:
  - The ECS App Deploy Workflow uses Terraform to deploy the app on AWS ECS Fargate, ensuring the app is automatically deployed and scaled in a containerized environment.

---