# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_ENV=production

# Run the application using Gunicorn for better performance in production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.routes:app"]
