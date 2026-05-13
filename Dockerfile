FROM registry.access.redhat.com/ubi9/ubi

WORKDIR /app

# Install vulnerable rsync version
RUN yum install -y rsync-3.2.5-3.el9 && \
    yum clean all

COPY app.py .

CMD ["python3", "app.py"]
