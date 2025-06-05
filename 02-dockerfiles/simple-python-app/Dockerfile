# Use official Python image with slim version to keep it small
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache for dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files into the container
COPY app.py .

# Command to run the Python script
CMD ["python", "app.py"]
