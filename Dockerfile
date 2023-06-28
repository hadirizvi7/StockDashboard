# WORK IN PROGRESS
FROM ubuntu:20.04
RUN apt update
RUN apt install -y python3
COPY . /usr/bin/
WORKDIR /usr/bin
RUN pip3 install -r requirements.txt
ENTRYPOINT [ “python3”]
CMD [“src/main.py”]