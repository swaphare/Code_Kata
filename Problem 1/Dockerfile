# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure the entrypoint script is executable
RUN chmod +x entrypoint.sh

# Define environment variable
ENV NAME World

# Run entrypoint.sh when the container launches
ENTRYPOINT ["./entrypoint.sh"]
