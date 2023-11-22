import os
import subprocess
import requests

def setup_virtualenv():
    os.system("python -m venv venv")
    os.system(". venv/bin/activate")
    os.system("pip install -r requirements.txt")

def run_tests():
    result = subprocess.run(["pytest", "tests"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Tests passed successfully.")
    else:
        print("Tests failed. Deployment aborted.")
        print("Test Output:")
        print(result.stdout)
        print(result.stderr)
        exit(1)

def deploy(jenkins_url, job_name):
    trigger_jenkins_build(jenkins_url, job_name)

def trigger_jenkins_build(jenkins_url, job_name):
    build_url = f"{jenkins_url}/job/{job_name}/build"
    response = requests.post(build_url)
    
    if response.status_code == 201:
        print(f"Jenkins build triggered successfully for job '{job_name}'")
    else:
        print(f"Failed to trigger Jenkins build. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace these values with your Jenkins server URL and job name
    jenkins_url = "http://your-jenkins-server-url"
    job_name = "your-jenkins-job-name"
    
    # Setting up virtual environment and installing dependencies
    setup_virtualenv()

    # Running tests
    run_tests()

    # Deploying the application using Jenkins
    deploy(jenkins_url, job_name)
