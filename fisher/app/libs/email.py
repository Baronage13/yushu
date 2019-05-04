from flask import current_app, render_template

from app import mail
from flask_mail import Message

def send_mail(to,subject,template,**kwargs):
    # Python email
    # msg = Message('测试邮件',sender='2194380700@qq.com',body='Test',recipients=['1696598870@qq.com'])

    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_SENDER'],
                  recipients=[to])
    msg.html = render_template(template,**kwargs)

    mail.send(msg)
    pass