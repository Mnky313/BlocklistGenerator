FROM python:3.12
RUN pip install requests schedule

ADD app /app
WORKDIR /app

CMD ["python", "./grab_lists.py"]
