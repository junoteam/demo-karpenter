FROM python:3.9

ARG USERNAME=flask
ARG USER_UID=1000
ARG USER_GID=$USER_UID

WORKDIR /app

RUN apt update -y && apt install htop vim -y

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -d /home/$USERNAME -s /bin/bash \
    && chown -R ${USER_UID}:${USER_GID} .

USER $USERNAME
ENV PATH "/home/$USERNAME/.local/bin:$PATH"

COPY . /app
RUN pip install -r requirements.txt

ENV FLASK_APP=development

CMD ["gunicorn", "--conf", "./gunicorn_conf.py", "--bind", "0.0.0.0:80", "app:app"]