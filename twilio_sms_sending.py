from twilio.rest import Client

count_up=7
count_down=5
SID="**********************************" # your twilio SID
Auth_token="********************************" # your twilio Auth_token
cl=Client(SID,Auth_token)
body="\n The number of people entered the mall is "+str(count_up)+"\n"+ "The number of people left the mall is "+str(count_down)
cl.messages.create(body=body,from_="+17179876731",to="+919562******")
print("SMS sent successfully")
