#!/usr/bin/python3
import subprocess # will use to call system commands
import re # will use regular expressions to find network info
import requests # will use to call HTTP GET for our email web app
import random

cows = (['apt', 'beavis.zen', 'bud-frogs', 'bunny', 'calvin', 'cock', 'daemon', 'default', 'dragon', 'dragon-and-cow', 'duck',
         'elephant', 'eyes', 'flaming-sheep', 'ghostbusters', 'gnu', 'koala', 'luke-koala', 'mech-and-cow', 'milk', 'moofasa',
         'moose', 'pony-smaller', 'ren', 'sheep', 'skeleton', 'snowman', 'stegosaurus', 'stimpy', 'suse', 'three-eyes', 'turkey',
         'turtle', 'tux', 'unipony-smaller', 'vader', 'vader-koala'])
randCow = cows[random.randint(0,len(cows)-1)]

ps = subprocess.Popen(('/usr/games/fortune'), stdout=subprocess.PIPE)
fortuneText = subprocess.check_output((['/usr/games/cowsay', '-f', randCow]), stdin=ps.stdout)
ps.wait()

webAppURL = "https://script.google.com/macros/s/AKfycbzKRyi2D2Cn_5lqk37SzzXfjxFxR23mnA_mGKPf1v5lTY9X6J8/exec"
dataToSend = {"fortune":fortuneText}
# Use the requests library to send an HTTP request to the Web App.
response=requests.get(webAppURL,params=dataToSend)
# After receiving this request the Web App kicks in and sends the email.
print(response.text)
