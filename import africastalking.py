import africastalking
username = "sandbox"
api_key = "[bf6d105cd95a2cf965ff758e5ec8a2a7ec7115138546e8d946c3bb0cac69a515]"

africastalking.initialize(username, api_key)
SMS = africastalking.SMS
def send(self)
    recipients = ["+2347037921562"]
    message = "Happy new week.";
    sender = "Ajagbe"
try:
	response = self.sms.send("Happy new week", ["+2347037921562"], "Ajagbe") #Enter your phone number here
	print(response)
except Exception as e:
	print(f"Something went wrong {e}")

    SMS().send()
print response