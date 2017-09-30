import os
import sys
import json
import groupy
import pynewtonmath as newton

from groupy import Group
from groupy import Bot
from groupy import Member

from flask import Flask, request

app = Flask(__name__)

acceptableMathList = ['simplify', 'factor', 'derive', 'integrate', 'zeroes', 'tangent', 'area', 'cos', 'sin', 'tan', 'arccos', 'arcsin', 'arctan', 'abs', 'log']
group = Group.list().first
bot = Bot.list().first
newMsg = group.messages().newest
author = newMsg.name
bot.post(newMsg.text.split()[0])
# We don't want to reply to ourselves!
if author != 'testbot':
    msgArr = newMsg.text.split()
    if msgArr[0] == '!help':
        msg = 'help me!'
        bot.post(msg)
    elif msgArr[0] == '!math':
        if msgArr[1] not in acceptableMathList:
            msg = 'I couldn\'t understand which operation to perform'
            bot.post(msg)
        elif msgArr[0] == '!math':
            if msgArr[1] == 'simplify':
                bot.post(newton.simplify(msgArr[2]))
            elif msgArr[1] == 'factor':
                bot.post(newton.factor(msgArr[2]))
            elif msgArr[1] == 'derive':
                bot.post(newton.derive(msgArr[2]))
            elif msgArr[1] == 'integrate':
                bot.post(newton.integrate(msgArr[2]))
            elif msgArr[1] == 'zeroes':
                bot.post(newton.zeroes(msgArr[2]))
            elif msgArr[1] == 'tangent':
                bot.post(newton.tangent(msgArr[2], msgArr[3]))
            elif msgArr[1] == 'area':
                bot.post(newton.area(msgArr[2]), msgArr[3], msgArr[4])
            elif msgArr[1] == 'cos':
                bot.post(newton.cos(msgArr[2]))
            elif msgArr[1] == 'sin':
                bot.post(newton.sin(msgArr[2]))
            elif msgArr[1] == 'tan':
                bot.post(newton.tan(msgArr[2]))
            elif msgArr[1] == 'arccos':
                bot.post(newton.arccos(msgArr[2]))
            elif msgArr[1] == 'arcsin':
                bot.post(newton.arcsin(msgArr[2]))
            elif msgArr[1] == 'arctan':
                bot.post(newton.arctan(msgArr[2]))
            elif msgArr[1] == 'abs':
                bot.post(newton.abs(msgArr[2]))
            elif msgArr[1] == 'log':
                bot.post(newton.log(msgArr[2], msgArr[3]))

