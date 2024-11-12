# Start from the official Python base image.
FROM python:3.9.11-buster

# Set the current working directory to /project. 
# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /app

# Copy the file with the requirements to the /app directory.
# Copy only the file with the requirements first, not the rest of the code.
# As this file doesn't change often, Docker will detect it and use the cache for this step, enabling the cache for the next step too.
COPY requirements.txt /app/requirements.txt

# Install the package dependencies in the requirements file.
# The --no-cache-dir option tells pip to not save the downloaded packages locally, as that is only if pip was going to be run again to install the same packages, but that's not the case when working with containers.
# The --upgrade option tells pip to upgrade the packages if they are already installed.
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the ./ directory inside the /app directory.
COPY . /app/backend

EXPOSE 8000
# Set the command to run the uvicorn server.
# CMD takes a list of strings, each of these strings is what you would type in the command line separated by spaces.
# This command will be run from the current working directory, the same /app directory you set above with WORKDIR /app.
# Because the program will be started at /app and inside of it is the directory ./app with your code, Uvicorn will be able to see and import app from app.main.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

