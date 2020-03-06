import re

language = '''
        <table width="100%">
            <tbody><tr class="item">
                <td width="100" valign="top">
                    <a class="nbg" href="https://book.douban.com/subject/1770782/" onclick="moreurl(this,{i:'0'})">
                        <img src="https://img3.doubanio.com/view/subject/m/public/s1727290.jpg" width="90">
                    </a>
                </td>
                <td valign="top">

                    <div class="pl2">


                    <a href="https://book.douban.com/subject/1770782/" onclick="&quot;moreurl(this,{i:'0'})&quot;" title="追风筝的人">
                    追风筝的人


                    </a>



                    &nbsp; <img src="https://img3.doubanio.com/pics/read.gif" alt="可试读" title="可试读">


                    <br>
                    <span style="font-size:12px;">The Kite Runner</span>
                    </div>

              <p class="pl">[美] 卡勒德·胡赛尼 / 李继宏 / 上海人民出版社 / 2006-5 / 29.00元</p>




              <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">8.9</span>##

                <span class="pl">(
                    582600人评价
                )</span>
              </div>


              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">为你，千千万万遍</span>
              </p>


          </td>
        </tr>
      </tbody></table>'''

pattrn = re.compile(
    r'<table width="100%">\s*?<tbody>\s*?<tr class="item">.*?<td valign="top">\s*?<div class="pl2">\s*?<a href="(.*?)".*?title="(.*?)">.*?</a>.*?<span style="font-size:12px;">(.*?)</span>.*?</div>.*?<div class="star clearfix">.*?<span class="rating_nums">(.*?)</span>.*?<span class="pl">\(\s+(.*?)\s+\)',
    re.S)
m_tr = re.findall(pattrn, language)
for i in m_tr:
    print(i)
