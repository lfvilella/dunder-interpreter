FROM silkeh/clang:9

RUN apt-get update && apt-get install -y python3 python3-pip
COPY src/requirements/ /requirements/
RUN pip install --upgrade pip && pip install -r /requirements/deploy.txt
