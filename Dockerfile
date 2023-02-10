FROM python:buster

RUN python3 -m pip install -U discord.py

WORKDIR /app

COPY ["./VoteBot.py", "token", "./"]

ENTRYPOINT [ "python3", "VoteBot.py" ]