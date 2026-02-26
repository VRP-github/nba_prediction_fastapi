FROM python:3.12-slim

WORKDIR /nba_prediction

COPY . /nba_prediction

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["fastapi", "run", "main.py"]