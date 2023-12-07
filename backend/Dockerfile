FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git
RUN pip install git+https://github.com/Asterios7/dlib-wrapper.git

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

# CMD ["main:app", "--host", "0.0.0.0"]

CMD ["main:app", "--host", "0.0.0.0", "--reload"]