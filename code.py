# -*- coding: UTF-8 -*-
import web
import pymysql

from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

render = web.template.render('templates/')
# MySql-以List形式输出
db = pymysql.connect("localhost", "root", "root", "moviesite", cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

urls = (
    '/', 'index',
    '/movie/(\d+)', 'movie',
    '/cast/(.*)', 'cast',
    '/director/(.*)', 'director',
)


class index:
    def GET(self):
        cursor.execute("select * from movie")
        movies = cursor.fetchall()
        cursor.execute('SELECT COUNT(*) AS COUNT FROM movie')
        count = cursor.fetchall()[0]['COUNT']
        return render.index(movies, count, None)

    def POST(self):
        data = web.input()
        condition = r'title like "%' + data.title + r'%"'
        print("select * from movie where %s" % condition)
        cursor.execute("select * from movie where %s" % condition)
        movies = cursor.fetchall()
        #查询数量
        cursor.execute('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)
        count = cursor.fetchall()[0]['COUNT']
        return render.index(movies, count, data.title)


class movie:
    def GET(self, movie_id):
        movie_id = int(movie_id)
        cursor.execute("select * from movie where id=%s" % movie_id)
        # 只返回一条数据
        movie = cursor.fetchall()[0]
        print(movie)
        return render.movie(movie)


class cast:
    def GET(self, cast_name):
        condition = r'casts like "%' + cast_name + r'%"'
        cursor.execute("select * from movie where %s" % condition)
        movies = cursor.fetchall()
        cursor.execute('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)
        count = cursor.fetchall()[0]['COUNT']
        return render.index(movies, count, cast_name)


class director:
    def GET(self, director_name):
        condition = r'directors like "%' + director_name + r'%"'
        cursor.execute("select * from movie where %s" % condition)
        movies = cursor.fetchall()
        cursor.execute('SELECT COUNT(*) AS COUNT FROM movie WHERE ' + condition)
        count = cursor.fetchall()[0]['COUNT']
        return render.index(movies, count, director_name)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
