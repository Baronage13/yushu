from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from contextlib import contextmanager

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

class Query(BaseQuery):
    def filter_by(self,**kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query,self).filter_by(**kwargs)

db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    __abstract__ = True #不创建Base表
    create_time = db.Column('create_time',db.Integer)
    status = db.Column(db.SmallInteger,default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
            # 判断当前对象有没有Key属性
                setattr(self,key,value)
                # 对当前对象的key属性赋值

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

