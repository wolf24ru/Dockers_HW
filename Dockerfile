FROM python:3

WORKDIR /usr/src/CRUD

COPY Django_project Django_project

RUN pip install --no-cache-dir -r Django_project/requirements.txt

ENV SECRET_KEY="sd1fsd2f11sdf21sd54f" 
ENV DEBUG = "True"

CMD [ "python", "Django_project/manage.py", "migrate" ]

CMD [ "python", "Django_project/manage.py", "runserver", "0.0.0.0:8000" ]
