FROM ubuntu:20.04
FROM python:3.9

RUN apt-get -y update && apt-get install -y ffmpeg
RUN pip3 install -U openai-whisper
RUN echo "All packages installed successfully"

COPY jfk.flac .

COPY jfk.txt .

COPY main.py .

CMD [ "python3", "main.py"]