from urllib.request import urlopen
from bs4 import BeautifulSoup

naver = "https://www.naver.com/"

def get_text(ref):
    txt_list = list()

    html = urlopen(ref)
    item = BeautifulSoup(html, "html.parser")

    for txt in item.text: 
        txt_list.append(txt)
    
    word = ''.join(txt_list)
    word_list = word.split('\n')
    
    return word_list

with open("Text.txt", "w", encoding='UTF8') as file:
    lst = get_text(naver)
    for i in range(0, len(lst)):
        file.write("{0}\n".format(lst[i]))
