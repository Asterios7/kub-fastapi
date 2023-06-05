FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install deepface==0.0.78
RUN pip install fastapi==0.95.1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./backend

EXPOSE 8000

ENTRYPOINT ["uvicorn"]

# CMD ["main:app", "--host", "0.0.0.0"]

CMD ["backend.main:app", "--host", "0.0.0.0", "--reload"]