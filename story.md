# legend-of-8ball-bot

_* Names are anonymized with random gfycat URLs to protect the identities of the original people._

_* TLDR; skip to [Decline](#decline)_


### Start

I usually only lurk in Twitch channels that I watch, except for the occasional reaction image spam, for when the streamer messes up, or a general comedic timing. Its fun to be a part of a huge community, cheering on the streamer together. Although occasionally we get called out as [backseating](https://www.urbandictionary.com/define.php?term=Backseat%20Gamer).

I have been frequenting a streamer for his variety streaming. His streams were generally entertaining, and the community was fun to be with. One day, I decided to stick around while the stream had not started. The chat is not as active, with only a handful of people. The slower pace of conversation allows the people to get to know each other better and closer. In the end, I got to know a handful of people who do programming as well, and it was nice.

One of the moderators of the Twitch channel, who goes by the name **HighCleverDromaeosaur**, was kind enough to gift a Twitch Subscription, to me. I was overjoyed and honored. Its as if someone actually acknowledged my existence, and invited me to be a part of the bigger community.


### Rise

At the same time, I was fiddling around with a basic IRC Twitch bot. The original intention was simple, archive the chat messages. If one wishes to be more ambitious, one could feed the logs into neural network, or even churn out statistics. But to start with, let's just archive things.

```python
def sync_fn(con, channel, epoch, user, msg):
    with open('out.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow((epoch, user, msg))
```

And for its basic purpose, it worked! Occasionally my home network dies, and I did not write a proper handler for that, so I had to rerun the script again. But its not too long before I realized, with `user` and `msg`, you can write functions that respond to command, like how a bot would.

But, the stream I frequented already had two well known bots, in which both were controlled by moderators as well. In a bid to help out, I asked if they were open-sourced. **QuaintReliableDorado** replied that his bot is not ready for the world, which was understandable. While **AgreeableCloseGalago** did not reply to my questions. To note, the bots in place were rather comprehensive, with an in-chat currency, and games which allow you to have fun with them.

Alright then, maybe I will try writing my own bot, and it will be open-source. But what command would be fun? And then I thought of something really, really basic. A simple Magic-8 Ball. Just fire `!8ball {question}`, and get answers. Hey wouldn't that be fun?


### Summit

After several hours of sloppy coding, it was done! With an array of official answers and a random number generator, 8BallBot started dishing out answers. And it was fun. People were asking ridiculous questions, and they have gotten some really funny answers from 8BallBot. Over the time it was running, I also had help from **QuaintReliableDorado**, who was kind enough to point out that I have to watch out for the chat rate limit in Twitch.

```
EssentialGiantAmethystsunbird: !8ball will i ever get laid?
8BallBot                     : yes - definitely
JauntyFinishedHoverfly       : !8ball are you sure EssentialGiantAmethystsunbird will be getting laid?
8BallBot                     : without a doubt
```

8BallBot provided a fun time for the community, and that was good. But at the end of the day, when I go to sleep and turn off the computer, 8BallBot will rest as well. I am assuming that the moderator bots run on servers, and have a better uptime and management than I do. If they had this implemented, it would be good! 8BallBot can be phased out, and be a part of something bigger.


### Decline

**HighCleverDromaeosaur** had told me that generally the streamer and **AgreeableCloseGalago** did not like too many bots, for it will interfere with the chat when the stream is online. And I agreed with that. I thought 8BallBot was generally harmless, as it only provided one sentence of reply, but clearly I thought wrong.

**AgreeableCloseGalago** was online, and said that he had implemented `!8ball` into his own bot. And I was glad, my efforts had been successful. After **AgreeableCloseGalago** tried it out once, his bot had responded with a Magic-8 Ball response. Great! 8BallBot, you have done well for your time. Its time to put you to rest!

I started typing out the messages to congratulate **AgreeableCloseGalago** on implementing Magic-8 Ball, but I was surprised to know that I was instead banned for ten hours.

Wait, I am banned?

Oh, he probably thinks that my bot is still active, and did a ban for now. Maybe after a minute or two, I can post again!

Maybe after five minutes!

Maybe after ten minutes.

Maybe.


### Reason

Truth be told, I was truly devastated. It felt like a low blow punch to the gut, but I guess I have to take it like a man? Again, I clarify, I do not mind having to phase out 8BallBot. But being banned after, I felt as if someone had pressed S to spit on me. Even now when I think about it, I get pretty sad about it. As the whole community embraces the new `!8ball`, I was casted aside, as if I was never part of the community, as if I would be better off gone.

I contacted **AgreeableCloseGalago** on why I was banned, and informed him that I did not mind him implementing `!8ball`, and I took down 8BallBot too. His reason was the same as what **HighCleverDromaeosaur** had warned me about, too many bots. I could not accept that as an asnwer, and I was too frustrated to discuss about this with him any further. I left a good day wish, and closed the Whisper tab.

**QuaintReliableDorado** soon let me know that my ban was lifted. I gave him my two cents, but I know that there is nothing much he could do either. Him removing the ban was the kindest thing he could do for me. Along with **HighCleverDromaeosaur**, a couple more users of 8BallBot asked if 8BallBot was well.

Its nice to know that there are some who cared, but I do not know. I guess I will go back to lurking. I guess I'm too tired of being a part of community.

Does not really matter now, does it?


### Parting

Deepest thanks to:

- **HighCleverDromaeosaur**, for the gift subscription.
- **QuaintReliableDorado**, for your kind help on bots.
- And many other users of 8BallBot.

It was a fun ride. It was nice to know you. It was nice to be of service to you, 8BallBot.
