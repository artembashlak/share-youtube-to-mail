FROM jenkins/jenkins:2.249.2-lts-jdk11
USER root
RUN apt-get update
RUN apt-get install -y python-pip
# Install app dependencies
RUN pip install --upgrade pip
