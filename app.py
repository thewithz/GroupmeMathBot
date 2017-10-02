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

@app.route('/', methods=['POST'])
def webhook():
    newMsg = group.messages().newest
    author = newMsg.name
    # We don't want to reply to ourselves!
    if author != 'testbot':
        msgArr = newMsg.text.split()
        if msgArr[0] == '!help':
            msg = 'Examples\n!math simplify 2x+4x-5 = 6x-5\n!math factor x^4-x^2 = x^2 (x+1) (x-1)\n!math integrate 10x = 5x^2\n!math tangent x^2 4\n!math area -x^2 3 8'
            bot.post(msg)
            return 'ok', 200
        elif msgArr[0] == '!math':
            if msgArr[1] not in acceptableMathList:
                msg = 'I couldn\'t understand which operation to perform'
                bot.post(msg)
                return 'ok', 200
            elif msgArr[0] == '!math':
                if msgArr[1] == 'simplify':
                    bot.post(str(newton.simplify(msgArr[2])))
                elif msgArr[1] == 'factor':
                    bot.post(str(newton.factor(msgArr[2])))
                elif msgArr[1] == 'derive':
                    bot.post(str(newton.derive(msgArr[2])))
                elif msgArr[1] == 'integrate':
                    bot.post(str(newton.integrate(msgArr[2])))
                elif msgArr[1] == 'zeroes':
                    bot.post(str(newton.zeroes(msgArr[2])))
                elif msgArr[1] == 'tangent':
                    bot.post(str(newton.tangent(msgArr[2], int(msgArr[3]))))
                elif msgArr[1] == 'area':
                    bot.post(str(newton.area(msgArr[2], int(msgArr[3]), int(msgArr[4]))))
                elif msgArr[1] == 'cos':
                    bot.post(str(newton.cos(msgArr[2])))
                elif msgArr[1] == 'sin':
                    bot.post(str(newton.sin(msgArr[2])))
                elif msgArr[1] == 'tan':
                    bot.post(str(newton.tan(msgArr[2])))
                elif msgArr[1] == 'arccos':
                    bot.post(str(newton.arccos(msgArr[2])))
                elif msgArr[1] == 'arcsin':
                    bot.post(str(newton.arcsin(msgArr[2])))
                elif msgArr[1] == 'arctan':
                    bot.post(str(newton.arctan(msgArr[2])))
                elif msgArr[1] == 'abs':
                    bot.post(str(newton.abs(msgArr[2])))
                elif msgArr[1] == 'log':
                    bot.post(str(newton.log(int(msgArr[2]), int(msgArr[3]))))
    return 'ok', 200

