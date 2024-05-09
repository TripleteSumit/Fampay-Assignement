FROM python:alpine3.19
RUN addgroup app && adduser -S -G app app
USER app
WORKDIR /fam

COPY requirements.txt .
RUN ["pip","-r","install","requirements.txt"]
COPY . .

ENV DEFAULT_API_KEY=$DEFAULT_API_KEY
ENV API_KEY_1=$API_KEY_1
EXPOSE 8000 6379 3306

CMD [ "python" ,"manage.py","runserver"]