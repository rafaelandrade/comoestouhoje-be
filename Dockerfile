from python:3.7

EXPOSE 5000
ENV PORT=5000

WORKDIR /app
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4003"]
