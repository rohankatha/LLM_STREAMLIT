grok_key = "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"
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
model = ChatGroq(groq_api_key = grok_key, model= "Gemma2-9b-it")

message=[
     SystemMessage(content =  "translate language into telugu"),
    HumanMessage(content =  "My name is kahn"),
   
]
parser = StrOutputParser()
chain = model|parser
print(chain.invoke(message))
