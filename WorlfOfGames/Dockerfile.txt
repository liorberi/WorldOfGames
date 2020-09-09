FROM python:3.8.3-alpine
        COPY . .
        RUN pip install Flask==1.1.2
        CMD python MainGame.py