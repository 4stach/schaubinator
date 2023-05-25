
import random
from bs4 import BeautifulSoup
import requests

class Schaubinator():

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    }
    strona1 = []
    url = 'http://www.feelthewords.com/brendan-schaub-quotes'
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    result1 = soup.find_all("p", class_="color-dark text-center")
    for p_tag in result1:
        nohtml_result = p_tag.text
        strona1.append(nohtml_result)
        if nohtml_result is not None:
            print(type(nohtml_result))
    if nohtml_result in strona1:
        print(strona1)
    else:
        print("niedziala")

    for x in range(len(strona1)):
        print(strona1[x])

    ###### Reddit Input
    headers2 = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    }
    strona2 = []
    url2 = 'http://www.reddit.com/r/tfatk/comments.json'
    page2 = requests.get(url2, headers=headers2)
    soup2 = BeautifulSoup(page2.content, "html.parser")
    result2 = soup.find_all("a", class_="md")

    for a_tag in result2:
        reddit_result = a_tag.text
        strona2.append(reddit_result)
        if reddit_result is None:
            print(type(reddit_result))
        if reddit_result in strona2:
            print(strona2)
        else:
            print("niedziala")
    zdania = strona1 + strona2

    def schaub_random():
        zart = random.choice(strona1)
        return zart

    if __name__ == "__main__":
        print(schaub_random())







