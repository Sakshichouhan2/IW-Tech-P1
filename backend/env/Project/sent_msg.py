# Download the helper library from https://www.twilio.com/docs/python/install
import os
import twilio
from twilio.rest import Client
#from .models import  generateOTP
#from .models import Registration
#from .models import Login


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACc1829f3ff87275849108e39bf586148a'
auth_token = '5a363beb8f87cf0521d486ad69437059'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='generateOTP',
         from_='+19736015956',
         to='+917987416380'
     )

print(message.sid)
