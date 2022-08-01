import requests        #导入requests包
from bs4 import    BeautifulSoup

def save_html(url):
    strhtml = requests.get(url).text        #Get方式获取网页数据
    pdb.set_trace()
    soup=BeautifulSoup(strhtml,'lxml')
    with open(html_name, "wb") as file:
        file.write(str(soup).encode())

def get_text_from_local():
    with open("pretty.html","rb")as f:
        html_text = f.read().decode()
    return html_text

#检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

if __name__ == "__main__":
    url = "https://www.kexiaoguo.com/laoyouji/94"
    save_html(url)