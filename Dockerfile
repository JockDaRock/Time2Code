FROM python:alpine

RUN apk update && apk add git

ADD https://github.com/alexellis/faas/releases/download/0.5.1-alpha/fwatchdog /usr/bin

RUN chmod +x /usr/bin/fwatchdog

WORKDIR /root/

COPY test_methods.py .

ENV fprocess="python test_methods.py"

HEALTHCHECK --intervals=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]