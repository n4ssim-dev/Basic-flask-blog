from flask import Flask, render_template
import datetime
from guess_infos import get_age,get_gender
from blogs import get_all_blog_post,get_blog_post

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html",year=current_year)

@app.route('/guess/<name>')
def guess(name):
    country_id = "FR"
    age = get_age(name, country_id)
    gender = get_gender(name)
    return render_template("guess.html", name=name.title(), age=age,gender=gender)

@app.route('/blogs')
def get_all_blogs():
    all_blogs = get_all_blog_post()
    return render_template("blogs.html",blogs = all_blogs)

@app.route('/blog/<int:num>')
def get_blog(num):
    num = int(num) -1
    blog = get_blog_post(num)
    return render_template("blog.html",blog=blog)

if __name__ == "__main__":
    app.run(debug=True)
