from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from app_blog import mail


def send_mail(sender, recipients, subject, template, mailtype='html', **kwargs):
    """
    sender:的部份可以考慮透過設置default
    recipients:記得要list格式
    subject:是郵件主旨
    template:
        mailtype=body:郵件內容文字
        mailtype=txt、html:樣板名稱
    mailtype:
        html:html樣板(預設)
        txt:txt樣板
        body:文字方式
    **kwargs:參數
    """
    app = current_app._get_current_object()
    msg = Message(subject,
                  sender=sender,
                  recipients=recipients)
    if mailtype == 'html':
        msg.html = render_template(template + '.html', **kwargs)
    elif mailtype == 'txt':
        msg.body = render_template(template + '.txt', **kwargs)
    elif mailtype == 'body':
        msg.body = template

    #  使用多線程
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


def send_async_email(app, msg):
    """
    利用多執行緒來處理郵件寄送，因為使用另一執行緒來寄信，
    所以需要利用app_context來處理。
    :param app: 實作Flask的app
    :param msg: 實作Message的msg
    :return:
    """
    with app.app_context():
        mail.send(msg)