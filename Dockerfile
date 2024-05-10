FROM python:3.12-slim-bookworm as base

# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED TRUE
ENV PYTHONFAULTHANDLER TRUE

RUN echo "Europe/London" > /etc/timezone

RUN pip install --upgrade pip
RUN pip install poetry
RUN apt update
RUN apt install gcc git -y

RUN mkdir -p /home/app
ENV HOME=/home/app
WORKDIR $HOME/

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry config virtualenvs.create false


FROM base as streamlit
EXPOSE 8501
#COPY src .  #volume mounted on compose
RUN poetry install --no-dev --no-interaction
CMD ["streamlit", "run", "streamlit_app.py"]

FROM base as jupyter
EXPOSE 8888

RUN poetry install --no-dev --no-interaction
RUN mkdir -p /home/app/notebooks
CMD ["jupyter", "lab"]
