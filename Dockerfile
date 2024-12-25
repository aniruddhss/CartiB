# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for Chromium and Selenium
# RUN apt-get update && apt-get install -y \
#     wget \
#     unzip \
#     chromium \
#     chromium-driver \
#     && apt-get clean
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    chromium=131.* \
    chromium-driver=131.* \
    && apt-get clean


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the FastAPI app
EXPOSE 80

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
