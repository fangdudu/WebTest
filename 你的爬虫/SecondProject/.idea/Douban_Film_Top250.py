import requests
from bs4 import BeautifulSoup
import xlwt

n = 1
film = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = film.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)


def _init_excel():
    sheet.write(0, 0, 'Name')
    sheet.write(0, 1, 'Picture')
    sheet.write(0, 2, 'Ranking')
    sheet.write(0, 3, 'Score')
    sheet.write(0, 4, 'Author')
    sheet.write(0, 5, 'Brief Introduction')


def request_douban(url):
    try:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
        response = requests.get(url, headers={'User-Agent': user_agent})
        if response.text is None:
            print("被安排了！")
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        print("访问出错了！")
        return None


def save_to_excel(soup):
    list = soup.find(class_='grid_view').find_all('li')

    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if (item.find(class_='inq') != None):
            item_intr = item.find(class_='inq').string

        global n
        n += 1
        sheet.write(n, 0, item_name)
        sheet.write(n, 1, item_img)
        sheet.write(n, 2, item_index)
        sheet.write(n, 3, item_score)
        sheet.write(n, 4, item_author)
        sheet.write(n, 5, item_intr)


def main(page):
    url = "https://movie.douban.com/top250?start=" + str(page * 25) + "&filter="
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


if __name__ == '__main__':
    for i in range(0, 10):
        main(i)
    film.save(u'豆瓣最受欢迎的250部电影.xlsx')
