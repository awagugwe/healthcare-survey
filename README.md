# README.md
# Healthcare Spending Survey Application

## Overview
This application collects and analyzes healthcare spending data through a web-based survey. It uses Flask for the backend, MongoDB for data storage, and provides data visualization capabilities using Python data science libraries.

## Features
- Web-based survey form for data collection
- MongoDB integration for data storage
- Data analysis and visualization
- Containerized deployment
- AWS deployment ready

## Prerequisites
- Python 3.9 or higher
- MongoDB
- Docker (for containerized deployment)
- AWS CLI (for AWS deployment)

## Local Development Setup
1. Clone the repository:
   ```bash
   git clone repository
   cd healthcare-survey
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Run the application:
   ```bash
   flask run
   ```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t healthcare-survey .
   ```

2. Run the container:
   ```bash
   docker run -d -p 5000:5000 healthcare-survey
   ```

## AWS Deployment
1. Configure AWS CLI:
   ```bash
   aws configure
   ```

2. Create EC2 instance:
   ```bash
   # Follow AWS EC2 setup instructions in documentation
   ```

3. Deploy application:
   ```bash
   # SSH into EC2 instance
   ssh -i your-key.pem ec2-user@your-instance-ip
   
   # Clone repository and deploy
   git clone repository
   cd healthcare-survey
   docker-compose up -d
   ```


## Database Schema
User Collection:
```json
{
  "age": int,
  "gender": string,
  "income": float,
  "expenses": {
    "utilities": float,
    "entertainment": float,
    "school_fees": float,
    "shopping": float,
    "healthcare": float
  },
  "timestamp": datetime
}
```

## API Endpoints
- `GET /`: Serves the survey form
- `POST /submit`: Submits survey data

## Data Analysis
The application includes Jupyter notebooks for:
- Income distribution analysis
- Gender-based spending patterns
- Healthcare expense trends
