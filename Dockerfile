FROM python:3.8.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /var/www/src

COPY . ./


RUN pip install -r requirements.txt

EXPOSE 8000
RUN ls -la
RUN pwd
CMD ["python", "manage.py" , "runserver", "0.0.0.0:8000"]