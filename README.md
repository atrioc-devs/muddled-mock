A cheap mock server for muddled-ws.

**Requirements**

- [Docker](https://docker.com)
- A chatlog CSV (see below)
- **Without Docker**
  - [Python 3.11](https://www.python.org/)
  - [pipenv 2023.10](https://pypi.org/project/pipenv/) or pip v23

**Chatlog CSV**

You can acquire a copy of a VOD chat from
[here](https://www.twitchchatdownloader.com/). We read the CSV in the following
format below. Then the path to the CSV is declared through the `CHAT_LOG`
environment variable.

```csv
time,user_name,user_color,message
1,justinfan,#6BFF9A,"Hello world!"
```

# Setup

```sh
docker run -p 8765:8765 -e CHANNEL=atriocdevs -v $PWD/sample:/opt/app/sample ghcr.io/atrioc-devs/muddled-mock:latest
```

