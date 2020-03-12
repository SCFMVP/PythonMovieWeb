# coding:utf8
import web
import pymysql

# MySql
con = pymysql.connect(dbn='mysql', host='localhost', user='root', pw='root', db='moviesite', charset='utf8')
# SQLite
db = web.database(
    dbn='mysql',
    host='localhost',
    user='root',
    pw='root',
    db='moviesite',
    charset='utf8'
)
render = web.template.render('templates/')

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        movies = db.select('movie')
        return render.index(movies)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
