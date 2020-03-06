import os
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
from twisted.scripts.htmlizer import header

ua = UserAgent()


def request_page(url):
    try:
        response = requests.get(url, headers={'User-Agent': ua.random})
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        print("Refuse!")
        return None


def get_page_urls():
    for i in range(1, 2):
        baseurl = 'https://www.mzitu.com/page/{}'.format(i)
        html = request_page(baseurl)
        soup = BeautifulSoup(html, 'lxml')
        list = soup.find(class_='postlist').find_all('li')
        urls = []
        for item in list:
            url = item.find('span').find('a').get('href')
            urls.append(url)
    return urls


def download_Pic(title, image_list):
    # 新建文件夹
    os.mkdir(title)
    j = 1
    # 下载图片
    for item in image_list:
        filename = '%s/%s.jpg' % (title, str(j))
        print('downloading....%s : NO.%s' % (title, str(j)))
        with open(filename, 'wb') as f:
            img = requests.get(item, headers=header(item)).content
            f.write(img)
        j += 1


def download(url):
    html = request_page(url)
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find(class_='pagenavi').find_all('a')[-2].find('span').string  # 图片的总数
    title = soup.find('h2').string  # 图片的名称
    image_list = []
    for i in range(int(total)):
        html = request_page(url + '/%s' % (i + 1))
        soup = BeautifulSoup(html, 'lxml')
        img_url = soup.find('img').get('src')
        print(img_url)
        image_list.append(img_url)
    download_Pic(title, image_list)


if __name__ == '__main__':
    urls = get_page_urls()
    for url in urls:
        print(url)
    for url in urls:
        download(url)
