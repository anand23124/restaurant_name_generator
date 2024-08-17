# Use the official Python 3.12.2-slim image as a base image
FROM python:3.12.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Expose the port that Streamlit runs on
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "main.py"]