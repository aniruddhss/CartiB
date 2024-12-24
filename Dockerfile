# Use Fedora as the base image
FROM fedora:36

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Python, Chrome, ChromeDriver, and required dependencies
RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip \
    wget \
    unzip \
    libX11-xcb \
    nss \
    libXcomposite \
    libXcursor \
    libXdamage \
    libXrandr \
    libXtst \
    libstdc++ \
    pango \
    gtk3 \
    liberation-fonts \
    alsa-lib \
    && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm \
    && dnf install -y ./google-chrome-stable_current_x86_64.rpm \
    && wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && dnf clean all

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port for the FastAPI app
EXPOSE 80

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
