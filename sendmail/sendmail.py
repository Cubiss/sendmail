import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders


def sendmail(to, fro: str, subject: str, text: str, attachments=None, server="localhost"):
    """
    Send mail via a SMTP server without authentication.
    :param to: A recipient or a list of recipients.
    :param fro: Sender.
    :param subject: Subject.
    :param text: Body of the email.
    :param attachments: List of paths to attachments.
    :param server: SMTP server location.
    :return:
    """
    # convert single recipient to a list of one
    if type(to) == str:
        to = [to]

    # convert no attachments to empty list
    attachments = attachments or []

    # convert single attachment to list of one
    if type(attachments) == str:
        attachments = [attachments]

    assert type(to) == list
    assert type(attachments) == list

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = ', '.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for file in attachments:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                        % os.path.basename(file))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(fro, to, msg.as_string())
    smtp.close()
