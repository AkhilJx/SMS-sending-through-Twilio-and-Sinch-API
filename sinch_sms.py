import time
from sinchsms import SinchSMS

# Replace with actual values
number = '+919876543210'  # Use your mobile number here in international format
message = 'I love SMS!'
your_app_key = 'your_actual_app_key' # app key credential for the Sinch SMS API.
your_app_secret = 'your_actual_app_secret' # app secret key credential for the Sinch SMS API.

client = SinchSMS(your_app_key, your_app_secret)

print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']

# Checking status until successful
response = client.check_status(message_id)
while response['status'] != 'Successful':
    print(response['status'])
    time.sleep(1)
    response = client.check_status(message_id)

print("Message sent successfully!")
