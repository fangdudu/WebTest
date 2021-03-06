import re

string = '''
<table width="100%">
    <tr class="item">
        <td width="100" valign="top">
            <a class="nbg" href="https://book.douban.com/subject/25862578/" onclick="moreurl(this,{i:'1'})">
                <img src="https://img3.doubanio.com/view/subject/m/public/s207264181.jpg" width="90"/>
            </a>
        </td>
        <td valign="top">
            <div class="pl2">
                <a href="https://book.douban.com/subject/25862578/" onclick=&#34;moreurl(this,{i:&#39;1&#39;})&#34;
                   title="解忧杂货店">
                    解忧杂货店
                </a>
                <br/>
                <span style="font-size:12px;">ナミヤ雑貨店の奇蹟</span>
            </div>
            <p class="pl">[日] 东野圭吾 / 李盈春 / 南海出版公司 / 2014-5 / 39.50元</p>
            <div class="star clearfix">
                <span class="allstar45"></span>
                <span class="rating_nums">8.5</span>
                <span class="pl">(   
                    583389人评价
                )</span>
            </div>
            <p class="quote" style="margin: 10px 0; color: #666">
                <span class="inq">一碗精心熬制的东野牌鸡汤，拒绝很难</span>
            </p>
        </td>
    </tr>
</table>'''

print(re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", string))  # url
print(re.findall(r'<span.*?>(.*?)</span>', string))  # span
print(re.findall(r'<span.*?>((.|\r|\n)*?)</span>', string))  # span
print(re.findall(r'<span class="pl">\(\s+(\d*).*\s+\)</span>', string))  # 产生了歧义
print(re.findall(r'<span class="pl">\(\s+(.*?)\s+\)</span>', string))  # 产生了歧义
