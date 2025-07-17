# Flask Guestbook App with Docker and AWS

A simple Flask-based guestbook web app where users can submit messages. The app is containerized with Docker, versioned with Git, and deployed to AWS Elastic Beanstalk. Includes basic input sanitization for security.

## Features
- Users can submit a name and message via a form.
- Input validation to prevent malicious input.
- Dockerized for portability.
- Tested on Windows and Linux.

## Setup
1. Clone the repo: git clone https://github.com/Zimex01/flask-guestbook-app
2. Install Docker and AWS CLI on your system.
3. Build the Docker image: docker build -t flask-guestbook-app .
4. Run locally: docker run -p 5000:5000 flask-guestbook-app
5. Access at http://localhost:5000

## Testing
Run pytest tests/test_main.py to execute unit tests.

## Deployment
3. Run the deployment script:
   - Linux: bash scripts/deploy.sh
   - Windows: powershell scripts/deploy.ps1

## Technologies
- *OS*: Windows, Linux
- *Scripting*: Python (Flask), Bash/PowerShell
- *Source Control*: Git, GitHub
- *Security*: Input sanitization
- *Containerization*: Docker

## Security
- User inputs are sanitized to remove special characters and limit length.

## Testing on Windows/Linux
- *Linux*: Use Bash in an Ubuntu VM or WSL.
