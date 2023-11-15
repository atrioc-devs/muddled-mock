FROM python:3.11-alpine3.17

ENV CHANNEL ""
ENV CHAT_LOG "/opt/app/sample"
ENV PORT "8765"
WORKDIR /opt/app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python3 ./main.py

