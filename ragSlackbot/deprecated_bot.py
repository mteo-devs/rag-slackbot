from common import *
import embeddings_init
import slack
from flask import Flask
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events',app)

K = 15

query_engine = embeddings_init.index.as_query_engine(
    similarity_top_k=K,
    #filter=[("<", "publication_date", "2008-09-15")],
    sort_by="publication_date",
)

client = slack.WebClient(token=os.environ['SLACK_AUTH'])
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    print(BOT_ID)
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    print(user_id)
    text = event.get('text')

    if BOT_ID != user_id:
        result = query_engine.query(text)
        client.chat_postMessage(channel=channel_id,text=result.response)
        #client.chat_postMessage(channel=channel_id,text=text)


if __name__ == "__main__":
    app.run(debug=True)
