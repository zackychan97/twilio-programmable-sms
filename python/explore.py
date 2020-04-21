from twilio.rest import Client

#ACCOUNT SID AND AUTH TOKEN AS STRINGS
client = Client("Account SID goes here", "Auth Token Goes Here")

# Deletes all of our messages
for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()

# Sends new message
# msg = client.messages.create(
#     to="+16052287916",
#     from_="+12056497458",
#     body="Hello from Python!",
# )

# print(f"Created a new message: {msg.sid}")