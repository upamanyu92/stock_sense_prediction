# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Make port 5002 available to the world outside this container
EXPOSE 5002

# Run the application
CMD ["python", "main.py"]
