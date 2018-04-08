from fbchat import Client
from fbchat.models import *

client = Client('libertymutual48@gmail.com', 'libmutual')

print('Own id: {}'.format(client.uid))

#100002945516202
#1258483157512935
client.send(Message(text='Hi Ani.'), thread_id=1979668075394436, thread_type=ThreadType.USER)

client.logout()