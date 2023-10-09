# Example: https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi
# Each line in a docker file is a layer
# If the layer has been made and hasn't changed, docker copies it from the docker cache
# To build this use: docker build -t myimage .
# Then run it with: docker run -d --name mycontainer -p 80:80 --platform linux/amd64 myimage

# Start from official Python base image like python:3.11
# Can also use: https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the current working directory
WORKDIR /app

# Copy the requirements file to the app
COPY ./requirements.txt .

# Install depdendencies
# --no-cache-dir means not to save downloaded packages locally
# --upgrade upgrades existing packages
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copy the directory; has all the code in it and changes most frequently
# put at the end to optimize container image build times
COPY . .

# run the uvicorn server in the working directory
# CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]