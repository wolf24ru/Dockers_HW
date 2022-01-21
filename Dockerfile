FROM python:3.9.6-alpine

WORKDIR /usr/src/CRUD

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Django_project .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# ENV SECRET_KEY="sd1fsd2f11sdf21sd54f"
# ENV DEBUG = "True"

CMD [ "python", "manage.py", "migrate", "--noinput" ]
