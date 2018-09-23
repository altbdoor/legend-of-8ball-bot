import importlib
import json
import signal
import socket
import sys
import threading
import time

import handler

NEWLINE = '\r\n'
RECEIVE_BYTES = 4096


config = None

with open('config.json') as f:
    config = json.load(f)

con = socket.socket()
con.connect((config['twitch_endpoint_host'], config['twitch_endpoint_port']))
con.setblocking(False)


def send_bytes(message):
    con.send((f'{message}{NEWLINE}').encode('utf-8'))


def signal_handler(sig, frame):
    con.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

send_bytes(f'PASS {config["password"]}')
send_bytes(f'NICK {config["username"]}')
send_bytes(f'JOIN #{config["twitch_channel"]}')

pong_str = 'PONG :tmi.twitch.tv'
privmsg_key = f'PRIVMSG #{config["twitch_channel"]} :'

while True:
    time.sleep(1)

    try:
        response = con.recv(RECEIVE_BYTES).decode('utf-8')
        response_list = response.split(NEWLINE)

        for r in response_list:
            if r.startswith('PING :'):
                send_bytes(pong_str)

            elif privmsg_key in r:
                response_text = r.split(privmsg_key)[1]
                response_user = r.lstrip(':').split('!')[0]
                response_epoch = int(round(time.time() * 1000))

                importlib.reload(handler)
                args = (
                    con,
                    config["twitch_channel"],
                    response_epoch,
                    response_user,
                    response_text,
                )

                thread = threading.Thread(target=handler.async_fn, args=args)
                thread.daemon = True
                thread.start()

                handler.sync_fn(*args)

    except socket.error:
        continue
