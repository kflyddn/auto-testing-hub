# base container image
FROM docker-registry.digitalalchemy.net.au/python:3.6.1

# set environment variables for system
ENV TZ America/Los_Angeles

# setup working directory within container
RUN mkdir -p /data/auto-testting
RUN mkdir -p /data/auto-testting/testcode
WORKDIR /data/auto-testting

# copy requirements.txt for pip install
COPY requirements.txt /data/auto-testting/requirements.txt

# setup python environment, import required modules
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt


# Settings for the local user
ENV APP_USER docker
ENV APP_USER_UID 1000
ENV APP_USER_GROUP docker
ENV APP_USER_GROUP_GID 996

# Create user
RUN groupadd --gid ${APP_USER_GROUP_GID} ${APP_USER_GROUP}
RUN useradd --uid ${APP_USER_UID} --create-home -g ${APP_USER_GROUP} ${APP_USER}

RUN chown -R $APP_USER:$APP_USER_GROUP /data/auto-testting

# copy project files into working directory
USER ${APP_USER}
#COPY . /data/selenium

