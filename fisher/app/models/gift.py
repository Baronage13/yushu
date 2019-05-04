from flask import current_app
from sqlalchemy import ForeignKey, desc, func
from sqlalchemy.orm import relationship
from app.models.base import db, Base

from app.spider.yushu_book import YuShuBook



class Gift(Base):
    id = db.Column(db.Integer,primary_key=True)
    user = relationship('User')
    uid = db.Column(db.Integer,ForeignKey('user.id'))
    isbn = db.Column(db.String(15),nullable=False)

    # book = relationship('Book')
    # bid = db.Column(db.Integer,ForeignKey('book.id'))

    launched = db.Column(db.Boolean,default=False)

    @classmethod
    def get_user_gifts(cls,uid):
        gifts = Gift.query.filter_by(uid=uid,launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):
        from app.models.wish import Wish
        # 根据传入的一组isbn，到Wish表中计算出某个礼物的Wish心愿数量
        count_list = db.session.query(func.count(Wish.id),Wish.isbn).filter(Wish.launched == False,Wish.isbn.in_(isbn_list),
                                      Wish.status == 1).group_by(Wish.isbn).all()
        count_list = [{'count':w[0],'isbn':w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        # 链式调用
        recent_gift = Gift.query.filter_by(launched=False).group_by(Gift.isbn
            ).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()

        # recent_gift = Gift.query.filter_by(launched=False).order_by(desc(Gift.create_time)).limit(
        #     current_app.config['RECENT_BOOK_COUNT']).all()

        return  recent_gift