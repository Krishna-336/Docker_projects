# Use an official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements for app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code to app 
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
