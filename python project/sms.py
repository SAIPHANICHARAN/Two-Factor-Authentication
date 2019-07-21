from twilio.rest import Client
import random
i=(random.randint(1000,9999))
account_sid = "AC27337efba74fc815e2d6f55e184a3ee5"
auth_token  = "fce32b6eae24fd059ed94968d76235d2"
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+919629607721",
    from_="+12565675530",
    body=i)
message2 = client.messages.create(
    to="+919490898515",
    from_="+12565675530",
    body=i)

print(message.sid,"OTP Sent:",i);
print(message2.sid,"OTP Sent:",i);
