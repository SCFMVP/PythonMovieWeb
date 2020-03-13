# -*- coding: UTF-8 -*-
import web
import pymysql
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

render = web.template.render('templates/')
# MySql-以List形式输出
db = pymysql.connect("localhost", "root", "root", "moviesite",  cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

urls = (
    '/', 'index',
    '/movie/(\d+)', 'movie',
)


class index:
    def GET(self):
        cursor.execute("select * from movie")
        movies = cursor.fetchall()
        print(movies)
        return render.index(movies)


class movie:
    def GET(self, movie_id):
        movie_id = int(movie_id)
        cursor.execute("select * from movie where id=%s" % movie_id)
        movie = cursor.fetchall()[0]
        #movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
        return render.movie(movie)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
