import os
import embeddings_init
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(
    token=os.environ.get("SLACK_AUTH"),
    signing_secret=os.environ.get("SIGNING_SECRET")
)

K = 15

query_engine = embeddings_init.index.as_query_engine(
    similarity_top_k=K,
    #filter=[("<", "publication_date", "2008-09-15")],
    sort_by="publication_date",
)


@app.event("message")
def event_test(body, say, logger):
    logger.info(body)
    result = query_engine.query(body['event']['text'])
    say(result.response)

# from flask import Flask, request
# from slack_bolt.adapter.flask import SlackRequestHandler

# flask_app = Flask(__name__)
# handler = SlackRequestHandler(app)

# @flask_app.route("/slack/events", methods=["POST"])
# def slack_events():
#     return handler.handle(request)

if __name__ == "__main__":
    # flask_app.run(host='0.0.0.0', port='5000',debug=True)
    SocketModeHandler(app,os.environ.get("SLACK_SOCKET_TOKEN")).start()