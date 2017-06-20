# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals

import os
import sys
import random
import time
import math

from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError,
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
)

app = Flask(__name__)

# Megumi chat bot
"""  
channel_secret = '9d1e7500a205ddaec1c6f2ae0d190e6e'
channel_access_token = 'f/jBF6+aFLuvzEmI0NbPNWjfrsK3Kjwxzzl1XUeLun+3uRs6AbDEQGphezyssudufYiyiHBoLQWWjEBqTtV00P0jLOJuVlrEQly/Xjo7ZQXY0YMEoKm869aWpCnu9Jhog4zt4nb4DYB4zVMWApdjCQdB04t89/1O/w1cDnyilFU='
"""

channel_secret = "9b665635f2f8e005e0e9eed13ef18124"
channel_access_token = "ksxtpzGYTb1Nmbgx8Nj8hhkUR5ZueNWdBSziqVlJ2fPNblYeXV7/52HWvey/MhXjgtbml0LFuwQHpJHCP6jN7W0gaKZVUOlA88AS5x58IhqzLZ4Qt91cV8DhXztok9yyBQKAOSxh/uli4cP4lj+2YQdB04t89/1O/w1cDnyilFU="
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def get_receiver_addr(event):
    global address
    try:
        address = event.source.group_id
    except:
        address = event.source.user_id
    return address

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    global token,original_text,text
    original_text = event.message.text
    text = original_text.lower()
    token = event.reply_token
    get_receiver_addr(event)


    if any(word in text for word in Lines.megumi()):

        if "say " in text : Function.echo()
        elif all(word in text for word in ["pick ","num"])          : Function.rand_int()
        elif any(word in text for word in ["choose ","which one"])  : Function.choose_one_simple()
        elif any(word in text for word in ["what","show"]) :
            if any(word in text for word in ["date ","time"])           : Function.time_date()
            else                                                        : Function.false()
        elif "command3 " in text                                    : Function.notyetcreated()
        elif "command4 " in text                                    : Function.notyetcreated()
        elif "command5 " in text                                    : Function.notyetcreated()

        elif "push " in text                                        : Function.push()
        else                                                        : Function.false()

"""===================================  List of Usable Function & Class ============================================"""

class Function :
    """====================== Main Function List ==========================="""
    def rand_int():

        def random_number(min=1,max=5):
            # just in case
            if min > max :
                temp = min
                min = max
                max = temp

            a = random.randrange(min, max+1)
            b = random.randrange(min, max+1)
            c = random.randrange(min, max+1)
            d = random.randrange(min, max+1)
            e = random.randrange(min, max+1)

            return random.choice([a,b,c,d,e])

        splitted_text = text.split(" ")
        found_num = []
        for word in splitted_text:
            try:
                found_num.append(int(word))
            except:
                continue
        try :
            result = random_number(found_num[0],found_num[1])
            reply = Lines.rand_int() % str(result)
        except :
            reply = "Seems something wrong, try again maybe ?"

        line_bot_api.reply_message(token, TextSendMessage(text=reply))
    def echo():
        try :
            start_index = text.find("say ")+4
            reply = Lines.echo() % str(original_text[start_index:])
        except :
            reply = "What should I say?"

        line_bot_api.reply_message(token, TextSendMessage(text=reply))
    def choose_one():
        splitted_text = text.replace(",", " , ").split(" ")
        print(splitted_text)
        found_options = []
        cursor = 0
        for word in splitted_text:
            # print(word)
            if word == "or":
                # get the previous and after 'or' :
                try:
                    if splitted_text[cursor - 1] != "" and len(splitted_text[cursor - 1]) >= 2:
                        found_options.append(splitted_text[cursor - 1])
                    if splitted_text[cursor + 1] != "" and len(splitted_text[cursor + 1]) >= 2:
                        found_options.append(splitted_text[cursor + 1])
                except:
                    pass

                # check for natural language just in case people use comma, TBH not really important ...

                coloniterate = cursor - 2
                for i in range(0, 4):  # check back 3 times
                    try:
                        if splitted_text[coloniterate - i] == ",":
                            for j in range(1, 4):
                                try:
                                    if coloniterate - i - j >= 0:
                                        if splitted_text[coloniterate - i - j] != "" and len(
                                                splitted_text[coloniterate - i - j]) >= 2:
                                            found_options.append(splitted_text[coloniterate - i - j])
                                            break
                                except:
                                    pass
                    except:
                        pass

                # natural language check end here for each loop ~

            cursor = cursor + 1

        avoid_list = ['megumi', 'kato', 'meg', 'choose', 'or', 'and', ',', ' ']
        found_options = list(set(found_options) - set(avoid_list))
        try :
            result = random.choice(found_options)
            reply = Lines.choose_one() % str(result)
        except :
            reply = " Oops, something wrong... I don't see anything to pick.."
        line_bot_api.reply_message(token, TextSendMessage(text=reply))
    def choose_one_simple():
        splitted_text = text.split(" ")
        found_options = []
        for word in splitted_text:
            if '#' in word:
                try:
                    word = OtherUtil.remove_symbols(word)
                    found_options.append(word)
                except:
                    pass
        try :
            result = random.choice(found_options)
            reply = Lines.choose_one() % str(result)
        except :
            reply = "Try to add '#' before the item, like #this or #that"

        line_bot_api.reply_message(token, TextSendMessage(text=reply))
    def time_date():
        try:
            splited_time = time.ctime().split(" ")
            splitted_hour = splited_time[3].split(":")
            day = Lines.day()[splited_time[0]]
            MM = Lines.month()[splited_time[1].lower()]
            DD = splited_time[2]
            YYYY = splited_time[4]
            hh = splitted_hour[0]
            mm = splitted_hour[1]
            # ss = splitted_hour[2]
            # TimeZone = 7

        except:
            reply = "Seems I can't get the date or time, I wonder why..."
            line_bot_api.reply_message(token, TextSendMessage(text=reply))

        if "date" in text:
            reply = Lines.date(day, DD, MM, YYYY)
        elif "time" in text:
            AmPm = "Am"
            if int(hh) > 12:
                hh = int(hh)
                hh -= 12
                hh = str(hh)
                AmPm = "Pm"

            reply = Lines.time(hh, mm, AmPm)
        line_bot_api.reply_message(token, TextSendMessage(text=reply))

    def push():
        reply = "push message success ~ "
        line_bot_api.reply_message(token, TextSendMessage(text=reply))
    def notyetcreated():
        reply = Lines.notyetcreated()
        line_bot_api.reply_message(token, TextSendMessage(text=reply))
    def false():
        reply = Lines.false()
        line_bot_api.reply_message(token, TextSendMessage(text=reply))

class Lines : # class to store respond lines
    """=================== Main Function Lines Storage ======================="""

    def rand_int():
        lines = ["I think I will pick %s",
                 "How about %s ?",
                 "%s I guess ?",
                 "Let's try %s",
                 "%s ?",
                 "I think %s ?"]
        return random.choice(lines)
    def echo():
        lines = ["%s",
                 "%s :v",
                 "wutt... \n\nbut whatever,,, \"%s\" ahahah",
                 "no xD ! #pfft \n\n\nJK JK okay... \n\"%s\" xD",
                 "... \n\n\n\n\n\"%s\",, I guess (?)",
                 "hee... %s",
                 "\"%s\",, is that good ?",
                 "I don't understand, but \"%s\""]
        return random.choice(lines)
    def choose_one():
        lines = ["I think I will choose %s",
                 "How about %s ?",
                 "%s I guess (?)",
                 "Maybe %s (?)",
                 "%s (?)",
                 "I think %s (?)",
                 "%s then..",
                 "I prefer %s I think.."]
        return random.choice(lines)
    def time(hh,mm,AmPm):
        lines = ["It's %s:%s %s" % (hh,mm,AmPm), #It's 12:24 Am
                 "About %s:%s %s" % (hh,mm,AmPm), #About 12:24 Am
                 "%s:%s :>" % (hh,mm), # 12:24 :>
                 "It's %s:%s right now.." % (hh,mm), #It's 12:24 right now..
                 "Almost %s:%s,," % (hh,mm) ]#Almost 12:24,,
        return random.choice(lines)
    def date(day,DD,MM,YYYY):
        ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])
        lines = ["It's %s, %s %s, %s" % (day, MM,DD,YYYY), #It's Tuesday, June 16, 2017
                 "It's %s of %s" % (ordinal(int(DD)),MM), #It's 16th of June
                 "%s %s, %s" % (MM,DD,YYYY), # June 16, 2017
                 "Today is %s,%s %s" %(day,ordinal(int(DD)),MM), #Today is Tuesday, 16th June
                 "Today's date is %s" % (DD), # Today's date is 16
                 "I think it's %s %s" %(MM,DD)] # I think it's June 16
        return random.choice(lines)

    def notyetcreated():
        lines = ["Gomen,, this function is not ready..",
                 "Gomen,, please try again later :)",
                 "Gomen,, I can't do that yet :\">",
                 "Gomen,, this function is under maintenance :< ",
                 "Gomen,, please try ask me others",
                 "Gomen,, I'm still learning this..",
                 "Gomen,, He hasn't taught me about this yet",
                 "Gomen,, I don't understand this yet.., but I wish I could help :)"]
        return random.choice(lines)
    def false():
        lines = ["Gomen,, what was that ?",
                 "Are you calling me ?",
                 "Hmm ? ",
                 "I wonder what is that",
                 "Maybe you should try to call 'megumi help' (?)",
                 "hmmm... I wonder what is that",
                 " .-. ? ",
                 " what ?? ._. "]
        return random.choice(lines)

    """=================== some extra Lines Storage ======================="""

    def megumi():
        return ['megumi', 'kato', 'meg', 'megumi,', 'kato,', 'meg,']
    def day():
        return {'Mon' : 'Monday' ,
                "Tue" : "Tuesday" ,
                "Wed" : "Wednesday",
                "Thu" : "Thursday",
                "Fri" : "Friday",
                "Sat" : "Saturday",
                "Sun" : "Sunday"}
    def month():
        return {'jan' : 'January',
                'feb' : 'February',
                'mar' : 'March',
                'apr' : 'April',
                'may' : 'May',
                'jun' : 'June',
                'jul' : 'July',
                'aug' : 'August',
                'sep' : 'September',
                'oct' : 'October',
                'nov' : 'November',
                'dec' : 'December'}

class OtherUtil :
    def remove_symbols(word):
        symbols = "!@#$%^&*()_+=-`~[]{]\|;:'/?.>,<\""
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")  # strong syntax to remove symbols
        if len(word) > 0:
            return word


"""=============================================================================================================="""

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)