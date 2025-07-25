
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

ENV FLASK_APP=run.py
ENV FLASK_ENV=development


CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]