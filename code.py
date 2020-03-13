# coding:utf8
import web
import pymysql

# MySql
db = pymysql.connect("localhost", "root", "root", "moviesite")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
'''
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
# 关闭数据库连接
db.close()
'''

render = web.template.render('templates/')

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        cursor.execute("SELECT move")
        movies = cursor.fetchall()
        # movies = db.select('movie')
        return render.index(movies)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
