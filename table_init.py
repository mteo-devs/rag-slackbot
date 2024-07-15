from common import *

#connect to KDB.AI
session = kdbai.Session(api_key=os.environ['KDBAI_API_KEY'], endpoint=os.environ['KDBAI_ENDPOINT'])
table_name="rag_langchain"
schema = {'columns': [{'name': 'document_id', 'pytype': 'bytes'},
                     {'name': 'text', 'pytype': 'bytes'},
                       {'name': 'embedding',
                       'vectorIndex': {'dims': 1024, 'metric': 'L2', 'type': 'flat'}}]}

#!!! Note: The 'dims' parameter in the embedding column must reflect the output dimensions of the embedding model you choose.
#OpenAI 'text-embedding-3-small' outputs 1536 dimensions.

table = session.table(table_name)