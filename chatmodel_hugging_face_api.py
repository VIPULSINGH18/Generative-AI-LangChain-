from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large-chat:together",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)
result = chat_model.invoke("How is today's weather?")
print(result)
