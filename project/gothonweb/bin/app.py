import web

urls = (
    '/', 'Index',
    '/foo', 'Foo',
    '/db', 'DB',
    '/add', 'Add'
    )

app = web.application(urls, globals())
db = web.database(dbn='mysql', user='webpy', pw='', db='webpy')
render = web.template.render('templates/')

class Index(object):
    def GET(self, greeting):
#        greeting = "Sup Fucker!"
        salutation = web.input(greeting=None)
        return render.index(greeting)
#        return render.index(greeting = greeting)

class Foo(object):
    def GET(self):
        name = "Greg"
        return render.foo(name = "butts")

class DB(object):
    def GET(self):
        todos = db.select('todo')
        return render.dbfile(todos)

class Add(object):
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/db')
if __name__ == "__main__":
    app.run()
