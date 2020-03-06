import requests
import re
from prettytable import PrettyTable


def request_douban(url):
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
        response = requests.get(url, headers={'User-Agent': user_agent})
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        print("Refuse")
        return None


def parse_result(html):
    html = str(html)
    pattern = re.compile(
        r'<div class="pl2">\s*<a href="(.*?)".*?title="(.*?)".*?<span class="rating_nums">(.*?)</span>.*?<span class="pl">\(\s+(.*?)\s+\)',
        re.S)
    items = re.findall(pattern, html)
    dict = {}
    for item in items:
        dict[item[1]] = {'Reviews': item[3], 'Rate': item[2], 'Url': item[0]}
    return dict


def main(page):
    url = 'https://book.douban.com/top250?start=' + str(25 * page)
    html = request_douban(url)
    items = parse_result(html)
    return items


if __name__ == "__main__":
    dat = {}
    lst = []
    for i in range(0, 9):
        dat.update(main(i))
    lst = sorted(dat.items(), key=lambda x: x[1]["Rate"], reverse=True)  # 返回列表
    table = PrettyTable(['Book name', 'Book rate', 'Book url'])
    for i in lst:
        table.add_row([i[0], i[1]['Rate'], i[1]['Url']])
    print(table)

