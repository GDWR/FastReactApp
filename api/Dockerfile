FROM python:3.10

RUN pip install --upgrade pip

ADD requirements.txt api/main.py ./
RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn"]
CMD ["main:api", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]