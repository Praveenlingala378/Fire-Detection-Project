from smtplib import SMTP
import datetime

debuglevel = 0

smtp = SMTP()
smtp.set_debuglevel(debuglevel)
smtp.connect('smtp.gmail.com', 587)
smtp.login('praveenlingala378@gmail.com', '9740699375')

from_addr = "praveenlingala378@gmail.com"
to_addr = "rlucky540@gmail.com"

subj = "hello"
date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )

message_text = "Hello\nThis is a mail from your server\n\nBye\n"

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_addr, to_addr, subj, date, message_text )

smtp.sendmail(from_addr, to_addr, msg)
smtp.quit()