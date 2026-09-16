# Use a lightweight official Python image
FROM python:3.12-slim

# Define build-time application version
ARG APP_VERSION=1.0.0
ARG APP_ENV=development

# Configure the application environment
ENV APP_ENV=${APP_ENV} \
    APP_VERSION=${APP_VERSION} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only the application file required to run the program
COPY main.py .

# Run the Smart Quote Request Assistant
CMD ["python", "main.py"]