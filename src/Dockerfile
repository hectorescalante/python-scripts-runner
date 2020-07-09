FROM python:3
WORKDIR /usr/src/app

# Install python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY program.py .
COPY tasks ./tasks

# Run tests
RUN pytest

ENTRYPOINT [ "python", "./program.py" ]