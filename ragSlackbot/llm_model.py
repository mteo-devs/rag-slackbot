from common import *

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI


# loads BAAI/bge-small-en
# embed_model = HuggingFaceEmbedding()

# loads BAAI/bge-small-en-v1.5
embed_model = HuggingFaceEmbedding(model_name="Alibaba-NLP/gte-large-en-v1.5",trust_remote_code=True)

remotely_run = HuggingFaceInferenceAPI(
    #model_name="HuggingFaceH4/zephyr-7b-alpha", token=HF_TOKEN
    model_name="meta-llama/Meta-Llama-3-8B-Instruct", token=os.environ['HF_TOKEN']
)
#HuggingFaceInferenceAPI(token=HF_TOKEN)

Settings.llm = remotely_run
Settings.embed_model = embed_model