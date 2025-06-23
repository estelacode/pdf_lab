# Use the official Python image as a base
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the rest of the application code
COPY . /app

# Install pip and uv (for fast dependency management)
RUN pip install --upgrade pip 

#  Install the required dependencies
RUN pip install dist/*.whl

# Expose a port if your app runs a server (uncomment if needed)
EXPOSE 7860

# Set the default command to run your app (update as needed)
CMD ["python", "main.py"]
