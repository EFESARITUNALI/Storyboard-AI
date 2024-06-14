from langchain_cohere import ChatCohere
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from config import get_prompt_template

def get_cohere_client(api_key):
    return ChatCohere(cohere_api_key=api_key)

def create_prompt_template():
    template = get_prompt_template()
    return SystemMessagePromptTemplate.from_template(template)

def create_human_prompt_template():
    human_template = "Turn this text into a storyboard: {text}"
    return HumanMessagePromptTemplate.from_template(human_template)

def create_chat_prompt(system_message_prompt, human_message_prompt):
    return ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

def generate_prompts(text, api_key):
    cohere = get_cohere_client(api_key)
    system_message_prompt = create_prompt_template()
    human_message_prompt = create_human_prompt_template()
    chat_prompt = create_chat_prompt(system_message_prompt, human_message_prompt)
    chain = LLMChain(llm=cohere, prompt=chat_prompt)
    return chain.run(text=text)