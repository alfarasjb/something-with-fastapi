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
```Dockerfile
# Use the official Python image as a base for the build stage
FROM python:3.12.3-bookworm AS builder

# Environment variables to prevent Python from writing .pyc files and to ensure output is unbuffered
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Create a virtual environment in the /app/.venv directory
RUN python -m venv /app/.venv

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies into the virtual environment
RUN /app/.venv/bin/pip install -r requirements.txt

# Use a smaller Python image for the final stage
FROM python:3.12.3-slim-bookworm

# Set the working directory in the final container
WORKDIR /app

# Copy the virtual environment from the builder stage to the final image
COPY --from=builder /app/.venv /app/.venv/

# Copy the application code into the final image
COPY . .

# Add the virtual environment's bin directory to the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose port 8080 to the outside world
EXPOSE 8080

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```