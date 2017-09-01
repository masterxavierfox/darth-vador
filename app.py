from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://thechive.files.wordpress.com/2017/03/z6-add-memes-600-1.jpg",
    "http://s2.quickmeme.com/img/7b/7b3ddf3a55bafeb39e6713c3658479613e8a26411e377b3b9ee847a185668822.jpg",
    "https://i0.wp.com/www.quirkybyte.com/wp-content/uploads/2017/04/5-45.jpg",
    "http://slapwank.com/wp-content/uploads/2017/03/Funny-Darth-Vader-Memes-2.jpg",
    "http://cdn.humoropedia.com/wp-content/uploads/2014/11/funny-picture-darth-vader-elevader.jpg",
    "http://www.vitamin-ha.com/wp-content/uploads/2015/08/Darth-Vader-Memes8.jpg",
    "https://img.memecdn.com/Epic-Darth-Vader-Bob-Anderson-Tribute_o_120315.jpg",
    "http://cdn2-www.craveonline.com/assets/mandatory/legacy/2015/06/man_file_1059158_1b9dd37df346c49c11d1a9e317093a47.png",
    "http://starecat.com/content/wp-content/uploads/meth-not-even-once-darth-vader-mask.jpg",
    "https://i.imgflip.com/1v3qj7.jpg",
    "http://i0.kym-cdn.com/photos/images/facebook/000/065/016/teamwork.jpg",
    "https://i.imgflip.com/1v3qlw.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")