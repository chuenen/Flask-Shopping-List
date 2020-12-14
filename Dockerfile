FROM python:3.7.4
WORKDIR /workspace
COPY . ./
RUN pip install pipenv==2020.11.15 \
    && pipenv install --deploy --system \
    && rm Pipfile*


# vi:et:ts=2:sw=2:cc=80
