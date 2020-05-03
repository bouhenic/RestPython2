FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk add nano
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]