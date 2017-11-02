#!/usr/bin/python
# -*- coding: utf-8 -*-
import speedtest
import tweepy
import random
from secrets import consumer_key, consumer_secret, access_token, \
    access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

CONSTANT_PAYDOWN = 100
CONSTANT_PAYUP = 40


def tweet_textonly(message):
    api.update_status(message)
    return


def choose_speedtest_message(downspeed, upspeed):
    message_list = read_list('complaints')
    message = random.choice(message_list)
    message = message.format(downspeed,upspeed,downspeed)
    print(message)
    #tweet_textonly(message)
    return

def speed_test():
    results = []
    servers = [3254]
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    downspeed = s.download()
    downspeed = int(downspeed / 1048576)
    upspeed = s.upload()
    upspeed = int(upspeed / 1048576)
    results.append(downspeed)
    results.append(upspeed)
    return results

def read_list(file):
    possible_strings  = [line.rstrip('\n') for line in open(file)]
    return possible_strings


def choose_bantz():
       message_list = read_list('sassList')
       message = random.choice(message_list)
       print(message)
       #tweet_textonly(message)
       return


choose_speedtest_message(23,67)

