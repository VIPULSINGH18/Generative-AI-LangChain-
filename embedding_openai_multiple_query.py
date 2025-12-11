from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding= OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents= ["Delhi is the capital of India",
           "Paris us the capital of France",
           "Sydney is the capital of Australia"]

result= embedding.embed_documents(documents)
print(str(result))
