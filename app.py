from Lemon.components import Component
from Lemon.Server.server import Server

from Components.components import BlogPost

Root = Component("HTTP-Blog", stylesheet="public/css/style.css")
app = Server(static_dir="public")

class App(Component):
    name = "App"
    def item(props: dict):
        return f"<BlogPost title={props['title']} author={props['author']} body={props['body']}/>"

Root.add(
    [
        App,
        BlogPost
    ]
)

posts = [{"title": "Hello World", "author": "Lemon", "body": "This is a test post"}]

@app.route("/{post_id}")
def home(request, response, post_id):
    if post_id.isdigit():
        try:
            post = posts[int(post_id)-1]
            response.text = Root.render(f'<App title={post["title"]} author={post["author"]} body={post["body"]}/>')
        except IndexError:
            response.status_code = 404
            response.text = "<h3>Post not found</h3>"
    else:
        response.text = "<h3>This id should be an integer, Not String</h3>"

@app.route("/api/get/{post_id}") # the {id} is an argument in the url.
def api_get(request, response, post_id):
    #for now let's just return the post_id
    response.text = posts[post_id]

@app.route('/api/post/')
class api_post():
    def get(self, req, res):
        res.text = "method not allowed"
    def post(self, req, res):
        json = req.json
        if json["title"] and json["body"] and json["author"] and json["id"]:
            post_id = int(json["id"])
            if post_id not in posts:
                posts[post_id] = json
                res.text = "success"
            else:
                posts.append(json)
                res.text = "success"
        else:
            res.text = "failed"


app.run()