FROM alpine

RUN apk add -Uuv --no-cache python3 \
    && apk upgrade -v --available --no-cache \
    && apk add ca-certificates && pip3 install --no-cache-dir --upgrade pip setuptools wheel \
    && pip3 install requests flask markdown

# ADD https://github.com/alexellis/faas/releases/download/0.6.15/fwatchdog /usr/bin
ADD https://github.com/openfaas-incubator/of-watchdog/releases/download/0.2.1/of-watchdog /usr/bin/fwatchdog


RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

# COPY ide.py .
COPY ide_server.py .
COPY handler.py .
COPY templates ./templates

ENV fprocess="python3 handler.py"
ENV cgi_headers=true
ENV cgi_body=true
ENV mode=http

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]