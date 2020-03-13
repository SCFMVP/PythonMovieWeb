# -*- coding: UTF-8 -*-
import web
import pymysql
from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')

render = web.template.render('templates/')
# MySql-以List形式输出
db = pymysql.connect("localhost", "root", "root", "moviesite",  cursorclass=pymysql.cursors.DictCursor)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        cursor.execute("select * from movie")
        movies = cursor.fetchall()
        print(movies)
        return render.index(movies)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
