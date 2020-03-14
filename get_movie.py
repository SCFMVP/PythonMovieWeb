from urllib import request
import json
import time
from urllib.request import Request
import pymysql
import web

# 连接数据库
db = pymysql.connect("localhost", "root", "root", "moviesite")
cursor = db.cursor()

# 数组存放id
movie_ids = []
for index in range(0, 250, 50):
    print(index)
    url = 'https://douban.uieee.com/v2/movie/top250?start=%d&count=50' % index
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    ret = Request(url, headers=headers)
    response = request.urlopen(ret)
    data = response.read()
    # print data

    data_json = json.loads(data)
    movie250 = data_json['subjects']
    for movie in movie250:
        movie_ids.append(movie['id'])
        print(movie['id'], movie['title'])
    time.sleep(3)
print(movie_ids)


def add_movie(data):
    movie = json.loads(data)
    # sql 语句有点儿长
    sql = '''INSERT INTO movie(id, title, origin, url, rating, image, directors, casts, year, genres, countries, 
    summary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '''
    sqlvar = (movie['id'], movie['title'], movie['original_title'], movie['alt'], movie['rating']['average'], movie['images']['large'], ','.join([d['name'] for d in movie['directors']]), ','.join([c['name'] for c in movie['casts']]), movie['year'], ','.join(movie['genres']), ','.join(movie['countries']), movie['summary'])
    print(sql)
    cursor.execute(sql, sqlvar)
    db.commit()

    print(movie['title'])


count = 0
for mid in movie_ids:
    print(count, mid)
    url = 'https://douban.uieee.com/v2/movie/subject/%s' % mid
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    ret = Request(url, headers=headers)
    response = request.urlopen(ret)
    data = response.read()

    add_movie(data)
    count += 1
    time.sleep(3)
