from twilio.rest import Client

count_up = 7
count_down = 5
SID = "**********************************"  # your Twilio SID
Auth_token = "********************************"  # your Twilio Auth_token

try:
    # Create the Twilio client
    cl = Client(SID, Auth_token)

    # Prepare the message body
    body = "\n The number of people entered the mall is " + str(count_up) + "\n" + "The number of people left the mall is " + str(count_down)

    # Send the message
    message = cl.messages.create(   body=body,
                                    from_="+17179876731",  # Twilio number
                                    to="+919562******"  # Destination number
                                )

    print("SMS sent successfully. Message SID:", message.sid)

except Exception as e:
    # Handle the exception and print the error message
    print("Failed to send SMS. Error:", str(e))
