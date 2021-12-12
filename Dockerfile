FROM python:3.9-slim
COPY example.py .
COPY test_example.py .
CMD python -m unittest test_example