ARG BUILD_IMAGE_FOR="deploy"  # or "localdev"
ARG base_build="base-build-${BUILD_IMAGE_FOR}"
ARG PYTHON_VENV="/venv"

FROM python:3.9 AS python-base
ARG PYTHON_VENV
ENV PYTHON_VENV="${PYTHON_VENV}"
ARG venv_bin="${PYTHON_VENV}/bin"
ENV PATH="${PYTHON_VENV}/bin:$PATH"
RUN apt-get update && apt-get install -y gettext
RUN python -m venv "$PYTHON_VENV" && \
    "${venv_bin}/pip" install --upgrade pip setuptools && \
    echo "source \"${venv_bin}/activate\"" >> ~/.bashrc

FROM python-base AS base-build
ARG PYTHON_VENV
ENV PYTHON_VENV="${PYTHON_VENV}"
ARG venv_bin="${PYTHON_VENV}/bin"
ENV APP_DIR=/app
ENV PATH="${PYTHON_VENV}/bin:$PATH"
EXPOSE 8000
RUN apt-get update && apt-get install -y gettext
WORKDIR $APP_DIR
COPY src/requirements/ /requirements/
RUN "${venv_bin}/pip" install -r /requirements/deploy.txt


FROM base-build AS base-build-localdev
RUN echo "Building Image for Local Development"
ENV APP_LOCAL_DEV=1


FROM openjdk:8 AS java
ENV CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
RUN cd /usr/local/lib && curl -O https://www.antlr.org/download/antlr-4.9-complete.jar
# WORKING BUT NO IN Dockefilne
# RUN alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
# RUN alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'


FROM silkeh/clang:9 as clang


CMD ["/bin/bash"]
# FROM ${base_build} AS app
# # ENTRYPOINT [ "executable" ]
