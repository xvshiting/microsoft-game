import tornado.ioloop
import tornado.web
import get_hop as gp 
import json
import directreturn as dr

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	id1=self.request.arguments["id1"][0]
    	id2=self.request.arguments["id2"][0]
    	data=gp.get_hop(id1,id2)
    	self.write(json.dumps(data))

        
application = tornado.web.Application([
    (r'/.*', MainHandler),
])

if __name__ == "__main__":
    application.listen(8081)
    tornado.ioloop.IOLoop.instance().start()