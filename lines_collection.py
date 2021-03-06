import random


class Lines:  # class to store respond lines
    """=================== Main Function Lines Storage ======================="""

    @staticmethod
    def general_lines(cond):
        if cond == "failed to open page":  # Take 1 argument : web page
            lines = ["Sorry, '%s' is currently unreachable...",
                     "I think %s is down right now, it's unreachable...",
                     "I can't open %s.. I wonder if it's down right now...",
                     "Seems %s is unreachable right now...",
                     "How about trying again later? %s is unreachable right now..."]
        elif cond == "formatting error":  # Take 1 argument : what kind of data
            lines = ["I'm sorry, I can get the %s data, but seems it's corrupted... :<",
                     "I have the %s data, but somehow it's corrupted in a one another way... :<",
                     "I kinda have the %s data somehow..,\nBut I can't gather the information you want right now.. ",
                     "Ugh... %s data is somehow different from normal data,..\nI can't send it to you unless I know it's safe...",
                     "It's weird...I can't prettify the %s data...\nI'm sure you don't want a messy data right? "]
        elif cond == "search fail":  # Take 1 argument : something being searched
            lines = ["Try to put the %s, I need it ^^ ",
                     "Seems there's no %s ._. ",
                     "I don't see any %s ._. ",
                     "How about try again with %s included ?",
                     "Have you put in the %s already ? .-. "]
        elif cond == "offline":
            lines = ["Gomen, Megumi's currently unable to play with you :>",
                     "Gomen, Megumi will be back soon",
                     "Gomen, I'm having a date right now ..see ya later..",
                     "Gomen, Megumi's taking her break time...",
                     "Megumi will be back shortly ~ "]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def rand_int(cond):

        if cond == "success":  # Take 1 argument : number
            lines = ["I think I will pick %s",
                     "How about %s ?",
                     "%s I guess ?",
                     "Let's try %s",
                     "%s ?",
                     "I think %s ..."]
        elif cond == "failed":
            lines = ["Seems something wrong, try again maybe ?",
                     "Try to put only two numbers...",
                     "How about try again ?",
                     "Seems something wrong, maybe try again ?",
                     "Try to put two numbers at most :)"]
        elif cond == "default":  # Take 1 argument : number
            lines = ["Since you didn't specify, I'll choose between 1 to 5\n",
                     "I'll pick from 1 to 5 kay..\n",
                     "I'll limit the range from 1 to 5..\n",
                     "Usually I chose between 1 to 5...\n",
                     "Let say the minimum is 1 and maximum is 5..\n"]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def echo(cond):

        if cond == "success":  # Take 1 argument : text to be echo-ed
            lines = ["%s",
                     "%s :v",
                     "wutt... \n\nbut whatever,,, \"%s\" ahahah ^^ ",
                     "no xD ! #pfft \n\n\nJK JK okay... \n\"%s\" xD",
                     "... \n\n\n\n\n\"%s\",, I guess (?)",
                     "hee... %s",
                     "\"%s\",, is that good ? :3 ",
                     "Suree... \"%s\""]
        elif cond == "failed":
            lines = ["What should I say?",
                     "Which one?",
                     "Which one should I echo?",
                     "?? ._.\nWhat do you want me to say?",
                     "Which one should I say again?"]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def choose_one(cond):

        if cond == "success":
            lines = ["I think I will choose %s",
                     "How about %s ?",
                     "%s I guess (?)",
                     "Maybe %s (?)",
                     "%s (?)",
                     "I think %s (?)",
                     "%s then..",
                     "I prefer %s I think.."]
        elif cond == "fail":
            lines = ["Try to add '#' before the item, like #this or #that",
                     "I'm sorry, but please add '#' before the item",
                     "Gomen,, I didn't catch that...",
                     "Gomen,, what do you want me to choose ? ",
                     "Gomen,, I can only choose from item with '#' .. ",
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def date_time(cond):

        if cond == "show date":  # Take 5 format arguments : 0.day 1.DD 2.ordinal(int(DD) 3.MM 4.YYYY
            lines = ["It's {0}, {3} {1}, {4}",  # It's Tuesday, June 16, 2017
                     "It's {2} of {3}",         # It's 16th of June
                     "{3} {1}, {4}",            # June 16, 2017
                     "Today is {0},{2} {3}",    # Today is Tuesday, 16th June
                     "Today's date is {1}",     # Today's date is 16
                     "I think it's {3} {1}"     # I think it's June 16
                     ]
        elif cond == "show time":  # Take 3 format arguments : 0.hh 1.mm 2.AmPm
            lines = ["It's {0}:{1} {2}",  # It's 12:24 Am
                     "About {0}:{1} {2}",  # About 12:24 Am
                     "{0}:{1} :>",  # 12:24 :>
                     "It's {0}:{1} right now..",  # It's 12:24 right now..
                     "Almost {0}:{1},,"  # Almost 12:24,,
                     ]
        elif cond == "formatting error":
            lines = ["Seems there's kind of formatting error..",
                     "I think there's kind of formatting error...",
                     "I have the data, but I can't show it to you right now...",
                     "Seems the data is kinda messy...",
                     "I wonder why it's messy like this..."]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def invite(cond):

        if cond == "header":  # Take 1 argument : sender
            lines = ["Konichiwa, %s invite you to : ",
                     "Nee,, %s invite you to : ",
                     "Konichiwa,, you got invitation from %s : ",
                     "Nee,,you got invitation from %s : ",
                     "Sumimasen,, you got invitation from %s : "
                     ]
        elif cond == "success":  # Take 1 argument : amount of invitation sent
            lines = ["Done,, %s invitations sent ^^ ",
                     "Invitations sent, Megumi has delivered %s invitation",
                     "Megumi has delivered your invitation to %s participant",
                     "Done,, Megumi has sent your invitation to %s person",
                     "Megumi report : %s invitations sent successfully"
                     ]
        elif cond == "failed":
            lines = ["Gomenne, seems I can't send the invitation..",
                     "Seems something wrong about the invitation, wanna check it once more time ?",
                     "Megumi can't send your invitation right now.. sorry..",
                     "Hmm.. I wonder why I can't send your invitation though...",
                     "Gomen, please try to send the invitation again.."
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def invite_report(cond):

        if cond == "respond recorded":
            lines = ["Thanks for your response, Megumi will pass it right now ~",
                     "OK..Megumi will let (him/her) know...",
                     "I see.. thanks for your response ..",
                     "Thanks,, Megumi will tell (him/her) ASAP ^^",
                     "Kay, I will let (him/her) know.."
                     ]
        elif cond == "desc missing":
            lines = ["I think the description is missing...",
                     "Megumi will still send the invitation, even though there is no description..",
                     "Try to add description next time ,kay ? ^^ ",
                     "If you want to add description next time, just surround description with (*)",
                     "It's ok not having description, but it would be better to have it."
                     ]
        elif cond == "participant list missing":
            lines = ["I think the participant list is missing...",
                     "Megumi can not send the invitation, since there is no participant list..",
                     "Try to add participant list next time ,kay ? ^^ \n(not sent) ",
                     "If you want to add participant list next time, just use 'to participant_list'",
                     "If there is no participant list, it will not be sent."
                     ]
        elif cond == "yes":  # Take 1 argument : responder
            lines = ["About the invitation, %s said that (he/she) will come..",
                     "About the invitation, %s said 'OK'",
                     "About the invitation, %s confirmed 'OK'",
                     "About the invitation, %s said 'sure~'",
                     "About the invitation, I think %s said 'OK'"
                     ]
        elif cond == "no":  # Take 1 argument : responder
            lines = ["About the invitation, %s said sorry that (he/she) can't go..",
                     "About the invitation, %s rejected the offer",
                     "About the invitation, %s declined the offer",
                     "About the invitation, %s said 'maybe later'",
                     "About the invitation, I think %s said that (he/she) can't fulfill the request"
                     ]
        elif cond == "pending":  # Take 1 argument : responder
            lines = ["About the invitation, %s is still thinking whether going or not",
                     "About the invitation, %s will contact you later..",
                     "About the invitation, %s is unsure about that invitation outcome",
                     "About the invitation, %s can't guarantee (his/her) approval",
                     "About the invitation, %s said that (he/she) will think about it"
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def show_cinema_movie_schedule(cond):

        if cond == "header":  # Take 1 argument : search keyword
            lines = ["sure, %s's cinema schedule coming...",
                     "%s right? Let me check first... ",
                     "Sure, wait a second,.. looking for %s's cinema movie list...",
                     "Okay, please wait... searching for %s's cinema schedules...",
                     "%s?? Wait... let me check..."
                     ]
        elif cond == "information header":  # Take 1 argument : tag list
            lines = ["Here's the information Megumi found while using '%s' as tag..\n",
                     "I tried using '%s' as tag, and found those...\n",
                     "Here's the information you requested ^^\n(using '%s' as tag)\n",
                     "Here you go~ \nMegumi used '%s' as search tag btw..\n",
                     "Here's the schedule I found with '%s' as tag..\n"
                     ]
        elif cond == "cinema name":  # Take 1 argument : cinema name
            lines = [" ♦♦  %s  ♦♦ \n",
                     "(・ω・) %s (・ω・)\n",
                     " ❤❤   %s   ❤❤ \n",
                     " ~~~   %s   ~~~ \n",
                     " >>>   %s   <<< \n"
                     ]
        elif cond == "No cinema found":  # Take 1 argument : tag list
            lines = ["No cinema is found :<  \nI tried to search using '%s' as tag",
                     "Somehow Megumi can't find cinema with '%s' name..",
                     "There's no cinema under '%s' name..",
                     "I think you should try again using tag other than '%s'..",
                     "I can't figure out which cinema with '%s' ",
                     "Megumi can't find the cinema you requested (%s)..",
                     "I don't see any cinema by searching using '%s' :< "
                     ]
        elif cond == "Too many cinemas":  # Take 1 argument : tag list
            lines = ["I found too many cinemas with '%s' as tag",
                     "There're too many cinemas \n with '%s' as tag",
                     "Try using more specific tags than '%s', there're too many cinemas..",
                     "I can't figure out which cinema with '%s'\nThere're too many of them...",
                     "Be specific please,, there're tons of cinemas with '%s'"
                     ]
        elif cond == "No keyword found":
            lines = ["Megumi can't find without keyword.. .-.",
                     "Please specify which cinema :> ",
                     "Did you include keyword already ? I don't see those..",
                     "Which cinema do you want ?",
                     "There're a lot of cinemas, which one ?"
                     ]
        elif cond == "failed to open the the page":
            lines = ["Megumi seems can't open the page..",
                     "Something wrong happened when I tried to open the page..",
                     "Gomen, Megumi can't give you the schedule right now..",
                     "Gomen, Megumi failed to open the the page..",
                     "Seems Megumi can't access the information right now.."
                     ]
        elif cond == "failed to get movie data":
            lines = ["Gomen, Megumi failed to gather movies data",
                     "Seems I can't get the schedule..",
                     "Gomenne, somehow I can't get the schedule..",
                     "Gomenne, there's some problem when I want to get the schedule..",
                     "I've opened the page, but I can't get the data right now ..",
                     ]
        elif cond == "failed to show movie data":
            lines = ["Gomen, Megumi failed to show movies data",
                     "Seems I can't show the schedule..",
                     "Gomenne, somehow I can't show the schedule..",
                     "Gomenne, there's some problem when I want to show the schedule..",
                     "I've gathered the schedule, but I can't send it to you right now ..",
                     ]
        elif cond == "footer":
            lines = [" ♦ ＼(＾∀＾)  end   (＾∀＾)ノ ♦ ",
                     " Hope you enjoy the show later ~",
                     " (=^ ◡ ^=) end 	(=^ ◡ ^=)",
                     " (＾• ω •＾) enjoy the show ~ ",
                     "      ヾ(・ω・)メ(・ω・)ノ    ",
                     ]
        elif cond == "asking to show cinema list":
            lines = ["Wanna see the cinema list ?",
                     "Nee,, wanna see the cinema list ?",
                     "Let's take a look at the cinema list :> ",
                     "How about seeing the cinema list ? ",
                     "I have the cinema list, wanna see ?",
                     ]
        elif cond == "show cinema list":
            lines = ["Here you go..  \n",
                     "These are the cinemas I could find ~\n",
                     "Pick the cinemas from the list below kay ? :> \n",
                     "Try to add some of this name into search next time ^^\n",
                     "These are the cinema list you requested..\n",
                     ]
        elif cond == "specify the company":
            lines = ["Does it have CGV or XXI ? I don't remember...\n(Try to add either 'cgv' or 'xxi')",
                     "Is it CGV ? or maybe XXI ? I'm not sure...\n(Try to add either 'cgv' or 'xxi')",
                     "Which cinema list is it? CGV or XXI ? \n(Try to add either 'cgv' or 'xxi')",
                     "Which cinema list should I search from?\n(Try to add either 'cgv' or 'xxi')",
                     "Gomen,, please specify which cinema do you want me to search for..\n(Try to add 'cgv' or 'xxi')",
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def wiki_search(cond):

        if cond == "page not found":  # Takes 2 argument : language, keyword
            lines = ["I think %s wikipedia does not have an article about '%s' ... ",
                     "Gomen, I tried to search %s wikipedia, but I can't find '%s' ",
                     "%s wikipedia doesn't have '%s' titled page I think...",
                     "I don't see any pages on %s wikipedia titled '%s'...",
                     "Seems %s wikipedia doesn't have information about '%s'..."]
        elif cond == "try different keyword / language":
            lines = ["How bout trying different keyword / language ? \n\nJust in case you need it..",
                     "How bout trying other keyword / language ? \n\nHere's the wiki list, just in case..",
                     "Wanna try other keyword? or maybe language? \n\nI will put it here, just in case..",
                     "How about trying other language ? \n\nHere's the list of wikipedia you can pick..",
                     "Maybe try other keyword / language ? \n\nJust in case you need it btw,.. ",
                     "\nJust in case you need wiki list... ",
                     ]
        elif cond == "no keyword found":
            lines = ["What do you want me to search for ? ",
                     "Gomen, what was that ? ",
                     "Gomen, say it again please ? what was that ? ",
                     "Gomen, what do you want me to search for ?",
                     "Gomen, what did you ask just now ?",
                     "Sorry, I missed the thing you asked just now.. ",
                     "Please say it again what I should be looking for...",
                     "Pardon, what do you want me to look for ? "]
        elif cond == "has disambiguation":
            lines = ["FYI, this keyword has other uses...\n",
                     "Just saying, this keyword has other uses..\n",
                     "This keyword has other uses\n",
                     "This keyword has other disambiguation choices\n",
                     "This page is auto-redirected, there are other disambiguation..\n",
                     "FYI, there are other disambiguation available...\n",
                     "Just saying, this keyword has other meaning as well..\n",
                     "FYI, this keyword has other meaning as well.. \n"]
        elif cond == "not specific page - header":
            lines = ["Seems '%s' is not a specific keyword,..",
                     "I think there are a lot different uses of '%s'..",
                     "I can't determine which '%s' you are looking for...",
                     "I'm not sure which is the appropriate answer for '%s' ",
                     "There are a lot of '%s' ,,"
                     ]
        elif cond == "not specific page - content":
            lines = ["Here's the list of '%s' people usually search for : \n",
                     "These are some common uses of '%s'...\n",
                     "How about pick one from the list of '%s' below ? \n",
                     "I found some common uses of '%s', how about pick one ? \n",
                     "I wonder if '%s' you looking for is listed below... \n"
                     ]
        elif cond == "ask detail info":
            lines = ["Wanna see more detailed info ?",
                     "Nee,, wanna see the detailed page ?",
                     "Do you want to see the full page ?  ",
                     "Take a look at the original page ? ",
                     "I also have the full page, wanna see ?",
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def download_youtube(cond):

        if cond == "page not found":
            lines = ["Are you sure you include the youtube link correctly ?",
                     "I can't find the link you want to download...",
                     "Seems the page is unavailable...",
                     "I can't find the youtube page you requested..",
                     "The youtube page is unavailable, I think..."]
        elif cond == "no video found":  # Takes 3 argument : 0.format, 1.min , 2.max
            lines = ["There's no video with that format ({0}, {1}p - {2}p) ...",
                     "I don't see any video in {0}, ({1}p - {2}p) available to download...",
                     "Seems this video doesn't meet the requested format ({0}, {1}p - {2}p)..",
                     "Seems this video is not available in {0}, ({1}p - {2}p) format..",
                     "I can't find any video to download...\nno result for {0}, ({1}p - {2}p)...try other format(?) "]
        elif cond == "gathering video data failed":
            lines = ["The page is so slow, I can't gather any data...",
                     "Gomen, seems the video download data corrupted..",
                     "Gomen, the video data is so unresponsive...",
                     "Seems something missing from the video download data, making it's unavailable",
                     "I can't gather the data you requested, seems something wrong..."]
        elif cond == "pick one to download":
            lines = ["Here's the list of available video(s) ",
                     "Pick one form the list below ,kay ? ^^",
                     "Here you go :> ",
                     "Choose one to download...",
                     "Which one do you want ? .."]
        elif cond == "send option header":
            lines = ["I found some videos with %s",
                     "Here are some videos with %s",
                     "Those videos passed %s as filter",
                     "I tried to filter with %s and these are the result..",
                     "I tried to use %s as filter, and found those..."]
        elif cond == "roger":  # Take 1 argument : keyword
            lines = ["Sure.. Wait a minute, searching for '{}' ...\nIt's gonna take a while",
                     "'{}' ? Sure... Wait a minute.. ",
                     "Sure.. Let me find '{}' for you.. \nPlease wait :>",
                     "'{}' right ? Understood... \nLooking for the one you want...",
                     "Kay, I'll search for '{}'...please be patient :) "]
        elif cond == "header : too much option":
            lines = ["This is the list of available formats...\n",
                     "Try to include one of the format next time...\n",
                     "These are the available formats... \n",
                     "Why did you make such a wide filtering ? Try to narrow it down..\n",
                     "I wonder which one do you want...\n"]
        elif cond == "footer : too much option":
            lines = ["\n ♦ ＼(＾∀＾)  end   (＾∀＾)ノ ♦ ",
                     "\n Hope you find the one you want ~",
                     "\n (=^ ◡ ^=) end 	(=^ ◡ ^=)",
                     "\n \(＾• ω •＾) found it ?  ",
                     "\n      ヾ(・ω・)メ(・ω・)ノ    ",
                     ]
        elif cond == "footer plural":
            lines = ["I'm not sure which one you want, but hope you enjoy it :> ",
                     "Since I found a lot, I randomly pick some for you :)",
                     "There's a lot of videos under that title, pick yourself kay.. :) ",
                     "That's what I found, hope you enjoy it~ ",
                     "I think I overdid a little bit.. #teehee..."]
        elif cond == "footer singular":
            lines = ["Hope you enjoy it :> ",
                     "I only found one, so this must be it..",
                     "This video isn't too popular is it ?",
                     "That's what I found, hope you enjoy it~ ",
                     "I'm not lazy kay..\nI did search and I only found one..."]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def summonerswar_wiki(cond):

        if cond == "send button header":
            lines = ["Just tap the information you need...",
                     "I have several info about this monster..",
                     "Which one do you want to know ?",
                     "Here you go...",
                     "Hope this is what you looking for.."]
        elif cond == "ask detailed page":
            lines = ["Wanna see more detailed info ?",
                     "Nee,, wanna see the detailed review ?",
                     "Do you want to see the full page ?  ",
                     "Need more detailed info ? ",
                     "I also have the full page, wanna see ?",
                     ]
        elif cond == "page not found":
            lines = ["I think sw wiki does not have information about that ... ",
                     "Gomen, I tried to search in sw wiki, but I can't find it.. ",
                     "Sw wiki doesn't have that monster info I think...",
                     "I don't see any monster with that name...",
                     "Are you sure you spelled the name correctly ?"
                     ]
        elif cond == "no keyword found":
            lines = ["What monster do you want me to search for ? ",
                     "Gomen, what monster was that ? ",
                     "Gomen, say the name again please ? what was that ? ",
                     "Gomen, which monster you want me to search for ?",
                     "Gomen, what did you ask just now ?",
                     "Sorry, I missed the name you asked just now.. ",
                     "Please say it again which monster I should be looking for...",
                     ]
        elif cond == "overview header":  # Take 2 arguments : monster type, usage
            lines = ["This is a/an %s type monsters, which excels for %s",
                     "Typically %s type monster, people usually use it for %s",
                     "Simply %s type monster, you should use it for %s ...",
                     "This monster is kind of %s type monsters..\nEspecially good for %s",
                     "Most users said that this %s type monster is good for %s"]
        elif cond == "good points":
            lines = ["Good things about this monster :",
                     "Some good points of this monster :",
                     "This monster is good because of :",
                     "Some reason to use this monster :",
                     "Some good features of this monster : "]
        elif cond == "bad points":
            lines = ["Weak points you should take care :",
                     "Some Cons of using this monster :",
                     "Some people don't use it because of :",
                     "Things that this monster lacks : ",
                     "Some users avoid using this monster because of : "]
        elif cond == "stats header":
            lines = ["Here's the Lv40 (Awakened) stats :",
                     "Here's the stats when it hit Lv40 and awakened",
                     "When it's at Lv40, the stats look like : ",
                     "Detail stats of Lv40 (Awakened) monster : ",
                     "Lv 40 (Awakened) monster stats : "]
        elif cond == "skills header":
            lines = ["SKILLS :",
                     "Some usable skills :",
                     "Here's the list of it's skills :",
                     "Here you go...",
                     "Take a look at the skills carefully.."]
        elif cond == "random errors":
            lines = ["I'm really sorry, but me and Dev have tried our best..\n"
                     "But you know,, this wiki page is super inconsistent in terms of syntax..\n"
                     "We're sorry if some of the feature is not working properly...",
                     "I'm really sorry if some of the features is not working properly,,\n "
                     "But you know,, this wiki page is super inconsistent in terms of syntax..\n"
                     "We're sorry since we can't do anything about that..",
                     "I'm really sorry if some of the features is not working properly,,\n"
                     "Me and Dev have tried our best..\n"
                     "But the wiki is super inconsistent in terms of syntax.."
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def weatherforecast(cond):

        if cond == "header":
            lines = ["I found the information you requested :>",
                     "Here's the information you asked for..",
                     "Here you go...",
                     "One weather forecast request coming ~",
                     "Let me check first... ",
                     "Wait a second.. hmm...."
                     ]
        elif cond == "city search : 3 or more cities":
            lines = ["btw, there are some cities which name similar to the one you ask for,..",
                     "anyway, I picked one to show you, but just let you know,\nThere are some cities with similar name : ",
                     "I randomly picked one from the list below :",
                     "There are a lot of cities with similar name you know...\nI chose one from the list below :",
                     "I'm not sure which one is the legit one.., \nthere are a lot of cities similar to the one you ask for.. like :"
                     ]
        elif cond == "city search : 2 cities":  # Take 1 argument : city name
            lines = ["There is another city which it's name similar to the one you search for : %s ",
                     "Try to ask for %s if this is not the correct one",
                     "There is another alternative : %s",
                     "If this is not what you want, try %s instead..",
                     "I'm not sure if this is what you want, if I'm wrong, try %s instead ^^ ",
                     "I don't know which one is the correct one, but try to look at %s instead.."
                     ]
        elif cond == "default location":  # Take 1 argument : default location
            lines = ["Since you did't ask for specific location, \nI assume you are at %s now... ",
                     "I'll give you weather information at %s since you didn't ask for specific location...",
                     "Did you ask for weather around %s ? I assume so...",
                     "I'll give you weather forecast around %s...",
                     "Since you did't ask for specific location, \nI assume you ask for weather forecast around %s... ",
                     "I think you asked for weather forecast around %s, right? "
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def weatherforecast_tips(cond):
        # USE LOWER AS COND

        if cond == "clouds":
            lines = ["The sky seems a bit cloudy today...\nI wonder if it will rain soon...",
                     "Don't forget to bring umbrella if you are going out.. \nIt's kinda cloudy right now..",
                     "Do you have any outdoor activity ?\n If you do, probably you should bring an umbrella just in case..",
                     "What a gloomy day... \n\nBut I know you love this kind of weather don't you ? :>",
                     "Cloudy with a chance of meatballs !! \n#JK :P",
                     "A cloudy day have as great an influence on many constitutions as the most recent blessings or misfortunes.",
                     "I think it will be a gloomy and windy day.. \ntry not to catch the 'gloominess' ,kay?.. xD ",
                     "Best day to curl up in blanket and just do nothing..."
                     ]
        elif cond == "clear":
            lines = ["It's a nice weather.. what a waste to do nothing ! ",
                     "Such a nice weather outside... Thanks God :> ",
                     "Such a perfect day... ^^ ",
                     "The sky is crystal-clear...\n\nI wonder if we could stargaze tonight... ",
                     "Such a perfect day to play outside...",
                     "Look at the sky, look at the earth... \nwhat a blessing to be alive ~ "
                     "This is a nice weather right ? don't you think so too ? :) "
                     ]
        elif cond == "rain":
            lines = ["Rain rain rain... pouring into my feeling...",
                     "Make sure you stay dry ,kay ? :)",
                     "I wish I could stay at home, curling inside blanket and.. zzz",
                     "The best thing one can do when it's raining is to let it rain ~",
                     "Rain is grace, without rain, there would be no life..",
                     "Hot chocolate, warm blanket, and of course you, make a rainy day feels good :3 ",
                     "Stay silent... \nthe sound of the rain is so soothing isn't it ? ",
                     "Just don't go outside when it's pouring..."
                     ]
        elif cond == "snow":
            lines = ["Make sure you stay warm :>",
                     "Don't go outside when it's pouring..",
                     "I wonder if it will piled up or not...",
                     "SO COLD...",
                     "Imagine sitting in front of a fireplace with hot chocolate on a snowy day..."
                     ]
        elif cond == "extreme":
            lines = ["I'm not sure about this weather.. try to stay at home..",
                     "I think it's better to stay at home...",
                     "The weather is not very good to go outside... how bout stay at home ?",
                     "It's not very recommended to go outside right now.."
                     "Hope this weather passed quickly... "
                     ]
        elif cond == "mist":
            lines = ["Woa... what a rare sight...",
                     "It's been a while since the last time isn't it ?",
                     "No wonder it's kinda cold right now...",
                     "Drive slowly if you have to ... safety first !",
                     "Feels like kinda magical or mysterious feeling..."
                     ]
        elif cond == "drizzle":
            lines = ["Make sure you stay dry ,kay ? :)",
                     "I wonder if it will keep goes on..",
                     "Drop more pleasee... :> ",
                     ]
        else:
            lines = ["I'm not sure about this weather.. never seen it before..",
                     "I'm not sure, but I think it's better to stay at home...",
                     "I'm not sure about the weather to be honest..",
                     "I'm not sure if you want to go outside right now.."
                     "I'm not sure how long this will be..."
                     ]

        return random.choice(lines)

    @staticmethod
    def itb_arc_database(cond):

        if cond == "header":  # Take 1 argument itb_keyword
            lines = ["Wait, I'm trying to find information about %s in the ARC-ITB database...",
                     "%s right? Let me check first... ",
                     "Sure, wait a second,.. looking for %s in the ARC-ITB database...",
                     "Okay, please wait... searching for %s in the ARC-ITB database...",
                     "%s?? Wait... let me check..."
                     ]
        elif cond == "database unreachable":
            lines = ["I think there's some problem with the database right now...\nI will try to use sub-database...",
                     "Seems ARC-ITB database is down or unreachable...\nI will try to search on sub-database",
                     "I can't access the database right now...\nNo worries, I will try searching in sub-database",
                     "I wonder if the ARC-ITB database is down or under maintenance...\nI will try to use sub-database...",
                     "Seems the database is offline right now..\nNo worries, I will try searching in sub-database"]
        elif cond == "sub database unreachable":
            lines = ["Sorry,..\nI think there's some problem here too...",
                     "Sorry,..\nSeems all database is down or unreachable...",
                     "Sorry,..\nI can't access the sub-database as well...",
                     "Sorry,..\nNo result as well...",
                     "Sorry,..\nSeems all the database are offline right now.."]
        elif cond == "default category":
            lines = ["I'm searching under 'students' category, since you didn't specify the category..",
                     "Btw, I'm searching for the keyword under 'students' category..",
                     "I'm not sure if it is listed under 'students' category, but let's try...",
                     "I assume it is listed under 'students', since it's the most common category...",
                     "I assume you want me to search under 'students', since you didn't specify it"
                     ]
        elif cond == "count result plural":  # Take 1 argument result count
            lines = ["I've found %s data after doing a quick search...",
                     "There are %s listed data that fulfil the keyword",
                     "The database has %s data under that keyword",
                     "I've found %s data by searching through the database",
                     "Seems these %s are the one you search for",
                     "I'm not sure which one of these %s, is the one you looking for.."]
        elif cond == "count result one":
            lines = ["I only found one detail which fulfils the keyword...",
                     "Seems there is only one... ",
                     "I tried to search in ARC - ITB database, and found this one..",
                     "I'm pretty sure that this one is the correct one :> ",
                     "Is this one the right one? "]
        elif cond == "not found":
            lines = ["Are you sure that keyword listed? I can't find it...",
                     "There are no data under that tag..",
                     "Nothing found... try another key word maybe? ",
                     "Hmm... I didn't see anything that fulfils the keyword...",
                     "Please re-check the keyword.. I found nothing here..."]
        elif cond == "only send top 5":
            lines = ["Since there are too much information to send,...\nI will send only the first-five",
                     "Are the first-five results enough ??",
                     "There are too much information to send,..can't send them all..",
                     "I will pick and send the first-five ,kay ? ",
                     "I can't send them all in a batch, how bout the first-five only ?"]
        elif cond == "footer":
            lines = ["\n ♦ ＼(＾∀＾)  end   (＾∀＾)ノ ♦ ",
                     "\n   (✿◠‿◠)     (◠‿◠✿)    ",
                     "\n (=^ ◡ ^=) end 	(=^ ◡ ^=)",
                     "\n \(＾• ω •＾) (＾• ω •＾)/   ",
                     "\n     ヾ(・ω・)メ(・ω・)ノ    ",
                     ]
        elif cond == "data formatting failed":
            lines = ["I have the raw data, but I shouldn't send it without formatting it right?",
                     "I have problems when tried to format the data that I've gathered",
                     "Call Ra to fix the formatting.. It has been changed recently..",
                     "I have the data, but can't format it... \nSeems they changed the layout(?)",
                     "The data is kinda messy... \nI don't think I should give it to you in this state.. :<"]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def anime_download_link(cond):

        if cond == "header":  # Take 1 argument : title
            lines = ["Sure...be right back, getting %s download links from cyber12...",
                     "%s right? Let me check first for the download links... ",
                     "Sure, wait a second,.. searching cyber12 for %s links...",
                     "Okay, please wait...\n%s download links coming ~",
                     "%s?? Wait... let me check in cyber12 database first..."
                     ]

        elif cond == "default start ep":
            lines = ["I'm getting the links from ep 1, since you didn't specify it..",
                     "I assume you want the links from ep 1 :> ",
                     "It's gonna take a while, since I'm digging from ep 1..",
                     "Is this a new series ? Or you have not downloaded a single one yet ?",
                     "Just to make sure you got everything, I will give all the links I found"
                     ]

        elif cond == "default host":
            lines = ["Btw, is zippyshare sound's good? ",
                     "I will recommend zippyshare as the host..",
                     "I'm looking for zippyshare links since I prefer that..",
                     "I'll recommend using zippyshare as file host...",
                     "Since you didn't specify, I will pick zippyshare as the host..."]

        elif cond == "keyword not found":
            lines = ["Which anime do you want me to search for ?",
                     "I'm not sure which anime do you want though...",
                     "Can you say the title again? \nFor example like 're:zero' or 'idolmaster' .. ",
                     "Sorry, what was the anime's title again ?",
                     "Sorry, can you repeat the title again?\nSay it like 'fate' or 'sakurasou',.."]

        elif cond == "starting episode not aired":
            lines = ["I tried to look for the episode you requested, but seems it's not aired yet..",
                     "Cyber12 doesn't have that episode yet..",
                     "I don't think that episode is available right now...",
                     "Seems that episode is not encoded yet...",
                     "Did you say the wrong episode?\nI can't find that episode though..."]

        elif cond == "send latest episode count":  # Take 1 argument : last episode
            lines = ["I think the latest episode is ep. %s",
                     "The database only shows %s episode...",
                     "Seems ep. %s is the latest until now... ",
                     "Seems the series only has %s episode until now..",
                     "It's only available up to ep. %s"]

        elif cond == "header for result":
            lines = ["Sorry for the delay..",
                     "I'm back with something you want ~ ",
                     "Here's what I found on cyber 12 : ",
                     "Here you go ~ :> ",
                     "Sorry for the delay,.. here's the list.."]

        elif cond == "title not found":  # Take 1 argument : title
            lines = ["I don't see any '%s' titled anime..\nMaybe you spelled it wrong ?",
                     "The database doesn't have %s titled anime..\nHow about request it personally?",
                     "Please double check the title.. I can't find %s at the database...",
                     "Seems there's no anime with that title...you sure it's '%s'? ",
                     "How about trying other title ? Seems %s is not in the database yet.. "]

        elif cond == "host not available":  # Take 1 argument : episode
            lines = ["Seems ep. %s is not available on this host",
                     "Failed to get the link of ep.%s",
                     "Seems the ep. %s is not properly uploaded on this host",
                     "Unable to retrieve ep. %s link, it's not available",
                     "Ep. %s is not available on this host, try other host..."]

        elif cond == "send animelist":
            lines = ["Here's the 2017 and 2016 anime list,..\nMaybe you need it..",
                     "I can only grab the links if the title is listed here..",
                     "Please check first whether your anime is listed or not",
                     "How about take a look at those list first?",
                     "Here's the list of all animes which has download links.."]

        elif cond == "dev mode extension failed":  # Take 1 argument : kind of error
            lines = ["Extension error : %s\n",
                     "Dev mode extension error : %s\n"]

        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def translate_text(cond):

        if cond == "text to translate not found":
            lines = ["Which should I translate?",
                     "Which sentence do you want me to translate?",
                     "Sorry, I didn't catch which one should I translate..",
                     "Which one .-. ?",
                     "Whatt ?? .-."]
        elif cond == "language list not found":
            lines = ["I can't get the language list",
                     "Seems there's something wrong with microsoft...",
                     "I can't get the list of language available for translate...",
                     "The translation module seems having some issue when getting list of language...",
                     "Sorry.. translation module can't get the list of languages :( "]
        elif cond == "destination language not found":
            lines = ["To which language? English?\n",
                     "Which language should I translate to? English?\n",
                     "I'm translating it to english then..\n",
                     "To what language? English? .-.\n",
                     "Since you didn't specify, I guess English is fine for you?\n"]
        elif cond == "destination language not available":  # Take 1 argument : language
            lines = ["I'm not confident about my %s skill, how about other language?",
                     "Sorry... I haven't learned %s yet,.. Maybe another language?",
                     "My %s is pretty bad, how about another language?",
                     "I don't know the suitable translation in %s,...\nI'm sorry...",
                     "I'm not sure what it is in %s, \nhow about other general language like English?"]
        elif cond == "send translated":  # Take 3 argument : 0.text 1.to 2.translated
            lines = ["I think in {1},'{0}' is '{2}'",
                     "'{0}' can be translated into {1} as '{2}'",
                     "'{2}' means '{0}' in {1}",
                     "Mostly people say '{2}' for '{0}' in {1}",
                     "I think '{2}' is common trasnlation for '{0}' in {1}"]
        elif cond == "already in that language":  # Take 1 argument : to language
            lines = ["Wait..isn't it already in %s ?",
                     "Wait..I think it's already in %s...isn't it ?",
                     "Seems it's already in %s... isn't it ?",
                     "I think it's already in %s,.. right ? ",
                     "Seems it doesn't need any translation,\nI'm pretty sure it's already in %s..."]
        else:
            lines = [""]
        return random.choice(lines)

    @staticmethod
    def report_bug(cond):

        if cond == "success":
            lines = ["Thank you for your report :>",
                     "Arigatoo... wish me luck to fix this problem :\")",
                     "Arigatoo, I'll let dev know about this",
                     "Arigatoo, I'll tell dev later ~",
                     "Sankyu for your feedback :)",
                     "Gomenne, hope I can fix this soon...\nthanks for the report btw :)",
                     "Gomenne,.. thanks for the feedback though ^^",
                     ]
        elif cond == "fail":
            lines = ["Gomen,, try to send it again..",
                     "Gomen,, dev is busy fixing other stuff :'> ",
                     "Gomenne,, seems report function is not working properly ...",
                     "Gomenne,, please try to tell dev by personal chat .. ",
                     "Gomen,, can you repeat the report please ? .. :'> ",
                     "Gomen,, I'm still learning how to report stuff... :'> ",
                     ]
        elif cond == "report":
            lines = ['Master, here is the report... : \n\n"%s" \n\nSubmitted by : %s',
                     'Master, I think there are some problems... : \n\n"%s" \n\nSubmitted by : %s',
                     'Master, I\'ve got you a report :3 \n\n"%s" \n\nSubmitted by : %s',
                     'Master, please take a look at this... : \n\n"%s" \n\nSubmitted by : %s',
                     'Master, how should I solve this ? \n\n"%s" \n\nSubmitted by : %s',
                     'Master, please fix this :3 \n\n"%s" \n\nSubmitted by : %s',
                     'Master, try to fix this owkay ?? :3 \n\n"%s" \n\nSubmitted by : %s',
                     'Master, seems something is not working properly.. : \n\n"%s" \n\nSubmitted by : %s']
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def show_manual(cond):

        if cond == "header":
            lines = ["Manual? Okay, wait a second...",
                     "Sure... Wait a second :)",
                     "Do you need help? Wait a second :)",
                     "Sure..Megumi's manuals coming~",
                     "Summoning Megumi's manuals ~"]
        elif cond == "tips":
            lines = ["\nfriendly tips : I can handle many different input format, try it out yourself ~",
                     "\nfriendly tips : Don't let me disappoint you, I learn every time you talk to me",
                     "\nfriendly tips : Try out other way to call my functions, there're lots of different ways to do it",
                     "\nfriendly tips : You have to include my name, otherwise I won't help you :3",
                     "\nfriendly tips : Don't worry if you input wrong command, I will let you know..",
                     "\nfriendly tips : I am still learning, that's why don't hesitate to tell me if I'm wrong or if you have new suggestion",
                     "\nfriendly tips : Use report bug function to send feedback for better future !",
                     "\nfriendly tips : Practice make's perfect, so train me to get better and better !",
                     "\nfriendly tips : There are many different type of examples for one function, try them all ! "]
        elif cond == "see example?":
            lines = ["Would you like to try it ?",
                     "Let's test it out ~",
                     "Try it now ?",
                     "See example ?",
                     "Try this out ?"]
        elif cond == "see manual?":
            lines = ["Would you like to see Megumi's manual ?",
                     "Wanna see Meg's manual ? :> ",
                     "I can do some things to help you, wanna see ? :)",
                     "Would you like to know what can I do? :)",
                     "Do you want to know me better ? :)"]

        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def stalk_instagram(cond):

        if cond == "header":  # Take 1 argument : keyword
            lines = ["{0} ? Wait a second.. I will try to stalk... :> ",
                     "Sure.. Wait...trying to get {0} information for you ",
                     "Hmm... Stalking is not a good habit...\nBut who cares right ? :>\nStalking {0}",
                     "Stalking {0} .... Someone tried to stalk {0}....\n#teehee...",
                     "Megumi used 'stalk' to {0}...\n.\n.\n.\nGotcha !!"]
        elif cond == "private":
            lines = ["Oops... Seems the page is private :P",
                     "This page is private dude... Try other one...",
                     "P R I V A T E ..... You have to pay me more for this page :>",
                     "I have it already... But you have to pay me some moneh for this :P\n\n#JK.. Its private..",
                     "Seems I can't stalk this page...They rejected my request to stalk .-. \n\nI did politely ask 'can I stalk here?'... "]
        elif cond == "user information header":
            lines = ["Here's some information about him/her...",
                     "Here you go... ",
                     "I'm back ~ ",
                     "I'm back with something you want :)",
                     "Stalk operation success ! :> "]

        elif cond == "picture count 0":
            lines = ["This user seems haven't post anything yet",
                     "I don't see any picture to send..",
                     "This user doesn't have any picture yet..",
                     "I'm pretty sure this account is inactive",
                     "I wonder if this user never posted anything yet.."]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def hoax_or_fact(cond):

        if cond == "fact":  # Take 2 argument : percentage, query
            lines = ["I think '{1}' is true...\n\nAbout {0}%...",
                     "It's true.. \nI can guarantee {0}% :> ",
                     "Yea, it's true...\nI'm {0}% sure about that :>",
                     "I think '{1}' is {0}% true...",
                     "{0}% fact..., and the rest is made up..."]

        elif cond == "hoax":  # Take 2 argument : percentage, query
            lines = ["Nah.. that's just bullsh*t...\nI can guarantee {0}%",
                     "I'm {0}% sure that '{1}' is not true at all...",
                     "Nah, {0}% sure it's not true at all...",
                     "'{1}' is hoax...I'm {0}% sure about that",
                     "'{1}' proven as hoax... "]
        else:
            lines = ["I'm not sure about that either...",
                     "Dunno.. maybe yes maybe no...",
                     "Nah, I'm not sure about that..",
                     "Seems It need more further investigation...",
                     "Dunno... Not sure either..."]

        return random.choice(lines)

    @staticmethod
    def play_music(cond):

        if cond == "header":  # Take 1 argument : keyword
            lines = ["Sure.. Wait a minute, searching for '{}'...\nIt's gonna take a while",
                     "'{}' ? Sure... Wait a minute.. ",
                     "Sure.. Let me find '{}' for you.. \nPlease wait :>",
                     "'{}' right ? Understood... \nLooking for the one you want...",
                     "Kay, I'll search for '{}'...please be patient :) "]
        elif cond == "video not found":  # Take 1 argument : keyword
            lines = ["Seems there's no '{}' titled song..",
                     "Are you sure about the title ({}) ? ",
                     "How bout try other title? I can't find '{}'",
                     "I don't see any song with '{}' title...",
                     "Did you misspelled ? No result for '{}' when I tried to search for it..."]
        elif cond == "nothing to play":
            lines = ["Seems the song is too long... \nIt has to be under 8 mins...",
                     "I'm sorry but I can't find song that's under 8 mins with that title...",
                     "That titled songs are too long to play... ",
                     "Have I told you that the music duration has to be under 8 mins ?",
                     "I can't find any music that is under 8 mins... I'm sorry ... "]
        elif cond == "footer plural":
            lines = ["I'm not sure which one you want, but hope you enjoy it :> ",
                     "Since I found a lot, I randomly pick some for you :)",
                     "There's a lot of musics under that title, pick yourself kay.. :) ",
                     "That's what I found, hope you enjoy it~ ",
                     "I think I overdid a little bit.. #teehee..."]
        elif cond == "footer singular":
            lines = ["Hope you enjoy it :> ",
                     "I only found one, so this must be it..",
                     "This song isn't too popular is it ?",
                     "That's what I found, hope you enjoy it~ ",
                     "I'm not lazy kay..\nI did search and I only found one..."]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def join(cond):

        if cond == "join":
            lines = [" Thanks for adding me ^^",
                     " Thanks for inviting Megumi :3 ",
                     " Yoroshiku onegaishimasu~ ^^ ",
                     " Megumi desu ! ^^",
                     " Megumi desu, you can call me kato or meg aswell... :> ",
                     " Megumi desu, just call me kato or meg  ^^ ~",
                     " Megumi desu ! ehehehe",
                     " Supp xD .. Megumi desu :3 ,,"]
        elif cond == "report":  # Take 1 argument : group id
            lines = ["Master, Megumi joined a group ~ :> \n\nGroup id : %s",
                     "Master, I'm leaving for a while ,kay? ^^ \n\nGroup id : %s",
                     "Master, I got invitation to join a group..\n\nGroup id : %s",
                     "Master, I'm going to a group ,kay? :3 \n\nGroup id : %s",
                     "Master, Wish me luck ,, Megumi joined a group #teehee ^^ \n\nGroup id : %s",
                     ]
        else:
            lines = [""]
        return random.choice(lines)

    @staticmethod
    def leave(cond):

        if cond == "leave":
            lines = ['“To say goodbye is to die a little.” \n― Raymond Chandler',

                     '“I don\'t know when we\'ll see each other again or what the world will be like when we do.\n'
                     'I will think of you every time I need to be reminded that there is beauty and goodness in the world.” \n'
                     '― Arthur Golden',

                     'One day in some far off place, I will recognize your face, I won\'t say goodbye my friend, For you and I will meet again',
                     '“Something or someone is always waving goodbye.”\n― Marty Rubin ',

                     'Even if we walk on different paths, one must always live on as you are able! '
                     'You must never treat your own life as something insignificant! You must never forget the friends you love for as long as you live! '
                     'Let bloom the flowers of light within your hearts.',

                     'Smile. Not for anyone else, but for yourself. Show yourself your own smile. You\'ll feel better then.',

                     'No matter what painful things happens, even when it looks like you\'ll lose... '
                     'when no one else in the world believes in you... '
                     'when you don\'t even believe in yourself... I will believe in you!',

                     'I\'ll always be by your side. You\'ll never be alone. '
                     'You have as many hopes as there are stars that light up the sky.'
                     ]
        elif cond == "regards":
            lines = ["See you later my friend.., bye~ \n\n              ~ Megumi ~",
                     'Wish you guys very best in everything.., bye~ \n\n              ~ Megumi ~',
                     'I hope this is not the end of us :> , bye~ \n\n              ~ Megumi ~',
                     'Try adding me sometimes okay ? :> I will wait for it.. bye for now !\n\n              ~ Megumi ~',
                     'Hope can see you again in the future ^^ .. , bye ~\n\n              ~ Megumi ~'
                     ]
        elif cond == "report":
            lines = ['Master, I\'m done with a group :> \n\n%s : %s',
                     'Master, I have left a group... xD \n\n%s : %s',
                     'Master, Megumi has returned from a group :3 \n\n%s : %s',
                     'Master, I think I\'ve been kick out from a group :"> \n\n%s : %s',
                     'Master, Can you invite me into the group again ? \n\n%s : %s',
                     ]
        else:
            lines = ["I can't leave... it's not a group or room .-. ",
                     'I think you mistaken this for group (?) xD',
                     'C\'mon, this is private chat xD',
                     'This is not group lol.. xD',
                     'I can only leave group and room, even though I don\'t want to TBH'
                     ]

        return random.choice(lines)

    @staticmethod
    def false():
        lines = ["Gomen,, what was that ?",
                 "Gomen,, I don't understand that :> ",
                 "Since I don't understand it,..\nHow about a big smile? :D",
                 "Are you calling me ?",
                 "Meg this meg that\nI wonder what is that",
                 "Ask simpler things kay ? .-.",
                 "How about trying to do it yourself ? :>",
                 "Hmm .. ",
                 "C= C= C= C= C=┌(;・ω・)┘	",
                 "┐(￣～￣)┌	┐(￣～￣)┌	┐(￣～￣)┌	",
                 "¯\_(ツ)_/¯ ",
                 "ヽ(*・ω・)ﾉ ??",
                 "(・・ ) ?",
                 "＼(￣▽￣)／",
                 "(︶︹︺)	",
                 "I'm sorry I don't understand ~ (≧◡≦) ♡",
                 "Ugh,...",
                 "._.",
                 "I wonder what is that..",
                 "Maybe you should try to call 'megumi help' and see what can I do..",
                 "hmmm... I wonder what is that",
                 "Have you read manual yet ?",
                 "...",
                 "meh...",
                 " .-. ? ",
                 " what ?? ._. "]
        return random.choice(lines)

    @staticmethod
    def tag_notifier():
        lines = ['Master, I think %s is calling you.. \n\n"%s"',
                 '%s is calling you master.. \n\n"%s"',
                 'Master, I think your name is being called by %s..\n\n"%s"',
                 'Master,.. tag message from %s \n\n"%s"',
                 'Check this out .. %s tagged you \n\n"%s"',
                 ]
        return random.choice(lines)

    @staticmethod
    def added(cond):

        if cond == "added":
            lines = [" Thanks for adding me ^^ \nhope we can be friend !",
                     " Thanks for adding Megumi :3 \nHope we can be friend ^^",
                     " Megumi desu~ \(^.^)/ ",
                     " Megumi desu ! yoroshiku nee ~ ^^",
                     " Megumi desu, you can call me kato or meg aswell.. \nhope we can be friends ~ :> ",
                     " Megumi desu, just call me kato or meg  ^^ ~ ",
                     " Megumi desu ! ehehehe",
                     " Megumi desu :3 ,,yoroshiku nee ~ "
                     ]
        elif cond == "report":  # Takes 2 argument : username , userid
            lines = ["Master, Megumi got a new friend named %s ~ ^^\n\nUser id : %s",
                     "Master, %s added Megumi as a friend ~ YAY ^^\n\nUser id : %s",
                     "Master, do you know %s ? he/she added me.. \n\nUser id : %s",
                     "Master, %s just added me ^^ \n\nUser id : %s",
                     "Look master, Megumi got a new friend : %s\n\nUser id : %s",
                     "Nee mastah,, %s added me o(>ω<)o \n\nUser id : %s",
                     ]
        else:
            lines = [""]
        return random.choice(lines)

    @staticmethod
    def removed(cond):

        if cond == "removed":
            lines = ['“To say goodbye is to die a little.” \n― Raymond Chandler',
                     '“I don\'t know when we\'ll see each other again or what the world will be like when we do.\n'
                     'I will think of you every time I need to be reminded that there is beauty and goodness in the world.” \n'
                     '― Arthur Golden',

                     'One day in some far off place, I will recognize your face, I won\'t say goodbye my friend, '
                     'For you and I will meet again',

                     '“Something or someone is always waving goodbye.”\n― Marty Rubin ',

                     'Even if we walk on different paths, one must always live on as you are able! '
                     'You must never treat your own life as something insignificant! '
                     'You must never forget the friends you love for as long as you live! '
                     'Let bloom the flowers of light within your hearts.',

                     'Smile. Not for anyone else, but for yourself. Show yourself your own smile. '
                     'You\'ll feel better then.',

                     'No matter what painful things happens, even when it looks like you\'ll lose... '
                     'When no one else in the world believes in you... When you don\'t even believe in yourself... '
                     'I will believe in you!',

                     'I\'ll always be by your side. You\'ll never be alone. '
                     'You have as many hopes as there are stars that light up the sky.'
                     ]
        elif cond == "regards":
            lines = ["See you later %s.., bye~ \n\n              ~ Megumi ~",
                     'Wish you very best in everything.., bye %s ... \n\n              ~ Megumi ~',
                     'I hope this is not the end of us :> , bye %s ... \n\n              ~ Megumi ~',
                     'Nee %s, play with me again OK ? :> I will wait for you.. \n\n              ~ Megumi ~',
                     'Thanks for playing with me until now %s... , bye ~\n\n              ~ Megumi ~'
                     ]
        elif cond == "report":
            lines = ["Master, seems %s blocked me ...",
                     "Megumi just lost a friend... %s - chan left me...",
                     "Gomenne master,, seems %s don't want to play with me anymore...",
                     "Nee mastah,, can you ask %s to add me again ? ",
                     "Master, gomenne.. %s blocked me I guess...Megumi wasn't a very good girl"
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def dev_mode_set_tag_notifier(cond):

        if cond == "on":
            lines = ["OK, I will tell you if someone tag you ~",
                     "Tag notifier is on active mode :> ",
                     "Sure, I will notify you",
                     "Roger..",
                     "Done.., itterasai :3 ~"]
        elif cond == "off":
            lines = ["Okaeri.. :3",
                     "OK, welcome back ~",
                     "Roger.. :3 ",
                     "Done,, Tag notifier is off now..",
                     "Sure,, glad to see you again.."]
        elif cond == "same":
            lines = ["Hmm.. seems nothing changed...",
                     "Hmm.. try to do it one more time.. ^^ \nsometimes it takes more than once",
                     "I don't see any difference though...",
                     "Please try again until it's changed ^^,,\nsometimes it takes more than once "]
        else:
            lines = ["Gomen, I don't catch that.. :/",
                     "Hmm.. try to do it one more time.. ^^",
                     "Gomen, seems notifier setting is failed...",
                     "I think you gave wrong instruction (?) xD"]

        return random.choice(lines)

    @staticmethod
    def dev_mode_userlist(cond):

        if cond == "print userlist success":
            lines = ["Print success, %d new entries recorded.\nDon't forget to print until 0 updates ^^ ~ ",
                     "Roger master,, %d new entries has been recorded.",
                     "Done..., don't forget to copy these %d new entries",
                     "Ryokai ^^.,,, just don't forget to copy these %d new entries later, kay ? ",
                     "Sure master.., there are %d new entries recorded FYI..."
                     ]
        elif cond == "print userlist failed":
            lines = ["Gomenne master, seems Megumi can't access the userlist... ",
                     "Gomen master, there's some errors Megumi can't handle when printing the userlist",
                     "Gomenne master, I don't know why but Megumi can't do that...",
                     "Gomen master, the userlist seems can't be printed out in the logs.. I wonder why...",
                     "Hmm... seems Megumi can't do that now.. how about try again ?"
                     ]
        elif cond == "userlist not updated yet":
            lines = ["Gomenne master, I think the userlist hasn't changed yet... ",
                     "Gomen master, Megumi just printed the same userlist before...",
                     "Gomenne master, I don't think you have to print it again...",
                     "Gomen master, the userlist seems same as before...",
                     "Hmm... are you sure want to print the same list ? \nHow about try again later ?"
                     ]
        elif cond == "notify update userlist":
            lines = ["Master, I think there're %s updates on userlist,,",
                     "Master, userlist has %s updates, how about updating now ?",
                     "The userlist has %s updates, wanna update now ?",
                     "%s entries on userlist, should I update now?",
                     "Let's update the userlist master.. %s new entries"
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def dev_mode_authority_check(cond):

        if cond == "failed":
            lines = ["Megumi can't enter Dev Mode now, try again later..",
                     "Megumi can't verify your id, so I can't grant you access..",
                     "Seems Megumi can't grant you access now..",
                     "Try calling dev mode once again.. seems some error occurred...",
                     "Megumi can't verify your id, please try again later..",
                     ]
        elif cond == "reject":
            lines = ["Gomenne,,Megumi can't grant you access for that..",
                     "Do not try to access dev mode.. you are not allowed to !",
                     "Gomen,, you are not allowed to do that..",
                     "Gomen, your request has been rejected.",
                     "Megumi does not allow you to enter dev mode !",
                     "Gomenne,,Megumi can't do that for you..",
                     "Gomenne,,Megumi is told not to give you access..",
                     "Gomen,,Megumi does not recognize you as developer..."
                     ]
        elif cond == "notify report":
            lines = ["Master, %s is trying to enter dev mode...",
                     "Be careful master, %s is trying to enter dev mode... ",
                     "Be careful master, %s has tried to enter dev mode just now.",
                     "Master, just now %s tried to enter dev mode.",
                     "Nee mastah, %s tried to enter dev mode. ",
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def dev_mode_general_error(cond):

        if cond == "common":
            lines = ["Seems some unexpected error happened...",
                     "Gommen, I tried to do it but I can't...",
                     "Ugh,, there's some unexpected errors...\nI can't do it now... ",
                     "Sorry, I can't do that now, seems something wrong happened...",
                     "Something bad happened...\nI can't do that now.."]
        elif cond == "dev":  # Take 2 argument : func name , exception detail
            lines = ["Mastah, seems some unexpected error happened with %s :\n\nHere's the detail : \n%s",
                     "Mastah, check this out...\nError with : %s\n\nHere's the detail : \n%s",
                     "I think you should take a look at this..\nError with : %s\n\nHere's the detail : \n%s",
                     "Mastah, seems you need to check this out..\nError with : %s\n\nHere's the detail : \n%s",
                     "Mastah, help me with this...\nError with : %s\n\nHere's the detail : \n%s"]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def dev_print_megumi_logger(cond):

        if cond == "header":
            lines = ["Preparing logs to print...",
                     "Wait a second, preparing files to print...",
                     "Printing command understood :>",
                     "Wait a second, printing logs...",
                     "Printing logs on process.."]

        elif cond == "success":  # Take 1 argument : log count
            lines = ["Printing Megumi's log succeed, {} logs printed...",
                     "Megumi's log printed out, {} logs successfully printed",
                     "{} logs successfully printed...",
                     "Megumi printed out {} logs...",
                     "Printing Megumi's log succeed, {} new entries... "]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def template_cond(cond):

        if cond == "a":
            lines = ["",
                     "",
                     "",
                     "",
                     ""]
        elif cond == "b":
            lines = ["",
                     "",
                     "",
                     "",
                     ""]
        elif cond == "c":
            lines = ["",
                     "",
                     "",
                     "",
                     ""]
        else:
            lines = [""]

        return random.choice(lines)

    """=================== Some Extra Lines Storage ======================="""

    @staticmethod
    def megumi():
        return ['megumi', 'kato', 'meg', 'megumi,', 'kato,', 'meg,']

    @staticmethod
    def jessin():
        return ['jessin', 'jes', '@jessin d', 'jess', 'jssin']

    @staticmethod
    def day():
        return {'Mon': 'Monday',
                "Tue": "Tuesday",
                "Wed": "Wednesday",
                "Thu": "Thursday",
                "Fri": "Friday",
                "Sat": "Saturday",
                "Sun": "Sunday"}

    @staticmethod
    def month():
        return {'jan': 'January',
                'feb': 'February',
                'mar': 'March',
                'apr': 'April',
                'may': 'May',
                'jun': 'June',
                'jul': 'July',
                'aug': 'August',
                'sep': 'September',
                'oct': 'October',
                'nov': 'November',
                'dec': 'December'}


class Labels:  # Responses template
    """=================== Main Labels Storage ======================="""

    @staticmethod
    def confirmation(cond):

        if cond == "yes":
            lines = ["Sure,,",
                     "Yes please..",
                     "Ok..",
                     "Yeah,..",
                     "Why not...",
                     "Sure Kato..",
                     ]
        elif cond == "no":
            lines = ["Nope..",
                     "Not now..",
                     "Don't do it..",
                     "Better not",
                     "No..",
                     "Later..",
                     ]
        else:
            lines = [""]

        return random.choice(lines)

    @staticmethod
    def print_userlist():
        lines = ["Sure,,print it out",
                 "Go ahead..",
                 "Go ahead Megumi..",
                 "Yes please Megumi..",
                 "Ok Megumi..",
                 "Yeah, do it Megumi..",
                 "Do it Megumi..",
                 "Sure Kato..",
                 ]
        return random.choice(lines)

    @staticmethod
    def template():
        lines = ["",
                 "",
                 "",
                 "",
                 ""]
        return random.choice(lines)

    @staticmethod
    def template_cond(cond):

        if cond == "a":
            lines = ["",
                     "",
                     "",
                     "",
                     ""]
        else:
            lines = ["",
                     "",
                     "",
                     "",
                     ""]

        return random.choice(lines)


class Picture:
    """=================== Main Picture URL Storage ======================="""

    @staticmethod
    def header(cond):

        if cond == "background":
            pic = ["https://il2.picdn.net/shutterstock/videos/1974016/thumb/1.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/005/037/small/Abstract_Blur_4K_Motion_Background_Loop.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/004/941/small/jellyfish-4k-living-background.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/005/030/small/silk-4k-wedding-background.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/005/045/small/Blurry_Vision_4K_Motion_Background_Loop.jpg",
                   "https://il2.picdn.net/shutterstock/videos/15516307/thumb/1.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/005/038/small/Alive_4K_Motion_Background_Loop.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/005/042/small/Beautiful_Slide_4K_Motion_Background_Loop.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/005/615/small/abstract-blue-bokeh-b-roll-4k-stock-video.jpg",
                   "https://static.videezy.com/system/resources/thumbnails/000/006/812/small/colorful-bokeh.jpg",
                   "https://image.prntscr.com/image/XnWrAZXzRbusdRR2Oa1jqQ.png",
                   "https://image.prntscr.com/image/p_ZhtpMXQbefEpBOkx8zGg.png",
                   "https://image.prntscr.com/image/ZLb5kK1URSmuAS4h26tzdg.png",
                   "https://image.prntscr.com/image/zf5HTDIrSbebNcNqJS_t7g.png"
                   ]
        elif cond == "ask":  # Picture of question mark
            pic = ["https://image.prntscr.com/image/t2BFLWxiRf2OJq_G4kKKtw.png",
                   "https://image.prntscr.com/image/nSJazwxBSxeClYngG-TJRA.png",
                   "https://image.prntscr.com/image/cOcP56B-TZmMB1JPyHr6jA.png",
                   "https://image.prntscr.com/image/GZM3QV4ARKqd-2yrYJiMlA.png",
                   "https://image.prntscr.com/image/CpdR3MrwRP2vpvNBQvRe-w.png"
                   ]
        else:
            pic = [""]

        return random.choice(pic)

    @staticmethod
    def weatherforecast(cond):
        # USE LOWER AS COND

        if cond == "clouds":
            pic = ["https://image.prntscr.com/image/PGZ4Gs3tTYWr9qFJVfxIpQ.png",
                   "https://image.prntscr.com/image/gUspo5phTG6Zaak1ZIgUIQ.png",
                   "https://image.prntscr.com/image/vG5496PTQhCDsNUR2DPW9Q.png",
                   "https://image.prntscr.com/image/_rcPb1dfQ52rtgrckc1ylw.png",
                   "https://image.prntscr.com/image/q9GM5yHxQ4qZDqwMOHpthg.png"
                   ]
        elif cond == "clear":
            pic = ["https://image.prntscr.com/image/J_axWG2PQIiLhffxLSz4hg.png",
                   "https://image.prntscr.com/image/8C3uy2XhT1_Z2iTogruoRg.png",
                   "https://image.prntscr.com/image/CoMxClunSnSUkUR9ICxXTA.png",
                   "https://image.prntscr.com/image/Y1DcoH_ZQduyfKrJisT7vA.png",
                   "https://image.prntscr.com/image/DL6R4D5jRdi6zjby21L8gA.png",
                   "https://image.prntscr.com/image/Bh3wW9k7SDevz5hhJcFirg.png",
                   "https://image.prntscr.com/image/0SO5lsxvQUCP6BiLSyRNbg.png"
                   ]
        elif (cond == "rain") or (cond == "drizzle"):
            pic = ["https://image.prntscr.com/image/5WT8CDGzRJiwmB4LWiruqQ.png",
                   "https://image.prntscr.com/image/e9_Nsew_SQuheBN4igjwhQ.png",
                   "https://image.prntscr.com/image/cn7TJRnCSlizpt8LZY5o5A.png",
                   "https://image.prntscr.com/image/q-wiQ4zJTnqvvMb0gba58Q.png",
                   "https://image.prntscr.com/image/oiSibwvPS_O4qB6bpnfghA.png",
                   "https://image.prntscr.com/image/edf1XiRGR2u_A0ke2DWaqQ.png",
                   "https://image.prntscr.com/image/2ZC8qpGkTxGPmLONeVfQWA.png",
                   "https://image.prntscr.com/image/OXYCQVeKQrWJg7a6QQW7Xw.png"
                   ]
        elif cond == "snow":
            pic = ["https://image.prntscr.com/image/LDEYpPsWRLK-Ir7pxDddAw.png",
                   "https://image.prntscr.com/image/cgpt7PqgRQaQ93bpz8rlkw.png",
                   "https://image.prntscr.com/image/ETEH05euQVWOMBKk1_d5yw.png",
                   "https://image.prntscr.com/image/F1kazAtERguXiHHNQE6ZLA.png",
                   "https://image.prntscr.com/image/v7_tw7goTCKWjRnMm3kfZg.png"
                   ]
        elif cond == "extreme":
            pic = ["https://image.prntscr.com/image/_v2Sl2sWQlyiSv-Q77Namw.png",
                   "https://image.prntscr.com/image/_N8jIhjESsSObPC2t-mxHA.png",
                   "https://image.prntscr.com/image/dWJnXtkDSW_FgHZpwZXbUA.png",
                   "https://image.prntscr.com/image/wNkCAYQFTECGU2JPYxuTgw.png",
                   "https://image.prntscr.com/image/LY4H7k31QQaWilsIx_ySfQ.png"
                   ]
        elif cond == "mist":
            pic = ["https://image.prntscr.com/image/KQsc4A9jSF2e55otWrE3Bw.png",
                   "https://image.prntscr.com/image/vV0IeYeyROCPsZFyldQmNA.png",
                   "https://image.prntscr.com/image/orjbuhdWRRS83ENUMIuXjg.png",
                   "https://image.prntscr.com/image/fE6WH_NqR9GD6Sw6XEBa1Q.png",
                   "https://image.prntscr.com/image/ixc6IBMERZyedENAsuV-Ww.png"
                   ]
        else:
            pic = ["https://image.prntscr.com/image/t2BFLWxiRf2OJq_G4kKKtw.png",
                   "https://image.prntscr.com/image/nSJazwxBSxeClYngG-TJRA.png",
                   "https://image.prntscr.com/image/cOcP56B-TZmMB1JPyHr6jA.png",
                   "https://image.prntscr.com/image/GZM3QV4ARKqd-2yrYJiMlA.png",
                   "https://image.prntscr.com/image/CpdR3MrwRP2vpvNBQvRe-w.png"
                   ]

        return random.choice(pic)
