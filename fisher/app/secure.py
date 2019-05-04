# 密码账号类的机密配置,不要上传到git上
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '%E7%BA%A2%E6%A5%BC%E6%A2%A6.'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '2194380700@qq.com'
MAIL_PASSWORD = 'udgvdiasdfsee'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'