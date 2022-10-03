from Lemon.components import Component

class BlogPost(Component):
    name = "BlogPost"

    def item(props: dict):
        return f"""
        <div>
            <h2>{props['title']}</h2>
            <h3>By {props['author']}</h3>
            <br>
            <p>{props['body']}</p>
        </div>
        """