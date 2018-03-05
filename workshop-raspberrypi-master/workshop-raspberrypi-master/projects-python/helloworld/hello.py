## Hello World, PubNub

import sys
from pubnub import Pubnub

# Initiate Pubnub State - Get your own keys at admin.pubnub.com
pubnub = Pubnub(publish_key='pub-c-2feb27d6-3859-4a13-9445-d06b03e406ee',
                subscribe_key='sub-c-636e0cde-ea8f-11e5-871f-0619f8945a4f')

channel = 'hello-pi'

username = 'Your name'
message = 'Hello World from Pi!'

data = {
    'username': username,
    'message': message
}

# Asynchronous usage
def callback(m):
    print(m)

pubnub.publish(channel, data, callback=callback, error=callback)
