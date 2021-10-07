"""
Written by: Rashid Mamadolimov, on 13/11/2019

The code laods the certain web page and lists emoticons from the page.

Note: The output accuracy is not 100%. The reason maybe UNICODE_EMOJI method can't fully recognize eastern emojis.
"""


from lxml import html
import requests
import emoji

#loading page
page = requests.get('https://en.wikipedia.org/wiki/List_of_emoticons')
tree = html.fromstring(page.content)

#selecting appropriate nodes for emoticons
emoticons = tree.xpath('//table[@class="wikitable"]//tbody//tr//td[position()<last()]/text()')

#detecting emoji function
def text_has_emoji(text):
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            return True
    return False

#filtering emojies
for item in emoticons:
    if text_has_emoji(item)==True:
        emoticons.remove(item)

#filtering "\n"s
for i in range (len(emoticons)):
    if "\n" in emoticons[i]:
        emoticons[i]=emoticons[i].replace("\n","")

for item in emoticons:
    if item=="":
        emoticons.remove(item)

print(*emoticons, sep="\t\t")