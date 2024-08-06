# ExcelAI - Server 

### Fly.io Deployment
- On the command line, run `fly launch`
- Add necessary secrets to Fly.io 
  - On the main screen, select `Apps` on the left-hand navigation panel.
  - Select your app 
  - On the left-hand navigation panel, select `Secrets` 
  - Click `New Secret`
  - Add your environment variables 
- Generate Fly.io Access Token and add it to GitHub Secrets
  - Navigate to the top right corner of the main screen on Fly.io, hover over `Account` and click `Access Tokens`
  - On the right-hand side, enter a `Token Name` and click `Create access token`. 
  - Navigate to your GitHub repository. 
  - On the upper taskbar, select `Settings`
  - On the left-hand navigation panel, select `Secrets and variables`, then select `Actions`.
  - Under the `Secrets` tab, click `New repository secret`
  - Set your `SECRET_NAME` as `FLY_API_TOKEN`, and paste the generated access token as the value.
- Modify the Dockerfile as follows:
```Dockerfile# Use the official Python image as a base
FROM python:3.12.3-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Install system dependencies, including PostgreSQL development libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies directly into the system Python environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the final image
COPY . .

# Expose port 8080 to the outside world
EXPOSE 8080

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```