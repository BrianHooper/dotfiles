# coding: utf-8

import requests
from bs4 import BeautifulSoup as BS
import textwrap
from termcolor import colored, cprint
import shutil

wrapper = textwrap.TextWrapper(width=60)


def print_wrap(line):
    word_list = wrapper.wrap(text=line[0].upper() + line[1:])

    print("\t• " + word_list[0])
    for element in word_list[1:]:
        print("\t\t" + element)


request = requests.get("http://en.wikipedia.org")
lines = request.text.splitlines()

dyk = []
itn = []
otd = []

i = 0
while "Did_you_know..." not in lines[i]:
    i = i + 1
while "<li>" not in lines[i]:
    i = i + 1
while "<li>" in lines[i]:
    dyk += [lines[i]]
    i = i + 1
while "In_the_news" not in lines[i]:
    i = i + 1
while "<li>" not in lines[i]:
    i = i + 1
while "<li>" in lines[i]:
    itn += [lines[i]]
    i = i + 1
while "On_this_day" not in lines[i]:
    i = i + 1
while "<li>" not in lines[i]:
    i = i + 1
while "<li>" in lines[i]:
    otd += [lines[i]]
    i = i + 1

print(colored("Did you know?", "green"))
for line in dyk:
    print_wrap(BS(line, "html.parser").text[9:])
print(colored("In the news", "green"))
for line in itn:
    print_wrap(BS(line, "html.parser").text)
print(colored("On this day", "green"))
for line in otd:
    print_wrap(BS(line, "html.parser").text)
