# Use the official Python image as a base
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
