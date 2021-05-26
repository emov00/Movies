from groupy.client import Client
from groupy.api.groups import Groups
from groupy.api.bots import Bots
from groupy import session

#*** infor found on https://dev.groupme.com/

group_id = '***'
token = '***'
session = session.Session(token)
bot_id = '***'

client = Client.from_token(token)
bot_count = client.bots.list()

group = Groups(session).get(group_id)

if len(bot_count) == 0:
    group.create_bot('Test Bot')
else:
    pass

def message(text):
    return Bots(session).post(bot_id, text)
