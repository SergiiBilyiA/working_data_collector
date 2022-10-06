from flask import Flask, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import base64
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pnahkcxihrrzjr:29ba5ea5b346d61c14669cbdd5bdad48de6aeed1cf67539a8f05603f57d92d9b@ec2-46-51-187-237.eu-west-1.compute.amazonaws.com:5432/d6l57e709ho9u8'
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


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    return render_template('dataclip.html')


@app.route('/pictures')
def pictures():
    pictures = Pictures.query.order_by(Pictures.id).all()
    res_pictures = []
    for picture in pictures:
        res_pictures.append({
            'id': picture.id,
            'blob': base64.encodebytes(picture.pictureBlob).decode('utf-8'),
            'label': picture.label
        })
    return res_pictures


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