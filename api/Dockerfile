FROM python:3.9

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv

RUN pipenv requirements > requirements.txt
# will use pipenv to create list of all requirements from pipenv file.
RUN pip install -r requirements.txt
# Install dependencies using pipenv, and create a virtual environment in the container


EXPOSE 5050

COPY . ./

CMD ["python", "main.py"]

# L116








