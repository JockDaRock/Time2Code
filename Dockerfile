FROM alpine

RUN apk add -Uuv --no-cache python3 \
    && apk upgrade -v --available --no-cache \
    && apk add ca-certificates && pip3 install --no-cache-dir --upgrade pip setuptools wheel \
    && pip3 install requests certifi flask

# ADD https://github.com/alexellis/faas/releases/download/0.5.1-alpha/fwatchdog /usr/bin

# RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

COPY ide.py .
COPY templates ./templates

ENV fprocess="python3 ide.py"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

EXPOSE 5000

CMD ["python3", "./ide.py"]