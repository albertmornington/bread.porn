FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python3 virtualenv make
ADD . /srv/code
WORKDIR /srv/code
RUN make venv
CMD /srv/code/venv/bin/python /srv/code/breadporn.py
