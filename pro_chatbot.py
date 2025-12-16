#using system_message,human_message,AI_message to specify each and every conversation in our chat history
# so that our chat bot will not hallucinate if chat-history becomes too large...

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv 

load_dotenv()

model= ChatOpenAI()

chat_history= [
    SystemMessage(content="You are helful AI assistant")
]

while True:
    user_input= input("Ask:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result= model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)

print(chat_history)

