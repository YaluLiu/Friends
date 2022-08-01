import util
import requests        #导入requests包
from bs4 import    BeautifulSoup
import pdb
import time
import os
import re



def get_titile(soup):
    company = soup.find_all(id="fanyi")[0]
    h1s = company.find_all({"h1"})
    title = h1s[1].string
    season = int(title[8:10])
    episode = int(title[12:14])

    return title,season,episode

def get_role(words):
    idx = words.find(":")
    if idx == -1:
        idx = words.find("：")
    
    # not found role name
    if idx == -1:
        return ""

    return words[:idx+1]

def filter_lines(all_lines):
    ret_lines = []
    for line in all_lines:
        if line.startswith("<strong>"):
            continue
        line = line.replace("<strong>","")
        line = line.replace("</strong>","")
        line = line+"\n"
        ret_lines.append(line)
    return ret_lines


def get_cn_words(soup):
    neirong = soup.find_all(id="neirong")
    lines_result = neirong[0]
    lines = str(lines_result)

    lines = lines.replace("<p>","")
    lines = lines.replace("</p>","")
    lines = lines.replace("<h1>","")
    lines = lines.replace("</h1>","")
    lines = lines.replace("♥","")
    lines = lines.replace("<br/>","\n")
    lines = lines.split("\n")

    lines = filter_lines(lines)
    
    cn_lines = []
    for line in lines:
        if  util.is_contains_chinese(line[:3]):
            cn_line = role + line
            cn_lines.append(cn_line)
        else:
            role = get_role(line)
    return cn_lines

def make_dir():
    for season in range(1,11):
        dir_path = "S{:02d}".format(season)
        os.makedirs(dir_path)

def test(url):
    strhtml = requests.get(url).text
    soup=BeautifulSoup(strhtml,'lxml')
    cn_lines = get_cn_words(soup)
    with open("test.txt", "wb") as file:
        for line in cn_lines:
            file.write(line.encode())


if __name__ == "__main__":
    url = "https://www.kexiaoguo.com/laoyouji/1"
    test(url)