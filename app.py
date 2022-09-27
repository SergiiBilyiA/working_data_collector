from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fhitjbmwnvsvny:d41f01c074becfd52c1bcaa0e46249b2a39edefe2013760b8c101b2b193965b8@ec2-63-34-180-86.eu-west-1.compute.amazonaws.com:5432/d6bh5qhqq69rde'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Pictures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pictureBlob = db.Column(db.LargeBinary, nullable=False)
    label = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<Pictures %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        pictureBlob = request.files['pictureBlob'].read()
        label = request.form['label']

        picture = Pictures(pictureBlob=pictureBlob, label=label)

        try:
            db.session.add(picture)
            db.session.commit()
            return 'OK!'
        except:
            return "NOT OK!"


if __name__ == "__main__":
    app.run(debug=True)