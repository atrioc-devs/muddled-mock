FROM python:3.11-alpine3.17

ENV CHANNEL ""
ENV CHAT_LOG "/opt/app/sample"
ENV PORT "8765"
WORKDIR /opt/app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8765
CMD python3 ./main.py

