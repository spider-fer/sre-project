FROM python:3-alpine

WORKDIR /api

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=api.py

EXPOSE 8000

CMD [ "flask", "run","--host","0.0.0.0","--port","8000"]