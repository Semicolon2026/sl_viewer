FROM registry.access.redhat.com/ubi9/ubi

WORKDIR /app

ENV PYTHONPATH=/app

# Install Python + intentionally vulnerable rsync package
RUN yum install -y \
    python3 \
    python3-pip \
    rsync && \
    yum clean all

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY config/ ./config/
COPY data/ ./data/
COPY scripts/ ./scripts/

RUN chmod +x scripts/run.sh 

CMD ["./scripts/run.sh"]
