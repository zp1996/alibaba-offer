# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import options

def getHeader(s):
    return Header(s, 'utf-8')

receivers = [ options.get('receivers') ]

def sendemail(receivers, status):
    # 发送邮箱
    sender = 'lsgogroup@gmail.com'
    # 页面主体信息
    main = '''
    恭喜大佬，目前校招状态已经改变了~

        状态为：''' + status
    msg = MIMEText(main, 'plain', 'utf-8')
    # 设置头信息
    msg['From'] = getHeader('zp1996')
    msg['To'] = getHeader('大佬~')
    msg['Subject'] = getHeader('阿里巴巴校招状态改变~')
    try:
        server = smtplib.SMTP('smtp.gmail.com', 25)
        server.ehlo()
        server.starttls()
        server.login(sender, 'Lsgogroup')
        server.sendmail(sender, receivers, msg.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException as err:
        print err

sendemail(receivers, '已入职')
