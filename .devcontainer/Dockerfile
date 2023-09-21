# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Make a directory for your project
WORKDIR /usr/src/app

# Install general dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    git

# Copy the local requirements.txt to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Open up port for web server
EXPOSE 8000
