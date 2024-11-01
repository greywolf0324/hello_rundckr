from python:3.11.1-buster
WORKDIR /
RUN pip install runpod
ADD main.py .
CMD ["python", "main.py"]