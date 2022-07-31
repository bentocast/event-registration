FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="/workspace"

COPY . .
RUN pip3 --disable-pip-version-check --no-cache-dir install -r requirements.txt
RUN python manage.py showmigrations
RUN python manage.py migrate

EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]