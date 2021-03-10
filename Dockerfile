# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy the source files into the container
WORKDIR /app
COPY . /app

# Define the command to be run when the container is started
CMD ["python", "app\main.py"]
