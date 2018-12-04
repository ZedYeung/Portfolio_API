FROM python:alpine

LABEL maintainer="Yue Yang <yeungzed@gmail.com>"

# Set work directory
COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

# Run http server on port 8088
EXPOSE 8088

ENTRYPOINT ["gunicorn", "api:app", "-b", "0.0.0.0:8088"]
