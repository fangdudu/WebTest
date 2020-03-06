Dict1 = {'追风筝的人': {
    'Reviews': 1,
    'Rate': 8.9,
    'Url': 'https://book.douban.com/subject/1770782/'},
    '解忧杂货店': {
        'Reviews': 2,
        'Rate': 8.5,
        'Url': 'https://book.douban.com/subject/25862578/'},
    '解忧': {
        'Reviews': 3,
        'Rate': 8.6,
        'Url': 'https://book.douban.com/subject/25862578/'}

}
print(sorted(Dict1.items(), key=lambda x: x[1]['Rate'], reverse=True))  #
# print(dat)
# print(sorted(dat, key=lambda book:book[]))
# 我们要做的是 写一个稍微复杂的字典（有点麻烦，数据结构的知识） 也可以通过写一个对象（舒服）
# 1)Name 2)Info  也可以用isbn作key 其他数据作为value来写
# Info 是一个字典
# {
# 'Reviews':评论人数,
# 'Rete':评价
# 'Url':书的url
# }
