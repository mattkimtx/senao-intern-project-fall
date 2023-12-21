# Use an official Python runtime as the base image
FROM python:3.12.1

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=mysite.settings

# Set the working directory in the container
WORKDIR /senao-intern-project

# Copy the Django project files into the container
COPY . /senao-intern-project

# Install any Python dependencies
# RUN pip install -r requirements.txt

# Expose the port that your Django application will run on (e.g., 8000)
EXPOSE 8000

# Start the Django development server
CMD ["/bin/bash", "-c", "source ./myenv/bin/activate && pip install -r requirements.txt && cd mysite && python manage.py runserver 0.0.0.0:8000"]
