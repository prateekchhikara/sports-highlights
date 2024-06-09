# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app


RUN apt-get update && apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

    # Install system dependencies
RUN apt-get update && apt-get install -y \
libsndfile1 \ 
libgomp1 \
&& rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit when the container launches
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

