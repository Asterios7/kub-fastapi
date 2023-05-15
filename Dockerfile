FROM python:3.9

COPY ./api/requirements.txt /api/requirements.txt

WORKDIR /api

RUN pip install -r requirements.txt

COPY ./api /api

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

CMD ["main:app", "--host", "0.0.0.0"]