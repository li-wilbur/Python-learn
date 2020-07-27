import requests
import time
import re
from bs4 import BeautifulSoup


class dytt_worm(object):

    def __init__(self):
        # 本次爬虫使用的头部信息
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
            "Referer": "https://www.dy2018.com/html/gndy/dyzz/index.html",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive"
        }
        # 网址前部分，用来合成完整网址
        self.piece = "https://www.dy2018.com/html/gndy/dyzz/"
        # 存储页面所有电影的详情url列表(已包含第一页)
        self.index_pages = ["https://www.dy2018.com/html/gndy/dyzz/index.html"]
        # 存储每部电影的详情页面url及名字信息
        self.movie_url = {}

    def pull_page(self, num):
        if num == 1:
            pass
        else:
            # 根据num的值添加页码对应网址
            for index_num in range(2, num + 1):
                self.index_pages.append(self.piece + 'index' + '_' + str(index_num) + '.html')
        return self.index_pages

    def movieurl(self):
        # 使用BeautifulSoup解析页面拿到具体每部电影的详细地址
        for page in self.index_pages:
            print("正在请求：", page)
            reponse = requests.get(url=page, headers=self.header, timeout=25)
            reponse.encoding = 'gb2312'
            soup = BeautifulSoup(reponse.text, 'lxml')
            for url in soup.find_all('a', class_='ulink'):
                href = url.get('href')
                movie = url.get('title')
                self.movie_url[movie] = "https://www.dy2018.com" + href

    def magnet(self, choice=None):
        # 拿到每部电影具体的磁力链接
        for movie_name, magnet_url in self.movie_url.items():
            if magnet_url == 'https://www.dy2018.com/i/101661.html':
                continue
            print("开始寻找 {} 的磁力链接......".format(movie_name))
            reponse_magent = requests.get(url=magnet_url, headers=self.header, timeout=35)
            reponse_magent.encoding = 'gb2312'
            soup_magnet = BeautifulSoup(reponse_magent.text, 'lxml')
            for movie_url_td in soup_magnet.find_all('td', style="WORD-WRAP: break-word"):
                movie_url_td_a = movie_url_td.find_all('a')
                zheng = re.compile("href=\"(.*?)\">")
                Re_magnet = re.findall(zheng, str(movie_url_td_a))
                print(Re_magnet[0])
                # 将电影的磁力链接保存到本地
                if str(choice) == 'y' or str(choice) == 'Y':
                    with open('movie.txt', 'a', encoding='gb2312') as file_obj:
                        file_obj.write(Re_magnet[0] + '\n')


dytt_worm_open = dytt_worm()
file_choice = None
num_choice = 1
if __name__ == '__main__':
    choice_file = input("是否要将磁力链接保存到文件中（输入y保存）：")
    num_choice = int(input("请输入爬取页码范围(正整数)："))

    start_time = time.time()
    if str(choice_file) == 'y' or str(choice_file) == 'Y':
        file_choice = 'y'
        dytt_worm_open.pull_page(num_choice)
        dytt_worm_open.movieurl()
        dytt_worm_open.magnet(file_choice)
        print("\n\n磁力保存完成，打开'movie.txt'和磁力下载软件即可复制下载。（如：迅雷、Bitcomet）")
    else:
        dytt_worm_open.pull_page()
        dytt_worm_open.movieurl()
        dytt_worm_open.magnet()

    print("\n\n运行结束，感谢使用本工具！")
    end_time = time.time()
    print('本次运行花费了{}秒。'.format(int(end_time - start_time)))
