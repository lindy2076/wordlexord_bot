FROM python:3.10 as builder
RUN python3.10 -m venv /usr/share/python3/app
COPY . /appp
EXPOSE 8080
WORKDIR /appp
RUN /usr/share/python3/app/bin/pip install -r requirements.txt
CMD ["/usr/share/python3/app/bin/python3", "-m", "word_lexord_bot"]