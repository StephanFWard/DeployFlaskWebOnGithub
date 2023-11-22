This README provides step-by-step instructions on how to set up and use the auto-deployment script if Flask web application is hosted on GitHub. It covers prerequisites, installation steps, configuration, and additional notes for customization. Users can follow these instructions to deploy their Flask web application using Jenkins.

# Auto Deployment Script

This Python script automates the deployment of a Flask web application using Jenkins. It includes setting up a virtual environment, installing dependencies, running tests, and triggering a Jenkins build.

## Prerequisites

- Python 3.x
- `virtualenv` package (optional but recommended)
- `requests` library. 

Clone the web application repository:

git clone https://github.com/StephanFWard/DeployFlaskWebOnGithub.git
cd DeployFlaskWebOnGithub

Install the required packages:

  pip install -r requirements.txt

Replace the placeholders in the deploy_app.py script with your Jenkins server URL and job name.

Set up a virtual environment (optional but recommended):

  python -m venv venv
  
  . venv/bin/activate
  
Install dependencies:

  pip install -r requirements.txt

Run tests:

  pytest tests

If tests pass, deploy the application:

  python deploy_app.py

Notes:

Make sure your Jenkins server is accessible from the machine where you run this script.
Ensure that Jenkins job is properly configured for auto deployment.
You can customize the test command and deployment process based on your application's needs.
