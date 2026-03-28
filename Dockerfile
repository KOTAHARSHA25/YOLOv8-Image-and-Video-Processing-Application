FROM python:3.9-slim

# Install system dependencies required by OpenCV and YOLO
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirement list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the application files
COPY . .

# Ensure data/raw directory exists and has permissions
RUN mkdir -p data/raw && chmod -R 777 data/raw

# Expose the port Hugging Face Spaces uses by default for Docker
EXPOSE 7860

# Run the Flask app
CMD ["python", "app.py"]