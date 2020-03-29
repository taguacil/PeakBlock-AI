#This image runs PeakBlock :
FROM ubuntu:18.04

RUN apt-get -y update && \
    apt-get install -y python-dev python3-dev python3-pip git zlib1g-dev\
                       apt-transport-https ca-certificates wget build-essential\
                       libcurl4-openssl-dev g++ htop nano parallel curl locales\
                       daemontools unzip python3-distutils && \
    apt-get clean

RUN pip3 install --upgrade pip setuptools dumb-init ipython

# Ensure that we always use UTF-8 and with US English locale
RUN locale-gen en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PYTHONIOENCODING utf-8

#Add non-root user to run app
RUN useradd -G users -m runner

WORKDIR /mnt/
COPY . /mnt/
RUN pip3 install -r requirements.txt
#Argument to rebuild from this point after an update
ARG COMMIT_SHA1=1

EXPOSE 5555

#Default configuration
ENV PORT 5555
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

########################################
## PEAKBLOCK DEFAULT ENVIRONMENT VARIABLES ##
########################################

# Environment variables:

#ENV PEAKBLOCK_WEBSERVICE_HOST 0.0.0.0
#ENV PEAKBLOCK_WEBSERVICE_PORT 5050
# Max request size will be 100 megabytes
#ENV PEAKBLOCK_WEBSERVICE_REQUEST_MAX_SIZE 100000000
# request timeout is 10 mins
#ENV PEAKBLOCK_WEBSERVICE_REQUEST_TIMEOUT 600
# graceful shutdown times out in 3 seconds
#ENV PEAKBLOCK_WEBSERVICE_GRACEFUL_SHUTDOWN_TIMEOUT 3
# Websocket max size is 1 MB
#ENV PEAKBLOCK_WEBSERVICE_WEBSOCKET_MAX_SIZE 1000000
#ENV PEAKBLOCK_WEBSERVICE_WEBSOCKET_MAX_QUEUE 32
#ENV PEAKBLOCK_WEBSERVICE_MAX_NUM_ANSWERS 50
#ENV PEAKBLOCK_HOSTNAME DEV_SERVER
# max size of inline text will be 150000 characters:
#ENV PEAKBLOCK_WEBSERVICE_MAX_SIZE_INLINE_TEXT 150000

WORKDIR /mnt/
CMD ["bash" ,"-c", "python3 run.py " ]

#docker stop my_service;docker rm my_service;docker build -t my_service_image -f analytics/deployment/Dockerfile . && docker run -ti --ulimit core=0:0 --user runner --name my_service my_service_image