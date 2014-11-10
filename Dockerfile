FROM ubuntu:14.04.1
RUN apt-get update && apt-get -y install git python2.7
RUN mkdir /workspace
WORKDIR /workspace/app
ENTRYPOINT ["/usr/bin/python2.7", "test_foo.py"]
