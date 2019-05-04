from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import db, Base
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(Base,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(24),nullable=False)
    phone_number = db.Column(db.String(18),unique=True)
    _password = db.Column('password',db.String(128),nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    confirmed = db.Column(db.Boolean,default=False)
    beans = db.Column(db.Float,default=0)
    send_counter = db.Column(db.Integer,default=0)
    receive_counter = db.Column(db.Integer,default=0)
    wx_open_id = db.Column(db.String(50))
    wx_name = db.Column(db.String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)

    def check_password(self,raw):
        return check_password_hash(self._password,raw)

    def can_save_to_list(self,isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        gifting = Gift.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
        if gifting or wishing:
            return False
        return True

    # def get_id(self):
    #     return self.id

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))