FROM python:3.7.3-alpine3.9

WORKDIR /tuxts-backend
COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "tuxts/manage.py", "runserver", "0.0.0.0:8000"]
