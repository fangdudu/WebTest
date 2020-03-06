import random

import requests

My_User_Agent = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

Headers = {
    'User-Agent': random.choice(My_User_Agent),
    'authority': 'www.mzitu.com',
    'method': 'GET',
    # 'path': '/',  #:path: /222486
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6',
    'cache-control': 'max-age = 0',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    # sec - fetch - site: same - origin
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'referer': 'https://www.mzitu.com/'
    # if-modified-since: Sun, 09 Feb 2020 13:57:52 GMT
}


def request_page(url):
    try:
        response = requests.get(url, headers=Headers)
        if response.status_code == 200:
            return response.text
        else:
            print('获取失败!页面返回：', response.status_code)
    except requests.RequestException:
        print("页面获取失败，再来！")
        request_page(url)
        return None


def get_page_urls():
    for i in range(1, 3):
        baseurl = 'https://www.mzitu.com/215445'
        html = request_page(baseurl)
        print(html)
        print(baseurl)
        print(html)


if __name__ == '__main__':
    get_page_urls()
