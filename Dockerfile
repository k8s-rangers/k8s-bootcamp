FROM python:latest
RUN pip install requests
COPY . /app/
WORKDIR /app
RUN touch logs.txt
CMD ["python","weather.py",">>","logs.txt","sleep 50"]
