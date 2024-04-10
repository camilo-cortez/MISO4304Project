FROM python:3.9

EXPOSE 3004

WORKDIR /blacklist

COPY . /blacklist/

RUN pip install pipenv && pipenv install

ENV PYTHONPATH /blacklist

ENTRYPOINT ["pipenv", "run", "python", "./src/main.py"]