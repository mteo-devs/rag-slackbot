from common import *
import llm_model
#from llama_index.readers.s3 import S3Reader
import table_init

#loader = S3Reader(
#    bucket=os.environ['S3_BUCKET'],
#    key=file,
#    aws_access_id=os.environ['AWS_ACCESS_KEY'],
#    aws_access_secret=os.environ['AWS_SECRET_KEY'],
#)
#documents = loader.load_data()
table=table_init.table

from s3fs import S3FileSystem
#file = 'state_of_the_union.txt'

s3_fs = S3FileSystem(
    anon=False, 
    endpoint_url=os.environ['S3_ENDPOINT'],
    key=os.environ['AWS_ACCESS_KEY'],
    secret=os.environ['AWS_SECRET_KEY'],
)

required_exts = [".json"]
reader = SimpleDirectoryReader(
    input_dir=os.environ['S3_BUCKET'],
    fs=s3_fs,
    required_exts=required_exts,
    recursive=True,  # recursively searches all subdirectories
)


vector_store = KDBAIVectorStore(table)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)