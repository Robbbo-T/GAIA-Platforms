# Dockerfile - For AMEDEO Ontology Analyzer
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create directories for data
RUN mkdir -p ontologies
RUN mkdir -p reports
RUN mkdir -p visualizations

# Expose ports
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=ontology_server.py
ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "ontology_server:app"]
