from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from langchain.chains import LLMChain

chat_open_ai = ChatOpenAI()

# Predict
print (chat_open_ai.predict("hello world!"))

# Chain
system_message_prompt = SystemMessagePromptTemplate.from_template("You are funny documentation writer and a dad, who is a fan of Xzibit.")

human_message_prompt = HumanMessagePromptTemplate.from_template("{user_input}")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(
    prompt = chat_prompt,
    llm = chat_open_ai,
    output_parser = None
) 

print (chain.run("what makes a rainbow?"))