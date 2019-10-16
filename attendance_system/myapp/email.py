"""
import syntax :
from docketservice.core.common.email import Email
"""

import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText

from django.conf import settings




class Email():

    def __init__(self):
        self.__ses_host = 'smtp.office365.com'


    def send_attachment(self):
        result = None
        try :
            """
            mail_dto.subject
            mail_dto.from_address
            mail_dto.body
            mail_dto.file_content
            mail_dto.file_name
            mail_dto.to_addresses
            mail_dto.smtp_username
            mail_dto.smtp_password
            """
            # sendto = 'kssubish999@gmail.com'
            # user= 'subish@digitalmesh.com'
            # password = "Myserver#18"
            # smtpsrv = "smtp.office365.com"
            # smtpserver = smtplib.SMTP(smtpsrv,587)

            # smtpserver.ehlo()
            # smtpserver.starttls()
            # smtpserver.ehlo
            # smtpserver.login(user, password)
            # #header = 'To:' + sendto + 'n' + 'From: ' + user + 'n' + 'Subject:testing n'
            # #print header
            # msgbody = 'This is a test Email send using Python nn'
            # smtpserver.sendmail(user, sendto, msgbody)
            # #print 'done!'
            # smtpserver.close()
            # a=1/0

            msg = MIMEMultipart()
            msg['Subject'] = 'celery msg'
            msg['From'] = 'meghalrag@digitalmesh.com'
            msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
            msg.attach(MIMEText('completed','html',"utf-8"))
            #attach additional files
            # part1 = MIMEBase('application', 'octet-stream')
            # part1.add_header('Content-Disposition', 'attachment;filename='+str(mail_dto.file_name))
            # encoders.encode_base64(part1)
            # msg.attach(part1)

            smtp_server = smtplib.SMTP(self.__ses_host, 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo
            smtp_server.login('meghalrag@digitalmesh.com', 'Gam05193')

            #smtp_server.login(mail_dto.smtp_username, mail_dto.smtp_password)
            smtp_server.sendmail('meghalrag@digitalmesh.com', 'amritha.s@digitalmesh.com', msg.as_string())
            smtp_server.close()
        except Exception as e:

            print ('eeeeeeeee',e)
            # msg = """Error in the method Email.send_attachment,
            # Error: {0}, Error traceback: {1}""".format(str(e), self.__exception.get_exception())
            #self.__log.error(msg)
        finally:
            return result