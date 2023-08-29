# Use an official Python runtime as the base image
FROM python:3.9

## Set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt \
&& pip install --upgrade pip setuptools wheel

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose the port the FastAPI app runs on
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]