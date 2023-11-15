#!/usr/bin/env python3
"""A cheap mock Twitch chat Websocket+IRC mock server for atrioc-devs/muddled-ws"""
import asyncio
import os
import csv
from websockets.server import serve

PORT=os.getenv('PORT')
TWITCH_CHANNEL=os.getenv('CHANNEL')
CHAT_LOG=os.getenv("CHAT_LOG")

def read_log(channel: str, path: str) -> list:
    """
    CSV Format Example

    ```csv
    time,user_name,user_color,message
    1,justinfan,#6BFF9A,"Hello world!"
    ```

    Parameters:
        channel: str The channel this log is from
        path: str Chat log CSV location
    Returns:
        List[str] [...[time, user_name, user_color, message]]
    """
    result = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        chatreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in chatreader:
            result.append(format_message(channel, row))
    return result

def format_message(channel: str, data: list) -> str:
    """
    Parameters:
        data: List[str] = [time, user_name, user_color, message]
    Result:
        str :user_name!username@username.tmi.twitch.tv PRIVMSG #channel :message
    """
    author = data[1]
    message_raw = data[3]
    message = message_raw[1:len(message_raw) - 1]
    return f':{author}!{author}@{author}.tmi.twitch.tv PRIVMSG #{channel} :{message}'

async def send(websocket, data: str):
    """Send data with trailing CRLF"""
    await websocket.send(f"{data}\r\n")

async def ping(websocket):
    """Broadcast ping to connected peers"""
    while True:
        await asyncio.sleep(5)
        await send(websocket, "PING :tmi.twitch.tv")

async def mock_handler(websocket):
    """WebsocketServer handler"""
    asyncio.create_task(ping(websocket))
    async for message in websocket:
        if message == "PING :tmi.twitch.tv":
            await send(websocket, "PONG :tmi.twitch.tv")
        elif message == f"JOIN #{TWITCH_CHANNEL}":
            for chat_message in read_log(TWITCH_CHANNEL, CHAT_LOG):
                await asyncio.sleep(1)
                await send(websocket, chat_message)

async def main():
    """
    Required environment variables
     - CHANNEL
     - CHAT_LOG
    """
    port=int(PORT) if len(PORT) > 0 else 8765
    async with serve(mock_handler, "0.0.0.0", port):
        print(f"Listening 0.0.0.0:{port}")
        await asyncio.Future()  # run forever

asyncio.run(main())

