from . import db
from flask_login import UserMixin

player = db.Table('player',
                  db.Column('playerID', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                  db.Column('gameId', db.Integer, db.ForeignKey('game.id'), primary_key=True),
                  db.Column('max_score', db.Integer),
                  db.Column('ratting_point', db.Integer)
                  )


class Comment(db.Model):
    gameID = db.Column(db.Integer, db.ForeignKey('game.id'))
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    added_date = db.Column(db.DateTime)
    commentContent = db.Column(db.String(100))
    id = db.Column(db.Integer, primary_key=True)


favorite = db.Table('favorite',
                    db.Column('userId', db.Integer, db.ForeignKey('user.id')),
                    db.Column('gameID', db.Integer, db.ForeignKey('game.id'))
                    )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    avatar = db.Column(db.String)

    userName = db.Column(db.String(150), unique=True)
    dateOfBirth = db.Column(db.String)
    sex = db.Column(db.String(15))  # giới tính là nam, nữ, không muốn nói
    country = db.Column(db.String(100))
    bio = db.Column(db.String(100))
    link = db.Column(db.String(100000))

    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    gameComment = db.relationship(Comment)
    # favoriteList = db.relationship('Game', secondary = favorite)
    favoriteList = db.relationship('Game', secondary=favorite,
                                   backref=db.backref('personLikeGame', lazy='dynamic'))
    gameScore = db.relationship('Game', secondary=player,
                                backref=db.backref('personPlayScore', lazy='dynamic'))


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameName = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    gamePath = db.Column(db.String(2000), unique=True)
    tag = db.Column(db.String(100))
    gameImgPath = db.Column(db.String(1000))
    gameComment = db.relationship(Comment)
    rankingScore = db.relationship('User', secondary=player)
    videoPath = db.Column(db.String)


print('Hello world!')