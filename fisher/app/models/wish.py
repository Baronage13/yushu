from sqlalchemy import ForeignKey, desc, func
from sqlalchemy.orm import relationship
from app.models.base import db, Base

from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = db.Column(db.Integer,primary_key=True)
    user = relationship('User')
    uid = db.Column(db.Integer,ForeignKey('user.id'))
    isbn = db.Column(db.String(15),nullable=False)

    # book = relationship('Book')
    # bid = db.Column(db.Integer,ForeignKey('book.id'))

    launched = db.Column(db.Boolean,default=False)

    @classmethod
    def get_user_wishes(cls,uid):
        wishes = Wish.query.filter_by(uid=uid,launched=False).order_by(desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gift_counts(cls,isbn_list):
        from app.models.gift import Gift
        # 根据传入的一组isbn，到Wish表中计算出某个礼物的Wish心愿数量
        count_list = db.session.query(func.count(Gift.id),Gift.isbn).filter(Gift.launched == False,Gift.isbn.in_(isbn_list),
                                      Gift.status == 1).group_by(Gift.isbn).all()
        count_list = [{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first