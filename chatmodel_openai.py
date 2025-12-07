from langchain_openai import ChatOpenAI
from dotenv import  load_dotenv

load_dotenv()

chat_model= ChatOpenAI(model='gpt-4', )
result= chat_model.invoke("What is the name of first Prime Minister of India?")
print(result.content)  ##when we use chatmodel then we get content along with lots of meta data so if we want only string result then we use .content function*/