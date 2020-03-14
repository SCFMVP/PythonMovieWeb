import time
import urllib
from urllib import request
from urllib.request import Request

import pymysql


def get_poster(id, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    ret = Request(url, headers=headers)
    #pic = request.urlopen(ret)
    pic = urllib.request.urlopen(ret).read()
    file_name = 'static/poster/%d.jpg' % id
    f = open(file_name, "wb")
    f.write(pic)
    f.close()


# MySql-以List形式输出
db = pymysql.connect("localhost", "root", "root", "moviesite", cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()
cursor.execute("select * from movie")
movies = cursor.fetchall()

count = 0
for movie in movies:
    get_poster(movie['id'], movie['image'])
    count += 1
    print(count, movie['title'])
    time.sleep(2)
