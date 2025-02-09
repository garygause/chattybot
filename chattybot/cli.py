import os
import warnings

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough

# Ignore deprecation warnings from langchain
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)

chatbot = ChatOpenAI(model="gpt-3.5-turbo")
chatbotMemory = {}

# input: session_id, output: chatbotMemory[session_id]
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in chatbotMemory:
        chatbotMemory[session_id] = ChatMessageHistory()
    return chatbotMemory[session_id]

def limited_memory_of_messages(messages, number_of_messages_to_keep=100):
    return messages[-number_of_messages_to_keep:]

session1 = {"configurable": {"session_id": "001"}}

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability but do so with humor.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

limitedMemoryChain = (
    RunnablePassthrough.assign(messages=lambda x: limited_memory_of_messages(x["messages"]))
    | prompt 
    | chatbot
)

chatbot_history = RunnableWithMessageHistory(
    limitedMemoryChain,
    get_session_history,
    input_messages_key="messages",
)

def run_shell():
    while True:
        user_input = input("chatty >> ")
        if user_input.lower() == 'exit':
            break
        
        try:
            response = chatbot_history.invoke(
                {
                    "messages": [HumanMessage(content=user_input)],
                },
                config=session1,
            )            
            print(response.content)
        except Exception as e:
             print(f"Error: {e}")
            

if __name__ == "__main__":
    print("ChattyBot - an ai chat bot. Type 'exit' to quit.")
    run_shell()