FROM python:3.9

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv requirements > requirements.txt
# + will use pipenv to create list of all requirements from pipenv file.
RUN pip install -r requirements.txt
# Install dependencies using pipenv, and create a virtual environment in the container


EXPOSE 5050

COPY . ./

CMD ["python", "main.py"]



# L116
# ---------- IMAGES
# docker build .
# docker images

# docker build . -t images-gallery-api
# docker images

# ---------- CONTAINERS
# docker run -p 5050:5050 images-gallery-api

# docker exec -it practical_saha bash
# i = interactive, t = terminal

# docker run -it images-gallery-api /bin/bash


