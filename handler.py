import random
import time


def send_bytes(con, channel, msg):
    con.send((f'PRIVMSG #{channel} : {msg}\r\n').encode('utf-8'))


def sync_fn(con, channel, epoch, user, msg):
    pass


def async_fn(con, channel, epoch, user, msg):
    if msg.startswith('!8ball'):
        answer_list = [
            'it is certain',
            'it is decidedly so',
            'without a doubt',
            'yes - definitely',
            'you may rely on it',
            'as I see it, yes',
            'most likely',
            'outlook good',
            'yes',
            'signs point to yes',
            'reply hazy, try again',
            'ask again later',
            'better not tell you now',
            'cannot predict now',
            'concentrate and ask again',
            "don't count on it",
            'my reply is no',
            'my sources say no',
            'outlook not so good',
            'very doubtful',
        ]

        time.sleep(1)
        answer_index = random.randint(0, len(answer_list) - 1)
        send_bytes(con, channel, f'[8ball] @{user}, {answer_list[answer_index]}')
