from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

hobbies = {
    "Watching Movies": "https://movie-recommending-model.streamlit.app/",
    "Listening to Songs": "https://song-recommender-model.streamlit.app/",
    "Reading Books": "https://book-recommender-model.streamlit.app/"
}

@app.route('/')
def home():
    return render_template('index.html', hobbies=hobbies)

@app.route('/hobby/<hobby_name>')
def hobby(hobby_name):
    if hobby_name in hobbies:
        return redirect(hobbies[hobby_name])
    elif hobby_name == "Random":
        random_hobby = random.choice(list(hobbies.keys()))
        return redirect(hobbies[random_hobby])
    else:
        return "Hobby not found", 404

if __name__ == '__main__':
    app.run(debug=True)
