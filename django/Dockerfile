FROM python:3.5

ENV PYTHONUNBUFFERED=1
ENV C_FORCE_ROOT=1
ENV DJANGODIR=/webapp

RUN mkdir $DJANGODIR
WORKDIR $DJANGODIR

COPY requirements.txt $DJANGODIR/
RUN pip install -r requirements.txt

COPY . $DJANGODIR/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
