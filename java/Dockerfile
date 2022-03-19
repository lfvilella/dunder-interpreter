FROM openjdk:8

ENV CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"

RUN apt-get update
RUN apt-get install vim -y

RUN cd /usr/local/lib && curl -O https://www.antlr.org/download/antlr-4.9-complete.jar

WORKDIR /app

CMD ["/bin/bash"]
