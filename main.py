import requests        #导入requests包
import util
from bs4 import    BeautifulSoup
import pdb
import time
import os
from single import get_titile,get_cn_words

def main():
    base_url = 'https://www.kexiaoguo.com'
    movie_name = "laoyouji"
    
    # change every time
    first_idx = 1
    last_idx = 382

    # first_idx = 73
    # last_idx = 144

    idx = first_idx
    while True:
        url = "{}/{}/{}".format(base_url,movie_name,idx)
        strhtml = requests.get(url).text
        soup=BeautifulSoup(strhtml,'lxml')
        
        title,season,episode = get_titile(soup)
        print(url,title)

        dir_path = "S{:02d}".format(season)
        file_name = os.path.join(dir_path,title)+".txt"
        cn_lines = get_cn_words(soup)
        with open(file_name, "ab") as file:
            for line in cn_lines:
                file.write(line.encode())

        time.sleep(1)
        idx += 1
        if idx > last_idx:
            break

def make_dir():
    for season in range(1,11):
        dir_path = "S{:02d}".format(season)
        # os.makedirs(dir_path,exist_ok=True)
        os.makedirs(dir_path)

if __name__ == "__main__":
    
    make_dir()
    main()

