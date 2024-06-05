# Dockerfile
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        musl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#install pipenv
RUN pip install pipenv  
RUN pip install django  
    
# Set the working directory in the container
WORKDIR /usr/src/app
# Install Python dependencies
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --deploy --system

# Copy the Django project code into the container
COPY . /usr/src/app/

#collect static files
RUN python manage.py collectstatic --noin