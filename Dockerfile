FROM python:3.12-alpine
LABEL maintainer="Konstantin-SVT"

WORKDIR app/

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p app/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    secret-user

RUN chown -R secret-user app/media
RUN chmod -R 755 app/media

USER secret-user