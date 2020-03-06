# coding=utf-8
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import xlwt

# browser = webdriver.PhantomJS()
# browser = webdriver.Firefox()
options = Options()
options.add_argument('-headless')  # 无头参数
browser = Firefox(executable_path='geckodriver', firefox_options=options)
WAIT = WebDriverWait(browser, 10)
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('蔡徐坤篮球', cell_overwrite_ok=True)
n = 1


def _excel_init():
    global sheet
    sheet.write(0, 0, '名称')
    sheet.write(0, 1, '地址')
    sheet.write(0, 2, '描述')
    sheet.write(0, 3, '观看次数')
    sheet.write(0, 4, '弹幕数')
    sheet.write(0, 5, '发布时间')


n = 1


def init(key='蔡徐坤篮球'):
    '''
    初始化
    '''
    global browser
    browser.get("https://search.bilibili.com/all?keyword=" + str(key) + "&order=dm&duration=0&tids_1=0")


## 我们要设计一个  可以获取搜索结果总页数  如果出现了<li class="page-item last"><button class="pagination-btn">只显示50页数据
## <li class="page-item next"><button class="nav-btn iconfont icon-arrowdown3">
#        下一页
#      </button></li>
# 在这个标签之前的那个标签就是最后一页的数据
## 出现了<div class="no-content"></div> 说明是没有数据的
## 如果只有一页  <div class="page-wrap"><!----></div>

def count():
    # 页面内容 >= 2 页时
    total = WAIT.until(method=EC.presence_of_element_located((By.CSS_SELECTOR,
                                                              "#all-list > div.flow-loader > div.page-wrap > div > ul > li:nth-last-child(2) > button")))
    # 页面不存在时
    # 只存在一个页面
    return int(total.text)


def save(soup):
    list = soup.find(class_='video-list clearfix').find_all(class_='video-item matrix')

    for item in list:
        item_title = item.find('a').get('title')
        item_link = item.find('a').get('href')
        item_dec = item.find(class_='des hide').text
        item_view = item.find(class_='so-icon watch-num').text
        item_biubiu = item.find(class_='so-icon hide').text
        item_date = item.find(class_='so-icon time').text

        print('爬取：' + item_title)
        global sheet
        global n
        sheet.write(n, 0, item_title)
        sheet.write(n, 1, item_link)
        sheet.write(n, 2, item_dec)
        sheet.write(n, 3, item_view)
        sheet.write(n, 4, item_biubiu)
        sheet.write(n, 5, item_date)
        n += 1


def get_source():
    try:
        WAIT.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#all-list > div.flow-loader > div.mixin-list')))
    except TimeoutException:
        browser.refresh()
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    save(soup)


def next_page():
    print('开始获取下一页数据')
    n_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                   '#all-list > div.flow-loader > div.page-wrap > div > ul > li.page-item.next > button')))
    n_btn.click()


def dig(sum):
    i = 1
    sum = 2
    while i <= sum:
        get_source()
        next_page()
        i += 1


def main():
    _excel_init()
    init()  # 初始化
    sum = count()  # 获取总页数
    dig(sum)  # 如果有页面，则开始搜索页面的数据  搜索的同时进行输出


if __name__ == '__main__':
    main()
    book.save('蔡徐坤篮球.xlsx')
