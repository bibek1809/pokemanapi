## base image
FROM python:3.9.9-slim-buster AS base

# Update the package index and clean up
RUN apt-get update && \
    apt-get clean

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file
COPY requirement.txt .

# Install Python dependencies including gunicorn
RUN pip install -r requirement.txt

## builder image (you probably meant to use a different name)
FROM base AS builder

# This stage is missing the actual build commands, but it's commonly used for things like compiling assets, etc.
# If you don't need it, you can remove this stage.

## final image
FROM base

# Copy Python dependencies from the builder image
COPY --from=builder /opt/venv /opt/venv

# Set the PATH environment variable
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Expose the port on which the application will run
EXPOSE 8000

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
