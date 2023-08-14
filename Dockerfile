# Use the official Python base image
FROM python:3.11.3

# Set the working directory to /app
WORKDIR /app

# Update PYTHONPATH
ENV PYTHONPATH=/app:$PYTHONPATH

# Copy the FastAPI application files to the container's working directory
COPY ./app /app

# Install Poetry
RUN pip install --upgrade pip \
    && pip install poetry

# Install the application dependencies from pyproject.toml and poetry.lock
COPY /app/pyproject.toml /app/poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Specify the command to run when the container starts
CMD ["python", "main.py"]
