import re

# string = "A1.45，b5，6.45，8.82，d1."
# print(re.findall(r"\d+\.?\d*", string))
# # ['1.45', '5', '6.45', '8.82', '1.']匹配数字 出现错误 1.


string = '''
<!DOCTYPE html>
<html lang="zh-cmn-Hans" class="ua-linux ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
    300个国外优秀网站
</title>
    
    
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    
    <meta http-equiv="Cache-Control" content="no-siteapp" />
    

    <meta name="mobile-agent" content="format=html5; url=https://m.douban.com/group/topic/4002607/">

    <script >var _head_start = new Date();</script>
    <script src="https://img3.doubanio.com/f/shire/72ced6df41d4d158420cebdd254f9562942464e3/js/jquery.min.js"></script>
    <script src="https://img3.doubanio.com/f/shire/5ecaf46d6954d5a30bc7d99be86ae34031646e00/js/douban.js"></script>
    <link href="https://img3.doubanio.com/f/shire/3e5dfc68b0f376484c50cf08a58bbca3700911dc/css/douban.css" rel="stylesheet" type="text/css">
    <style type="text/css">
    
        

    

    </style>
    


<link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" />
<link rel="stylesheet" type="text/css" href="https://img3.doubanio.com/f/shire/6955e5a57af3e891380cbab06b7c68e8c919404c/css/doulist/tooltip.css" />

<script type="text/javascript" src="https://img3.doubanio.com/f/group/aaf1129ac0f59e5d7377c448af87c8c2ad29b339/js/group/editor/libs.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/group/cdee4dfa96662f68b1890cd7d8c30f9c5595c8d9/js/group/pos_fixed.js"></script>
<script type="text/javascript" src="https://img3.doubanio.com/f/group/11d2157b933d679a0e72e916364a9fab4dc7ff50/js/group/topic/index.js"></script>
<script type="text/javascript">
    $(function () {
        var sidebar = fixed($('#content .aside'), {
            fixedBound: 'bottom',
            gap: 197
        });
        sidebar.init();
    })
</script>





<script type="application/ld+json">
{
	"@context": "http://schema.org",
	"@type": "Conversation",
  "text": "偶尔的发现，感谢原作者！


1 People(人物） 
http://people.aol.com/people/index.html 
娱乐 全球五十位最XX的人 
2 TV Guide（电视指南） 
http://www.tvguide.com 
娱乐默多克旗下 
3 Time（时代）http://www.time.com/ 
新闻年度风云人物 
4 Sports Illustrated（体育画报）http://sportsillustrated.cnn.com/ 
体育 本世纪 最佳运动员 
5 Better Homes  Gardens（美好家园）http://www.bhg.com/ 家居 
6 Reader’s Digest(读者文摘）http://www.rd.com/splash.jhtml 综合 美国发行量最 

大的商业杂志 
7 Parade（旅行）http://www.parade.com/auth/entry.lasso 旅游 
8 Newsweek（新闻周刊）http://www.msnbc.com/news/NW-front_Front.asp 新闻 微软收
购 
9 Business Week（商业周刊）http://www.businessweek.com/ 商业 25位XX人 全球最有
价值品牌　 
10Good Housekeeping（好主妇）http://www.goodhousekeeping.com/ 家庭 
11Fortune（财富）http://www.fortune.com/ 商业全球五百强 
12Cosmopolitan（全球主义者）http://www.cosmopolitan.com/ 娱乐 
13Woman’s Day（妇女日）http://www.womansday.com/xp6/WomansDay/home.xml 妇女 

14Forbes（福布斯）http://www.forbes.com/ 商业全球最富的多少人 
15Family Circle（家庭圈）http://www.familycircle.com/home/homepage.jsp 家庭 

16USA Weekend（美国周末）http://www.usaweekend.com/ 休闲甘尼特报业公司旗下 
17Instyle（时髦）http://www.instyle.com/instyle 时尚 年度性感偶像 
18Entertainment Weekly(娱乐周刊）http://www.ew.com/ew/ 娱乐 
19Martha Stewart Living（玛萨斯图尔特生活） http://www.marthastewart.com/ 生活

指导美国人生活的女王 
20U.S. News  World Report（美国新闻与世界报道）http://www.usnews.com/ 新闻全美
大学排行榜 
21Ladies’ Home Journal(妇女家庭杂志) http://www.lhj.com/ 家庭 
22National Geographic(国家地理杂志) http://www.nationalgeographic.com/ 地理 

23Southern Living（南方生活）http://www.southernliving.com/ 生活 
24Vogue（时尚）http://www.style.com/vogue/index.html 时尚 
25PC Magazine（个人电脑）http://www.pcmag.com/ IT 
26Money（金钱）http://money.cnn.com/ 理财 
27Maxim（马克西姆）http://www.maximonline.com/index.html 娱乐 
28O, The Oprah Magazine http://www.oprah.com/omagazine 妇女 
29Glamour（魅力）http://www.glamour.com/ 时尚 
30National Enquirer, The（国家寻问者）http://www.nationalenquirer.com/ 新闻 

31New York Times Magazine（纽约时报杂志）http://www.nytimes.com/ 新闻 
32Golf Digest（高尔夫文摘）http://www.golfdigest.com/ 体育 
33Rolling Stone（滚石）http://www.rollingstone.com/ 音乐 
34Playboy（花花公子）http://www.playboy.com/ 男性 
35Vanity Fair（名利场）http://www.vanityfair.com/ 娱乐名人采访 
36Seventeen（十七岁）http://www.seventeen.com/ 青年 
37Parents（父母）http://www.parents.com/ 教育 
38Star Magazine（明星杂志）http://www.starmagazine.com/ 娱乐 
39ESPN The Magazine（ESPN杂志）http://espn.go.com/magazine/ 体育 
40Prevention（预防）http://www.prevention.com/ 健康 
41Redbook（红书）http://magazines.ivillage.com/redbook/ 妇女 
42Rosie http://www.rosieo.com/ 
43Golf Magazine（高尔夫杂志）http://sportsillustrated.cnn.com/golfonline/ 体育

44Travel  Leisure（旅游和休闲）http://www.travelandleisure.com/ 休闲 
45Elle http://www.elle.com/ 时尚 
46New Yorker, The（纽约客）http://www.newyorker.com/ 文艺 
47W http://www.style.com/w/ 时尚 
48Woman’s World(妇女世界）http://www.robertcraig.com/womansworld.html 妇女 

49Parenting（养育）http://www.parenting.com/parenting/ 家庭 
50Car  Driver（人车志）http://www.caranddriver.com/xp/Caranddriver/home.xml 

机车 
51Endless Vacation（无尽假日）http://www.endlessvacation.com/ 休闲 
52Bride’s Magazine（新娘杂志）http://www.brides.com/ 婚礼 
53InformationWeek（信息周刊）http://www.informationweek.com/ IT 
54Country Living（乡村生活）http://magazines.ivillage.com/countryliving/ 生活 

55Us Weekly（美国周刊）http://usweekly.abc.com/ 新闻 
56Marie Claire（玛丽克莱尔）http://www.marieclaire.com/ 时尚 
57Sunset（日落）http://www.sunset.com/ 科学 
58Soap Opera Digest（肥皂剧文摘）http://www.soapoperadigest.com/ 娱乐 
59AARP Modern Maturity（现代文明） http://www.modernmaturity.org/ 公益 
美国发 行量最大的杂志 
60GQ http://www.gq.com/ 时尚 
61Architectural Digest（建筑学文摘） 
http://www.condenet.com/mags/archdigest/ 建筑 
62Harper’s Bazaar(哈泼氏）http://www.harpersbazaar.com/ 时尚 
63Travel Agent（旅游代理）http://www.travelagents.com/ 旅游 
64Smithsonian（史密森尼)http://www.si.edu/ 博物 
65PC World（PC世界）http://www.pcworld.com/ IT 
66Modern Bride（现代新娘）http://www.modernbride.com/ 婚礼 
67Men’s Health（男性健康）http://www.menshealth.com/ 健康 
68Bon Appetit（好　）http://www.epicurious.com/b_ba/b00_home/ba.html 烹饪 
69Motor Trend（机车潮流）http://www.motortrend.com/ 机车 
70Economist, The（经济学人）http://www.economist.com/ 
政经世界上最牛的政经杂志 
71Self（自我）http://www.self.com/ 妇女 
72Shape（体形）http://www.shapeonline.com/ 健康 
73Teen People http://www.teenpeople.com/teenpeople/ 青年 
74YM http://www.ym.com/ 时尚 
75Consumer Reports（消费者报告） 
http://www.consumerreports.org/main/home.jsp 消费 
76Cooking Light（烹饪之光）http://www.cookinglight.com/ 烹饪 
77Travel Weekly（旅行周刊） 
http://www.travelweekly.co.uk/tw_home/home.asp 旅游 
78House Beautiful（美丽住宅）http://magazines.ivillage.com/housebeautiful/ 家居

79Ebony（乌木）http://www.ebony.com/ 成人 
80Popular Photography（大众摄影）http://www.popularphotography.com/index.asp 摄
影 
81Country Home（乡村家庭）http://www.countryhome.com/ch/index.html 家庭 
82Barron’s http://www.barrons.com/ 商业 
83eWeek http://www.eweek.com/ 消费 
84Conde Nast Traveler http://www.concierge.com/cntraveler/ 旅游 
85Town  Country(城镇和乡村) http://magazines.ivillage.com/townandcountry/ 生活

86InfoWorld(信息世界) http://www.infoworld.com/ IT 
87EE Times http://www.eetimes.com/ 电子 
88Food  Wine(食物和酒) http://www.foodandwine.com/ 食品 
89New York(纽约) http://www.newyorkmetro.com/ 城市 
90Essence(本质) http://www.essence.com/ 黑人 
91Road  Track(公路与轨迹) http://www.roadandtrack.com/ 机车 
92Health(健康) http://www.health.com/ 健康 
93Inc(公司) http://www.inc.com/home/ 商业 
94Allure(吸引) http://www.allure.com/ 时尚 
95Vibe http://www.vibe.com/new/home/pointer.html 娱乐 
96Gourmet(美食家) http://www.gourmet.com/ 烹饪 
97Taste of Home(家的滋味) http://www.tasteofhome.com/ 烹饪 
98Muscle  Fitness(肌肉和健身) http://www.muscleandfitness.com/ 健康 
99Popular Mechanics(大众机械) http://popularmechanics.com/ 机械 
100Home(家) http://www.homemag.com/ 家居 

101fitness（健身) http://www.fitnessmagazine.com/home/index.jsp 健康 
102Field  Stream（田园和小溪) http://www.fieldandstream.com/ 休闲 
103American Baby（美国宝贝) 
http://www.americanbaby.com/ab/CDA/homepage/ 家庭 
104FamilyFun（家庭乐趣） http://familyfun.go.com/ 家庭 
105Sporting News, The（体育新闻) http://www.sportingnews.com/ 体育 
106Esquire（先生） http://www.esquire.com/ 男性 
107Penthouse（小棚屋） http://www.penthouse.com/ 成人 
108Kiplinger’s Personal Finance Magazine(吉朴林的个人金融杂志) 
http://www.kiplinger.com/ 理财 
109Globe(环球) http://www.boston.com/globe/ 环境 
110SmartMoney(精明理财) http://www.smartmoney.com/ 理财 
111Stuff(素材) http://www.stuffmagazine.com/ 男性 
112CRN　http://www.crn.com/ IT 
113Men’s Journal(男人) http://www.mensjournal.com/ 男性 
114House  Garden(家园) http://www.condenet.com/mags/hg/ 家居 
115Fast Company(快速公司) http://www.fastcompany.com/homepage/ 商业 
116Computer Shopper(计算机购物者) http://shopper.cnet.com/ 消费 
117Jet(黑玉) http://www.jetmag.com/ 黑人 
118First For Women　 http://www.ffwmarket.com/ 妇女 
119Traditional Home（传统家庭） http://www.traditionalhome.com/ 家庭 
120Automobile Magazine(汽车杂志） http://www.automobilemag.com/ 机车 
121Red Herring（红鲱鱼） http://www.redherring.com/ 商业 
122Highlights for Children（儿童文粹） http://www.highlights.com/ 儿童 
123Wired（连线） http://www.wired.com/ IT 
124Outside（户外） http://outsidemag.com/index.html 休闲 
125This Old House（这个老屋子） http://www.thisoldhouse.com/toh/ 家居 
126NetworkWorld（网络世界） http://www.networkworld.com/　IT 
127Entrepreneur（企业家） http://www.entrepreneur.com/ 商业 
128Popular Science（大众科学） http://www.popsci.com/popsci/ 科普 
129Elle Decor　 http://www.elledecor.co.th/ 设计 
130Quick Cooking （速煮） http://www.quickcooking.com/ 烹饪 
131Family Handyman（家庭佣人） http://www.familyhandyman.com/ 家居 
132Science（科学） http://www.sciencemag.org/ 科学 
133Bridal Guide（新娘指南） http://www.bridalguide.com/ 婚礼 
134Child（孩子） http://www.child.com/index.jsp 家庭 
135Cable Guide（有线电视指南） http://www.cableguide.co.uk/ 娱乐 
136Midwest Living（中西部生活） http://www.midwestliving.com/ 生活 
137Metropolitan Home（大城市生活） http://www.mho.co.uk/ 生活 
138Chronicle of Higher Education, The（高等教育编年史） 
http://chronicle.com / 教育 
139Mutual Funds Magazine（互动基金杂志） 
http://www.mutual-funds.com/mfmag/ 商业 
140Travelhost（旅游主人） http://www.travelhost.com/ 旅游 
141Sound  Vision（声与影） http://www.soundandvisionmag.com/index.asp 电影 

142CIO（首席信息官） http://www.cio.com/ IT 
143Hot Rod　 http://www.hotrod.com/ 机车 
144Computerworld（计算机世界） http://www.computerworld.com/ IT 
145Source, The（来源） http://www.thesource.com/ 黑人 
146Departures（启程） http://www.departures.com/ 商业 
147Spin（旋转） http://www.spin.com/ 音乐 
148Travel Holiday（旅行假日） http://www.travelholiday.com/ 旅游 
149Black Enterprise（黑人企业） http://www.blackenterprise.com/ 商业 
150BabyTalk（宝贝说话） 
http://www.parenting.com/parenting/...s/babytalk.html 家庭 
151New England Journal of Medicine（新英格兰医学期刊） 
http://content.nejm.org/ 医学 
152EBN Electronic Buyer’s News(EBN电子买主新闻) 
http://www.ebnonline.com/ 电 子 
153Jane(简) http://www.janes.com/ 军事 
154Working Mother(妇女运动者)　http://www.workingwoman.com/ 妇女 
155Men’s Fitness(男性健身) http://www.mensfitness.com/mens.html 健康 
156Victoria(维多利亚) http://magazines.ivillage.com/victoria/ 生活 
157CosmoGirl(都市女孩) http://www.cosmogirl.com/ 时尚 
158Nation’s Restaurant News(国家餐馆新闻) http://www.nrn.com/ 行业 
159Harvard Business Review(哈佛商业评论) http://www.hbr.com/ 商业 
160FHM(男人帮) http://www.fhm.com/ 男性 
161Sports Illustrated For Kids(儿童体育画报) http://www.sikids.com/ 儿童 
162Boating(航船) http://www.boatingmag.com/ 体育 
163Discover(探索) http://www.discover.com/ 科普 
164Real Simple(反朴归真) http://www.realsimple.com/realsimple/ 生活 
165Guideposts（路标） http://www.guideposts.com/ 宗教 
166Cycle World(环形世界) 
http://www.cycleworld.com/xp6/CycleWorld/main.xml 机车 
167EDN http://www.e-insite.net/ednmag/ 电子 
168Tennis Magazine(网球杂志) http://www.tennis.com/ 体育 
169Advertising Age(广告时代) http://www.adage.com/ 行业 
170Hemispheres(半球) http://www.hemispheresmagazine.com/home.htm 收藏 
171Fortune Small Business(财富小商业) 
http://www.fortune.com/smallbusiness/ 商业 
172Meetings  Conventions(会议) 
http://www.meetings-conventions.com/ 行业 
173Worth(价值) http://www.worth.com/magazine/index.cfm 理财 
174Outdoor Life(户外生活) http://www.outdoorlife.com/outdoor/ 休闲 
175Official U.S. Playstation Magazine(美国官方PS杂志) 
http://www.gamers.com/opm/index.jsp 游戏 
176Automotive News(汽车新闻) http://www.autonews.com/ 机车 
177Scientific American(科学美国人) http://www.sciam.com/ 科普 
178Nickelodeon　 http://www.nick.com/ 娱乐 
179More(更多) http://www.more.com/ 时尚 
180Ski(滑雪) http://www.skinet.com/skinet/ 体育 
181Lucky(幸运) http://www.luckymag.com/ 时尚 
182Interior Design(室内装饰设计) http://www.interiordesign.net/　行业 
183Sky (Delta Air Lines)(天空 三角航线) http://www.delta-sky.com/ 航线 
184Power  Motoryacht(能源和摩托艇) http://powerandmotoryacht.about.com/mbody.
htm 休闲 
185GamePro(专业游戏) http://www.gamepro.com/ 游戏 
186JAMA(睡衣裤) http://jama.ama-assn.org/ 健康 
187Furniture Today(今日家具) http://www.furnituretoday.com/index.shtml 家居 

188My Generation(我们这一代) http://www.mygeneration.org/ 音乐 
189Successful Meetings(成功会议) 
http://www.successmtgs.com/successmtgs/index.jsp 行业 
190Premiere(首映) http://www.premiere.com/ 电影 
191Birds  Blooms(鸟语花香) http://www.birdsandblooms.com/ 家居 
192Aviation Week  Space Technology(航空技术周刊) 
http://www.aviationnow.com/ 休闲 
193Electronic Design(电子设计) http://www.e-insite.net/ednmag/ 电子 
194T  L Golf(T  L高尔夫) http://www.tlgolf.com/　休闲 
195Wine Spectator(酒的旁观者) http://www.winespectator.com/ 休闲 
196National Geographic Traveler(国家地理旅行者) 
http://www.nationalgeographic.com/traveler/ 旅游 
197AutoWeek(汽车周刊) http://www.autoweek.com/ 机车 
198Wood(木工)　 http://www.woodmagazine.com/ 工艺 
199Chemical  Engineering News(化工新闻) http://pubs.acs.org/cen/ 行业 
200Electronic Gaming Monthly(电子游戏月刊) 
http://www.gamers.com/egm/index.j sp 游戏 
201Disney Adventures(迪斯尼冒险) http://disney.go.com/disneyadventures/ 孩子 

202National Examiner(国家主考者) http://www.nationalexaminer.com/ 教育 
203Soap Opera Weekly(肥皂剧周刊) http://www.soapoperaweekly.com/ 娱乐 
204Golf World(高尔夫世界) http://www.worldgolf.com/ 体育 
205Runner’s World(跑步者世界) http://www.runnersworld.com/ 体育 
206Country Weekly(乡村周刊) http://www.countryweekly.com/ 音乐 
207American Way(美国道路) http://www.americanwaymag.com/ 旅游 
208Upside(上面) http://www.upside.com/ IT 
209Design News (设计新闻) http://www.manufacturing.net/ 行业 
210Details(详细资料) http://www.condenet.com/mags/details/ 时尚 
211American Profile(美国外形) http://www.americanprofile.com/ 健康 
212ENR http://enr.construction.com/Default.asp 建筑 
213Machine Design(机械设计) http://www.machinedesign.com/ 行业 
214PC Gamer(PC游戏玩家) http://www.pcgamer.com/ 游戏 
215Biography(传记)http://www.biography.com/ 文学 
216Atlantic Monthly(大西洋月刊) http://www.theatlantic.com/ 文艺 
217Successful Farming(成功农业) http://www.agriculture.com/sfonline/ 行业 
218Texas Monthly(德克莎斯月刊) http://www.texasmonthly.com/ 地区 
219Skiing(滑雪运动) http://www.skiingmag.com/skiing/ 体育 
220Southern Accents(南方口音) http://www.southernaccents.com/accents/ 家庭 
221American Rifleman(美国步枪射手) 
http://www.americanrifleman.org/site/index.asp 枪械 
222Bassmaster http://www.bassmaster.com/ 休闲 
223SN-Supermarket News(超级市场新闻) http://www.supermarketnews.com/ 行业 
224ABA Journal(美国银行家协会期刊) 
http://www.abanet.org/journal/redesign/home.html 行业 
225Nature(自然) http://www.nature.com/ 科学 
226Architectural Record(建筑学档案) http://www.archrecord.com/ 行业 
227Adweek(广告周刊) http://www.adweek.com/adweek/index.jsp 行业 
228Petersen’s 4-Wheel  Off Road http://www.4wheeloffroad.com/ 机车 
229Business 2.0(商业2.0) http://www.business2.com/ 商业 
230Flying(飞行) http://www.flyingmag.com/ 休闲 
231Billboard(公告牌) http://www.billboard.com/billboard/index.jsp 音乐 
232Coastal Living(海岸生活) http://www.coastalliving.com/coastal/ 生活 
233Country Woman(乡村女人) http://www.countrywomanmagazine.com/ 家庭 
234Boys’sLife(男孩生活) http://www.boyslife.org/ 孩子 
235Transworld Skateboarding(环球滑板)http://www.skateboarding.com/skate/ 体育 

236NFL Insider（美国足球联盟知情者） http://ww2.nfl.com/insider/ 体育 
237People en Espanol（人物西班牙语版） 
http://www.peopleenespanol.com/pespanol/index.html/ 娱乐 
238Journal of Accountancy（会计学期刊） 
http://www.aicpa.org/pubs/jofa/joaho me.htm 
239Windows 2000 Magazine（视窗2000杂志） http://www.win2000mag.net/ IT 
240Veranda（阳台） http://www.veranda.com/　家居 
241Video Business（视频商业） http://www.videobusiness.com/ 商业 
242Backpacker（背包） http://www.backpacker.com/ 休闲 
243Cigar Aficionado（雪茄迷） http://www.cigaraficionado.com/ 休闲 
244Telephony（技术） http://www.telephonyonline.com/ IT 
245Flex（弯曲） http://www.flexonline.com/ 健康 
246Variety (weekly)（品种周刊） http://www.variety.com/ 商业 
247Cruising World （巡航世界） http://www.cruisingworld.com/ 休闲 
248American Hunter（美国猎人） http://www.american-hunter.com/ 休闲 
249Crain’s Chicago Business(克瑞恩芝加哥商业) 
http://www.chicagobusiness.com/ 商业 
250Broadcastin Cable(宽带与有线电视) http://www.broadcastingcable.com/ 行业 

251Petersen’s Photographic　http://www.photographic.com/ 摄影 
252Golf for Women(女性高尔夫)　http://www.golfdigest.com/gfw/ 体育 
253USAirways Attache Magazine 
254Progressive Farmer(改进农场主) http://www.progressivefarmer.com/farmer/ 农业

255Easyriders http://www.easyriders.com/Home/Home.asp 机车 
256Crain’s New York Business(克瑞恩纽约商业) http://www.crainsny.com/ 商业 

257Yachting(游艇) http://www.yachtingnet.com/yachting/ 休闲 
258Chicago(芝加哥) http://www.chicagomag.com/ 城市 
259Computer Gaming World(计算机游戏世界) http://www.gamers.com/cgw/index.jsp 游
戏 
260Video Store(视频商店) http://www.videostoremag.com/ 商业 
261Country(乡村)　 http://www.country-magazine.com/ 生活 
262Fine Homebuilding(好家建造者) 
http://www.taunton.com/finehomebuilding/index.asp 家居 
263Yankee(美国佬) http://www.yankeemagazine.com/travel/index.php 旅游 
264Publisher’s Weekly(出版者周刊) http://www.publishersweekly.com/ 行业 
265Restaurants  Institutions(餐馆与协会) http://www.rimag.com/ 行业 
266American Medical News(美国医学新闻) 
http://www.ama-assn.org/public/journa ls/amnews/ 行业 
267North American Hunter(北美猎人) http://visitors.huntingclub.com/magazine.as
p 
268Federal Computer Week(联邦计算机周刊)　http://www.fcw.com/ IT 
269Guns  Ammo(枪与军火) http://www.gunsandammomag.com/dynamic.asp 枪械 
270Transworld Snowboarding(环球滑雪板) 
http://www.snowboarding-online.com/ 体育 
271New Equipment Digest(新设备文摘)　http://www.newequipment.com/ 行业 
272Weekly World News(世界新闻周刊)　 http://www.weeklyworldnews.com/ 新闻 
273Chemical Week(化学周刊)　http://www.chemweek.com/ 行业 
274Four Wheeler(四轮车)　http://www.fourwheeler.com/ 机车 
275Gear(齿轮)　 http://www.gearmagazine.com/ 家居 
276Pensions  Investments(养老金和投资)　http://www.pionline.com/ 理财 
277Macworld(Mac世界)　 http://www.macworld.com/ IT 
278Builder(建筑者)　 http://builder.com.com/ IT 
279RB Restaurant Business(餐馆业)　 
http://www.foodservicetoday.com/rb/index.shtml 行业 
280CFO(首席运营官)　 http://www.cfo.com/ IT 
281American Family Physician(美国家庭医生)　http://www.aafp.org/afp.xml 健康 

282Los Angeles Times Magazine(洛杉矶时报杂志)　http://www.latimes.com/ 新闻 

283Saveur　 http://www.saveur.com/ 烹饪 
284Multichannel News(多频道新闻)　http://www.multichannel.com/ 行业 
285Purchasing(购买)　 http://www.manufacturing.net/ 消费 
286Laser Focus World(激光焦点世界) http://lfw.pennnet.com/home.cfm 行业 
287HANDY(手工) http://visitors.handymanclub.com/handy_mag.asp 家居 
288Medical Economics(医药经济) http://www.medec.com/ 行业 
289Reminisce(回忆) http://www.reminisce.com/　休闲 
290Pillsbury Classic Cookbooks http://www.pillsbury.com/ 烹饪 
291Skin Diver(滑水) http://www.skin-diver.com/ 休闲 
292Nursing 2002 http://www.nursinghomesmagazine.com/ 护理 
293Hemmings Motor News http://cars.hemmings.com/ 机车 
294American Legion Magazine(美国军团杂志) http://www.legion.org/ 公益 
295Farm Journal(农业期刊) http://www.farmjournal.com/ 农业 
296Southwest Airlines Spirit(西南航线精灵) http://www.spiritmag.com/ 航行 
297Dr. Dobb’s Journal http://www.ddj.com/ IT 
298Chicago Tribune Magazine(芝加哥论坛杂志) 
http://www.chicagotribune.com/features/magazine/ 新闻 
299Islands(岛屿) http://www.islands.com/ 休闲 
300Institutional Investor(金融机构投资者) http://www.epinions.com/

原作者：打湿的双翼 
来自：blogbus",
	"name": "300个国外优秀网站",
	"url": "https://www.douban.com/group/topic/4002607/",
  "commentCount": "177",
  "dateCreated": "2008-08-21T20:28:41",
  "interactionStatistic": {
    "@type": "InteractionCounter",
    "interactionType": "http://schema.org/LikeAction",
    "userInteractionCount": 1922
  }
}
</script>


    <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/3013a811308c889b.css">
    <script></script>

    <link rel="stylesheet" href="https://img3.doubanio.com/f/group/2f4c6f83940e2bbb76f5a23a7d987b9093919799/css/group/init.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    
    <script type="text/javascript">var _body_start = new Date();</script>
    
   



    <link href="//img3.doubanio.com/dae/accounts/resources/f5f3d66/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://accounts.douban.com/passport/login?source=group" class="nav-login" rel="nofollow">登录/注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="on">
      <a href="https://www.douban.com/group"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/f5f3d66/shire/bundle.js" defer="defer"></script>




      
    









<div id="db-nav-group" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary clearfix">
    <div class="nav-logo">
      <a href="https://www.douban.com/group/">豆瓣小组</a>
    </div>

    <div class="nav-items">
    <ul>
      <li><a href="https://www.douban.com/group/explore">精选</a></li>
      <li><a href="https://www.douban.com/group/explore/culture">文化</a></li>
      <li><a href="https://www.douban.com/group/explore/travel">行摄</a></li>
      <li><a href="https://www.douban.com/group/explore/ent">娱乐</a></li>
      <li><a href="https://www.douban.com/group/explore/fashion">时尚</a></li>
      <li><a href="https://www.douban.com/group/explore/life">生活</a></li>
      <li><a href="https://www.douban.com/group/explore/tech">科技</a></li>
   </ul>
   </div>

    <div class="nav-search">
      <form id='form' action="https://www.douban.com/group/search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          
          <input type="hidden" name="cat" value="1019" />
          <label for="inp-query">小组、话题</label>
          <div class="inp"><input id="inp-query" name="q" size="22" maxlength="60" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
        </fieldset>
      </form>
    </div>
  </div>
  </div>

</div>

<script>
Do(function(){
  var nav = $('#db-nav-group');
  var inp=$("#inp-query"),label=inp.closest(".nav-search").find("label");inp[0]&&"placeholder"in inp[0]?(label.hide(),inp.attr("placeholder",label.text())):(""!==inp.val()&&label.hide(),inp.parent().click(function(){inp.focus(),label.hide()}).end().focusin(function(){label.hide()}).focusout(function(){""===$.trim(this.value)?label.show():label.hide()}).keydown(function(){label.hide()})),inp.parents("form").submit(function(){if(!$.trim(inp.val()).length)return!1}),nav.find(".lnk-more, .lnk-account").click(function(n){n.preventDefault();var i,e=$(this),t=e.hasClass("lnk-more")?$("#db-productions"):$("#db-usr-setting");t.data("init")||(i=e.offset(),t.css({"margin-left":i.left-$(window).width()/2-t.width()+e.width()+parseInt(e.css("padding-right"),10)+"px",left:"50%",top:i.top+e.height()+"px"}),t.data("init",1),t.hide(),$("body").click(function(n){var i=$(n.target);i.hasClass("lnk-more")||i.hasClass("lnk-account")||i.closest("#db-usr-setting").length||i.closest("#db-productions").length||t.hide()})),"none"===t.css("display")?($(".dropdown").hide(),t.show()):$(".dropdown").hide()});
});
</script>




    <div id="wrapper">
        

        
<div id="content">
    
    <h1>
    300个国外优秀网站
</h1>

    <div class="grid-16-8 clearfix">
        
        
        <div class="article">
               

    
    

    

    

    <input type="hidden" id="start" value="0" />
    <div class="topic-content clearfix" id="topic-content">
        <div class="user-face">
            <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
        </div>
        <div class="topic-doc">
            <h3>
                <span class="from">来自: <a href="https://www.douban.com/people/dido1987/">DL</a></span>
                <span class="color-green" style="display:inline-block">2008-08-21 20:28:41</span>
            </h3>


            
            <div id="link-report" class="">

                <div class="topic-content">
                          
                          <p>偶尔的发现，感谢原作者！
<br/>
<br/>
<br/>1 People(人物） 
<br/><a href="http://people.aol.com/people/index.html" target="_blank" rel="nofollow">http://people.aol.co<wbr/>m/people/index.html</a> 
<br/>娱乐 全球五十位最XX的人 
<br/>2 TV Guide（电视指南） 
<br/><a href="http://www.tvguide.com" target="_blank" rel="nofollow">http://www.tvguide.c<wbr/>om</a> 
<br/>娱乐默多克旗下 
<br/>3 Time（时代）<a href="http://www.time.com/" target="_blank" rel="nofollow">http://www.time.com/<wbr/></a> 
<br/>新闻年度风云人物 
<br/>4 Sports Illustrated（体育画报）<a href="http://sportsillustrated.cnn.com/" target="_blank" rel="nofollow">http://sportsillustr<wbr/>ated.cnn.com/</a> 
<br/>体育 本世纪 最佳运动员 
<br/>5 Better Homes &amp; Gardens（美好家园）<a href="http://www.bhg.com/" target="_blank" rel="nofollow">http://www.bhg.com/</a> 家居 
<br/>6 Reader’s Digest(读者文摘）<a href="http://www.rd.com/splash.jhtml" target="_blank" rel="nofollow">http://www.rd.com/sp<wbr/>lash.jhtml</a> 综合 美国发行量最 
<br/>
<br/>大的商业杂志 
<br/>7 Parade（旅行）<a href="http://www.parade.com/auth/entry.lasso" target="_blank" rel="nofollow">http://www.parade.co<wbr/>m/auth/entry.lasso</a> 旅游 
<br/>8 Newsweek（新闻周刊）<a href="http://www.msnbc.com/news/NW-front_Front.asp" target="_blank" rel="nofollow">http://www.msnbc.com<wbr/>/news/NW-front_Front<wbr/>.asp</a> 新闻 微软收
<br/>购 
<br/>9 Business Week（商业周刊）<a href="http://www.businessweek.com/" target="_blank" rel="nofollow">http://www.businessw<wbr/>eek.com/</a> 商业 25位XX人 全球最有
<br/>价值品牌　 
<br/>10Good Housekeeping（好主妇）<a href="http://www.goodhousekeeping.com/" target="_blank" rel="nofollow">http://www.goodhouse<wbr/>keeping.com/</a> 家庭 
<br/>11Fortune（财富）<a href="http://www.fortune.com/" target="_blank" rel="nofollow">http://www.fortune.c<wbr/>om/</a> 商业全球五百强 
<br/>12Cosmopolitan（全球主义者）<a href="http://www.cosmopolitan.com/" target="_blank" rel="nofollow">http://www.cosmopoli<wbr/>tan.com/</a> 娱乐 
<br/>13Woman’s Day（妇女日）<a href="http://www.womansday.com/xp6/WomansDay/home.xml" target="_blank" rel="nofollow">http://www.womansday<wbr/>.com/xp6/WomansDay/h<wbr/>ome.xml</a> 妇女 
<br/>
<br/>14Forbes（福布斯）<a href="http://www.forbes.com/" target="_blank" rel="nofollow">http://www.forbes.co<wbr/>m/</a> 商业全球最富的多少人 
<br/>15Family Circle（家庭圈）<a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.familycircle.com%2Fhome%2Fhomepage.jsp" target="_blank" rel="nofollow">http://www.familycir<wbr/>cle.com/home/homepag<wbr/>e.jsp</a> 家庭 
<br/>
<br/>16USA Weekend（美国周末）<a href="http://www.usaweekend.com/" target="_blank" rel="nofollow">http://www.usaweeken<wbr/>d.com/</a> 休闲甘尼特报业公司旗下 
<br/>17Instyle（时髦）<a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.instyle.com%2Finstyle" target="_blank" rel="nofollow">http://www.instyle.c<wbr/>om/instyle</a> 时尚 年度性感偶像 
<br/>18Entertainment Weekly(娱乐周刊）<a href="http://www.ew.com/ew/" target="_blank" rel="nofollow">http://www.ew.com/ew<wbr/>/</a> 娱乐 
<br/>19Martha Stewart Living（玛萨斯图尔特生活） <a href="http://www.marthastewart.com/" target="_blank" rel="nofollow">http://www.marthaste<wbr/>wart.com/</a> 生活
<br/>
<br/>指导美国人生活的女王 
<br/>20U.S. News &amp; World Report（美国新闻与世界报道）<a href="http://www.usnews.com/" target="_blank" rel="nofollow">http://www.usnews.co<wbr/>m/</a> 新闻全美
<br/>大学排行榜 
<br/>21Ladies’ Home Journal(妇女家庭杂志) <a href="http://www.lhj.com/" target="_blank" rel="nofollow">http://www.lhj.com/</a> 家庭 
<br/>22National Geographic(国家地理杂志) <a href="http://www.nationalgeographic.com/" target="_blank" rel="nofollow">http://www.nationalg<wbr/>eographic.com/</a> 地理 
<br/>
<br/>23Southern Living（南方生活）<a href="http://www.southernliving.com/" target="_blank" rel="nofollow">http://www.southernl<wbr/>iving.com/</a> 生活 
<br/>24Vogue（时尚）<a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.style.com%2Fvogue%2Findex.html" target="_blank" rel="nofollow">http://www.style.com<wbr/>/vogue/index.html</a> 时尚 
<br/>25PC Magazine（个人电脑）<a href="http://www.pcmag.com/" target="_blank" rel="nofollow">http://www.pcmag.com<wbr/>/</a> IT 
<br/>26Money（金钱）<a href="http://money.cnn.com/" target="_blank" rel="nofollow">http://money.cnn.com<wbr/>/</a> 理财 
<br/>27Maxim（马克西姆）<a href="http://www.maximonline.com/index.html" target="_blank" rel="nofollow">http://www.maximonli<wbr/>ne.com/index.html</a> 娱乐 
<br/>28O, The Oprah Magazine <a href="http://www.oprah.com/omagazine" target="_blank" rel="nofollow">http://www.oprah.com<wbr/>/omagazine</a> 妇女 
<br/>29Glamour（魅力）<a href="http://www.glamour.com/" target="_blank" rel="nofollow">http://www.glamour.c<wbr/>om/</a> 时尚 
<br/>30National Enquirer, The（国家寻问者）<a href="http://www.nationalenquirer.com/" target="_blank" rel="nofollow">http://www.nationale<wbr/>nquirer.com/</a> 新闻 
<br/>
<br/>31New York Times Magazine（纽约时报杂志）<a href="http://www.nytimes.com/" target="_blank" rel="nofollow">http://www.nytimes.c<wbr/>om/</a> 新闻 
<br/>32Golf Digest（高尔夫文摘）<a href="http://www.golfdigest.com/" target="_blank" rel="nofollow">http://www.golfdiges<wbr/>t.com/</a> 体育 
<br/>33Rolling Stone（滚石）<a href="http://www.rollingstone.com/" target="_blank" rel="nofollow">http://www.rollingst<wbr/>one.com/</a> 音乐 
<br/>34Playboy（花花公子）<a href="http://www.playboy.com/" target="_blank" rel="nofollow">http://www.playboy.c<wbr/>om/</a> 男性 
<br/>35Vanity Fair（名利场）<a href="http://www.vanityfair.com/" target="_blank" rel="nofollow">http://www.vanityfai<wbr/>r.com/</a> 娱乐名人采访 
<br/>36Seventeen（十七岁）<a href="http://www.seventeen.com/" target="_blank" rel="nofollow">http://www.seventeen<wbr/>.com/</a> 青年 
<br/>37Parents（父母）<a href="http://www.parents.com/" target="_blank" rel="nofollow">http://www.parents.c<wbr/>om/</a> 教育 
<br/>38Star Magazine（明星杂志）<a href="http://www.starmagazine.com/" target="_blank" rel="nofollow">http://www.starmagaz<wbr/>ine.com/</a> 娱乐 
<br/>39ESPN The Magazine（ESPN杂志）<a href="http://espn.go.com/magazine/" target="_blank" rel="nofollow">http://espn.go.com/m<wbr/>agazine/</a> 体育 
<br/>40Prevention（预防）<a href="http://www.prevention.com/" target="_blank" rel="nofollow">http://www.preventio<wbr/>n.com/</a> 健康 
<br/>41Redbook（红书）<a href="http://magazines.ivillage.com/redbook/" target="_blank" rel="nofollow">http://magazines.ivi<wbr/>llage.com/redbook/</a> 妇女 
<br/>42Rosie <a href="http://www.rosieo.com/" target="_blank" rel="nofollow">http://www.rosieo.co<wbr/>m/</a> 
<br/>43Golf Magazine（高尔夫杂志）<a href="http://sportsillustrated.cnn.com/golfonline/" target="_blank" rel="nofollow">http://sportsillustr<wbr/>ated.cnn.com/golfonl<wbr/>ine/</a> 体育
<br/>
<br/>44Travel &amp; Leisure（旅游和休闲）<a href="http://www.travelandleisure.com/" target="_blank" rel="nofollow">http://www.traveland<wbr/>leisure.com/</a> 休闲 
<br/>45Elle <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.elle.com%2F" target="_blank" rel="nofollow">http://www.elle.com/<wbr/></a> 时尚 
<br/>46New Yorker, The（纽约客）<a href="http://www.newyorker.com/" target="_blank" rel="nofollow">http://www.newyorker<wbr/>.com/</a> 文艺 
<br/>47W <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.style.com%2Fw%2F" target="_blank" rel="nofollow">http://www.style.com<wbr/>/w/</a> 时尚 
<br/>48Woman’s World(妇女世界）<a href="http://www.robertcraig.com/womansworld.html" target="_blank" rel="nofollow">http://www.robertcra<wbr/>ig.com/womansworld.h<wbr/>tml</a> 妇女 
<br/>
<br/>49Parenting（养育）<a href="http://www.parenting.com/parenting/" target="_blank" rel="nofollow">http://www.parenting<wbr/>.com/parenting/</a> 家庭 
<br/>50Car &amp; Driver（人车志）<a href="http://www.caranddriver.com/xp/Caranddriver/home.xml" target="_blank" rel="nofollow">http://www.caranddri<wbr/>ver.com/xp/Caranddri<wbr/>ver/home.xml</a> 
<br/>
<br/>机车 
<br/>51Endless Vacation（无尽假日）<a href="http://www.endlessvacation.com/" target="_blank" rel="nofollow">http://www.endlessva<wbr/>cation.com/</a> 休闲 
<br/>52Bride’s Magazine（新娘杂志）<a href="http://www.brides.com/" target="_blank" rel="nofollow">http://www.brides.co<wbr/>m/</a> 婚礼 
<br/>53InformationWeek（信息周刊）<a href="http://www.informationweek.com/" target="_blank" rel="nofollow">http://www.informati<wbr/>onweek.com/</a> IT 
<br/>54Country Living（乡村生活）<a href="http://magazines.ivillage.com/countryliving/" target="_blank" rel="nofollow">http://magazines.ivi<wbr/>llage.com/countryliv<wbr/>ing/</a> 生活 
<br/>
<br/>55Us Weekly（美国周刊）<a href="http://usweekly.abc.com/" target="_blank" rel="nofollow">http://usweekly.abc.<wbr/>com/</a> 新闻 
<br/>56Marie Claire（玛丽克莱尔）<a href="http://www.marieclaire.com/" target="_blank" rel="nofollow">http://www.marieclai<wbr/>re.com/</a> 时尚 
<br/>57Sunset（日落）<a href="http://www.sunset.com/" target="_blank" rel="nofollow">http://www.sunset.co<wbr/>m/</a> 科学 
<br/>58Soap Opera Digest（肥皂剧文摘）<a href="http://www.soapoperadigest.com/" target="_blank" rel="nofollow">http://www.soapopera<wbr/>digest.com/</a> 娱乐 
<br/>59AARP Modern Maturity（现代文明） <a href="http://www.modernmaturity.org/" target="_blank" rel="nofollow">http://www.modernmat<wbr/>urity.org/</a> 公益 
<br/>美国发 行量最大的杂志 
<br/>60GQ <a href="http://www.gq.com/" target="_blank" rel="nofollow">http://www.gq.com/</a> 时尚 
<br/>61Architectural Digest（建筑学文摘） 
<br/><a href="http://www.condenet.com/mags/archdigest/" target="_blank" rel="nofollow">http://www.condenet.<wbr/>com/mags/archdigest/<wbr/></a> 建筑 
<br/>62Harper’s Bazaar(哈泼氏）<a href="http://www.harpersbazaar.com/" target="_blank" rel="nofollow">http://www.harpersba<wbr/>zaar.com/</a> 时尚 
<br/>63Travel Agent（旅游代理）<a href="http://www.travelagents.com/" target="_blank" rel="nofollow">http://www.travelage<wbr/>nts.com/</a> 旅游 
<br/>64Smithsonian（史密森尼)<a href="http://www.si.edu/" target="_blank" rel="nofollow">http://www.si.edu/</a> 博物 
<br/>65PC World（PC世界）<a href="http://www.pcworld.com/" target="_blank" rel="nofollow">http://www.pcworld.c<wbr/>om/</a> IT 
<br/>66Modern Bride（现代新娘）<a href="http://www.modernbride.com/" target="_blank" rel="nofollow">http://www.modernbri<wbr/>de.com/</a> 婚礼 
<br/>67Men’s Health（男性健康）<a href="http://www.menshealth.com/" target="_blank" rel="nofollow">http://www.menshealt<wbr/>h.com/</a> 健康 
<br/>68Bon Appetit（好　）<a href="http://www.epicurious.com/b_ba/b00_home/ba.html" target="_blank" rel="nofollow">http://www.epicuriou<wbr/>s.com/b_ba/b00_home/<wbr/>ba.html</a> 烹饪 
<br/>69Motor Trend（机车潮流）<a href="http://www.motortrend.com/" target="_blank" rel="nofollow">http://www.motortren<wbr/>d.com/</a> 机车 
<br/>70Economist, The（经济学人）<a href="http://www.economist.com/" target="_blank" rel="nofollow">http://www.economist<wbr/>.com/</a> 
<br/>政经世界上最牛的政经杂志 
<br/>71Self（自我）<a href="http://www.self.com/" target="_blank" rel="nofollow">http://www.self.com/<wbr/></a> 妇女 
<br/>72Shape（体形）<a href="http://www.shapeonline.com/" target="_blank" rel="nofollow">http://www.shapeonli<wbr/>ne.com/</a> 健康 
<br/>73Teen People <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.teenpeople.com%2Fteenpeople%2F" target="_blank" rel="nofollow">http://www.teenpeopl<wbr/>e.com/teenpeople/</a> 青年 
<br/>74YM <a href="http://www.ym.com/" target="_blank" rel="nofollow">http://www.ym.com/</a> 时尚 
<br/>75Consumer Reports（消费者报告） 
<br/><a href="http://www.consumerreports.org/main/home.jsp" target="_blank" rel="nofollow">http://www.consumerr<wbr/>eports.org/main/home<wbr/>.jsp</a> 消费 
<br/>76Cooking Light（烹饪之光）<a href="http://www.cookinglight.com/" target="_blank" rel="nofollow">http://www.cookingli<wbr/>ght.com/</a> 烹饪 
<br/>77Travel Weekly（旅行周刊） 
<br/><a href="http://www.travelweekly.co.uk/tw_home/home.asp" target="_blank" rel="nofollow">http://www.travelwee<wbr/>kly.co.uk/tw_home/ho<wbr/>me.asp</a> 旅游 
<br/>78House Beautiful（美丽住宅）<a href="http://magazines.ivillage.com/housebeautiful/" target="_blank" rel="nofollow">http://magazines.ivi<wbr/>llage.com/housebeaut<wbr/>iful/</a> 家居
<br/>
<br/>79Ebony（乌木）<a href="http://www.ebony.com/" target="_blank" rel="nofollow">http://www.ebony.com<wbr/>/</a> 成人 
<br/>80Popular Photography（大众摄影）<a href="http://www.popularphotography.com/index.asp" target="_blank" rel="nofollow">http://www.popularph<wbr/>otography.com/index.<wbr/>asp</a> 摄
<br/>影 
<br/>81Country Home（乡村家庭）<a href="http://www.countryhome.com/ch/index.html" target="_blank" rel="nofollow">http://www.countryho<wbr/>me.com/ch/index.html<wbr/></a> 家庭 
<br/>82Barron’s <a href="http://www.barrons.com/" target="_blank" rel="nofollow">http://www.barrons.c<wbr/>om/</a> 商业 
<br/>83eWeek <a href="http://www.eweek.com/" target="_blank" rel="nofollow">http://www.eweek.com<wbr/>/</a> 消费 
<br/>84Conde Nast Traveler <a href="http://www.concierge.com/cntraveler/" target="_blank" rel="nofollow">http://www.concierge<wbr/>.com/cntraveler/</a> 旅游 
<br/>85Town &amp; Country(城镇和乡村) <a href="http://magazines.ivillage.com/townandcountry/" target="_blank" rel="nofollow">http://magazines.ivi<wbr/>llage.com/townandcou<wbr/>ntry/</a> 生活
<br/>
<br/>86InfoWorld(信息世界) <a href="http://www.infoworld.com/" target="_blank" rel="nofollow">http://www.infoworld<wbr/>.com/</a> IT 
<br/>87EE Times <a href="http://www.eetimes.com/" target="_blank" rel="nofollow">http://www.eetimes.c<wbr/>om/</a> 电子 
<br/>88Food &amp; Wine(食物和酒) <a href="http://www.foodandwine.com/" target="_blank" rel="nofollow">http://www.foodandwi<wbr/>ne.com/</a> 食品 
<br/>89New York(纽约) <a href="http://www.newyorkmetro.com/" target="_blank" rel="nofollow">http://www.newyorkme<wbr/>tro.com/</a> 城市 
<br/>90Essence(本质) <a href="http://www.essence.com/" target="_blank" rel="nofollow">http://www.essence.c<wbr/>om/</a> 黑人 
<br/>91Road &amp; Track(公路与轨迹) <a href="http://www.roadandtrack.com/" target="_blank" rel="nofollow">http://www.roadandtr<wbr/>ack.com/</a> 机车 
<br/>92Health(健康) <a href="http://www.health.com/" target="_blank" rel="nofollow">http://www.health.co<wbr/>m/</a> 健康 
<br/>93Inc(公司) <a href="http://www.inc.com/home/" target="_blank" rel="nofollow">http://www.inc.com/h<wbr/>ome/</a> 商业 
<br/>94Allure(吸引) <a href="http://www.allure.com/" target="_blank" rel="nofollow">http://www.allure.co<wbr/>m/</a> 时尚 
<br/>95Vibe <a href="http://www.vibe.com/new/home/pointer.html" target="_blank" rel="nofollow">http://www.vibe.com/<wbr/>new/home/pointer.htm<wbr/>l</a> 娱乐 
<br/>96Gourmet(美食家) <a href="http://www.gourmet.com/" target="_blank" rel="nofollow">http://www.gourmet.c<wbr/>om/</a> 烹饪 
<br/>97Taste of Home(家的滋味) <a href="http://www.tasteofhome.com/" target="_blank" rel="nofollow">http://www.tasteofho<wbr/>me.com/</a> 烹饪 
<br/>98Muscle &amp; Fitness(肌肉和健身) <a href="http://www.muscleandfitness.com/" target="_blank" rel="nofollow">http://www.muscleand<wbr/>fitness.com/</a> 健康 
<br/>99Popular Mechanics(大众机械) <a href="http://popularmechanics.com/" target="_blank" rel="nofollow">http://popularmechan<wbr/>ics.com/</a> 机械 
<br/>100Home(家) <a href="http://www.homemag.com/" target="_blank" rel="nofollow">http://www.homemag.c<wbr/>om/</a> 家居 
<br/>
<br/>101fitness（健身) <a href="http://www.fitnessmagazine.com/home/index.jsp" target="_blank" rel="nofollow">http://www.fitnessma<wbr/>gazine.com/home/inde<wbr/>x.jsp</a> 健康 
<br/>102Field &amp; Stream（田园和小溪) <a href="http://www.fieldandstream.com/" target="_blank" rel="nofollow">http://www.fieldands<wbr/>tream.com/</a> 休闲 
<br/>103American Baby（美国宝贝) 
<br/><a href="http://www.americanbaby.com/ab/CDA/homepage/" target="_blank" rel="nofollow">http://www.americanb<wbr/>aby.com/ab/CDA/homep<wbr/>age/</a> 家庭 
<br/>104FamilyFun（家庭乐趣） <a href="http://familyfun.go.com/" target="_blank" rel="nofollow">http://familyfun.go.<wbr/>com/</a> 家庭 
<br/>105Sporting News, The（体育新闻) <a href="http://www.sportingnews.com/" target="_blank" rel="nofollow">http://www.sportingn<wbr/>ews.com/</a> 体育 
<br/>106Esquire（先生） <a href="http://www.esquire.com/" target="_blank" rel="nofollow">http://www.esquire.c<wbr/>om/</a> 男性 
<br/>107Penthouse（小棚屋） <a href="http://www.penthouse.com/" target="_blank" rel="nofollow">http://www.penthouse<wbr/>.com/</a> 成人 
<br/>108Kiplinger’s Personal Finance Magazine(吉朴林的个人金融杂志) 
<br/><a href="http://www.kiplinger.com/" target="_blank" rel="nofollow">http://www.kiplinger<wbr/>.com/</a> 理财 
<br/>109Globe(环球) <a href="http://www.boston.com/globe/" target="_blank" rel="nofollow">http://www.boston.co<wbr/>m/globe/</a> 环境 
<br/>110SmartMoney(精明理财) <a href="http://www.smartmoney.com/" target="_blank" rel="nofollow">http://www.smartmone<wbr/>y.com/</a> 理财 
<br/>111Stuff(素材) <a href="http://www.stuffmagazine.com/" target="_blank" rel="nofollow">http://www.stuffmaga<wbr/>zine.com/</a> 男性 
<br/>112CRN　<a href="http://www.crn.com/" target="_blank" rel="nofollow">http://www.crn.com/</a> IT 
<br/>113Men’s Journal(男人) <a href="http://www.mensjournal.com/" target="_blank" rel="nofollow">http://www.mensjourn<wbr/>al.com/</a> 男性 
<br/>114House &amp; Garden(家园) <a href="http://www.condenet.com/mags/hg/" target="_blank" rel="nofollow">http://www.condenet.<wbr/>com/mags/hg/</a> 家居 
<br/>115Fast Company(快速公司) <a href="http://www.fastcompany.com/homepage/" target="_blank" rel="nofollow">http://www.fastcompa<wbr/>ny.com/homepage/</a> 商业 
<br/>116Computer Shopper(计算机购物者) <a href="http://shopper.cnet.com/" target="_blank" rel="nofollow">http://shopper.cnet.<wbr/>com/</a> 消费 
<br/>117Jet(黑玉) <a href="http://www.jetmag.com/" target="_blank" rel="nofollow">http://www.jetmag.co<wbr/>m/</a> 黑人 
<br/>118First For Women　 <a href="http://www.ffwmarket.com/" target="_blank" rel="nofollow">http://www.ffwmarket<wbr/>.com/</a> 妇女 
<br/>119Traditional Home（传统家庭） <a href="http://www.traditionalhome.com/" target="_blank" rel="nofollow">http://www.tradition<wbr/>alhome.com/</a> 家庭 
<br/>120Automobile Magazine(汽车杂志） <a href="http://www.automobilemag.com/" target="_blank" rel="nofollow">http://www.automobil<wbr/>emag.com/</a> 机车 
<br/>121Red Herring（红鲱鱼） <a href="http://www.redherring.com/" target="_blank" rel="nofollow">http://www.redherrin<wbr/>g.com/</a> 商业 
<br/>122Highlights for Children（儿童文粹） <a href="http://www.highlights.com/" target="_blank" rel="nofollow">http://www.highlight<wbr/>s.com/</a> 儿童 
<br/>123Wired（连线） <a href="http://www.wired.com/" target="_blank" rel="nofollow">http://www.wired.com<wbr/>/</a> IT 
<br/>124Outside（户外） <a href="http://outsidemag.com/index.html" target="_blank" rel="nofollow">http://outsidemag.co<wbr/>m/index.html</a> 休闲 
<br/>125This Old House（这个老屋子） <a href="http://www.thisoldhouse.com/toh/" target="_blank" rel="nofollow">http://www.thisoldho<wbr/>use.com/toh/</a> 家居 
<br/>126NetworkWorld（网络世界） <a href="http://www.networkworld.com/" target="_blank" rel="nofollow">http://www.networkwo<wbr/>rld.com/</a>　IT 
<br/>127Entrepreneur（企业家） <a href="http://www.entrepreneur.com/" target="_blank" rel="nofollow">http://www.entrepren<wbr/>eur.com/</a> 商业 
<br/>128Popular Science（大众科学） <a href="http://www.popsci.com/popsci/" target="_blank" rel="nofollow">http://www.popsci.co<wbr/>m/popsci/</a> 科普 
<br/>129Elle Decor　 <a href="http://www.elledecor.co.th/" target="_blank" rel="nofollow">http://www.elledecor<wbr/>.co.th/</a> 设计 
<br/>130Quick Cooking （速煮） <a href="http://www.quickcooking.com/" target="_blank" rel="nofollow">http://www.quickcook<wbr/>ing.com/</a> 烹饪 
<br/>131Family Handyman（家庭佣人） <a href="http://www.familyhandyman.com/" target="_blank" rel="nofollow">http://www.familyhan<wbr/>dyman.com/</a> 家居 
<br/>132Science（科学） <a href="http://www.sciencemag.org/" target="_blank" rel="nofollow">http://www.sciencema<wbr/>g.org/</a> 科学 
<br/>133Bridal Guide（新娘指南） <a href="http://www.bridalguide.com/" target="_blank" rel="nofollow">http://www.bridalgui<wbr/>de.com/</a> 婚礼 
<br/>134Child（孩子） <a href="http://www.child.com/index.jsp" target="_blank" rel="nofollow">http://www.child.com<wbr/>/index.jsp</a> 家庭 
<br/>135Cable Guide（有线电视指南） <a href="http://www.cableguide.co.uk/" target="_blank" rel="nofollow">http://www.cableguid<wbr/>e.co.uk/</a> 娱乐 
<br/>136Midwest Living（中西部生活） <a href="http://www.midwestliving.com/" target="_blank" rel="nofollow">http://www.midwestli<wbr/>ving.com/</a> 生活 
<br/>137Metropolitan Home（大城市生活） <a href="http://www.mho.co.uk/" target="_blank" rel="nofollow">http://www.mho.co.uk<wbr/>/</a> 生活 
<br/>138Chronicle of Higher Education, The（高等教育编年史） 
<br/><a href="https://www.douban.com/link2/?url=http%3A%2F%2Fchronicle.com" target="_blank" rel="nofollow">http://chronicle.com<wbr/></a> / 教育 
<br/>139Mutual Funds Magazine（互动基金杂志） 
<br/><a href="http://www.mutual-funds.com/mfmag/" target="_blank" rel="nofollow">http://www.mutual-fu<wbr/>nds.com/mfmag/</a> 商业 
<br/>140Travelhost（旅游主人） <a href="http://www.travelhost.com/" target="_blank" rel="nofollow">http://www.travelhos<wbr/>t.com/</a> 旅游 
<br/>141Sound &amp; Vision（声与影） <a href="http://www.soundandvisionmag.com/index.asp" target="_blank" rel="nofollow">http://www.soundandv<wbr/>isionmag.com/index.a<wbr/>sp</a> 电影 
<br/>
<br/>142CIO（首席信息官） <a href="http://www.cio.com/" target="_blank" rel="nofollow">http://www.cio.com/</a> IT 
<br/>143Hot Rod　 <a href="http://www.hotrod.com/" target="_blank" rel="nofollow">http://www.hotrod.co<wbr/>m/</a> 机车 
<br/>144Computerworld（计算机世界） <a href="http://www.computerworld.com/" target="_blank" rel="nofollow">http://www.computerw<wbr/>orld.com/</a> IT 
<br/>145Source, The（来源） <a href="http://www.thesource.com/" target="_blank" rel="nofollow">http://www.thesource<wbr/>.com/</a> 黑人 
<br/>146Departures（启程） <a href="http://www.departures.com/" target="_blank" rel="nofollow">http://www.departure<wbr/>s.com/</a> 商业 
<br/>147Spin（旋转） <a href="http://www.spin.com/" target="_blank" rel="nofollow">http://www.spin.com/<wbr/></a> 音乐 
<br/>148Travel Holiday（旅行假日） <a href="http://www.travelholiday.com/" target="_blank" rel="nofollow">http://www.travelhol<wbr/>iday.com/</a> 旅游 
<br/>149Black Enterprise（黑人企业） <a href="http://www.blackenterprise.com/" target="_blank" rel="nofollow">http://www.blackente<wbr/>rprise.com/</a> 商业 
<br/>150BabyTalk（宝贝说话） 
<br/><a href="http://www.parenting.com/parenting/...s/babytalk.html" target="_blank" rel="nofollow">http://www.parenting<wbr/>.com/parenting/...s/<wbr/>babytalk.html</a> 家庭 
<br/>151New England Journal of Medicine（新英格兰医学期刊） 
<br/><a href="http://content.nejm.org/" target="_blank" rel="nofollow">http://content.nejm.<wbr/>org/</a> 医学 
<br/>152EBN Electronic Buyer’s News(EBN电子买主新闻) 
<br/><a href="http://www.ebnonline.com/" target="_blank" rel="nofollow">http://www.ebnonline<wbr/>.com/</a> 电 子 
<br/>153Jane(简) <a href="http://www.janes.com/" target="_blank" rel="nofollow">http://www.janes.com<wbr/>/</a> 军事 
<br/>154Working Mother(妇女运动者)　<a href="http://www.workingwoman.com/" target="_blank" rel="nofollow">http://www.workingwo<wbr/>man.com/</a> 妇女 
<br/>155Men’s Fitness(男性健身) <a href="http://www.mensfitness.com/mens.html" target="_blank" rel="nofollow">http://www.mensfitne<wbr/>ss.com/mens.html</a> 健康 
<br/>156Victoria(维多利亚) <a href="http://magazines.ivillage.com/victoria/" target="_blank" rel="nofollow">http://magazines.ivi<wbr/>llage.com/victoria/</a> 生活 
<br/>157CosmoGirl(都市女孩) <a href="http://www.cosmogirl.com/" target="_blank" rel="nofollow">http://www.cosmogirl<wbr/>.com/</a> 时尚 
<br/>158Nation’s Restaurant News(国家餐馆新闻) <a href="http://www.nrn.com/" target="_blank" rel="nofollow">http://www.nrn.com/</a> 行业 
<br/>159Harvard Business Review(哈佛商业评论) <a href="http://www.hbr.com/" target="_blank" rel="nofollow">http://www.hbr.com/</a> 商业 
<br/>160FHM(男人帮) <a href="http://www.fhm.com/" target="_blank" rel="nofollow">http://www.fhm.com/</a> 男性 
<br/>161Sports Illustrated For Kids(儿童体育画报) <a href="http://www.sikids.com/" target="_blank" rel="nofollow">http://www.sikids.co<wbr/>m/</a> 儿童 
<br/>162Boating(航船) <a href="http://www.boatingmag.com/" target="_blank" rel="nofollow">http://www.boatingma<wbr/>g.com/</a> 体育 
<br/>163Discover(探索) <a href="http://www.discover.com/" target="_blank" rel="nofollow">http://www.discover.<wbr/>com/</a> 科普 
<br/>164Real Simple(反朴归真) <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.realsimple.com%2Frealsimple%2F" target="_blank" rel="nofollow">http://www.realsimpl<wbr/>e.com/realsimple/</a> 生活 
<br/>165Guideposts（路标） <a href="http://www.guideposts.com/" target="_blank" rel="nofollow">http://www.guidepost<wbr/>s.com/</a> 宗教 
<br/>166Cycle World(环形世界) 
<br/><a href="http://www.cycleworld.com/xp6/CycleWorld/main.xml" target="_blank" rel="nofollow">http://www.cycleworl<wbr/>d.com/xp6/CycleWorld<wbr/>/main.xml</a> 机车 
<br/>167EDN <a href="http://www.e-insite.net/ednmag/" target="_blank" rel="nofollow">http://www.e-insite.<wbr/>net/ednmag/</a> 电子 
<br/>168Tennis Magazine(网球杂志) <a href="http://www.tennis.com/" target="_blank" rel="nofollow">http://www.tennis.co<wbr/>m/</a> 体育 
<br/>169Advertising Age(广告时代) <a href="http://www.adage.com/" target="_blank" rel="nofollow">http://www.adage.com<wbr/>/</a> 行业 
<br/>170Hemispheres(半球) <a href="http://www.hemispheresmagazine.com/home.htm" target="_blank" rel="nofollow">http://www.hemispher<wbr/>esmagazine.com/home.<wbr/>htm</a> 收藏 
<br/>171Fortune Small Business(财富小商业) 
<br/><a href="http://www.fortune.com/smallbusiness/" target="_blank" rel="nofollow">http://www.fortune.c<wbr/>om/smallbusiness/</a> 商业 
<br/>172Meetings &amp; Conventions(会议) 
<br/><a href="http://www.meetings-conventions.com/" target="_blank" rel="nofollow">http://www.meetings-<wbr/>conventions.com/</a> 行业 
<br/>173Worth(价值) <a href="http://www.worth.com/magazine/index.cfm" target="_blank" rel="nofollow">http://www.worth.com<wbr/>/magazine/index.cfm</a> 理财 
<br/>174Outdoor Life(户外生活) <a href="http://www.outdoorlife.com/outdoor/" target="_blank" rel="nofollow">http://www.outdoorli<wbr/>fe.com/outdoor/</a> 休闲 
<br/>175Official U.S. Playstation Magazine(美国官方PS杂志) 
<br/><a href="http://www.gamers.com/opm/index.jsp" target="_blank" rel="nofollow">http://www.gamers.co<wbr/>m/opm/index.jsp</a> 游戏 
<br/>176Automotive News(汽车新闻) <a href="http://www.autonews.com/" target="_blank" rel="nofollow">http://www.autonews.<wbr/>com/</a> 机车 
<br/>177Scientific American(科学美国人) <a href="http://www.sciam.com/" target="_blank" rel="nofollow">http://www.sciam.com<wbr/>/</a> 科普 
<br/>178Nickelodeon　 <a href="http://www.nick.com/" target="_blank" rel="nofollow">http://www.nick.com/<wbr/></a> 娱乐 
<br/>179More(更多) <a href="http://www.more.com/" target="_blank" rel="nofollow">http://www.more.com/<wbr/></a> 时尚 
<br/>180Ski(滑雪) <a href="http://www.skinet.com/skinet/" target="_blank" rel="nofollow">http://www.skinet.co<wbr/>m/skinet/</a> 体育 
<br/>181Lucky(幸运) <a href="http://www.luckymag.com/" target="_blank" rel="nofollow">http://www.luckymag.<wbr/>com/</a> 时尚 
<br/>182Interior Design(室内装饰设计) <a href="http://www.interiordesign.net/" target="_blank" rel="nofollow">http://www.interiord<wbr/>esign.net/</a>　行业 
<br/>183Sky (Delta Air Lines)(天空 三角航线) <a href="http://www.delta-sky.com/" target="_blank" rel="nofollow">http://www.delta-sky<wbr/>.com/</a> 航线 
<br/>184Power &amp; Motoryacht(能源和摩托艇) <a href="http://powerandmotoryacht.about.com/mbody" target="_blank" rel="nofollow">http://powerandmotor<wbr/>yacht.about.com/mbod<wbr/>y</a>.
<br/>htm 休闲 
<br/>185GamePro(专业游戏) <a href="http://www.gamepro.com/" target="_blank" rel="nofollow">http://www.gamepro.c<wbr/>om/</a> 游戏 
<br/>186JAMA(睡衣裤) <a href="http://jama.ama-assn.org/" target="_blank" rel="nofollow">http://jama.ama-assn<wbr/>.org/</a> 健康 
<br/>187Furniture Today(今日家具) <a href="http://www.furnituretoday.com/index.shtml" target="_blank" rel="nofollow">http://www.furniture<wbr/>today.com/index.shtm<wbr/>l</a> 家居 
<br/>
<br/>188My Generation(我们这一代) <a href="http://www.mygeneration.org/" target="_blank" rel="nofollow">http://www.mygenerat<wbr/>ion.org/</a> 音乐 
<br/>189Successful Meetings(成功会议) 
<br/><a href="http://www.successmtgs.com/successmtgs/index.jsp" target="_blank" rel="nofollow">http://www.successmt<wbr/>gs.com/successmtgs/i<wbr/>ndex.jsp</a> 行业 
<br/>190Premiere(首映) <a href="http://www.premiere.com/" target="_blank" rel="nofollow">http://www.premiere.<wbr/>com/</a> 电影 
<br/>191Birds &amp; Blooms(鸟语花香) <a href="http://www.birdsandblooms.com/" target="_blank" rel="nofollow">http://www.birdsandb<wbr/>looms.com/</a> 家居 
<br/>192Aviation Week &amp; Space Technology(航空技术周刊) 
<br/><a href="http://www.aviationnow.com/" target="_blank" rel="nofollow">http://www.aviationn<wbr/>ow.com/</a> 休闲 
<br/>193Electronic Design(电子设计) <a href="http://www.e-insite.net/ednmag/" target="_blank" rel="nofollow">http://www.e-insite.<wbr/>net/ednmag/</a> 电子 
<br/>194T &amp; L Golf(T &amp; L高尔夫) <a href="http://www.tlgolf.com/" target="_blank" rel="nofollow">http://www.tlgolf.co<wbr/>m/</a>　休闲 
<br/>195Wine Spectator(酒的旁观者) <a href="http://www.winespectator.com/" target="_blank" rel="nofollow">http://www.winespect<wbr/>ator.com/</a> 休闲 
<br/>196National Geographic Traveler(国家地理旅行者) 
<br/><a href="http://www.nationalgeographic.com/traveler/" target="_blank" rel="nofollow">http://www.nationalg<wbr/>eographic.com/travel<wbr/>er/</a> 旅游 
<br/>197AutoWeek(汽车周刊) <a href="http://www.autoweek.com/" target="_blank" rel="nofollow">http://www.autoweek.<wbr/>com/</a> 机车 
<br/>198Wood(木工)　 <a href="http://www.woodmagazine.com/" target="_blank" rel="nofollow">http://www.woodmagaz<wbr/>ine.com/</a> 工艺 
<br/>199Chemical &amp; Engineering News(化工新闻) <a href="http://pubs.acs.org/cen/" target="_blank" rel="nofollow">http://pubs.acs.org/<wbr/>cen/</a> 行业 
<br/>200Electronic Gaming Monthly(电子游戏月刊) 
<br/><a href="http://www.gamers.com/egm/index.j" target="_blank" rel="nofollow">http://www.gamers.co<wbr/>m/egm/index.j</a> sp 游戏 
<br/>201Disney Adventures(迪斯尼冒险) <a href="http://disney.go.com/disneyadventures/" target="_blank" rel="nofollow">http://disney.go.com<wbr/>/disneyadventures/</a> 孩子 
<br/>
<br/>202National Examiner(国家主考者) <a href="http://www.nationalexaminer.com/" target="_blank" rel="nofollow">http://www.nationale<wbr/>xaminer.com/</a> 教育 
<br/>203Soap Opera Weekly(肥皂剧周刊) <a href="http://www.soapoperaweekly.com/" target="_blank" rel="nofollow">http://www.soapopera<wbr/>weekly.com/</a> 娱乐 
<br/>204Golf World(高尔夫世界) <a href="http://www.worldgolf.com/" target="_blank" rel="nofollow">http://www.worldgolf<wbr/>.com/</a> 体育 
<br/>205Runner’s World(跑步者世界) <a href="http://www.runnersworld.com/" target="_blank" rel="nofollow">http://www.runnerswo<wbr/>rld.com/</a> 体育 
<br/>206Country Weekly(乡村周刊) <a href="http://www.countryweekly.com/" target="_blank" rel="nofollow">http://www.countrywe<wbr/>ekly.com/</a> 音乐 
<br/>207American Way(美国道路) <a href="http://www.americanwaymag.com/" target="_blank" rel="nofollow">http://www.americanw<wbr/>aymag.com/</a> 旅游 
<br/>208Upside(上面) <a href="http://www.upside.com/" target="_blank" rel="nofollow">http://www.upside.co<wbr/>m/</a> IT 
<br/>209Design News (设计新闻) <a href="http://www.manufacturing.net/" target="_blank" rel="nofollow">http://www.manufactu<wbr/>ring.net/</a> 行业 
<br/>210Details(详细资料) <a href="http://www.condenet.com/mags/details/" target="_blank" rel="nofollow">http://www.condenet.<wbr/>com/mags/details/</a> 时尚 
<br/>211American Profile(美国外形) <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.americanprofile.com%2F" target="_blank" rel="nofollow">http://www.americanp<wbr/>rofile.com/</a> 健康 
<br/>212ENR <a href="http://enr.construction.com/Default.asp" target="_blank" rel="nofollow">http://enr.construct<wbr/>ion.com/Default.asp</a> 建筑 
<br/>213Machine Design(机械设计) <a href="http://www.machinedesign.com/" target="_blank" rel="nofollow">http://www.machinede<wbr/>sign.com/</a> 行业 
<br/>214PC Gamer(PC游戏玩家) <a href="http://www.pcgamer.com/" target="_blank" rel="nofollow">http://www.pcgamer.c<wbr/>om/</a> 游戏 
<br/>215Biography(传记)<a href="http://www.biography.com/" target="_blank" rel="nofollow">http://www.biography<wbr/>.com/</a> 文学 
<br/>216Atlantic Monthly(大西洋月刊) <a href="http://www.theatlantic.com/" target="_blank" rel="nofollow">http://www.theatlant<wbr/>ic.com/</a> 文艺 
<br/>217Successful Farming(成功农业) <a href="http://www.agriculture.com/sfonline/" target="_blank" rel="nofollow">http://www.agricultu<wbr/>re.com/sfonline/</a> 行业 
<br/>218Texas Monthly(德克莎斯月刊) <a href="http://www.texasmonthly.com/" target="_blank" rel="nofollow">http://www.texasmont<wbr/>hly.com/</a> 地区 
<br/>219Skiing(滑雪运动) <a href="http://www.skiingmag.com/skiing/" target="_blank" rel="nofollow">http://www.skiingmag<wbr/>.com/skiing/</a> 体育 
<br/>220Southern Accents(南方口音) <a href="http://www.southernaccents.com/accents/" target="_blank" rel="nofollow">http://www.southerna<wbr/>ccents.com/accents/</a> 家庭 
<br/>221American Rifleman(美国步枪射手) 
<br/><a href="http://www.americanrifleman.org/site/index.asp" target="_blank" rel="nofollow">http://www.americanr<wbr/>ifleman.org/site/ind<wbr/>ex.asp</a> 枪械 
<br/>222Bassmaster <a href="http://www.bassmaster.com/" target="_blank" rel="nofollow">http://www.bassmaste<wbr/>r.com/</a> 休闲 
<br/>223SN-Supermarket News(超级市场新闻) <a href="http://www.supermarketnews.com/" target="_blank" rel="nofollow">http://www.supermark<wbr/>etnews.com/</a> 行业 
<br/>224ABA Journal(美国银行家协会期刊) 
<br/><a href="http://www.abanet.org/journal/redesign/home.html" target="_blank" rel="nofollow">http://www.abanet.or<wbr/>g/journal/redesign/h<wbr/>ome.html</a> 行业 
<br/>225Nature(自然) <a href="http://www.nature.com/" target="_blank" rel="nofollow">http://www.nature.co<wbr/>m/</a> 科学 
<br/>226Architectural Record(建筑学档案) <a href="http://www.archrecord.com/" target="_blank" rel="nofollow">http://www.archrecor<wbr/>d.com/</a> 行业 
<br/>227Adweek(广告周刊) <a href="http://www.adweek.com/adweek/index.jsp" target="_blank" rel="nofollow">http://www.adweek.co<wbr/>m/adweek/index.jsp</a> 行业 
<br/>228Petersen’s 4-Wheel &amp; Off Road <a href="http://www.4wheeloffroad.com/" target="_blank" rel="nofollow">http://www.4wheeloff<wbr/>road.com/</a> 机车 
<br/>229Business 2.0(商业2.0) <a href="http://www.business2.com/" target="_blank" rel="nofollow">http://www.business2<wbr/>.com/</a> 商业 
<br/>230Flying(飞行) <a href="http://www.flyingmag.com/" target="_blank" rel="nofollow">http://www.flyingmag<wbr/>.com/</a> 休闲 
<br/>231Billboard(公告牌) <a href="http://www.billboard.com/billboard/index.jsp" target="_blank" rel="nofollow">http://www.billboard<wbr/>.com/billboard/index<wbr/>.jsp</a> 音乐 
<br/>232Coastal Living(海岸生活) <a href="http://www.coastalliving.com/coastal/" target="_blank" rel="nofollow">http://www.coastalli<wbr/>ving.com/coastal/</a> 生活 
<br/>233Country Woman(乡村女人) <a href="http://www.countrywomanmagazine.com/" target="_blank" rel="nofollow">http://www.countrywo<wbr/>manmagazine.com/</a> 家庭 
<br/>234Boys’sLife(男孩生活) <a href="http://www.boyslife.org/" target="_blank" rel="nofollow">http://www.boyslife.<wbr/>org/</a> 孩子 
<br/>235Transworld Skateboarding(环球滑板)<a href="http://www.skateboarding.com/skate/" target="_blank" rel="nofollow">http://www.skateboar<wbr/>ding.com/skate/</a> 体育 
<br/>
<br/>236NFL Insider（美国足球联盟知情者） <a href="http://ww2.nfl.com/insider/" target="_blank" rel="nofollow">http://ww2.nfl.com/i<wbr/>nsider/</a> 体育 
<br/>237People en Espanol（人物西班牙语版） 
<br/><a href="http://www.peopleenespanol.com/pespanol/index.html/" target="_blank" rel="nofollow">http://www.peopleene<wbr/>spanol.com/pespanol/<wbr/>index.html/</a> 娱乐 
<br/>238Journal of Accountancy（会计学期刊） 
<br/><a href="http://www.aicpa.org/pubs/jofa/joaho" target="_blank" rel="nofollow">http://www.aicpa.org<wbr/>/pubs/jofa/joaho</a> me.htm 
<br/>239Windows 2000 Magazine（视窗2000杂志） <a href="http://www.win2000mag.net/" target="_blank" rel="nofollow">http://www.win2000ma<wbr/>g.net/</a> IT 
<br/>240Veranda（阳台） <a href="http://www.veranda.com/" target="_blank" rel="nofollow">http://www.veranda.c<wbr/>om/</a>　家居 
<br/>241Video Business（视频商业） <a href="http://www.videobusiness.com/" target="_blank" rel="nofollow">http://www.videobusi<wbr/>ness.com/</a> 商业 
<br/>242Backpacker（背包） <a href="http://www.backpacker.com/" target="_blank" rel="nofollow">http://www.backpacke<wbr/>r.com/</a> 休闲 
<br/>243Cigar Aficionado（雪茄迷） <a href="http://www.cigaraficionado.com/" target="_blank" rel="nofollow">http://www.cigarafic<wbr/>ionado.com/</a> 休闲 
<br/>244Telephony（技术） <a href="http://www.telephonyonline.com/" target="_blank" rel="nofollow">http://www.telephony<wbr/>online.com/</a> IT 
<br/>245Flex（弯曲） <a href="http://www.flexonline.com/" target="_blank" rel="nofollow">http://www.flexonlin<wbr/>e.com/</a> 健康 
<br/>246Variety (weekly)（品种周刊） <a href="http://www.variety.com/" target="_blank" rel="nofollow">http://www.variety.c<wbr/>om/</a> 商业 
<br/>247Cruising World （巡航世界） <a href="http://www.cruisingworld.com/" target="_blank" rel="nofollow">http://www.cruisingw<wbr/>orld.com/</a> 休闲 
<br/>248American Hunter（美国猎人） <a href="http://www.american-hunter.com/" target="_blank" rel="nofollow">http://www.american-<wbr/>hunter.com/</a> 休闲 
<br/>249Crain’s Chicago Business(克瑞恩芝加哥商业) 
<br/><a href="http://www.chicagobusiness.com/" target="_blank" rel="nofollow">http://www.chicagobu<wbr/>siness.com/</a> 商业 
<br/>250Broadcastin &amp;Cable(宽带与有线电视) <a href="https://www.douban.com/link2/?url=http%3A%2F%2Fwww.broadcastingcable.com%2F" target="_blank" rel="nofollow">http://www.broadcast<wbr/>ingcable.com/</a> 行业 
<br/>
<br/>251Petersen’s Photographic　<a href="http://www.photographic.com/" target="_blank" rel="nofollow">http://www.photograp<wbr/>hic.com/</a> 摄影 
<br/>252Golf for Women(女性高尔夫)　<a href="http://www.golfdigest.com/gfw/" target="_blank" rel="nofollow">http://www.golfdiges<wbr/>t.com/gfw/</a> 体育 
<br/>253USAirways Attache Magazine 
<br/>254Progressive Farmer(改进农场主) <a href="http://www.progressivefarmer.com/farmer/" target="_blank" rel="nofollow">http://www.progressi<wbr/>vefarmer.com/farmer/<wbr/></a> 农业
<br/>
<br/>255Easyriders <a href="http://www.easyriders.com/Home/Home.asp" target="_blank" rel="nofollow">http://www.easyrider<wbr/>s.com/Home/Home.asp</a> 机车 
<br/>256Crain’s New York Business(克瑞恩纽约商业) <a href="http://www.crainsny.com/" target="_blank" rel="nofollow">http://www.crainsny.<wbr/>com/</a> 商业 
<br/>
<br/>257Yachting(游艇) <a href="http://www.yachtingnet.com/yachting/" target="_blank" rel="nofollow">http://www.yachtingn<wbr/>et.com/yachting/</a> 休闲 
<br/>258Chicago(芝加哥) <a href="http://www.chicagomag.com/" target="_blank" rel="nofollow">http://www.chicagoma<wbr/>g.com/</a> 城市 
<br/>259Computer Gaming World(计算机游戏世界) <a href="http://www.gamers.com/cgw/index.jsp" target="_blank" rel="nofollow">http://www.gamers.co<wbr/>m/cgw/index.jsp</a> 游
<br/>戏 
<br/>260Video Store(视频商店) <a href="http://www.videostoremag.com/" target="_blank" rel="nofollow">http://www.videostor<wbr/>emag.com/</a> 商业 
<br/>261Country(乡村)　 <a href="http://www.country-magazine.com/" target="_blank" rel="nofollow">http://www.country-m<wbr/>agazine.com/</a> 生活 
<br/>262Fine Homebuilding(好家建造者) 
<br/><a href="http://www.taunton.com/finehomebuilding/index.asp" target="_blank" rel="nofollow">http://www.taunton.c<wbr/>om/finehomebuilding/<wbr/>index.asp</a> 家居 
<br/>263Yankee(美国佬) <a href="http://www.yankeemagazine.com/travel/index.php" target="_blank" rel="nofollow">http://www.yankeemag<wbr/>azine.com/travel/ind<wbr/>ex.php</a> 旅游 
<br/>264Publisher’s Weekly(出版者周刊) <a href="http://www.publishersweekly.com/" target="_blank" rel="nofollow">http://www.publisher<wbr/>sweekly.com/</a> 行业 
<br/>265Restaurants &amp; Institutions(餐馆与协会) <a href="http://www.rimag.com/" target="_blank" rel="nofollow">http://www.rimag.com<wbr/>/</a> 行业 
<br/>266American Medical News(美国医学新闻) 
<br/><a href="http://www.ama-assn.org/public/journa" target="_blank" rel="nofollow">http://www.ama-assn.<wbr/>org/public/journa</a> ls/amnews/ 行业 
<br/>267North American Hunter(北美猎人) <a href="http://visitors.huntingclub.com/magazine.as" target="_blank" rel="nofollow">http://visitors.hunt<wbr/>ingclub.com/magazine<wbr/>.as</a>
<br/>p 
<br/>268Federal Computer Week(联邦计算机周刊)　<a href="http://www.fcw.com/" target="_blank" rel="nofollow">http://www.fcw.com/</a> IT 
<br/>269Guns &amp; Ammo(枪与军火) <a href="http://www.gunsandammomag.com/dynamic.asp" target="_blank" rel="nofollow">http://www.gunsandam<wbr/>momag.com/dynamic.as<wbr/>p</a> 枪械 
<br/>270Transworld Snowboarding(环球滑雪板) 
<br/><a href="http://www.snowboarding-online.com/" target="_blank" rel="nofollow">http://www.snowboard<wbr/>ing-online.com/</a> 体育 
<br/>271New Equipment Digest(新设备文摘)　<a href="http://www.newequipment.com/" target="_blank" rel="nofollow">http://www.newequipm<wbr/>ent.com/</a> 行业 
<br/>272Weekly World News(世界新闻周刊)　 <a href="http://www.weeklyworldnews.com/" target="_blank" rel="nofollow">http://www.weeklywor<wbr/>ldnews.com/</a> 新闻 
<br/>273Chemical Week(化学周刊)　<a href="http://www.chemweek.com/" target="_blank" rel="nofollow">http://www.chemweek.<wbr/>com/</a> 行业 
<br/>274Four Wheeler(四轮车)　<a href="http://www.fourwheeler.com/" target="_blank" rel="nofollow">http://www.fourwheel<wbr/>er.com/</a> 机车 
<br/>275Gear(齿轮)　 <a href="http://www.gearmagazine.com/" target="_blank" rel="nofollow">http://www.gearmagaz<wbr/>ine.com/</a> 家居 
<br/>276Pensions &amp; Investments(养老金和投资)　<a href="http://www.pionline.com/" target="_blank" rel="nofollow">http://www.pionline.<wbr/>com/</a> 理财 
<br/>277Macworld(Mac世界)　 <a href="http://www.macworld.com/" target="_blank" rel="nofollow">http://www.macworld.<wbr/>com/</a> IT 
<br/>278Builder(建筑者)　 <a href="http://builder.com.com/" target="_blank" rel="nofollow">http://builder.com.c<wbr/>om/</a> IT 
<br/>279RB Restaurant Business(餐馆业)　 
<br/><a href="http://www.foodservicetoday.com/rb/index.shtml" target="_blank" rel="nofollow">http://www.foodservi<wbr/>cetoday.com/rb/index<wbr/>.shtml</a> 行业 
<br/>280CFO(首席运营官)　 <a href="http://www.cfo.com/" target="_blank" rel="nofollow">http://www.cfo.com/</a> IT 
<br/>281American Family Physician(美国家庭医生)　<a href="http://www.aafp.org/afp.xml" target="_blank" rel="nofollow">http://www.aafp.org/<wbr/>afp.xml</a> 健康 
<br/>
<br/>282Los Angeles Times Magazine(洛杉矶时报杂志)　<a href="http://www.latimes.com/" target="_blank" rel="nofollow">http://www.latimes.c<wbr/>om/</a> 新闻 
<br/>
<br/>283Saveur　 <a href="http://www.saveur.com/" target="_blank" rel="nofollow">http://www.saveur.co<wbr/>m/</a> 烹饪 
<br/>284Multichannel News(多频道新闻)　<a href="http://www.multichannel.com/" target="_blank" rel="nofollow">http://www.multichan<wbr/>nel.com/</a> 行业 
<br/>285Purchasing(购买)　 <a href="http://www.manufacturing.net/" target="_blank" rel="nofollow">http://www.manufactu<wbr/>ring.net/</a> 消费 
<br/>286Laser Focus World(激光焦点世界) <a href="http://lfw.pennnet.com/home.cfm" target="_blank" rel="nofollow">http://lfw.pennnet.c<wbr/>om/home.cfm</a> 行业 
<br/>287HANDY(手工) <a href="http://visitors.handymanclub.com/handy_mag.asp" target="_blank" rel="nofollow">http://visitors.hand<wbr/>ymanclub.com/handy_m<wbr/>ag.asp</a> 家居 
<br/>288Medical Economics(医药经济) <a href="http://www.medec.com/" target="_blank" rel="nofollow">http://www.medec.com<wbr/>/</a> 行业 
<br/>289Reminisce(回忆) <a href="http://www.reminisce.com/" target="_blank" rel="nofollow">http://www.reminisce<wbr/>.com/</a>　休闲 
<br/>290Pillsbury Classic Cookbooks <a href="http://www.pillsbury.com/" target="_blank" rel="nofollow">http://www.pillsbury<wbr/>.com/</a> 烹饪 
<br/>291Skin Diver(滑水) <a href="http://www.skin-diver.com/" target="_blank" rel="nofollow">http://www.skin-dive<wbr/>r.com/</a> 休闲 
<br/>292Nursing 2002 <a href="http://www.nursinghomesmagazine.com/" target="_blank" rel="nofollow">http://www.nursingho<wbr/>mesmagazine.com/</a> 护理 
<br/>293Hemmings Motor News <a href="http://cars.hemmings.com/" target="_blank" rel="nofollow">http://cars.hemmings<wbr/>.com/</a> 机车 
<br/>294American Legion Magazine(美国军团杂志) <a href="http://www.legion.org/" target="_blank" rel="nofollow">http://www.legion.or<wbr/>g/</a> 公益 
<br/>295Farm Journal(农业期刊) <a href="http://www.farmjournal.com/" target="_blank" rel="nofollow">http://www.farmjourn<wbr/>al.com/</a> 农业 
<br/>296Southwest Airlines Spirit(西南航线精灵) <a href="http://www.spiritmag.com/" target="_blank" rel="nofollow">http://www.spiritmag<wbr/>.com/</a> 航行 
<br/>297Dr. Dobb’s Journal <a href="http://www.ddj.com/" target="_blank" rel="nofollow">http://www.ddj.com/</a> IT 
<br/>298Chicago Tribune Magazine(芝加哥论坛杂志) 
<br/><a href="http://www.chicagotribune.com/features/magazine/" target="_blank" rel="nofollow">http://www.chicagotr<wbr/>ibune.com/features/m<wbr/>agazine/</a> 新闻 
<br/>299Islands(岛屿) <a href="http://www.islands.com/" target="_blank" rel="nofollow">http://www.islands.c<wbr/>om/</a> 休闲 
<br/>300Institutional Investor(金融机构投资者) <a href="http://www.epinions.com/" target="_blank" rel="nofollow">http://www.epinions.<wbr/>com/</a>
<br/>
<br/>原作者：打湿的双翼 
<br/>来自：blogbus</p>
              </div>
            </div>
            <div id="link-report_group">
                

            </div>
            
  


        </div>
        
        <div class="sns-bar" id="sep">
            


<div class="action-react">
    <a class="react-btn react-add j a_show_login" href="https://www.douban.com/accounts/register?reason=like">赞</a>
</div>


            

        </div>

    </div>

    <div id="dale_group_topic_banner_after_content"></div>

        






<div class="dialog_join_group">
    <span class="join_group_close">&times;</span>
    <div class="join_group_desc">加入小组后即可参加投票</div>
        <a href="javascript:;" class="join_group_cancel j a_show_login">确定</a>
</div>




    

    <div class="tabs" id='sep'>
    <a href="https://www.douban.com/group/topic/4002607/#sep" class=on>回应</a>
        <a href="https://www.douban.com/group/topic/4002607/?type=rec#sep" >转发</a>
    <a href="https://www.douban.com/group/topic/4002607/?type=like#sep" >赞</a>
    <a href="https://www.douban.com/group/topic/4002607/?type=collect#sep" >收藏</a>

            <span style="float:right">
                <a href="https://www.douban.com/group/topic/4002607/?author=1#sep">只看楼主</a>
            </span>
    </div>

                        

                    
    <ul class="topic-reply" id="comments">
        

<li class="clearfix comment-item reply-item "
id="31123215"
data-is_folded="False"
data-author-id="2392154"
data-cid="31123215" >
    <div class="user-face">
        <a href="https://www.douban.com/people/mia.wong/"><img class="pil" src="https://img9.doubanio.com/icon/u2392154-14.jpg" alt="*王秋秋Mia"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/mia.wong/" class="">*王秋秋Mia</a>
              <span class="pubtime">2008-08-21 20:29:12</span>
          </h4>
        </div>
        
            <p class=" reply-content">推荐保存了</p>

        <div
            class="operation_div"
            id="2392154"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31123215#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31123215" class="lnk-delete-comment" title="真的要删除*王秋秋Mia的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31123516"
data-is_folded="False"
data-author-id="1185883"
data-cid="31123516" >
    <div class="user-face">
        <a href="https://www.douban.com/people/jazzyan/"><img class="pil" src="https://img9.doubanio.com/icon/u1185883-154.jpg" alt="钟辉"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/jazzyan/" class="">钟辉</a>
              <span class="pubtime">2008-08-21 20:32:08</span>
          </h4>
        </div>
        
            <p class=" reply-content">很好的帖子 
但要等我英语过了4级才用到的上</p>

        <div
            class="operation_div"
            id="1185883"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31123516#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31123516" class="lnk-delete-comment" title="真的要删除钟辉的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31123659"
data-is_folded="False"
data-author-id="1842302"
data-cid="31123659" >
    <div class="user-face">
        <a href="https://www.douban.com/people/ITALO/"><img class="pil" src="https://img9.doubanio.com/icon/u1842302-5.jpg" alt="弗洛夏姆怪人"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/ITALO/" class="">弗洛夏姆怪人</a>
              <span class="pubtime">2008-08-21 20:33:46</span>
          </h4>
        </div>
        
            <p class=" reply-content">虽然很好  可是不会一个一个点的</p>

        <div
            class="operation_div"
            id="1842302"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31123659#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31123659" class="lnk-delete-comment" title="真的要删除弗洛夏姆怪人的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31126307"
data-is_folded="False"
data-author-id="1100945"
data-cid="31126307" >
    <div class="user-face">
        <a href="https://www.douban.com/people/Jane.W/"><img class="pil" src="https://img1.doubanio.com/icon/u1100945-189.jpg" alt="han"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/Jane.W/" class="">han</a>
              <span class="pubtime">2008-08-21 20:59:17</span>
          </h4>
        </div>
        
            <p class=" reply-content">留痕</p>

        <div
            class="operation_div"
            id="1100945"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31126307#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31126307" class="lnk-delete-comment" title="真的要删除han的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31127027"
data-is_folded="False"
data-author-id="1667324"
data-cid="31127027" >
    <div class="user-face">
        <a href="https://www.douban.com/people/y89614/"><img class="pil" src="https://img9.doubanio.com/icon/u1667324-654.jpg" alt="華生"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/y89614/" class="">華生</a>
              <span class="pubtime">2008-08-21 21:05:52</span>
          </h4>
        </div>
        
            <p class=" reply-content">-辛苦咯.</p>

        <div
            class="operation_div"
            id="1667324"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31127027#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31127027" class="lnk-delete-comment" title="真的要删除華生的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31127324"
data-is_folded="False"
data-author-id="2383284"
data-cid="31127324" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-21 21:08:16</span>
          </h4>
        </div>
        
            <p class=" reply-content">2008-08-21 20:33:46 ITALO (苏州)　　虽然很好 可是不会一个一个点的
====================
那就挑着点呗~~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31127324#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31127324" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31127387"
data-is_folded="False"
data-author-id="2383284"
data-cid="31127387" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-21 21:08:57</span>
          </h4>
        </div>
        
            <p class=" reply-content"> 2008-08-21 21:05:52 阿助|不明原因の原因总让人失眠 　　-辛苦咯.
 ======================
我只是用下复制和粘贴而已，辛苦的不是我，是原作者</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31127387#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31127387" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31136989"
data-is_folded="False"
data-author-id="2383284"
data-cid="31136989" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-21 22:29:38</span>
          </h4>
        </div>
        
            <p class=" reply-content">2008-08-21 20:32:08 yan 　　很好的帖子 
　　但要等我英语过了4级才用到的上
=====================
现在也可以的，看看图呗，说不定还能提高cet4~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31136989#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31136989" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31163122"
data-is_folded="False"
data-author-id="1908736"
data-cid="31163122" >
    <div class="user-face">
        <a href="https://www.douban.com/people/limeislim/"><img class="pil" src="https://img3.doubanio.com/icon/u1908736-33.jpg" alt="双城糖果"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/limeislim/" class="">双城糖果</a> (4月十几号是纪念日？)
              <span class="pubtime">2008-08-22 08:34:35</span>
          </h4>
        </div>
        
            <p class=" reply-content">真强！~~~~服了</p>

        <div
            class="operation_div"
            id="1908736"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31163122#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31163122" class="lnk-delete-comment" title="真的要删除双城糖果的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31163648"
data-is_folded="False"
data-author-id="2192049"
data-cid="31163648" >
    <div class="user-face">
        <a href="https://www.douban.com/people/two2roubao/"><img class="pil" src="https://img9.doubanio.com/icon/u2192049-56.jpg" alt="兔二肉包"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/two2roubao/" class="">兔二肉包</a> (白眼一翻，这世界与我无关)
              <span class="pubtime">2008-08-22 08:48:58</span>
          </h4>
        </div>
        
            <p class=" reply-content">收</p>

        <div
            class="operation_div"
            id="2192049"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31163648#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31163648" class="lnk-delete-comment" title="真的要删除兔二肉包的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31170214"
data-is_folded="False"
data-author-id="1401125"
data-cid="31170214" >
    <div class="user-face">
        <a href="https://www.douban.com/people/iCiCiC/"><img class="pil" src="https://img3.doubanio.com/icon/u1401125-1.jpg" alt="iC"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/iCiCiC/" class="">iC</a> (ז)
              <span class="pubtime">2008-08-22 10:21:50</span>
          </h4>
        </div>
        
            <p class=" reply-content">点上</p>

        <div
            class="operation_div"
            id="1401125"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31170214#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31170214" class="lnk-delete-comment" title="真的要删除iC的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31217602"
data-is_folded="False"
data-author-id="2383284"
data-cid="31217602" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-22 17:57:55</span>
          </h4>
        </div>
        
            <p class=" reply-content">点上？</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31217602#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31217602" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31217774"
data-is_folded="False"
data-author-id="2361474"
data-cid="31217774" >
    <div class="user-face">
        <a href="https://www.douban.com/people/zhoucindy/"><img class="pil" src="https://img3.doubanio.com/icon/u2361474-1.jpg" alt="小咪饼饼烧"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/zhoucindy/" class="">小咪饼饼烧</a>
              <span class="pubtime">2008-08-22 18:00:15</span>
          </h4>
        </div>
        
            <p class=" reply-content">不错，推荐了
</p>

        <div
            class="operation_div"
            id="2361474"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31217774#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31217774" class="lnk-delete-comment" title="真的要删除小咪饼饼烧的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31218125"
data-is_folded="False"
data-author-id="2494767"
data-cid="31218125" >
    <div class="user-face">
        <a href="https://www.douban.com/people/fengyue4/"><img class="pil" src="https://img9.doubanio.com/icon/u2494767-4.jpg" alt="风月四"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/fengyue4/" class="">风月四</a>
              <span class="pubtime">2008-08-22 18:05:05</span>
          </h4>
        </div>
        
            <p class=" reply-content">资源真丰富</p>

        <div
            class="operation_div"
            id="2494767"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31218125#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31218125" class="lnk-delete-comment" title="真的要删除风月四的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31218416"
data-is_folded="False"
data-author-id="2383284"
data-cid="31218416" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-22 18:08:48</span>
          </h4>
        </div>
        
            <p class=" reply-content">呵呵~~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31218416#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31218416" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31218635"
data-is_folded="False"
data-author-id="2706720"
data-cid="31218635" >
    <div class="user-face">
        <a href="https://www.douban.com/people/royzhong/"><img class="pil" src="https://img9.doubanio.com/icon/u2706720-455.jpg" alt="F.t"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/royzhong/" class="">F.t</a> (妇女，让我给你一个更刁钻的角度)
              <span class="pubtime">2008-08-22 18:11:33</span>
          </h4>
        </div>
        
            <p class=" reply-content">留名~</p>

        <div
            class="operation_div"
            id="2706720"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31218635#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31218635" class="lnk-delete-comment" title="真的要删除F.t的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31219024"
data-is_folded="False"
data-author-id="2158348"
data-cid="31219024" >
    <div class="user-face">
        <a href="https://www.douban.com/people/xiao_jue/"><img class="pil" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="[已注销]"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/xiao_jue/" class="">[已注销]</a>
              <span class="pubtime">2008-08-22 18:16:32</span>
          </h4>
        </div>
        
            <p class=" reply-content">国外的布局真TMD简洁..</p>

        <div
            class="operation_div"
            id="2158348"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31219024#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31219024" class="lnk-delete-comment" title="真的要删除[已注销]的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31226058"
data-is_folded="False"
data-author-id="2761936"
data-cid="31226058" >
    <div class="user-face">
        <a href="https://www.douban.com/people/BBkissyou/"><img class="pil" src="https://img3.doubanio.com/icon/u2761936-661.jpg" alt="BiBi"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/BBkissyou/" class="">BiBi</a> (時空穿梭機)
              <span class="pubtime">2008-08-22 19:54:18</span>
          </h4>
        </div>
        
            <p class=" reply-content">这个好！</p>

        <div
            class="operation_div"
            id="2761936"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31226058#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31226058" class="lnk-delete-comment" title="真的要删除BiBi的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31227320"
data-is_folded="False"
data-author-id="2745652"
data-cid="31227320" >
    <div class="user-face">
        <a href="https://www.douban.com/people/yumsnow/"><img class="pil" src="https://img3.doubanio.com/icon/u2745652-92.jpg" alt="南  方"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/yumsnow/" class="">南  方</a> (R U sleeping)
              <span class="pubtime">2008-08-22 20:07:47</span>
          </h4>
        </div>
        
            <p class=" reply-content">GOOD.</p>

        <div
            class="operation_div"
            id="2745652"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31227320#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31227320" class="lnk-delete-comment" title="真的要删除南  方的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31231181"
data-is_folded="False"
data-author-id="2383284"
data-cid="31231181" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-22 20:47:52</span>
          </h4>
        </div>
        
            <p class=" reply-content">2008-08-22 20:09:07 用倦殆和空虛饑餓細胞 　　有些鏈接過期了
=====================
有可能的，想必这些也是原作者经过很长时间的整理~~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31231181#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31231181" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31237074"
data-is_folded="False"
data-author-id="2642428"
data-cid="31237074" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2642428/"><img class="pil" src="https://img3.doubanio.com/icon/u2642428-41.jpg" alt="克松"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2642428/" class="">克松</a> (乘物游心)
              <span class="pubtime">2008-08-22 21:44:15</span>
          </h4>
        </div>
        
            <p class=" reply-content">呆了~</p>

        <div
            class="operation_div"
            id="2642428"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31237074#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31237074" class="lnk-delete-comment" title="真的要删除克松的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31238274"
data-is_folded="False"
data-author-id="1655289"
data-cid="31238274" >
    <div class="user-face">
        <a href="https://www.douban.com/people/o0c0o/"><img class="pil" src="https://img9.doubanio.com/icon/u1655289-166.jpg" alt="孤云独自闲"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/o0c0o/" class="">孤云独自闲</a> (心中犹如一万匹草泥马狂奔.)
              <span class="pubtime">2008-08-22 21:54:12</span>
          </h4>
        </div>
        
            <p class=" reply-content">没用 

这么多你看得过来呀？</p>

        <div
            class="operation_div"
            id="1655289"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31238274#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31238274" class="lnk-delete-comment" title="真的要删除孤云独自闲的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31250906"
data-is_folded="False"
data-author-id="2383284"
data-cid="31250906" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-22 23:45:38</span>
          </h4>
        </div>
        
            <p class=" reply-content">2008-08-22 21:54:12 孤雲獨自閑 (Montréal)　　没用 
　　 
　　这么多你看得过来呀？
======================


谁去书店还把所有的书读完过？</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31250906#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31250906" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31361089"
data-is_folded="False"
data-author-id="2383284"
data-cid="31361089" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-24 12:17:49</span>
          </h4>
        </div>
        
            <p class=" reply-content">如果觉得没用，何必要看~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31361089#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31361089" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31369889"
data-is_folded="False"
data-author-id="1336040"
data-cid="31369889" >
    <div class="user-face">
        <a href="https://www.douban.com/people/1336040/"><img class="pil" src="https://img3.doubanio.com/icon/u1336040-2.jpg" alt="dou"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/1336040/" class="">dou</a> (真情呼唤回归)
              <span class="pubtime">2008-08-24 14:25:18</span>
          </h4>
        </div>
        
            <p class=" reply-content">LZ好心人，这么好的资源共享。谢谢。
多一些像楼主这样的人，国家的精神文明肯定会提高一个大台阶，哈哈，
加油，</p>

        <div
            class="operation_div"
            id="1336040"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31369889#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31369889" class="lnk-delete-comment" title="真的要删除dou的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31372373"
data-is_folded="False"
data-author-id="2218734"
data-cid="31372373" >
    <div class="user-face">
        <a href="https://www.douban.com/people/sunnight/"><img class="pil" src="https://img3.doubanio.com/icon/u2218734-101.jpg" alt="m1ss Y 。°●"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/sunnight/" class="">m1ss Y 。°●</a>
              <span class="pubtime">2008-08-24 15:01:37</span>
          </h4>
        </div>
        
            <p class=" reply-content">mk</p>

        <div
            class="operation_div"
            id="2218734"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31372373#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31372373" class="lnk-delete-comment" title="真的要删除m1ss Y 。°●的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31373654"
data-is_folded="False"
data-author-id="2840294"
data-cid="31373654" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2840294/"><img class="pil" src="https://img1.doubanio.com/icon/u2840294-8.jpg" alt="啊 兔几"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2840294/" class="">啊 兔几</a>
              <span class="pubtime">2008-08-24 15:22:49</span>
          </h4>
        </div>
        
            <p class=" reply-content">非一般的强大啊~</p>

        <div
            class="operation_div"
            id="2840294"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31373654#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31373654" class="lnk-delete-comment" title="真的要删除啊 兔几的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31378937"
data-is_folded="False"
data-author-id="2030495"
data-cid="31378937" >
    <div class="user-face">
        <a href="https://www.douban.com/people/stonesmith/"><img class="pil" src="https://img1.doubanio.com/icon/u2030495-7.jpg" alt="stone"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/stonesmith/" class="">stone</a> (逃离 抽身)
              <span class="pubtime">2008-08-24 16:40:36</span>
          </h4>
        </div>
        
            <p class=" reply-content"> 哇 好东西也 </p>

        <div
            class="operation_div"
            id="2030495"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31378937#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31378937" class="lnk-delete-comment" title="真的要删除stone的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31383299"
data-is_folded="False"
data-author-id="2793256"
data-cid="31383299" >
    <div class="user-face">
        <a href="https://www.douban.com/people/SabrinaWind/"><img class="pil" src="https://img1.doubanio.com/icon/u2793256-29.jpg" alt="嫣然之夏"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/SabrinaWind/" class="">嫣然之夏</a> (深深深呼吸)
              <span class="pubtime">2008-08-24 17:35:34</span>
          </h4>
        </div>
        
            <p class=" reply-content">mark</p>

        <div
            class="operation_div"
            id="2793256"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31383299#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31383299" class="lnk-delete-comment" title="真的要删除嫣然之夏的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31384241"
data-is_folded="False"
data-author-id="2383284"
data-cid="31384241" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-24 17:46:30</span>
          </h4>
        </div>
        
            <p class=" reply-content">2008-08-24 14:25:18 dou 　　LZ好心人，这么好的资源共享。谢谢。 
　　多一些像楼主这样的人，国家的精神文明肯定会提高一个大台阶，哈哈， 
　　加油，
===================
哦哟，谢谢夸奖了，不过这冻死是我转载的，不是原创品。所以有“盗他人精神”之嫌~~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31384241#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31384241" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31393012"
data-is_folded="False"
data-author-id="2262678"
data-cid="31393012" >
    <div class="user-face">
        <a href="https://www.douban.com/people/pls/"><img class="pil" src="https://img3.doubanio.com/icon/u2262678-30.jpg" alt="莲生"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/pls/" class="">莲生</a> (一切法无我，得成于忍。)
              <span class="pubtime">2008-08-24 19:37:53</span>
          </h4>
        </div>
        
            <p class=" reply-content">sign</p>

        <div
            class="operation_div"
            id="2262678"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31393012#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31393012" class="lnk-delete-comment" title="真的要删除莲生的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31393300"
data-is_folded="False"
data-author-id="1335921"
data-cid="31393300" >
    <div class="user-face">
        <a href="https://www.douban.com/people/kscover/"><img class="pil" src="https://img1.doubanio.com/icon/u1335921-17.jpg" alt="落白"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/kscover/" class="">落白</a>
              <span class="pubtime">2008-08-24 19:41:13</span>
          </h4>
        </div>
        
            <p class=" reply-content">MARK</p>

        <div
            class="operation_div"
            id="1335921"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31393300#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31393300" class="lnk-delete-comment" title="真的要删除落白的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31404520"
data-is_folded="False"
data-author-id="2749380"
data-cid="31404520" >
    <div class="user-face">
        <a href="https://www.douban.com/people/cyanzhou/"><img class="pil" src="https://img9.doubanio.com/icon/u2749380-44.jpg" alt="okayyyyy"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/cyanzhou/" class="">okayyyyy</a> (我可能有病)
              <span class="pubtime">2008-08-24 21:43:54</span>
          </h4>
        </div>
        
            <p class=" reply-content">又一强帖</p>

        <div
            class="operation_div"
            id="2749380"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31404520#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31404520" class="lnk-delete-comment" title="真的要删除okayyyyy的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31405563"
data-is_folded="False"
data-author-id="1095774"
data-cid="31405563" >
    <div class="user-face">
        <a href="https://www.douban.com/people/tinkle.s./"><img class="pil" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="[已注销]"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/tinkle.s./" class="">[已注销]</a>
              <span class="pubtime">2008-08-24 21:49:33</span>
          </h4>
        </div>
        
            <p class=" reply-content">都是杂志阿</p>

        <div
            class="operation_div"
            id="1095774"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31405563#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31405563" class="lnk-delete-comment" title="真的要删除[已注销]的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31409747"
data-is_folded="False"
data-author-id="2383284"
data-cid="31409747" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-24 22:11:49</span>
          </h4>
        </div>
        
            <p class=" reply-content">回ls：应该都是</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31409747#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31409747" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31410998"
data-is_folded="False"
data-author-id="1548541"
data-cid="31410998" >
    <div class="user-face">
        <a href="https://www.douban.com/people/1548541/"><img class="pil" src="https://img1.doubanio.com/icon/u1548541-8.jpg" alt="陈小宝"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/1548541/" class="">陈小宝</a> (时间怎么过的那么慢又那么快啊)
              <span class="pubtime">2008-08-24 22:18:53</span>
          </h4>
        </div>
        
            <p class=" reply-content">我也过来留个痕迹啊。</p>

        <div
            class="operation_div"
            id="1548541"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31410998#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31410998" class="lnk-delete-comment" title="真的要删除陈小宝的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31412991"
data-is_folded="False"
data-author-id="1783635"
data-cid="31412991" >
    <div class="user-face">
        <a href="https://www.douban.com/people/coldcolor/"><img class="pil" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="[已注销]"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/coldcolor/" class="">[已注销]</a>
              <span class="pubtime">2008-08-24 22:29:29</span>
          </h4>
        </div>
        
            <p class=" reply-content">慢慢看~</p>

        <div
            class="operation_div"
            id="1783635"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31412991#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31412991" class="lnk-delete-comment" title="真的要删除[已注销]的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31425521"
data-is_folded="False"
data-author-id="1894196"
data-cid="31425521" >
    <div class="user-face">
        <a href="https://www.douban.com/people/1894196/"><img class="pil" src="https://img9.doubanio.com/icon/u1894196-116.jpg" alt="Anone"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/1894196/" class="">Anone</a>
              <span class="pubtime">2008-08-24 23:59:17</span>
          </h4>
        </div>
        
            <p class=" reply-content">我也来留名拉</p>

        <div
            class="operation_div"
            id="1894196"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31425521#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31425521" class="lnk-delete-comment" title="真的要删除Anone的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31425629"
data-is_folded="False"
data-author-id="2426337"
data-cid="31425629" >
    <div class="user-face">
        <a href="https://www.douban.com/people/MEMOIR/"><img class="pil" src="https://img3.doubanio.com/icon/u2426337-73.jpg" alt="C Fontaine"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/MEMOIR/" class="">C Fontaine</a> (Delicate)
              <span class="pubtime">2008-08-25 00:00:20</span>
          </h4>
        </div>
        
            <p class=" reply-content">藏</p>

        <div
            class="operation_div"
            id="2426337"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31425629#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31425629" class="lnk-delete-comment" title="真的要删除C Fontaine的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31432104"
data-is_folded="False"
data-author-id="1344321"
data-cid="31432104" >
    <div class="user-face">
        <a href="https://www.douban.com/people/mayday001/"><img class="pil" src="https://img1.doubanio.com/icon/u1344321-307.jpg" alt="🍯"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/mayday001/" class="">🍯</a> (昨天花谢花开不是梦)
              <span class="pubtime">2008-08-25 01:12:50</span>
          </h4>
        </div>
        
            <p class=" reply-content">好东东，收藏了</p>

        <div
            class="operation_div"
            id="1344321"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31432104#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31432104" class="lnk-delete-comment" title="真的要删除🍯的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31437375"
data-is_folded="False"
data-author-id="2240650"
data-cid="31437375" >
    <div class="user-face">
        <a href="https://www.douban.com/people/sogenannte/"><img class="pil" src="https://img3.doubanio.com/icon/u2240650-51.jpg" alt="仲雪春山"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/sogenannte/" class="">仲雪春山</a> (Being-toward-death)
              <span class="pubtime">2008-08-25 03:31:11</span>
          </h4>
        </div>
        
            <p class=" reply-content">很有爱啊&gt;&lt;
收藏了收藏了！</p>

        <div
            class="operation_div"
            id="2240650"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31437375#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31437375" class="lnk-delete-comment" title="真的要删除仲雪春山的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31437509"
data-is_folded="False"
data-author-id="1530775"
data-cid="31437509" >
    <div class="user-face">
        <a href="https://www.douban.com/people/gotcha/"><img class="pil" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="[已注销]"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/gotcha/" class="">[已注销]</a>
              <span class="pubtime">2008-08-25 03:38:56</span>
          </h4>
        </div>
        
            <p class=" reply-content">收藏了收藏了！</p>

        <div
            class="operation_div"
            id="1530775"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31437509#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31437509" class="lnk-delete-comment" title="真的要删除[已注销]的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31439786"
data-is_folded="False"
data-author-id="1281711"
data-cid="31439786" >
    <div class="user-face">
        <a href="https://www.douban.com/people/linxiaodou/"><img class="pil" src="https://img1.doubanio.com/icon/u1281711-9.jpg" alt="林小豆"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/linxiaodou/" class="">林小豆</a>
              <span class="pubtime">2008-08-25 08:13:57</span>
          </h4>
        </div>
        
            <p class=" reply-content">太好啦！</p>

        <div
            class="operation_div"
            id="1281711"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31439786#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31439786" class="lnk-delete-comment" title="真的要删除林小豆的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31441945"
data-is_folded="False"
data-author-id="2417065"
data-cid="31441945" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2417065/"><img class="pil" src="https://img3.doubanio.com/icon/u2417065-2.jpg" alt="Jessica"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2417065/" class="">Jessica</a>
              <span class="pubtime">2008-08-25 09:12:26</span>
          </h4>
        </div>
        
            <p class=" reply-content">顶了</p>

        <div
            class="operation_div"
            id="2417065"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31441945#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31441945" class="lnk-delete-comment" title="真的要删除Jessica的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31443183"
data-is_folded="False"
data-author-id="2793886"
data-cid="31443183" >
    <div class="user-face">
        <a href="https://www.douban.com/people/cd_net/"><img class="pil" src="https://img9.doubanio.com/icon/u2793886-6.jpg" alt="无名"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/cd_net/" class="">无名</a>
              <span class="pubtime">2008-08-25 09:34:05</span>
          </h4>
        </div>
        
            <p class=" reply-content">有用的资料～～～收了</p>

        <div
            class="operation_div"
            id="2793886"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31443183#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31443183" class="lnk-delete-comment" title="真的要删除无名的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31446057"
data-is_folded="False"
data-author-id="1041052"
data-cid="31446057" >
    <div class="user-face">
        <a href="https://www.douban.com/people/whiterhinoceros/"><img class="pil" src="https://img9.doubanio.com/icon/u1041052-14.jpg" alt="犀牛"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/whiterhinoceros/" class="">犀牛</a>
              <span class="pubtime">2008-08-25 10:13:15</span>
          </h4>
        </div>
        
            <p class=" reply-content">MARK</p>

        <div
            class="operation_div"
            id="1041052"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31446057#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31446057" class="lnk-delete-comment" title="真的要删除犀牛的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31447968"
data-is_folded="False"
data-author-id="2777598"
data-cid="31447968" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2777598/"><img class="pil" src="https://img9.doubanio.com/icon/u2777598-14.jpg" alt="等待黑骑士的猪"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2777598/" class="">等待黑骑士的猪</a> (我的秘密花园)
              <span class="pubtime">2008-08-25 10:36:39</span>
          </h4>
        </div>
        
            <p class=" reply-content">LZ辛苦了``谢谢</p>

        <div
            class="operation_div"
            id="2777598"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31447968#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31447968" class="lnk-delete-comment" title="真的要删除等待黑骑士的猪的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31449001"
data-is_folded="False"
data-author-id="1594870"
data-cid="31449001" >
    <div class="user-face">
        <a href="https://www.douban.com/people/assam/"><img class="pil" src="https://img3.doubanio.com/icon/u1594870-3.jpg" alt="Asa·阿萨"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/assam/" class="">Asa·阿萨</a> (等待春暖花开)
              <span class="pubtime">2008-08-25 10:47:36</span>
          </h4>
        </div>
        
            <p class=" reply-content">留爪印</p>

        <div
            class="operation_div"
            id="1594870"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31449001#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31449001" class="lnk-delete-comment" title="真的要删除Asa·阿萨的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31452489"
data-is_folded="False"
data-author-id="2284035"
data-cid="31452489" >
    <div class="user-face">
        <a href="https://www.douban.com/people/bestforyou/"><img class="pil" src="https://img9.doubanio.com/icon/u2284035-105.jpg" alt="非鱼"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/bestforyou/" class="">非鱼</a>
              <span class="pubtime">2008-08-25 11:21:27</span>
          </h4>
        </div>
        
            <p class=" reply-content">先攒着。。。</p>

        <div
            class="operation_div"
            id="2284035"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31452489#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31452489" class="lnk-delete-comment" title="真的要删除非鱼的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31464626"
data-is_folded="False"
data-author-id="2726961"
data-cid="31464626" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2726961/"><img class="pil" src="https://img9.doubanio.com/icon/u2726961-4.jpg" alt="亲爱的恬恬"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2726961/" class="">亲爱的恬恬</a>
              <span class="pubtime">2008-08-25 13:17:41</span>
          </h4>
        </div>
        
            <p class=" reply-content">不错</p>

        <div
            class="operation_div"
            id="2726961"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31464626#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31464626" class="lnk-delete-comment" title="真的要删除亲爱的恬恬的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31495013"
data-is_folded="False"
data-author-id="2517890"
data-cid="31495013" >
    <div class="user-face">
        <a href="https://www.douban.com/people/PrincessAlice/"><img class="pil" src="https://img3.doubanio.com/icon/u2517890-260.jpg" alt="Aliceisalice"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/PrincessAlice/" class="">Aliceisalice</a> (造布若梦。)
              <span class="pubtime">2008-08-25 17:46:40</span>
          </h4>
        </div>
        
            <p class=" reply-content">mark</p>

        <div
            class="operation_div"
            id="2517890"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31495013#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31495013" class="lnk-delete-comment" title="真的要删除Aliceisalice的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31495158"
data-is_folded="False"
data-author-id="1272145"
data-cid="31495158" >
    <div class="user-face">
        <a href="https://www.douban.com/people/peacebox/"><img class="pil" src="https://img1.doubanio.com/icon/u1272145-57.jpg" alt="SERENoelA"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/peacebox/" class="">SERENoelA</a>
              <span class="pubtime">2008-08-25 17:48:11</span>
          </h4>
        </div>
        
            <p class=" reply-content">GOOD</p>

        <div
            class="operation_div"
            id="1272145"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31495158#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31495158" class="lnk-delete-comment" title="真的要删除SERENoelA的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31526037"
data-is_folded="False"
data-author-id="2287416"
data-cid="31526037" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2287416/"><img class="pil" src="https://img9.doubanio.com/icon/u2287416-25.jpg" alt="利空出尽"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2287416/" class="">利空出尽</a> (诗酒趁年华)
              <span class="pubtime">2008-08-25 22:55:57</span>
          </h4>
        </div>
        
            <p class=" reply-content">好多都是付费网站啊</p>

        <div
            class="operation_div"
            id="2287416"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31526037#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31526037" class="lnk-delete-comment" title="真的要删除利空出尽的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31546532"
data-is_folded="False"
data-author-id="2383284"
data-cid="31546532" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-26 08:47:38</span>
          </h4>
        </div>
        
            <p class=" reply-content">回ls：这个我也不太清楚，我只是挑着去过几个</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31546532#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31546532" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31547105"
data-is_folded="False"
data-author-id="2241507"
data-cid="31547105" >
    <div class="user-face">
        <a href="https://www.douban.com/people/zey/"><img class="pil" src="https://img3.doubanio.com/icon/u2241507-11.jpg" alt="悦#奋斗ing"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/zey/" class="">悦#奋斗ing</a> (还有两个月...)
              <span class="pubtime">2008-08-26 08:58:18</span>
          </h4>
        </div>
        
            <p class=" reply-content">Good</p>

        <div
            class="operation_div"
            id="2241507"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31547105#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31547105" class="lnk-delete-comment" title="真的要删除悦#奋斗ing的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31551313"
data-is_folded="False"
data-author-id="2065048"
data-cid="31551313" >
    <div class="user-face">
        <a href="https://www.douban.com/people/nonon/"><img class="pil" src="https://img3.doubanio.com/icon/u2065048-1.jpg" alt="nonon"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/nonon/" class="">nonon</a> (应该给自己设定个期限了)
              <span class="pubtime">2008-08-26 09:56:08</span>
          </h4>
        </div>
        
            <p class=" reply-content">3Q</p>

        <div
            class="operation_div"
            id="2065048"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31551313#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31551313" class="lnk-delete-comment" title="真的要删除nonon的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31554622"
data-is_folded="False"
data-author-id="2708218"
data-cid="31554622" >
    <div class="user-face">
        <a href="https://www.douban.com/people/haohuimin/"><img class="pil" src="https://img1.doubanio.com/icon/u2708218-17.jpg" alt="瓢虫好"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/haohuimin/" class="">瓢虫好</a> (平静自然)
              <span class="pubtime">2008-08-26 10:28:36</span>
          </h4>
        </div>
        
            <p class=" reply-content">发现我的英文需要修炼修炼~</p>

        <div
            class="operation_div"
            id="2708218"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31554622#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31554622" class="lnk-delete-comment" title="真的要删除瓢虫好的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31556614"
data-is_folded="False"
data-author-id="1056236"
data-cid="31556614" >
    <div class="user-face">
        <a href="https://www.douban.com/people/bigcat/"><img class="pil" src="https://img3.doubanio.com/icon/u1056236-1.jpg" alt="大猫"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/bigcat/" class="">大猫</a>
              <span class="pubtime">2008-08-26 10:46:11</span>
          </h4>
        </div>
        
            <p class=" reply-content">收藏</p>

        <div
            class="operation_div"
            id="1056236"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31556614#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31556614" class="lnk-delete-comment" title="真的要删除大猫的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31556952"
data-is_folded="False"
data-author-id="2850220"
data-cid="31556952" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2850220/"><img class="pil" src="https://img1.doubanio.com/icon/u2850220-7.jpg" alt="κi料寶ル"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2850220/" class="">κi料寶ル</a> (神的孩子在跳舞)
              <span class="pubtime">2008-08-26 10:49:16</span>
          </h4>
        </div>
        
            <p class=" reply-content">还不错哦</p>

        <div
            class="operation_div"
            id="2850220"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31556952#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31556952" class="lnk-delete-comment" title="真的要删除κi料寶ル的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31561646"
data-is_folded="False"
data-author-id="1295646"
data-cid="31561646" >
    <div class="user-face">
        <a href="https://www.douban.com/people/1295646/"><img class="pil" src="https://img1.doubanio.com/icon/user_normal.jpg" alt="798"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/1295646/" class="">798</a>
              <span class="pubtime">2008-08-26 11:29:12</span>
          </h4>
        </div>
        
            <p class=" reply-content">强贴留言</p>

        <div
            class="operation_div"
            id="1295646"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31561646#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31561646" class="lnk-delete-comment" title="真的要删除798的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31579480"
data-is_folded="False"
data-author-id="1649698"
data-cid="31579480" >
    <div class="user-face">
        <a href="https://www.douban.com/people/Alaya/"><img class="pil" src="https://img3.doubanio.com/icon/u1649698-2.jpg" alt="布谷布谷"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/Alaya/" class="">布谷布谷</a> (终于还是没有注销豆瓣……)
              <span class="pubtime">2008-08-26 14:22:43</span>
          </h4>
        </div>
        
            <p class=" reply-content">技术贴留名</p>

        <div
            class="operation_div"
            id="1649698"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31579480#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31579480" class="lnk-delete-comment" title="真的要删除布谷布谷的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31582564"
data-is_folded="False"
data-author-id="1492400"
data-cid="31582564" >
    <div class="user-face">
        <a href="https://www.douban.com/people/EmptyHouse/"><img class="pil" src="https://img3.doubanio.com/icon/u1492400-2.jpg" alt="emptyhouse"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/EmptyHouse/" class="">emptyhouse</a>
              <span class="pubtime">2008-08-26 14:52:18</span>
          </h4>
        </div>
        
            <p class=" reply-content">哇，不错，很多有兴趣的地方
谢谢啦</p>

        <div
            class="operation_div"
            id="1492400"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31582564#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31582564" class="lnk-delete-comment" title="真的要删除emptyhouse的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31701359"
data-is_folded="False"
data-author-id="1545154"
data-cid="31701359" >
    <div class="user-face">
        <a href="https://www.douban.com/people/1545154/"><img class="pil" src="https://img3.doubanio.com/icon/u1545154-190.jpg" alt="Vanessa"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/1545154/" class="">Vanessa</a>
              <span class="pubtime">2008-08-27 16:10:22</span>
          </h4>
        </div>
        
            <p class=" reply-content">楼主辛苦拉</p>

        <div
            class="operation_div"
            id="1545154"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31701359#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31701359" class="lnk-delete-comment" title="真的要删除Vanessa的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31702793"
data-is_folded="False"
data-author-id="1598832"
data-cid="31702793" >
    <div class="user-face">
        <a href="https://www.douban.com/people/1598832/"><img class="pil" src="https://img3.doubanio.com/icon/u1598832-20.jpg" alt="七七nina"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/1598832/" class="">七七nina</a>
              <span class="pubtime">2008-08-27 16:23:02</span>
          </h4>
        </div>
        
            <p class=" reply-content">mark</p>

        <div
            class="operation_div"
            id="1598832"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31702793#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31702793" class="lnk-delete-comment" title="真的要删除七七nina的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31702929"
data-is_folded="False"
data-author-id="2196468"
data-cid="31702929" >
    <div class="user-face">
        <a href="https://www.douban.com/people/carissa15/"><img class="pil" src="https://img1.doubanio.com/icon/u2196468-98.jpg" alt="吃饭了否5，"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/carissa15/" class="">吃饭了否5，</a> (可能是只猫)
              <span class="pubtime">2008-08-27 16:24:19</span>
          </h4>
        </div>
        
            <p class=" reply-content">真强。</p>

        <div
            class="operation_div"
            id="2196468"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31702929#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31702929" class="lnk-delete-comment" title="真的要删除吃饭了否5，的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31705600"
data-is_folded="False"
data-author-id="1783988"
data-cid="31705600" >
    <div class="user-face">
        <a href="https://www.douban.com/people/qinglang1900/"><img class="pil" src="https://img9.doubanio.com/icon/u1783988-15.jpg" alt="年末"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/qinglang1900/" class="">年末</a>
              <span class="pubtime">2008-08-27 16:45:23</span>
          </h4>
        </div>
        
            <p class=" reply-content">很好。。</p>

        <div
            class="operation_div"
            id="1783988"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31705600#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31705600" class="lnk-delete-comment" title="真的要删除年末的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31723984"
data-is_folded="False"
data-author-id="2049420"
data-cid="31723984" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2049420/"><img class="pil" src="https://img3.doubanio.com/icon/u2049420-2.jpg" alt="小指"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2049420/" class="">小指</a> (不舒服)
              <span class="pubtime">2008-08-27 19:58:10</span>
          </h4>
        </div>
        
            <p class=" reply-content">啊噢，正好用来学英语</p>

        <div
            class="operation_div"
            id="2049420"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31723984#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31723984" class="lnk-delete-comment" title="真的要删除小指的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31729211"
data-is_folded="False"
data-author-id="1983196"
data-cid="31729211" >
    <div class="user-face">
        <a href="https://www.douban.com/people/vlea/"><img class="pil" src="https://img1.doubanio.com/icon/u1983196-18.jpg" alt="沈今鹭"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/vlea/" class="">沈今鹭</a> (这就是开始 这就是结束)
              <span class="pubtime">2008-08-27 20:48:59</span>
          </h4>
        </div>
        
            <p class=" reply-content">


哇列</p>

        <div
            class="operation_div"
            id="1983196"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31729211#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31729211" class="lnk-delete-comment" title="真的要删除沈今鹭的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31737672"
data-is_folded="False"
data-author-id="2042384"
data-cid="31737672" >
    <div class="user-face">
        <a href="https://www.douban.com/people/shuiqingqian/"><img class="pil" src="https://img9.doubanio.com/icon/u2042384-15.jpg" alt="金姑娘这棵树"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/shuiqingqian/" class="">金姑娘这棵树</a> (沉醉生活)
              <span class="pubtime">2008-08-27 21:55:48</span>
          </h4>
        </div>
        
            <p class=" reply-content">好东西，要怎么才能留得住~~~</p>

        <div
            class="operation_div"
            id="2042384"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31737672#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31737672" class="lnk-delete-comment" title="真的要删除金姑娘这棵树的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31740060"
data-is_folded="False"
data-author-id="2443436"
data-cid="31740060" >
    <div class="user-face">
        <a href="https://www.douban.com/people/EcHo--s/"><img class="pil" src="https://img3.doubanio.com/icon/u2443436-42.jpg" alt="西伯利亚"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/EcHo--s/" class="">西伯利亚</a> (喜怒无常+神经质)
              <span class="pubtime">2008-08-27 22:12:48</span>
          </h4>
        </div>
        
            <p class=" reply-content">哇哦
留个爪
</p>

        <div
            class="operation_div"
            id="2443436"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31740060#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31740060" class="lnk-delete-comment" title="真的要删除西伯利亚的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31741044"
data-is_folded="False"
data-author-id="2625430"
data-cid="31741044" >
    <div class="user-face">
        <a href="https://www.douban.com/people/wtt0553/"><img class="pil" src="https://img1.doubanio.com/icon/u2625430-79.jpg" alt="王脱盐"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/wtt0553/" class="">王脱盐</a> (七彩玲珑少女心)
              <span class="pubtime">2008-08-27 22:19:38</span>
          </h4>
        </div>
        
            <p class=" reply-content">标记下~</p>

        <div
            class="operation_div"
            id="2625430"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31741044#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31741044" class="lnk-delete-comment" title="真的要删除王脱盐的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31741698"
data-is_folded="False"
data-author-id="2613363"
data-cid="31741698" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2613363/"><img class="pil" src="https://img9.doubanio.com/icon/u2613363-4.jpg" alt="爱肉肉"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2613363/" class="">爱肉肉</a>
              <span class="pubtime">2008-08-27 22:24:52</span>
          </h4>
        </div>
        
            <p class=" reply-content">你们太厉害了,怎么收集的这么多呢!!厉害!</p>

        <div
            class="operation_div"
            id="2613363"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31741698#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31741698" class="lnk-delete-comment" title="真的要删除爱肉肉的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31770954"
data-is_folded="False"
data-author-id="2857050"
data-cid="31770954" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2857050/"><img class="pil" src="https://img3.doubanio.com/icon/u2857050-41.jpg" alt="方大同太太"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2857050/" class="">方大同太太</a> (收)
              <span class="pubtime">2008-08-28 09:45:11</span>
          </h4>
        </div>
        
            <p class=" reply-content">  怎么保存这个帖子啊</p>

        <div
            class="operation_div"
            id="2857050"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31770954#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31770954" class="lnk-delete-comment" title="真的要删除方大同太太的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31775420"
data-is_folded="False"
data-author-id="1912000"
data-cid="31775420" >
    <div class="user-face">
        <a href="https://www.douban.com/people/mooki/"><img class="pil" src="https://img3.doubanio.com/icon/u1912000-1.jpg" alt="一只蝙蝠"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/mooki/" class="">一只蝙蝠</a> (mooki)
              <span class="pubtime">2008-08-28 10:37:05</span>
          </h4>
        </div>
        
            <p class=" reply-content">woo~~~~</p>

        <div
            class="operation_div"
            id="1912000"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31775420#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31775420" class="lnk-delete-comment" title="真的要删除一只蝙蝠的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31779695"
data-is_folded="False"
data-author-id="1225107"
data-cid="31779695" >
    <div class="user-face">
        <a href="https://www.douban.com/people/summergirl/"><img class="pil" src="https://img1.doubanio.com/icon/u1225107-118.jpg" alt="Summergirlvivi"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/summergirl/" class="">Summergirlvivi</a>
              <span class="pubtime">2008-08-28 11:19:42</span>
          </h4>
        </div>
        
            <p class=" reply-content">ｗｏｗ～太多啦~</p>

        <div
            class="operation_div"
            id="1225107"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31779695#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31779695" class="lnk-delete-comment" title="真的要删除Summergirlvivi的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31789677"
data-is_folded="False"
data-author-id="1760772"
data-cid="31789677" >
    <div class="user-face">
        <a href="https://www.douban.com/people/canlone/"><img class="pil" src="https://img3.doubanio.com/icon/u1760772-33.jpg" alt="殘殘"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/canlone/" class="">殘殘</a> (保持庸俗)
              <span class="pubtime">2008-08-28 13:02:35</span>
          </h4>
        </div>
        
            <p class=" reply-content">那么多美国的..国外优秀仅仅局限在美国? 
　　太杂了..几乎是囊括,而非优秀的总结..
</p>

        <div
            class="operation_div"
            id="1760772"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31789677#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31789677" class="lnk-delete-comment" title="真的要删除殘殘的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31797676"
data-is_folded="False"
data-author-id="1451782"
data-cid="31797676" >
    <div class="user-face">
        <a href="https://www.douban.com/people/IshikawaKenji/"><img class="pil" src="https://img9.doubanio.com/icon/u1451782-56.jpg" alt="捡垃圾的提莫"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/IshikawaKenji/" class="">捡垃圾的提莫</a>
              <span class="pubtime">2008-08-28 14:19:11</span>
          </h4>
        </div>
        
            <p class=" reply-content">虽然多
但是一般般。。</p>

        <div
            class="operation_div"
            id="1451782"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31797676#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31797676" class="lnk-delete-comment" title="真的要删除捡垃圾的提莫的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31810504"
data-is_folded="False"
data-author-id="2383284"
data-cid="31810504" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-28 16:19:48</span>
          </h4>
        </div>
        
            <p class=" reply-content">自认为原作者已经很费心的整理了，我们应该感谢，而不是挑刺~~

要不，你们看谁优秀，自己整理个贴发上来吧~~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31810504#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31810504" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31816234"
data-is_folded="False"
data-author-id="2336534"
data-cid="31816234" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2336534/"><img class="pil" src="https://img3.doubanio.com/icon/u2336534-1.jpg" alt="阿佳妮"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2336534/" class="">阿佳妮</a> (半农半X)
              <span class="pubtime">2008-08-28 17:06:29</span>
          </h4>
        </div>
        
            <p class=" reply-content">多谢</p>

        <div
            class="operation_div"
            id="2336534"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31816234#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31816234" class="lnk-delete-comment" title="真的要删除阿佳妮的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31856813"
data-is_folded="False"
data-author-id="2093934"
data-cid="31856813" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2093934/"><img class="pil" src="https://img3.doubanio.com/icon/u2093934-1.jpg" alt="Masaki"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2093934/" class="">Masaki</a>
              <span class="pubtime">2008-08-28 23:44:35</span>
          </h4>
        </div>
        
            <p class=" reply-content">thanks</p>

        <div
            class="operation_div"
            id="2093934"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31856813#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31856813" class="lnk-delete-comment" title="真的要删除Masaki的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31856956"
data-is_folded="False"
data-author-id="2094055"
data-cid="31856956" >
    <div class="user-face">
        <a href="https://www.douban.com/people/allinlove/"><img class="pil" src="https://img1.doubanio.com/icon/u2094055-17.jpg" alt="非名"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/allinlove/" class="">非名</a> (我真的有变勇敢)
              <span class="pubtime">2008-08-28 23:45:58</span>
          </h4>
        </div>
        
            <p class=" reply-content">要放到精化帖里啊
呼吁~</p>

        <div
            class="operation_div"
            id="2094055"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31856956#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31856956" class="lnk-delete-comment" title="真的要删除非名的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31902589"
data-is_folded="False"
data-author-id="2629137"
data-cid="31902589" >
    <div class="user-face">
        <a href="https://www.douban.com/people/laura-luo/"><img class="pil" src="https://img1.doubanio.com/icon/u2629137-8.jpg" alt="E"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/laura-luo/" class="">E</a> (明明是浮云，却还是想抓住。。)
              <span class="pubtime">2008-08-29 13:51:12</span>
          </h4>
        </div>
        
            <p class=" reply-content">shou~~ thanks</p>

        <div
            class="operation_div"
            id="2629137"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31902589#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31902589" class="lnk-delete-comment" title="真的要删除E的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31933857"
data-is_folded="False"
data-author-id="2678155"
data-cid="31933857" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2678155/"><img class="pil" src="https://img3.doubanio.com/icon/u2678155-2.jpg" alt="地下灰尘→●打酱油才是正经事"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2678155/" class="">地下灰尘→●打酱油才是正经事</a>
              <span class="pubtime">2008-08-29 18:45:01</span>
          </h4>
        </div>
        
            <p class=" reply-content">唉 没病毒把</p>

        <div
            class="operation_div"
            id="2678155"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31933857#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31933857" class="lnk-delete-comment" title="真的要删除地下灰尘→●打酱油才是正经事的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31940033"
data-is_folded="False"
data-author-id="2383284"
data-cid="31940033" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dido1987/"><img class="pil" src="https://img1.doubanio.com/icon/u2383284-9.jpg" alt="DL"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dido1987/" class="">DL</a>
              <span class="pubtime">2008-08-29 20:03:28</span>
          </h4>
        </div>
        
            <p class=" reply-content">这个就不知道了，不过有大多是大网站，名字也是响当当的，所以应该可以信得过~~</p>

        <div
            class="operation_div"
            id="2383284"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31940033#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31940033" class="lnk-delete-comment" title="真的要删除DL的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31948166"
data-is_folded="False"
data-author-id="2378036"
data-cid="31948166" >
    <div class="user-face">
        <a href="https://www.douban.com/people/sweetya/"><img class="pil" src="https://img3.doubanio.com/icon/u2378036-1.jpg" alt="甜心牙Aeon"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/sweetya/" class="">甜心牙Aeon</a> (我X你大爷的!闲得真他妈D疼!)
              <span class="pubtime">2008-08-29 21:17:24</span>
          </h4>
        </div>
        
            <p class=" reply-content">HOHO```````</p>

        <div
            class="operation_div"
            id="2378036"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31948166#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31948166" class="lnk-delete-comment" title="真的要删除甜心牙Aeon的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="31952446"
data-is_folded="False"
data-author-id="2163255"
data-cid="31952446" >
    <div class="user-face">
        <a href="https://www.douban.com/people/roselee/"><img class="pil" src="https://img9.doubanio.com/icon/u2163255-195.jpg" alt="叫老猫的说"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/roselee/" class="">叫老猫的说</a> (对不起，您的签名正在审核中。。)
              <span class="pubtime">2008-08-29 21:53:47</span>
          </h4>
        </div>
        
            <p class=" reply-content">0.0</p>

        <div
            class="operation_div"
            id="2163255"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=31952446#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="31952446" class="lnk-delete-comment" title="真的要删除叫老猫的说的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32767059"
data-is_folded="False"
data-author-id="2343989"
data-cid="32767059" >
    <div class="user-face">
        <a href="https://www.douban.com/people/deadpipo/"><img class="pil" src="https://img3.doubanio.com/icon/u2343989-101.jpg" alt="pipo"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/deadpipo/" class="">pipo</a>
              <span class="pubtime">2008-09-08 20:50:39</span>
          </h4>
        </div>
        
            <p class=" reply-content">0</p>

        <div
            class="operation_div"
            id="2343989"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32767059#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32767059" class="lnk-delete-comment" title="真的要删除pipo的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32767651"
data-is_folded="False"
data-author-id="2798038"
data-cid="32767651" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2798038/"><img class="pil" src="https://img9.doubanio.com/icon/u2798038-16.jpg" alt="山雀儿"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2798038/" class="">山雀儿</a>
              <span class="pubtime">2008-09-08 20:58:23</span>
          </h4>
        </div>
        
            <p class=" reply-content">m</p>

        <div
            class="operation_div"
            id="2798038"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32767651#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32767651" class="lnk-delete-comment" title="真的要删除山雀儿的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32803603"
data-is_folded="False"
data-author-id="1985376"
data-cid="32803603" >
    <div class="user-face">
        <a href="https://www.douban.com/people/1985376/"><img class="pil" src="https://img1.doubanio.com/icon/u1985376-48.jpg" alt="屋子里没有人"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/1985376/" class="">屋子里没有人</a> (编一个完美的谎话。)
              <span class="pubtime">2008-09-09 11:10:23</span>
          </h4>
        </div>
        
            <p class=" reply-content">M</p>

        <div
            class="operation_div"
            id="1985376"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32803603#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32803603" class="lnk-delete-comment" title="真的要删除屋子里没有人的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32812395"
data-is_folded="False"
data-author-id="1497615"
data-cid="32812395" >
    <div class="user-face">
        <a href="https://www.douban.com/people/bobby_lg/"><img class="pil" src="https://img9.doubanio.com/icon/u1497615-14.jpg" alt="Bobo L"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/bobby_lg/" class="">Bobo L</a> (演变)
              <span class="pubtime">2008-09-09 13:04:59</span>
          </h4>
        </div>
        
            <p class=" reply-content">re-mark..</p>

        <div
            class="operation_div"
            id="1497615"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32812395#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32812395" class="lnk-delete-comment" title="真的要删除Bobo L的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32812862"
data-is_folded="False"
data-author-id="2845826"
data-cid="32812862" >
    <div class="user-face">
        <a href="https://www.douban.com/people/korekara/"><img class="pil" src="https://img9.doubanio.com/icon/u2845826-84.jpg" alt="酒酿圆子陈吞儿"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/korekara/" class="">酒酿圆子陈吞儿</a> (私は　自分を　大好きです)
              <span class="pubtime">2008-09-09 13:10:35</span>
          </h4>
        </div>
        
            <p class=" reply-content">好不错。</p>

        <div
            class="operation_div"
            id="2845826"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32812862#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32812862" class="lnk-delete-comment" title="真的要删除酒酿圆子陈吞儿的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32816564"
data-is_folded="False"
data-author-id="2434509"
data-cid="32816564" >
    <div class="user-face">
        <a href="https://www.douban.com/people/bilin-zhu/"><img class="pil" src="https://img3.doubanio.com/icon/u2434509-1691.jpg" alt="比邻·竹"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/bilin-zhu/" class="">比邻·竹</a> (月   日   時…   …)
              <span class="pubtime">2008-09-09 13:54:27</span>
          </h4>
        </div>
        
            <p class=" reply-content">：）不错！</p>

        <div
            class="operation_div"
            id="2434509"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32816564#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32816564" class="lnk-delete-comment" title="真的要删除比邻·竹的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32817350"
data-is_folded="False"
data-author-id="2556465"
data-cid="32817350" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2556465/"><img class="pil" src="https://img9.doubanio.com/icon/u2556465-6.jpg" alt="Epica"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2556465/" class="">Epica</a> (女人，你要快乐，要坚强，要坦荡)
              <span class="pubtime">2008-09-09 14:03:41</span>
          </h4>
        </div>
        
            <p class=" reply-content">支持</p>

        <div
            class="operation_div"
            id="2556465"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32817350#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32817350" class="lnk-delete-comment" title="真的要删除Epica的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32825853"
data-is_folded="False"
data-author-id="2527414"
data-cid="32825853" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2527414/"><img class="pil" src="https://img3.doubanio.com/icon/u2527414-2.jpg" alt="lena"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2527414/" class="">lena</a>
              <span class="pubtime">2008-09-09 15:58:43</span>
          </h4>
        </div>
        
            <p class=" reply-content">很多很好的信息。。。</p>

        <div
            class="operation_div"
            id="2527414"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32825853#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32825853" class="lnk-delete-comment" title="真的要删除lena的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32826356"
data-is_folded="False"
data-author-id="2192611"
data-cid="32826356" >
    <div class="user-face">
        <a href="https://www.douban.com/people/dadagood/"><img class="pil" src="https://img9.doubanio.com/icon/u2192611-85.jpg" alt="杜达达"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/dadagood/" class="">杜达达</a> (痛恨瞎联系～～讨厌胡乱搞～～)
              <span class="pubtime">2008-09-09 16:05:43</span>
          </h4>
        </div>
        
            <p class=" reply-content">先收！！</p>

        <div
            class="operation_div"
            id="2192611"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32826356#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32826356" class="lnk-delete-comment" title="真的要删除杜达达的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32828289"
data-is_folded="False"
data-author-id="2733939"
data-cid="32828289" >
    <div class="user-face">
        <a href="https://www.douban.com/people/2733939/"><img class="pil" src="https://img3.doubanio.com/icon/u2733939-31.jpg" alt="金蛋蛋"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/2733939/" class="">金蛋蛋</a> (说来说去还是要靠自己努力折腾~)
              <span class="pubtime">2008-09-09 16:30:53</span>
          </h4>
        </div>
        
            <p class=" reply-content">牛人,太厉害了..</p>

        <div
            class="operation_div"
            id="2733939"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32828289#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32828289" class="lnk-delete-comment" title="真的要删除金蛋蛋的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32828523"
data-is_folded="False"
data-author-id="1416900"
data-cid="32828523" >
    <div class="user-face">
        <a href="https://www.douban.com/people/ryoko151/"><img class="pil" src="https://img3.doubanio.com/icon/u1416900-3.jpg" alt="R"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/ryoko151/" class="">R</a>
              <span class="pubtime">2008-09-09 16:33:58</span>
          </h4>
        </div>
        
            <p class=" reply-content">优厚 </p>

        <div
            class="operation_div"
            id="1416900"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32828523#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32828523" class="lnk-delete-comment" title="真的要删除R的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32829060"
data-is_folded="False"
data-author-id="2454675"
data-cid="32829060" >
    <div class="user-face">
        <a href="https://www.douban.com/people/folksen/"><img class="pil" src="https://img3.doubanio.com/icon/u2454675-3.jpg" alt="folksen"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/folksen/" class="">folksen</a>
              <span class="pubtime">2008-09-09 16:40:44</span>
          </h4>
        </div>
        
            <p class=" reply-content">怎么很多打不开哪？</p>

        <div
            class="operation_div"
            id="2454675"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32829060#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32829060" class="lnk-delete-comment" title="真的要删除folksen的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32829077"
data-is_folded="False"
data-author-id="1532682"
data-cid="32829077" >
    <div class="user-face">
        <a href="https://www.douban.com/people/woaifengfeng/"><img class="pil" src="https://img3.doubanio.com/icon/u1532682-3.jpg" alt="笮赜"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/woaifengfeng/" class="">笮赜</a> (如果我就不想上班呢！)
              <span class="pubtime">2008-09-09 16:40:58</span>
          </h4>
        </div>
        
            <p class=" reply-content">留印儿</p>

        <div
            class="operation_div"
            id="1532682"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32829077#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32829077" class="lnk-delete-comment" title="真的要删除笮赜的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

        

<li class="clearfix comment-item reply-item "
id="32829106"
data-is_folded="False"
data-author-id="1532682"
data-cid="32829106" >
    <div class="user-face">
        <a href="https://www.douban.com/people/woaifengfeng/"><img class="pil" src="https://img3.doubanio.com/icon/u1532682-3.jpg" alt="笮赜"/></a>
    </div>
    <div class="reply-doc content" style="padding-left:0px;">
        <div class="bg-img-green">
          <h4>
              <a href="https://www.douban.com/people/woaifengfeng/" class="">笮赜</a> (如果我就不想上班呢！)
              <span class="pubtime">2008-09-09 16:41:22</span>
          </h4>
        </div>
        
            <p class=" reply-content">天，是我翻的页</p>

        <div
            class="operation_div"
            id="1532682"
        >
                <a href="https://www.douban.com/group/topic/4002607/?cid=32829106#last" class="lnk-reply ">回应</a>
                <a rel="nofollow" href="javascript:void(0);" class="comment-vote lnk-fav">赞</a>
            <div class="operation-more">
                <a rel="nofollow" href="javascript:void(0);" data-cid="32829106" class="lnk-delete-comment" title="真的要删除笮赜的发言?">删除</a>
            </div>
        </div>

        <!-- via  -->
    </div>
</li>

    </ul>

            


            
    
    

    
        <div class="paginator">
        <span class="prev">
            &lt;前页
        </span>
        
        

                <span class="thispage" data-total-page="2">1</span>
                
            <a href="https://www.douban.com/group/topic/4002607/?start=100" >2</a>
        
        <span class="next">
            <link rel="next" href="https://www.douban.com/group/topic/4002607/?start=100"/>
            <a href="https://www.douban.com/group/topic/4002607/?start=100" >后页&gt;</a>
        </span>

        </div>



            










    
    <h2>
        你的回应
            
    </h2>

    <span class="pl3" align="right">
        回应请先
        <a class="j a_show_login" href="/accounts/register?reason=discuss">登录</a>
        , 或
        <a  class="j a_show_register" href="/accounts/register?reason=discuss">注册</a>
    </span>
    <div class="txd">
        <form action="no_where_to_go">
            <textarea readonly id="last" class="j a_show_login" name="rv_comment" class="comment_textarea" rows="6" cols="64"></textarea><br/>
            <input type="file" name="img" accept="image/jpg,image/jpeg,image/bmp,image/gif,image/png">
            <span class="bn-flat-hot rr">
            <input name="submit_btn" type="submit" class="j a_show_login" value="发送"/>
            </span>
            
    <span>
      <label class="pl share-label share-shuo">
        <input type="checkbox" name="sync_to_mb"/>推荐到广播
      </label>
    </span>

        </form>
    </div>


        











    <script>var POPUP_REG = true;</script>

<script>
Do(function() {
    function deferred(){var t={done:[],fail:[]},o={done:function(i){return t.done.push(i),o},fail:function(i){return t.fail.push(i),o}};return{resolve:function(){for(var o,i=0;o=t.done[i++];)o.apply(this,arguments)},reject:function(){for(var o,i=0;o=t.fail[i++];)o.apply(this,arguments)},promise:o}}function asyncRequest(t,o,i){var e=deferred(),d=null,a=(i||"get").toLowerCase();return d=$.ajax({url:t,type:a,dataType:"json",data:"post"===a?$.extend(o,{ck:get_cookie("ck")}):o,error:function(t){e.reject(t)},success:function(t){e.resolve(t)}}),e.promise.abort=function(){d&&d.abort()},e.promise}var DOULIST_ADDITEM="/j/doulist/{doulist_id}/additem",DOULIST_EDITITEM="/j/doulist/{doulist_id}/edititem",DOULIST_COMMENT="/j/doulist/{doulist_id}/poke",DOULIST_CREATE="/j/doulist/add",DOULIST_LIST="/j/doulist/cat",DOULIST_SEARCH="/j/doulist/search",DOULIST_SEARCH_SELF="/j/doulist/search_user_doulists",DOULIST_GET_ITEM_INFO="/j/doulist/get_item_info",addTooltipToDoulistBtn=function(t){if(get_cookie("ck")){var o=/^https?:\/\/\w+\.douban\.com\/link2\/\?url=(\S+)$/i,i=function(t){var i=t.match(o);return i?decodeURIComponent(i[1]):t};$(document).delegate(".url-doulist-add","click",function(t){t.preventDefault();var o,e=$(this),d=i(e.data("url")),a=dui.Dialog({title:"添加到豆列",width:640,cls:"dialog-doulist dialog-tooltip-loading",content:'<div class="tooltip-text">内容加载中<i class="tooltip-loading-icon"></i></div>'}).open();a.node.find(".dui-dialog-close").click(function(t){o&&o.abort()}),o=asyncRequest(DOULIST_GET_ITEM_INFO,{url:d},"post").done(function(t){return t.r?void a.node.find(".tooltip-text").text(t.error):(t.cate=(t.kind||"")+"",t.picture="string"==typeof t.images?t.images:t.images&&t.images[0]||"",t.id=(t.id||"")+"",a.close(),void e.doulistDialog(t))}).fail(function(t){a.node.find(".tooltip-text").text("失败啦！再试一次吧")})});var e=85,d=!1,a="doulist-tooltip-hide",n=$('<div class="doulist-add-tooltip"><a class="url-doulist-add" ><i></i> 添加到豆列</a><div class="arrow"></div></div>'),s=n.find("a");n.addClass(a),n.appendTo($("body"));var l=function(t){d=setTimeout(function(){n.addClass(a)},e)};$(t).mouseenter(function(t){var o=$(this);n.css({top:o.offset().top-28,left:t.pageX-42}),s.data("url",o.attr("href")),clearTimeout(d),n.removeClass(a)}).mouseleave(l),n.mouseenter(function(){clearTimeout(d)}).mouseleave(l)}};

    addTooltipToDoulistBtn('#link-report .topic-content a');

    if (get_cookie('ck')) {
        $.each($(".popular-bd .operation-more"), function(i, el){
          if ($(el).find(".comment-report").length==0){
            $(el).append('<div class="comment-report"><a rel="nofollow" href="javascript:void(0)">举报</a></div>');
          }
        });
        $(".popular-bd").delegate(".comment-item", 'hover',
            function () {
              $(this).find(".comment-report").css('visibility', 'visible');
            },
            function () {
              $(this).find(".comment-report").css('visibility', 'hidden');
            }
        ).delegate(".comment-report a", 'click', function (e) {
            e.preventDefault();
            var auditUrl = "https://www.douban.com/misc/audit_report?url=",
                opt = "comment_id";
            var obj = $(e.target).closest('.comment-item');
            var cid = obj.data("cid");
            var url = "https://www.douban.com/group/topic/4002607/?".concat(opt, '=', cid);
            generate_report_dialog({report_url: url, type: 'comment'});
        });
    }
});
</script>

        </div>
        <div class="aside">
                
    







<div id="g-side-info" class="side-reg">
  <div class="bd">
      <div class="group-item">
          <div class="pic">
               <a href="https://www.douban.com/group/webwebweb/?ref=sidebar"><img src="https://img3.doubanio.com/icon/g12570-3.jpg"></a>
          </div>
          <div class="info">
              <div class="title">
				  <a href="https://www.douban.com/group/webwebweb/?ref=sidebar">网站推荐～</a>
              </div>
      </div>
    </div>
  </div>
  
  <div class="ft">
      <div class="member-status">
        <div class="ft-members">
        <i>220679</i> 人聚集在这个小组<br>
        </div>
        <a href="#" class="j a_show_login lnk-selection">加入小组</a>
      </div>
  </div>
</div>


<script src="https://img3.doubanio.com/f/shire/383a6e43f2108dc69e3ff2681bc4dc6c72a5ffb0/js/ui/dialog.js"></script>
<link href="https://img3.doubanio.com/f/shire/8377b9498330a2e6f056d863987cc7a37eb4d486/css/ui/dialog.css" rel="stylesheet" type="text/css">

<script>

  function generate_group_prompt_dialog(dui_config){
    var prompt_dlg = dui.Dialog({
        title: (dui_config.title? dui_config.title: '操作提示'),
        content: (dui_config.content? dui_config.content: '操作内容'),
        width: (dui_config.width? dui_config.width: 400),
        buttons: [
            {text: '去绑定', method: function() { window.location = dui_config.target; } },
            {text: '取消', method: function() { prompt_dlg.close(); } }
        ]
    });
    prompt_dlg.open();
  }
  /* common over */
  $('.dialog-confirm').click(function(){
    generate_group_prompt_dialog({content: '加入此小组需要绑定手机号', target: 'https://www.douban.com/accounts/phone/bind?ck=hjfn'});
    return false;
  });
</script>



    

    
    <!-- douban ad begin -->
    <div id="dale_group_topic_new_top_right"></div>
    <div id="dale_group_topic_new_top_right_large"></div>
    <div id="dale_group_topic_new_top_right2"></div>
    <!-- douban ad end -->

      
    
    <div class="mod">
        
    <h2>
        最新讨论
            
            <span class="pl">&nbsp;(
                
                    <a href="https://www.douban.com/group/webwebweb/#topics" target="_self">更多</a>
                ) </span>
    </h2>

        <div class="topic-list">
          <ul>
                <li><a href="https://www.douban.com/group/topic/47884610/" title="【严重推荐】每天一个好站推荐">【严重推荐】每天一个好站推荐</a> &nbsp;
                <span class ="pl">(维京) </span></li>
                <li><a href="https://www.douban.com/group/topic/37883575/" title="大家都有什么好的微信公众帐号推荐！！">大家都有什么好的微信公众帐号推荐！！</a> &nbsp;
                <span class ="pl">(大漠孤烟) </span></li>
                <li><a href="https://www.douban.com/group/topic/158147365/" title="推荐个免费资源博客">推荐个免费资源博客</a> &nbsp;
                <span class ="pl">(回忆你的美) </span></li>
                <li><a href="https://www.douban.com/group/topic/155396019/" title="可以批量打开多个网页的网站">可以批量打开多个网页的网站</a> &nbsp;
                <span class ="pl">(cnjc) </span></li>
                <li><a href="https://www.douban.com/group/topic/125775064/" title="【一个微信群 只推好电影】想加的来">【一个微信群 只推好电影】想加的来</a> &nbsp;
                <span class ="pl">(电影收纳盒小编) </span></li>
        </ul>
        </div>
      </div>


    <!-- douban app begin -->
    <div id="dale_group_topic_new_inner_middle"></div>
    <div id="dale_group_topic_new_download_middle"></div>
    <!-- douban app end -->

    <!-- douban ad begin -->
    <div id="dale_group_topic_doublemint"></div>
    
<!-- douban ad begin -->
<div id="dale_group_topic_new_bottom_right"></div>
<script type="text/javascript">
    (function (global) {
        if(!document.getElementsByClassName) {
            document.getElementsByClassName = function(className) {
                return this.querySelectorAll("." + className);
            };
            Element.prototype.getElementsByClassName = document.getElementsByClassName;

        }
        var articles = global.document.getElementsByClassName('article'),
            asides = global.document.getElementsByClassName('aside');

        if (articles.length > 0 && asides.length > 0 && articles[0].offsetHeight >= asides[0].offsetHeight) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_group_topic_new_bottom_right');
        }
    })(this);
</script>
<!-- douban ad end -->

    <!-- douban ad end -->

        </div>
        <div class="extra">
            
    
<!-- douban ad begin -->
<div id="dale_group_topic_bottom_super_banner"></div>
<script type="text/javascript">
    (function (global) {
        var body = global.document.body,
            html = global.document.documentElement;

        var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
        if (height >= 1200) {
            (global.DoubanAdSlots = global.DoubanAdSlots || []).push('dale_group_topic_bottom_super_banner');
        }
    })(this);
</script>
<!-- douban ad end -->

    <!-- douban ad begin -->
    <div id="dale_group_topic_hovering_video"></div>
    <!-- douban ad end -->

        </div>
    </div>
</div>

        
<div id="footer">
    
<span id="icp" class="fleft gray-link">
    &copy; 2005－2020 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/group" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

</div>

    </div>
    
    

    <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/75ffa04456510a50.js"></script>
    



<div class="back-to-top">
    <a href="#">&#8593;回顶部</a>
</div>
<script>
Do(function(){var h=$(window);var k=$(document);var l;var a=$(".back-to-top");var b=$(".aside");var g;var i=$("#content");var d=$.browser.msie&&($.browser.version|0)<7;var f=function(n){if(!f.cache){f.cache=[]}if(f.cache[n]){return}var m=new Date;(new Image()).src="/stat.html?source=group&action=back_top&iden="+n+"&month="+(m.getMonth()+1)+"&day="+m.getDate()+"&timestamp="+(+new Date);f.cache[n]=1};var e=function(){if(e.value){return e.value}return i.offset().top+i.find(".article").outerHeight()+30};h.load(function(){e.value=e()});var c=function(m){if(m+g>=e()){a.css({position:"absolute",bottom:"",top:e()-a.outerHeight()+40})}else{if(!d){a.css({position:"fixed",top:"",bottom:0})}}a.show().find("a").stop().animate({top:0});f("show")};var j=function(){a.hide().find("a").css("top",40)};h.resize(function(){g=h.height();a.css("left",b.offset().left+b.width()+20);l=k.height()/g>3?Math.max(2*g,$(".aside").height()):0}).trigger("resize");h.scroll((function(){var m;return function(){if(m){clearTimeout(m)}setTimeout(function(){if(l===0){return}var n=k.scrollTop();if(n>l){c(n)}else{j()}},100)}})());a.find("a").click(function(m){m.preventDefault();k.scrollTop(0);f("use")});if(d){h.scroll(function(){if(k.scrollTop()+g>=e()){return}a.css("top",k.scrollTop()+g-a.height()+40)})}});



Do(function() {
  // comment fav num
  var commentsVotes = '{"c31123215":1}',
      votes = $.parseJSON(commentsVotes),
      voteId;
  for (vote in votes) {
      voteId = vote.slice(1);
      $('li[data-cid="' + voteId + '"]').find('.comment-vote').append(' ('+ votes[vote] +')');
  }

  function removeComment(obj, cid){
    $.post_withck("/j/group/topic/4002607/remove_comment",{cid:cid}, function(d){
      d = $.parseJSON(d);
      if(d.r == 0){
        if(d.manager){
          window.location = d.url;
        }else{
          location.reload();
        }
      }else{
        alert(d.err_msg);
      }
    });
  }

  $('.reply-quote .toggle-reply').click(function(e) {
    e.preventDefault();
    var el = $(this);
    el.prevAll('span').toggle();
    el.find('span').toggle();
  });

$('.lnk-delete-comment').click(function(){
    var o = $(this);
    var comment = o.closest('.comment-item');
    var cid = $(this).attr("data-cid");
    var need_confirm = true;
    if(window._USER_ABNORMAL) {
        show_abnormal && show_abnormal()
        return
    }

    if(need_confirm){
      if(confirm($(this).attr('title'))){
      removeComment(comment, cid);
     }
    }else{
      removeComment(comment, cid);
    }
    return false;
  });

  $('.topic-reply').delegate('.lnk-fav', 'click', function() {
      if (!get_cookie('ck')) {
        $('.a_show_login').eq(0).trigger('click');
        return false;
      }
      if(window._USER_ABNORMAL) {
          show_abnormal && show_abnormal()
          return
      }
      var o = $(this),
          comment = o.closest('.comment-item'),
          cid = comment.attr("data-cid"),
          loadClass = 'start-processing';
      if (o.hasClass(loadClass)) {
          return;
      }
      o.addClass(loadClass);
      $.post_withck('/j/group/topic/4002607/add_comment_vote', {cid:cid, start:$('#start').val()}, function(d){
          d = $.parseJSON(d);
          if (d.r === 0 || d.r === 1) {
              var num = o.text().match(/\d+/) || 0;
              num = parseInt(num, 10);
              if (d.r === 0) {
                num ++;
              }
              o.replaceWith(
                  [
                      '<span>已赞 (',
                          num,
                      ')</span>'
                  ].join('')
              );
          }
      });
  });

  $('textarea, input[name=submit_btn]').click(function(e) {
      if(window._USER_ABNORMAL) {
          e.preventDefault()
          show_abnormal && show_abnormal()
      }
  })

  /* common dialog generator */
  function generate_group_prompt_dialog(dui_config){
    var prompt_dlg = dui.Dialog({
        cls: 'group-promote-dialog',
        title: (dui_config.title? dui_config.title: '操作提示'),
        content: (dui_config.content? dui_config.content: '操作内容'),
        width: (dui_config.width? dui_config.width: 400),
        buttons: [
            {text: '确定', method: function(){} }
        ]
    });
    var dui_dialog_ft_html = function(dui_config){
        $('.dui-dialog').undelegate();
        if(dui_config.callback){
            $('.dui-dialog').delegate('.btn-ok', 'click', function(){
                dui_config.callback();
            });
        }
        $('.dui-dialog').delegate('.btn-cancel', 'click', function(){
            $(".dui-dialog").hide();
        });

        var prompt_label = ''
        if(dui_config.prompt){
            prompt_label = '<label><input type="checkbox" ' + (dui_config.checked? 'checked=checked ': '') + '/>' + dui_config.prompt + '</label>'
        }
        return '<div><span class="dui-dialog-prompt">' + prompt_label + '</span><span class="bn-flat btn-cancel">取消</span><span class="bn-flat btn-ok">确定</span></div>';
    };
    prompt_dlg.open();
    prompt_dlg.node.find('.ft').html(dui_dialog_ft_html(dui_config));
  }
  /* common over */
  $('.ban-dialog-confirm').click(function(){
    if(window._USER_ABNORMAL) {
      window.show_abnormal && window.show_abnormal()
      return
    }
    var ban_action = function(){
        var ban_url = $('.ban-dialog-confirm').attr('href');
        var remove_topic_url = $('.remove-dialog-confirm').attr('href');
        console.log(ban_url);
        $.post(ban_url, {timestamp: (new Date()).getTime()}, function(d){
            $('.ban-dialog-confirm').closest('span').addClass('pl').html('已封禁');
            if($('.dui-dialog-prompt input').attr('checked')){
                window.location = remove_topic_url + "&delete_all=1";
            }
        });
        $('.dui-dialog').hide();
    };
    generate_group_prompt_dialog({content: '真的要把DL永久封禁？', prompt:'同时删除用户在本小组的所有发言和回应', checked: false, callback: ban_action, width: 420});
    return false;
  });
  $('.remove-dialog-confirm').click(function(){
    if(window._USER_ABNORMAL) {
      window.show_abnormal && window.show_abnormal()
      return
    }
    var remove_action = function(){
        var ban_url = $('.ban-dialog-confirm').attr('href');
        var remove_topic_url = $('.remove-dialog-confirm').attr('href');
        if($('.dui-dialog-prompt input').attr('checked')){
            $.post(ban_url, {timestamp: (new Date()).getTime()},
                function(r){
                  window.location = remove_topic_url;
            });
        }else{
            window.location = remove_topic_url;
        }
    };
    generate_group_prompt_dialog({content: '真的要删除小组讨论 300个国外优秀网站？', prompt:'同时封禁该成员', callback: remove_action});
    return false;
  });
  $('.lock-dialog-confirm').click(function(){
    var action_text = $('.lock-dialog-confirm').attr('title');
    var lock_action = function(){
        var lock_url = $('.lock-dialog-confirm').attr('href');
        window.location = lock_url;
    };
    if(window._USER_ABNORMAL) {
      window.show_abnormal && window.show_abnormal()
      return
    }
    generate_group_prompt_dialog({content: '真的要' + action_text + '？', prompt:'', callback: lock_action});
    return false;
  });
  // ad topic operate
  $('.ban-dialog-ad').click(function(){
    var prompt_dlg = dui.Dialog({
        cls: 'group-promote-dialog',
        title: '操作提示',
        content: '该帐号为豆瓣商务官方广告投放账号，不支持封禁操作，如有问题请联系小组组长或 business@douban.com',
        width: 400,
        buttons: [
            {text: '确定', method: function(){} },
        ]
    });
    var dui_dialog_ft_html = function(){
        $('.dui-dialog').undelegate('.btn-ok', 'click').delegate('.btn-ok', 'click', function(){
            $(".dui-dialog").hide();
        });
        return '<div><span class="bn-flat btn-ok">确定</span></div>';
    };
    prompt_dlg.open();
    prompt_dlg.node.find('.ft').html(dui_dialog_ft_html());
    return false
  });
  $('.remove-dialog-ad').click(function(){
    var prompt_dlg = dui.Dialog({
        cls: 'group-promote-dialog',
        title: '操作提示',
        content: '真的要删除小组讨论 300个国外优秀网站?',
        width:  400,
        buttons: [
            {text: '确定', method: function(){} },
        ]
    });
    var dui_dialog_ft_html = function(){
        $('.dui-dialog').undelegate('.btn-ok', 'click').delegate('.btn-ok', 'click', function(){
            var remove_topic_url = $('.remove-dialog-ad').attr('href');
            window.location = remove_topic_url;
        });
        $('.dui-dialog').delegate('.btn-cancel', 'click', function(){
            $(".dui-dialog").hide();
        });
        return '<div><span class="bn-flat btn-cancel">取消</span><span class="bn-flat btn-ok">确定</span></div>'
    };
    prompt_dlg.open();
    prompt_dlg.node.find('.ft').html(dui_dialog_ft_html());
    return false
  });
});
</script>
    <!-- douban ad begin -->
    
    




    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = 'In6Is2DzN0s',
            criteria = '1:12570|2:网站收藏夹|2:推荐网站|2:网站|2:推荐|2:好东西|3:/group/topic/4002607/',
            preview = '',
            debug = false,
            adSlots = ['dale_group_topic_new_top_right', 'dale_group_topic_new_top_right2', 'dale_group_topic_new_top_right_large', 'dale_group_topic_left_bottom', 'dale_group_topic_doublemint', 'dale_group_topic_new_inner_middle', 'dale_group_topic_new_download_middle', 'dale_group_topic_hovering_video', 'dale_group_topic_banner_after_content'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/eDRjYjNvdi9mL2FkanMvZTQ2YTNkMjgwYjBiMzc2OWE4YTI3MWFhMzI0NTQwMTBlMWY3OTYzMy9hZC5yZWxlYXNlLmpz');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>










    <!-- douban ad end -->



    
    








<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-7019765-1']);
_gaq.push(['_setCampNameKey', 'dcn']);
_gaq.push(['_setCampSourceKey', 'dcs']);
_gaq.push(['_setCampMediumKey', 'dcm']);
_gaq.push(['_setCampTermKey', 'dct']);
_gaq.push(['_setCampContentKey', 'dcc']);
_gaq.push(['_addOrganic', 'baidu', 'word']);
_gaq.push(['_addOrganic', 'soso', 'w']);
_gaq.push(['_addOrganic', '3721', 'name']);
_gaq.push(['_addOrganic', 'youdao', 'q']);
_gaq.push(['_addOrganic', 'so.360.cn', 'q']);
_gaq.push(['_addOrganic', 'vnet', 'kw']);
_gaq.push(['_addOrganic', 'sogou', 'query']);
_gaq.push(['_addIgnoredOrganic', '豆瓣']);
_gaq.push(['_addIgnoredOrganic', 'douban']);
_gaq.push(['_addIgnoredOrganic', '豆瓣网']);
_gaq.push(['_addIgnoredOrganic', 'www.douban.com']);
_gaq.push(['_setDomainName', '.douban.com']);

    _gaq.push(['_setCustomVar', 1, 'responsive_view_mode', 'desktop', 3]);
    
    _gaq.push(['_setCustomVar', 2, 'group', '网站推荐～', 3])
    _gaq.push(['_setCustomVar', 3, 'tags', '网站收藏夹|推荐网站|网站|推荐|好东西|', 3])
_gaq.push(['_trackPageview']);
_gaq.push(['_trackPageLoadTime']);
        _gaq.push(['_trackEvent', 'group tag', 'view', '网站收藏夹', 0, true]);
        _gaq.push(['_trackEvent', 'group tag', 'view', '推荐网站', 0, true]);
        _gaq.push(['_trackEvent', 'group tag', 'view', '网站', 0, true]);
        _gaq.push(['_trackEvent', 'group tag', 'view', '推荐', 0, true]);
        _gaq.push(['_trackEvent', 'group tag', 'view', '好东西', 0, true]);
window._ga_init = function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
};
if (window.addEventListener) {
    window.addEventListener('load', _ga_init, false);
} else {
    window.attachEvent('onload', _ga_init);
}
</script>






    <!-- dae-web-group--default-69b5c76f46-jf7hd-->

            







<div id="g-popup-reg" class="popup-reg" style="display:none;">
  <div class="bd">
  
  <iframe src="about:blank" frameborder="0" scrolling="no"></iframe>
    <a href="#" class="lnk-close">&times;</a>
  </div>
</div>

<div id="landing-bar" style="display:none;">
    <div class="bd">
        <p>在这里发现跟你一样特别的人，并与之交流...</p>
        <div class="operation">
            <a href="" class="j a_show_register">注册</a>
            <a href="" class="j a_show_login">登录</a>
        </div>
        
        
  
  <div class="item item-3rd">
    <label>
    第三方登录：
    </label>
    <a target="_top" href="https://www.douban.com/accounts/connect/qq/?from=group&amp;redir=http%3A//www.douban.com/accounts/join_and_redir%3Fgroup_id%3D12570" class="item-qq"><img src="https://img3.doubanio.com/pics/connect_qq.png" title="QQ"></a>
    <a target="_top" href="https://www.douban.com/accounts/connect/sina_weibo/?from=group&amp;redir=http%3A//www.douban.com/accounts/join_and_redir%3Fgroup_id%3D12570&amp;fallback=http://www.douban.com/group/webwebweb/" class="item-weibo"><img src="https://img3.doubanio.com/pics/connect_sina_weibo.png" title="新浪微博"></a>
  </div>

        <a href="#" class="lnk-close">&times;</a>
    </div>
</div>


<script>

var login_url = 'https://accounts.douban.com/popup/login?source=group';
var reg_url = 'https://accounts.douban.com/popup/login?source=group#popup_register';
</script>








  <script>_SPLITTEST=''</script>
</body>

</html>


'''
print(re.findall(r".*", string))  # 匹配空格
print(re.findall(r".+", string))  # 不匹配空格
print(re.findall(r"[^\t\r\n\f]+", string))  # 不匹配空格

# coding=utf-8

content = '''
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a href="https://www.baidu.com//articles/gz.html" title="贵州省">贵州省主题介绍</a>
</td>
'''

# 获取<a href></a>之间的内容
print(u'获取链接文本内容:')
res = r'<a .*?>(.*?)</a>'
mm = re.findall(
    res, content, re.S | re.M)
for value in mm:
    print(value)

# 获取所有<a href></a>链接所有内容
print(u'\n获取完整链接内容:')
urls = re.findall(r"<a.*?href=.*?</a>", content, re.I | re.S | re.M)
for i in urls:
    print(i)

# 获取<a href></a>中的URL
print(u'\n获取链接中URL:')
res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
link = re.findall(res_url, content, re.I | re.S | re.M)
for url in link:
    print(url)

# string = "WARNING:tensorflow: 20181011 15:28:39 Initialize training"
# pattern = re.compile(r'\d{2}:\d{2}:\d{2}')
# pattern.findall(string)
#
# # ['15:28:39']  匹配时间
#
# string = "WARNING:tensorflow: 20181011 15:28:39 Initialize training"
# pattern = re.compile(r'\d{4}\d{2}\d{2}\s\d{2}:\d{2}:\d{2}')
# pattern.findall(string)
#
# # ['20181011 15:28:39']
