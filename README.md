# NBN Twitter Shade Throwing Bot
This twitter bot puts a different spin on "Speed Complainer bots" (bots that tweet are your ISP if your internet connection is slower than you pay for) there is a good one by [James Atkinson](https://github.com/james-atkinson/speedcomplainer).

This bot tests your internet connection every hour and tweets at your ISP if the download speed is below 70% of what you pay for. Along with this, the bot also throws shade at NBN Co every day, picking a message randomly from a list ("sassList")

Currently the bot:
*Tests internet connection and complains about slow speeds if needed
*Throws shade everyday from a list of responses

Future Functions
- [ ] Tweet a historical graph of past internet speeds when asked
- [ ] Reply everytime NBN Co tweets with some playful bantz

Improvements needed
- [ ] Use the Tweepy Streamer object so the bot can pull new tweets constantly instead of being run from a cron job periodically 
- [ ] Add more zingers to the sassList (ongoing)

It's pretty obvious that this is not a serious bot, feel free to use it purely as a speed complainer but there are much better options out there (that also don't target just NBN Co) This was born out of frustration/ something to do with my limited Python knowledge 
