from decouple import config
from flask import Flask, render_template, request, redirect
from praw import Reddit
from urllib.parse import quote_plus


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return "Test Page"

    @app.route("/post_to_reddit/<subreddit>/<title>/<article>")
    def post_to_reddit(subreddit, article, title):
        return redirect("https://www.reddit.com/r/{}/submit?text={}&title={}".format(subreddit, (article), quote_plus(title)))

    @app.route("/app_login_user_name", methods=["POST"])
    def app_login_user_name():
        if request.method == "POST":
            print(request.data)
        return "test"

    @app.route("/app_login_password", methods=["POST"])
    def app_login_password():
        if request.method == "POST":
            print(request.data)
        return "test"

    @app.route("/article_text", methods=["POST", "GET"])  
    def article_text():
        if request.method == "POST":
            print(request.data)
        if request.method == "GET":
            return {"text": "This is a test."}
        return "test"
        
    @app.route("/app_login_password", methods=["POST"])
    def title_of_article():
        if request.method == "POST":
            print(request.data)
        return "test"

    @app.route("/recommended_subreddits", methods=["POST"])
    def recommended_subreddits():
        if request.method == "POST":
            print(request.data)
        return "test"

    @app.route("/user_choice_subreddit", methods=["POST"]) 
    def user_choice_subreddit():
        if request.method == "POST":
            print(request.data)
        return "test"
        

    return app
