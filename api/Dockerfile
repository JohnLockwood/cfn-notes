# TODO Add code for API container

FROM python:3.8.6-slim
RUN echo # > ./__init__.py
COPY ./app/requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./app /app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--root-path", "/api", "--port", "80"]