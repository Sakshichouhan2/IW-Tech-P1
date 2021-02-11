import os
from .models import Registration
from .models import Login
from twilio.rest import Client

client = Client(Registration, Login)

client.message.create(
	to = os.["Registration,Login"],
	from_ = "+12672140219",
	body = 'This is the just....'
)


