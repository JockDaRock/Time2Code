FROM alpine

RUN apk add -Uuv --no-cache python3 \
    && apk upgrade -v --available --no-cache \
    && apk add ca-certificates && pip3 install --no-cache-dir --upgrade pip setuptools wheel \
    && pip3 install requests flask markdown pymdown.extensions Pygments

WORKDIR /root/

COPY static ./static
COPY ide-server.py .
COPY templates ./templates

EXPOSE 5555

CMD ["python3", "ide-server.py"]