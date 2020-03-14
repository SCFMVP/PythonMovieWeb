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
        print(movies)
        return render.index(movies)

    def POST(self):
        data = web.input()
        condition = r'title like "%' + data.title + r'%"'
        print("select * from movie where %s" % condition)
        cursor.execute("select * from movie where %s" % condition)
        movies = cursor.fetchall()
        return render.index(movies)


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
        return render.index(movies)


class director:
    def GET(self, director_name):
        condition = r'directors like "%' + director_name + r'%"'
        cursor.execute("select * from movie where %s" % condition)
        movies = cursor.fetchall()
        return render.index(movies)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
