from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

chat_template= ChatPromptTemplate([
    SystemMessage(content= 'You are helpful {domain} expert'),
    HumanMessage(content='Explain in simple terms, what is {topic}')])


prompt= chat_template.invoke( {'domain':'cricket','topic':'LBW'})
print(prompt)


#when we deal with static prompt while building chatbot or multi-text application then this syntax
#is valid for system and human message...
# but if you are working with dynamic prompt in multi-text application then following syntax has to be follow: 

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage

chat_template= ChatPromptTemplate([
    ('system', 'You are helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')])


prompt= chat_template.invoke( {'domain':'cricket','topic':'LBW'})
print(prompt)