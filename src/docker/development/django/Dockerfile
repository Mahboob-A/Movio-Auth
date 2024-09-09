# 090924, Monday, 07.00 pm 

# Dockerfile for Django APlp 

ARG PYTHON_VERSION=3.10-bullseye

FROM python:${PYTHON_VERSION} as python 

FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=development

RUN apt-get update && apt-get install --no-install-recommends -y \
        build-essential \
        libpq-dev 

COPY ./requirements . 


RUN pip wheel --wheel-dir /usr/src/app/wheel \
        -r ${BUILD_ENVIRONMENT}.txt 


# image 
FROM python as python-run-stage 

RUN addgroup --system movio && adduser --system --ingroup movio movio

ARG BUILD_ENVIRONMENT=development

# Working dir 
ARG APP_HOME=/home/movio/app 

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 
ENV BUILD_ENV ${BUILD_ENVIRONMENT}


WORKDIR ${APP_HOME}

# static and media files 
RUN mkdir -p ${APP_HOME}/staticfiles ${APP_HOME}/mediafiles && \
        chown -R movio:movio ${APP_HOME}/staticfiles ${APP_HOME}/mediafiles && \
        chmod -R 775 ${APP_HOME}/staticfiles ${APP_HOME}/mediafiles


RUN apt-get update && apt-get install --no-install-recommends -y \
        libpq-dev \
        gettext netcat \
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
        && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheel /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
        && rm -rf /wheels/ 


COPY --chown=movio:movio ./docker/development/django/entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r$//g' /entrypoint.sh

RUN chmod +x /entrypoint.sh

COPY --chown=movio:movio ./docker/development/django/start.sh /start.sh

RUN sed -i 's/\r$//g' /start.sh

RUN chmod +x /start.sh 

COPY --chown=movio:movio . ${APP_HOME} 

RUN chown movio:movio ${APP_HOME} 

USER movio

# Checks Postgres availability 
ENTRYPOINT ["/entrypoint.sh"]