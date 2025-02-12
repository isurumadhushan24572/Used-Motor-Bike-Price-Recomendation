# Use an official lightweight Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
