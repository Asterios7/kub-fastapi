FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit" ]

CMD [ "run", "main.py" ]